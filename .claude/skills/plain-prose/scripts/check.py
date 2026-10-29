"""Score a Markdown document against the target register in `register.md`.

Prints a table of fingerprints for one or more files, with the target value
next to each and a mark on any value outside the target range. Plain developer
documentation tends to land inside those ranges. A document a model wrote
tends to miss several of them at once. The score is only a diagnostic:
fixing the prose fixes the numbers, never the other way around.

Usage:

    python3 check.py README.md [more.md ...]
    python3 check.py --allow delve,journey README.md
    cat README.md | python3 check.py -

`--allow` names domain words the marketing list should not count for this
document (a dungeon "delve" in a game's README). Exit status is 0 either way; the
table is the output.
"""

import re
import statistics
import sys

# (label, target value, "lo-hi" band considered in range)
BANDS = {
    "em_dash_per_1k":       (0.0, (0.0, 0.0)),
    "en_dash_per_1k":       (0.0, (0.0, 0.5)),
    "spaced_hyphen_per_1k": (2.0, (0.0, 15.0)),
    "sent_median":          (20, (9, 26)),
    "sent_p90":             (33, (20, 42)),
    "contractions_per_1k":  (15.0, (3.0, 30.0)),
    "semicolon_per_1k":     (0.1, (0.0, 2.0)),
    "parens_per_1k":        (10.0, (2.0, 40.0)),
    "excl_per_1k":          (0.0, (0.0, 1.0)),
    "you_per_1k":           (18.0, (3.0, 45.0)),
    "marketing_per_1k":     (0.0, (0.0, 0.5)),
    "title_case_headings":  (0, (0, 0)),
    "bold_bullet_dash":     (0, (0, 0)),
    "emoji":                (0, (0, 0)),
    "self_describing":      (0, (0, 0)),
    "claudisms_per_1k":     (0.0, (0.0, 0.5)),
}

MARKETING = re.compile(
    r"\b(seamless(ly)?|robust|powerful|intuitive|elegant|effortless(ly)?|blazing|"
    r"delightful|beautiful(ly)?|leverage[sd]?|utiliz\w+|delve[sd]?|streamlin\w+|"
    r"empower\w*|unlock\w*|supercharge\w*|game.?chang\w+|cutting.edge|"
    r"state.of.the.art|best.in.class|world.class|first.class|battle.tested|"
    r"production.ready|hassle.free|out of the box|under the hood|behind the scenes|"
    r"crucial(ly)?|vital|pivotal|paramount|comprehensive|holistic|"
    r"journey|landscape|ecosystem|paradigm|synerg\w+)\b", re.I)
# Stock words readers identify as model-written on sight (tells.md, "Stock words").
# Phrase forms only: bare "seam", "surface", and "honest" are ordinary nouns and
# adjectives in technical prose, an array's or a tensor's shape is a real term, and
# "brief" counts only as a noun or verb for a prompt ("a brief summary" is fine).
# "own" counts only after "its", "their", or a possessive noun: "your own" and
# "on its own" are fine. "surface" counts only as a verb, so not after "the", "API",
# "every", or another word that starts a noun phrase ("the API surface" is fine).
# Inert subjects for the speech and reference verbs (tells.md, tell 2, false
# agency): a save, an operand, or a failure can't name, tell, or answer anything.
# Software subjects are left out because a program really does name and label things
# ("the game names the item"), and compound nouns like "file names" and "field
# names" are left out because they read as the plural noun.
INERT = (
    r"(failure|error|warning|operand|comment|save|string|byte|entry|instruction|body|"
    r"message|value|flag|path|result|record|header|row|cell|test|diff|log|trace|list|"
    r"card|doc|document|page|section|sentence|paragraph|line|index|pointer|argument|"
    r"parameter|prompt|text|note|table|map|script|heading|title|stub|listing|report|"
    r"commit|signature|address|offset)")
ADV = r"( (still|also|already|only|never|now|then|just|always))?"
# A relative clause whose subject is a negative quantifier (tells.md, tell 24):
# "a bit that no script sets", "FFFFh, which nothing reads", "every block no run
# reaches". Up to three words may sit between the quantifier and the verb ("no
# saved record covers", "nothing downstream reads", "no phase of play gates"), but
# not a form of "be", which starts a passive or a statement. "that" after a verb
# like "reports" or "written" starts a statement, not a relative clause ("it reports
# that no class can rise"), and "no longer" is a time phrase.
NEG_MODIFIERS = r"( (?!(is|are|was|were|be|been)\b)\w+){0,3}?"
NEG_SUBJECT = (
    r"(no (?!longer\b|more\b|matter\b)\w+" + NEG_MODIFIERS + r"|nothing" + NEG_MODIFIERS +
    r"|nobody|no one)( (ever|still|yet))?")
NEG_VERB = r" (\w+s|\w+ed|can|could|will|would|does|did|has|had)"
NOT_STATEMENT = "".join(r"(?<!\b%s )" % v for v in (
    "so", "is", "was", "enough", "fact", "idea", "states", "stated", "asserts", "asserted", "reports",
    "report", "written", "wrote", "saw", "see", "says", "said", "shows",
    "showed", "found", "finds", "confirms", "confirmed", "means", "checks", "checked",
    "verify", "verified", "knows", "known", "notes", "noted", "rule", "sure", "ensure",
    "ensures", "assumes", "assumed", "expects", "expected", "claims", "claimed"))
NEGATIVE_CLAUSE = (
    r"which " + NEG_SUBJECT + NEG_VERB + r"|" + NOT_STATEMENT + r"that " + NEG_SUBJECT + NEG_VERB +
    r"|(every|each|any|a|an|the) \w+ (no (?!longer\b|more\b)\w+|nothing|nobody) (\w+s|ever \w+s)")
CLAUDISM = re.compile(
    r"\b(load.bearing|the (honest |load.bearing )?seams?|honestly|"
    r"the honest (part|take|answer)|honest take|genuinely|smoking gun|the real story|"
    r"the actual (gap|problem|issue)|not a fluke|(that|deeper) tension|tension between|"
    r"a valid signal|doing real work|earns? its (keep|place)|a dial worth turning|"
    r"blast radius|evidence boundary|"
    r"(measured|checked|verified|tested|computed|generated|derived|run|executed)"
    r"(,| rather than| instead of)( not)? (written|guessed|recalled|assumed|asserted|"
    r"claimed|described|estimated|hand.written|by hand)|"
    r"worth (noting|naming|stating|mentioning|calling out)|here'?s the thing|"
    r"there'?s a catch|you'?re absolutely right|the key insight|"
    r"(?<!the )(?<!all )(?<!API )(?<!each )(?<!every )(?<!other )(?<!these )(?<!those )"
    r"(surfaces?|surfaced|surfacing) (the|an?|errors?|issues?|problems?|bugs?)|"
    r"(the|its|their|this|that|same|one|a|(?!(array|tensor)'s)\w+'s) shapes?(?! of (an? |the )?(arrays?|tensors?))|"
    r"\w+-shaped|shap(e|es|ed|ing) (the|how|what|by)|"
    r"(writer|fork|agent|subagent|verifier|worker|research|session|episode|task)'?s? briefs?|"
    r"(the|every|each|its|their|this|that|a|one) briefs?(?=[.,;:)]| (for|to|says|said|tells|names|gives|lists|asks|beside|above|below)\b)|"
    r"brief(ed|ing)? (the|each|every|a|its|their) (agent|subagent|fork|writer|verifier|worker|model)s?|"
    r"(?<!on )(its|their|\w+'s) own|"
    r"\b" + INERT + ADV + r" (names|named) (the|a|an|one|it|them|its|their|this|what|no|each|"
    r"every|exactly|only|\d|`|map|block|routine|file|variable|spell|item|monster|level)|"
    r"\b" + INERT + ADV + r" (tells|told) (it|you|them|us|the \w+) (which|what|where|how|when|whether|that)|"
    r"\b" + INERT + ADV + r" (answers|answered)|"
    r"speaks? (directly )?to (the|a|an|this|that|how|why|what|its|their)|"
    r"(investment|change|design|approach|step|decision|choice) buys|buys? (us|you)|"
    r"(point|argument|joke|message|claim|idea|punchline) lands|" + NEGATIVE_CLAUSE + r")\b", re.I)
CONTRACTION = re.compile(
    r"\b(it|that|what|there|here|he|she|who|let)'s\b|\b\w+'(t|re|ve|ll|d|m)\b", re.I)
SELF_DESCRIBING = re.compile(
    r"^\s*(>\s*)?(\*\*)?(This|The following|In this|Throughout this)\s+"
    r"(article|document|doc|page|guide|readme|section|tutorial|quickstart|how-to|"
    r"walkthrough|overview|reference|chapter|post|write-?up|note)s?\b", re.I | re.M)
EMOJI = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u26FF\u2700-\u2712\u2715-\u27BF]")


def strip_front_matter(text):
    return re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "x", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return text


def measure(raw, allow=()):
    raw = strip_front_matter(raw)
    nocode = strip_code(raw)
    headings = re.findall(r"^#{1,6}\s+(.+)$", nocode, flags=re.M)
    title_case = 0
    stop = {"a", "an", "the", "of", "in", "on", "to", "for", "and", "or", "with",
            "it", "is", "by", "as", "at", "vs"}
    for h in headings:
        h = re.sub(r"`[^`]*`", "", h)
        words = [w for w in h.split()
                 if re.match(r"^[A-Za-z][A-Za-z'-]*[,:!?]?$", w)     # plain words only
                 and w.lower().strip(",:!?") not in stop
                 and not re.search(r"[a-z][A-Z]", w)                  # not CamelCase
                 and not w.strip(",:!?").isupper()]                    # not an acronym
        if len(words) >= 2 and all(w[0].isupper() for w in words):
            title_case += 1
    # A bold-led bullet punctuated with an em or en dash. The bullet is not the
    # defect and is never counted on its own: the dash after the bold term is.
    # `**Term** - definition` and `**Term**: definition` are fine.
    bold_lead = len(re.findall(r"^\s*[-*+]\s+\*\*[^*]+\*\*\s*[—–]", nocode, flags=re.M))
    emoji = len(EMOJI.findall(nocode))
    self_describing = len(SELF_DESCRIBING.findall(nocode))

    text = nocode
    prose = "\n".join(
        l for l in text.split("\n")
        if l.strip()
        and not l.lstrip().startswith(("#", "|", "<", "---"))
        and not re.match(r"\s*>\s*\[!", l)
    )
    prose = re.sub(r"^\s*>\s?", "", prose, flags=re.M)
    words = prose.split()
    nw = max(len(words), 1)
    sents = [s for s in re.split(r"(?<=[.!?])\s+", prose) if len(s.split()) >= 3]
    sl = sorted(len(s.split()) for s in sents) or [0]
    per = lambda n: n / nw * 1000
    c = lambda pat: len(re.findall(pat, prose))
    return {
        "words": nw,
        "em_dash_per_1k": per(c("—")),
        "en_dash_per_1k": per(c("–")),
        "spaced_hyphen_per_1k": per(c(" - ")),
        "sent_median": statistics.median(sl),
        "sent_p90": sl[int(len(sl) * 0.9)] if sl else 0,
        "contractions_per_1k": per(len(CONTRACTION.findall(prose))),
        "semicolon_per_1k": per(c(";")),
        "parens_per_1k": per(c(r"\(")),
        "excl_per_1k": per(c("!")),
        "you_per_1k": per(c(r"\b[Yy]ou\b")),
        "marketing_per_1k": per(len(marketing_hits(prose, allow))),
        "title_case_headings": title_case,
        "bold_bullet_dash": bold_lead,
        "emoji": emoji,
        "self_describing": self_describing,
        "claudisms_per_1k": per(len(CLAUDISM.findall(prose))),
    }


def marketing_hits(text, allow=()):
    """Marketing-word matches, minus any word in `allow` (compared lowercase)."""
    allowed = {w.lower() for w in allow}
    return [m for m in MARKETING.finditer(text) if m.group(1).lower() not in allowed]


def report(name, m):
    print("\n%s  (%d prose words)" % (name, m["words"]))
    print("  %-22s %8s %9s %10s" % ("fingerprint", "doc", "target", ""))
    misses = 0
    for key, (typical, (lo, hi)) in BANDS.items():
        v = m[key]
        ok = lo <= v <= hi
        misses += not ok
        print("  %-22s %8.1f %9.1f %10s" % (key, v, typical, "" if ok else "<- out of range"))
    print("  %d of %d fingerprints out of range" % (misses, len(BANDS)))
    return misses


if __name__ == "__main__":
    args = sys.argv[1:]
    allow = ()
    if "--allow" in args:
        i = args.index("--allow")
        allow = tuple(w.strip() for w in args[i + 1].split(",") if w.strip())
        del args[i:i + 2]
    paths = args or ["-"]
    for p in paths:
        text = sys.stdin.read() if p == "-" else open(p, errors="replace").read()
        report(p, measure(text, allow))
        text = strip_code(strip_front_matter(text))
        found = sorted(set(m.group(0).lower() for m in marketing_hits(text, allow)))
        if found:
            print("  marketing words:", ", ".join(found))
        found = sorted(set(m.group(0).lower() for m in CLAUDISM.finditer(text)))
        if found:
            print("  stock words:", ", ".join(found))
