# Register

The register to write in for every document in this repository: plain developer documentation, in the plain-language sense of ISO 24495-1:2023. Every number here is per 1,000 words of prose unless noted otherwise. `scripts/check.py` measures them.

## The register in one paragraph

Plain declarative sentences addressed to *you*, in the present tense and active voice, with contractions wherever speech would use them. One idea per sentence, a colon before an example, parentheses for a short aside or an abbreviation. Nothing is called easy, powerful, or seamless. The reader decides that. Headings are sentence case. Lists are for steps, prerequisites, options, and link collections. The document ends when the information ends.

## Numbers

| Measure | Target | Model drafts | Notes |
|---|---|---|---|
| Em dash `—` | 0.0 | 14 to 27 | The strongest single tell. |
| En dash `–` | 0.0 | 0.8 to 1.3 | Write ranges as `3-5 minutes`. No `--` either. |
| Spaced hyphen ` - ` | about 2 | 0 to 6 | The only dash to use. It's for a light aside, and for `**Term** - definition` lists. |
| Semicolon | 0.1 | 4 to 5 | Effectively never. Two clauses get two sentences. |
| Colon | about 10 | about 8 | Common: it introduces an example, a list, or the code that follows. |
| Parentheses `(` | about 10 | 13 to 20 | Abbreviations `(ECL)`, "for example" asides, a clarifying word. |
| Exclamation | 0.0 | 0 | None. A cheerful send-off (*Have fun!*, *Happy coding!*) is a model tell. |
| Sentence length, median | 20 words (docs), 11 (reference one-liners) | 15 to 24 | Similar medians. The difference is what the long ones are made of. |
| Sentence length, 90th percentile | 33 | 40 to 44 | A long sentence is one clause with qualifiers, not three clauses spliced. |
| Contractions | about 15 | 6 to 12 | *it's*, *you'll*, *don't*, *you've*, *that's*, *isn't*, in reference material too. |
| *you* / *your* | about 18 / 16 | 1 to 6 | The reader is the subject of most instructions. |
| *we* | under 1 | 0 | Only for a recommendation the project makes: *we recommend*. |
| *I* | 0.0 | 0 | Never in docs. Fine in a commit message or a PR description. |
| Evaluative adjectives | about 0 | 1 to 12 | *seamless*, *robust*, *powerful*, *intuitive*, *elegant*, *battle-tested*. |
| Title Case headings | 0 | most | Sentence case, always. |
| `e.g.` / `i.e.` | 0.0 | varies | Write *for example* and *that is*. |
| Unicode emoji | 0 | varies | None. |

## Sentences

A sentence starts with its subject or with a short framing clause, and then makes one point. Common openers: *The* ..., *If you* ..., *To* [do X], ..., *For* [more information / example] ..., *You* ..., *This* ..., *When* ..., *Because* ...

Framing clauses come first and are short: *If you'd like to skip the harness, run the engine with `--no-check`.* *Because the run is deterministic, the corpus stores inputs, not memory.*

A long sentence is fine when the extra length is qualifiers, not extra ideas. *When the two engines diverge, the harness reports the first input where they differ, the state fields that differ, and the random seed in each engine* is one idea. A sentence of the same length that splices three facts with two dashes is three ideas. Split the second kind. Leave the first.

Transitions to use: *also*, *instead*, *however*, *typically*, *for example*, *in that case*. Transitions to drop: *additionally*, *furthermore*, *moreover*, *importantly*, *crucially*, *notably*, *in other words*, *behind the scenes*, *under the hood*.

## Diction

- **Never open by describing the document.** No *This document explains*, *This README covers*, *In this guide, you'll learn*, *This section walks through*, or any variant. The title and the context already say what the reader is looking at. Delete the sentence. If it stated a fact the reader needs (a prerequisite, a scope limit), state the fact directly.
- **Say the fact, not the evaluation.** No *simply*, *easily*, or *just* as minimizers. No adjectives whose only job is approval. Let the reader decide whether something is easy, simple, or good.
- **State recommendations explicitly.** *We recommend ...*, *Don't ...*, *Always run the lockstep tests before you merge a change to the rules.* Not hedged, not implied.
- **State limits as limits.** *The engine loads saves **only** from Pools of Darkness.* *You **can't** replay a log from a save file.* Bold the operative word (*only*, *can't*, *not*), sparingly.
- **Introduce a term once, in italics, then use it plainly.** Introduce an abbreviation in parentheses at first use: *Event Control Language (ECL)*.
- **Use a fixed form for cross-references.** *For more information about X, see Y.* *To learn more about X, see Y.* Link text is the target's title, not "here" or "this page".
- **Use plain verbs for software.** The engine *loads*, the harness *compares*, the CLI *reports*, the server *returns*. Software isn't *honest*, doesn't *remember*, doesn't *want*. Inert things don't act at all: a file contains text, and a log lists inputs.
- **Be concise.** Make each document as short as possible but as long as it needs to be.

## The reader

Second person, imperative for steps, present tense. *Enter the path to your game folder. You can change it later.* State the reader's situation in a conditional, then answer it: *If you haven't installed Rust, install it with rustup.*

Name UI elements exactly and in bold: *Select **Play Demo**.* Put code identifiers, commands, and file paths in backticks.

## Structure of a docs page

1. **What it is and what it's for**, in one paragraph. Then one sentence on what the reader gets from it. No tagline, no "why you'll love it".
2. **Prerequisites**, as a short plain list of only the things the reader must already have. If the instructions are going to get something for the reader, it isn't a prerequisite.
3. **Install or getting started**, with commands the reader can copy and paste, and no prompt prefix.
4. **The core tasks**, one section each, with a sentence of context and the code.
5. **Next steps**: a list of specific links, not a link to a home page. Nothing after the list.

A conceptual page opens on the subject itself, states the concept in declaratives, puts a note where a reader would otherwise trip, and ends with next steps and links.

## Lists and callouts

- Numbered lists for steps the reader performs in order. Each step is one imperative sentence, sometimes with a second sentence of consequence: *Run `cargo test`. When the tests finish, the harness prints the scoreboard.*
- Bulleted lists for prerequisites, options, and link collections. Items are plain. A `**Term** - definition` item uses a spaced hyphen, never an em dash.
- When you draft from nothing, write a description of what the software does as prose. That doesn't mean you convert a list that a draft already has. Under tell 10 in `tells.md` (dashes and wording inside list items), an existing list stays a list, and you fix the dash and the wording inside each item.
- Callouts (`> [!NOTE]`, `> [!TIP]`) contain one or two sentences the reader needs before the next step, not asides.

## Headings

Sentence case. Verb first for task sections (*Build the engine*, *Replay a log*, *Run the harness*), noun for concept sections (*Lockstep runs*, *Prerequisites*, *Next steps*). No emoji, no numbering, no colons.

## What to keep from a model draft

Facts, code, commands, link targets, and any sentence that already reads like the "after" lines in `tells.md`. In an edit in place, keep the section order too, and limit the job to cutting and rephrasing. In a rewrite for the reader, `SKILL.md` describes what moves and what goes.

## Commit messages and PR descriptions

These use a different register: first person, direct, short. In a commit message, say what changed and why, at a length that fits the change. In a PR description, say what changed, why, and what the reviewer should check. *I added the ECL interpreter's jump opcodes. All 14 pass in lockstep. Check the wrap in `op_jump_rel`, which the specification puts at 8 bits.* The docs numbers above (*you* at about 18 per thousand words, *I* at zero) don't apply here, and `check.py` isn't meant for these.

Code comments are short statements of the code's intent, sometimes in the first person plural: *The specification wraps this value at 8 bits, so the add stays `u8`.* *Always restore the seed, even when the step fails.*
