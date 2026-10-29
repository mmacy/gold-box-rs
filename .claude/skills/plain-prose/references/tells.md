# Tells

What marks prose as model-written, and what to write instead. Each entry is absent from, or rare in, plain developer documentation (`register.md` describes that register and gives its numbers). The "before" lines are real lines from model-written READMEs, docs, and replies. The "after" lines state the same fact in the target register.

The tells in the first group change what a sentence means, so fix those first. When the fix names something the draft left unnamed, verify the new wording against the code before you make the edit (see "Verify before you change what a sentence claims" in `SKILL.md`). The tells in the second group change how a sentence sounds. The third group is about what a document contains and where the answer sits. The fourth group is about grammar that the reader has to work to parse: a phrase packed into fewer words than the reader needs, or a clause that makes the reader hold a noun and then cancel a whole set of things. On the second read that `SKILL.md` describes, check tells 17 through 21 again. After the tells come a list of stock words, a short table of word swaps, and a list of what to leave alone.

## Contents

Other documents cite a tell by its number in this list (*tell 18*), so don't renumber the tells. Give a new tell the next unused number.

**Defects of meaning**

1. The metaphorical carry, and hold or keep where contain, fit, or remember belongs
2. False agency
3. Unresolved and drifting referents
4. History, journey, and confession
5. Compression jargon and coined terms
6. Passive voice where the actor is known

**Register**

7. The document describing itself
8. The em dash, and the colon where a comma belongs
9. Literary register
10. Dashes and wording inside list items
11. Title Case headings and taglines
12. Evaluation, persuasion, and flattery
13. Stage-direction openers, teasers, and closers
14. Semicolons, clause stacking, and density

**What the document contains**

15. The buried answer
16. Comments and commit messages that outweigh the code
17. Absolute qualifiers
18. Insider shorthand
19. Two ways, one example
20. Material that serves someone other than the reader
21. The repeated slogan

**Compressed syntax**

22. Noun stacks
23. Nouns used as verbs
24. Relative clauses with a negative subject

**Reference lists**

- Stock words
- Word swaps
- Not a tell

## Defects of meaning

### The metaphorical carry, and hold or keep where contain, fit, or remember belongs

"Carry" meaning include, contain, have, or hold: *the file carries the license text*, *each flag carries a dismissal mark*, *an id carrying a slash*. "Carry" meaning remember is the same defect as "keep" below: *this is the thing to carry*, *the picture to carry*, *small enough to carry*. Write the verb actually meant. A file includes or contains text, a list contains entries, an item has a property, an id names a target. Carry is for literal carrying: a person, character, or vehicle holding and moving an object.

"Hold" gets the same treatment. Write *contain* for containment: a log contains lines, a save contains data, a cache contains items, a result contains the dice and the total. Write *fit* for capacity: at most 2-3 fit side by side in a 10-foot passage. Write *keep* or *have* for a kept reference: you keep one session per game, your game has custom classes. That leaves *hold* for logic (the condition must hold, the theory still holds) and for literal or idiomatic holding (hold the line, hold fire).

"Keep" is overloaded the same way, in two senses. Keep meaning remember or take away: *the fact to keep*, *two numbers worth keeping*, *if you keep four things from this episode, keep these*. Write *remember*: the fact to remember, two numbers worth remembering. Keep meaning an inert thing has, records, or retains something: *the report keeps the corrected versions*, *the model doesn't keep unknown fields*. Write the verb meant, the same ones that replace carry and hold: contains, includes, has, records, or lists. The report contains the corrected versions, the log lists each run, and the model drops unknown fields. That leaves *keep* for a person or program choosing to retain or continue something (you keep one session per game, keep the default, keep reading) and for idioms (keep in mind, keep up, keep apart).

Before: *Each save carries the party's position and the turn count.*

After: *Each save contains the party's position and the turn count.*

Before: *Here's the fact to keep: on September 28, the SDK file had the endpoint and the docs file didn't.*

After: *Remember this date: on September 28, the SDK file had the endpoint and the docs file didn't.*

### False agency

Inert things given verbs they can't perform: a door wants a key, a gate says so, a room rolls monsters, a card generates treasure, a file logs a warning about itself, a source refuses, a page remembers, a keyboard can't tell left from right. Name the real actor: the engine, the app, the editor, the dice, the user.

Before: *A trap shows no trigger field.*

After: *The builder shows no trigger field for a trap.*

Before: *Leaving a game is honest about what it costs: the menu's return, save, and load destroy nothing.*

After: *Return, save, and load don't change anything.*

Ownership and knowledge are the same defect in quieter verbs. *The engine owns every roll*, *the engine only knows 3d6 in order*, *the plugin creates the directory the first time it needs it*, *the compiler records every swap*, *every session after that plays from the bundle*, *the skill takes it from there*. Engines make rolls and have rules for things. They don't own or know them. A directory gets created when a person does something, so name the software that creates it and the thing the person did. "The compiler" in a draft is usually a skill, a script, or Claude running one of them. Find out which and name it. Name who acts, and when the reader is the one acting, make the reader the subject.

Before: *The engine only knows 3d6 in order, so there's no 4d6-drop-lowest.*

After: *The engine builds characters from 3d6 in order, and the referee's rules say not to use any other method, so there's no 4d6-drop-lowest.*

Before: *Your logs live in `~/gold-box-logs`, which the harness creates the first time it needs it.*

After: *Your logs live in `~/gold-box-logs`, which the harness creates the first time you record a log.*

Before: *The `compile-adventure` skill takes it from there and shows you the map before the bundle is accepted.*

After: *Claude takes it from there with the `compile-adventure` skill. It shows you the map to check, and you sign off before it uses the bundle.*

Speech and reference verbs are the same defect again, and the most common one is *names*. A failure, an operand, a save, a comment, or a table entry *names* something. A map *tells* a routine which wall to draw, a table *answers with* a word, a design *speaks to* a need, and one investment *buys* three things. The verb hides the relation. Write the relation: the save *contains* map 20, the operand *is* a block number, the comment *gives* the wrong address, the card *mentions* a program, the game text *cites* a journal entry by number.

Before: *A failure names one routine.*

After: *When a test fails, you know which routine is wrong.*

Before: *Every `NEWECL` with an immediate operand names a real block.*

After: *In every `NEWECL` with an immediate operand, the operand is the number of a real block.*

Before: *The map tells it which wall type is on each square.*

After: *The routine reads the wall type for each square from the map.*

People name things, and so does software that assigns or shows a name: the game calls the item "Potion" until it's identified, and `poolr.ecl` labels the runes in its listings. Even then, a plainer verb usually reads better (*calls*, *labels*, *shows the name*). A document that cites a source is fine.

A relative clause whose subject is an absence, like *a bit that no script sets*, is tell 24.

Software may be the subject of an action it performs: the editor draws the map, the CLI reports the error, the panel says so, the server returns a token, the engine rolls the dice. People and in-fiction characters are subjects of whatever they do. Stative verbs are fine for inert things (holds in the logical sense, governs, applies, sits, encloses), and so are physical events in a game's fiction (a trap springs).

### Unresolved and drifting referents

"It" or "them" with a shifting, distant, or not-yet-introduced referent. "Both" or "either" that never name their members. "Those X" pointing at a noun that never appeared. A filename used as the subject of a sentence about what a person did (*`session.py` decided to cache the token*). A pronoun whose antecedent changes between the start of a sentence and its end. Each pronoun gets one obvious, nearby referent, and each quantifier names its members, even at the cost of repetition.

Before: *Load the save and open the map. It appears in the left panel.*

After: *Load the save and open the map. The map appears in the left panel.*

Before: *`session.py` now validates the token before it reads the cache, so it never sees a stale one.*

After: *The session loader validates the token before it reads the cache, so the cache never returns a stale token.*

### History, journey, and confession

A durable document states current truth and forward-looking rationale. Git history records how the document came to be. Remove:

- **Decision history.** *Originally X, then changed to Y*, decision dates, *a survey found ...*, *inspection showed ...*, *as of 2025*, a list of every alternative that was dropped. Changelogs and ADRs are history documents by design and are exempt.
- **Past states in code comments.** What the code used to do, why the earlier approach was wrong, why a constant was bumped on a given date.
- **Session detail.** Row counts from a dev instance, a reference to a review document that was never committed, the user's name (*the owner said X, so I did Y*), and time estimates for how long ago something happened.
- **Journey narration.** *This looked like a red herring but turned out to matter*, *the real story*, *the smoking gun*, *not a fluke*. State the finding.
- **Narrating what was not done.** *I edited this file but did not edit the README and did not commit.* In code, when the code already shows it: *returns directly, not through a callback.* A reader learns what the code does from the code. Name what was left undone only when the owner has to act on it.
- **Escalating self-correction.** *It's worse than what I'd previously stated.* *My earlier explanation was wrong about more than I said.* Say the corrected fact once.
- **Apology and post-mortem.** *That one is on me. This won't happen again.* *The mistake was mine.* For a mistake in a PR description, a commit message, or a summary: the cause in one sentence, the fix in one sentence, nothing else.

### Compression jargon and coined terms

Arrow chains (*A → B → fails*, *plan + PDF → sessions/NN.script.json*), hyphen-stacked compounds, terse fragments where sentences belong, and names for mechanisms that match nothing in the codebase or the docs: *rotation slabs* for log rotation, *evidence boundary*, *UIM-001*, *this leg of the decision tree*, a label or codename invented mid-task and never introduced. Write the sentence with the terms spelled out, using the name the code or the docs already use for the thing. In a table, an arrow column becomes two columns or a sentence in one column, and that's a permitted change to the table.

A domain term or coinage used without definition anywhere in the docs is the same defect. Define it at first use when you can verify the definition against an authoritative source. A clause is usually enough, and a tool or sibling project gets a link. Terms you can't verify go in the closing message with their locations.

### Passive voice where the actor is known

*Individual clips are concatenated into a single MP3* when the pipeline does the concatenating, *the finished episode is uploaded* when the app uploads it, *each application needs to be registered* when the reader registers it. The defect is a passive that leaves the reader to work out who acts. An implied actor costs the reader a translation at best, and at worst the reader guesses wrong. Whether the actor is obvious is not the writer's call, any more than whether a step is simple or easy. The writer's job is to make it obvious. Name the component, and address the reader as *you*: *you register each application*, *Batch downloads the package onto each node*. Naming the actor is a claim, so verify it against the code first, as `SKILL.md` describes.

A passive can hide in a noun phrase with no verb at all. *The first launch after installing takes a few seconds longer* has nobody launching and nobody installing. Put the reader back: *The first time you launch Claude Code after you install the plugin, expect a few extra seconds.* The pattern is an article, a noun for an action, and a preposition with a gerund: *the first launch after installing*, *the initial run before configuring*, *a restart on updating*.

## Register

### The document describing itself

*This article describes ...*, *This document explains ...*, *This README covers ...*, *In this guide, you'll learn ...*, *This section walks through ...*, *Here is the breakdown ...*. The title and the surrounding context already say what the reader is looking at, so the sentence adds nothing (see Diction in `register.md`).

Delete the sentence. If it stated a real fact (a scope limit, a prerequisite, who the reader is assumed to be), state that fact on its own.

Before: *This article describes how to replay an input log against the original game.*

After: *Replay an input log against the original game.* (or go straight to the first step)

Before: *In this quickstart, you learn how to build the engine and run its tests.*

After: *To build the engine and run its tests:*

The same rule applies mid-document: *This section covers ...*, *The following sections describe ...*, *As mentioned above ...*, an intro paragraph that restates the content of the sections below, an outro paragraph that restates the sections above. Say the thing. A one-sentence lead-in to a list is not this tell (*The harness compares four things after every step:*). Those are fine.

### The em dash, and the colon where a comma belongs

The em dash is the most reliable single tell, and plain documentation doesn't use it. Model prose uses it mostly to splice two clauses or to set off a phrase that renames the noun before it.

Replace each one with the punctuation that does the same job:

- A full stop, when the dash joins two independent clauses.
- A comma, when it sets off a short aside.
- A colon, when what follows explains or lists.
- Parentheses, for an aside the reader can skip.
- A spaced hyphen ` - ` only for a light, conversational aside, rarely more than one per paragraph.

Before: *A new engine for Pools of Darkness — written in Rust and checked against the original, byte for byte.*

After: *A new engine for Pools of Darkness. It's written in Rust, and a harness checks it against the original game byte for byte.*

Before: *Sessions live in server memory. Use **Save** (or the menu — Esc) to snapshot to disk; saves survive server restarts and are named for where they stand ("The Cold Vein — level 1, turn 60") or whatever you rename them to.*

After: *Sessions live in server memory. To save one to disk, use **Save** or the menu (Esc). Saves survive server restarts. Each is named for where the party is ("The Cold Vein, level 1, turn 60") unless you rename it.*

En dashes in ranges (*3–5 minutes*) get the same treatment: write *3-5 minutes*.

A model told to stop using em dashes moves the same splice onto a colon. A colon introduces an explanation, an example, or a list. When the second half is just the next clause, use a full stop or a comma. *The fix is small: one line in the loader* is a colon doing its job. *The loader is fast: it runs on every request* is a colon where a full stop belongs.

### Literary register

Models decorate documentation with metaphor, inversion, and cadence. Plain docs are declarative. The warmth comes from directness and the occasional aside, not from imagery.

Before: *And if the dark takes the whole party first — a fight, a trap, the long cold — that ending gets a screen too.*

After: *If the whole party dies, you get a different ending screen.*

Before: *...so they are on your phone by morning, even with the Mac asleep.*

After: *...so the episodes are available on your phone the next morning.*

Before: *A dead drag handle during a booked half-day you do not get back.*

After: *The drag handle didn't work, and the session was booked for a half-day.*

Watch for:

- **Metaphor and analogy** where a plain statement would do: *the bucket that drips into the ocean*, *a smoking footgun*, *blast radius*, *prose a person has to sign*. Swapping one metaphor for another (*has to put their name on*) is not a fix. State the fact or drop the clause.
- **Negative parallelism** as a rhetorical pattern: *not X, it's Y*, *X rather than Y*, where X was never on the table and exists only to be knocked down. State Y. A contrast with a real alternative stays (*the response comes from a tenant, not /common*).
- **Method contrasts**: *measured rather than written*, *run instead of written*, *derived, not hand-written*, *generated from the scripts, not from play*, *measured, not guessed*. The second half names a way of working that nobody proposed, so the sentence boasts about rigor and leaves the reader to work out what the thing is. Say what it is and where it comes from: *the harness lists every routine where the two games differ*. A method stays when it changes what the reader does or trusts (*the counts come from a scan that misses near calls, so they're lower bounds*).
- **Personified software** (*the page remembers*, *the door stays open*) and ritual-sounding nouns (*the tale is told*, *3d6-in-order honesty*).
- **Tricolons built for rhythm** (*a fight, a trap, the long cold*) and participle-phrase pileups.
- **Flourishes**: *the X itself*, *the X's own* (see *own* under stock words), *the shape stays*, *the task wins*.
- **A fact restated for effect** after it has been stated once: *so the commit landed on a branch nobody was going to merge*.
- **Punchline cadence**: short sentence, then a shorter one for effect. The clickbait rhythm of a talk, not a doc.
- **Slogan UI copy**: *Your keys, supercharged.* *Searches the app remembers.* UI strings say what the control does.

### Dashes and wording inside list items

Model READMEs punctuate every enumeration as `- **Term** — definition`, and the item after the dash is usually a fragment with its modifiers stacked up. The list is not the problem. Bullets suit prerequisites, options, link collections, and steps, and a definition list is a fine format.

Fix two things, both inside the item:

- **The dash.** `**Term** — definition` becomes `**Term** - definition` (spaced hyphen) or `**Term**: definition`. Both are fine. Never an em dash, never an en dash.
- **The wording.** Rewrite the item the way you would rewrite a sentence: drop the evaluative adjective, unstack the modifiers, name the actor, spell out the arrow chain, resolve the pronoun. An item may become a full sentence, and often should.

Before:

```text
- **HN Pulse** — the original mode. Auto-discovers Hacker News front-page stories matching a selected topic...
- **Study Session** — feed in up to 100 sources (article URLs, pasted text, and/or uploaded files)...
```

After:

```text
- **HN Pulse** - finds Hacker News front-page stories on a topic you pick and turns them into a daily news-style episode.
- **Study Session** - takes up to 100 sources (URLs, pasted text, or uploaded .txt and .md files) and produces an educational episode that walks through them.
```

Leave a list a list. Never convert a bulleted or numbered list into a paragraph, and never merge items. When you draft from nothing, running prose often reads better than bullets, but that's not a reason to restructure a document that already has lists. Converting a list also introduces other tells: a distributive *each* or *every* at the front of every resulting sentence, one sentence pattern repeated down the run, and pronouns pointing across a paragraph break at nothing.

### Title Case headings and taglines

Headings are sentence case (*Getting started*, *Subscribe to battle events*). Models write *How It Works*, *Getting Started*, and open with a blockquoted tagline. Change the case and delete the tagline.

### Evaluation, persuasion, and flattery

Keep to the facts, and let readers decide whether something is easy, simple, or good. Delete or replace: seamless, robust, powerful, intuitive, elegant, effortless, delightful, blazing, production-ready, battle-tested, first-class, *just works*, *simply*, *easily*, and every superlative. Delete the sentences whose only job is to contain those words (*Whether you're building X or Y, Z has you covered*), any aside whose only job is the writer's opinion of the fact just stated, and any sentence written to persuade rather than inform.

Flattery is the same defect pointed at the reader: *You're absolutely right*, *Sharp, appreciate the pushback*, *you already own the right question*, *your understanding of X is better than most people's*, *the reason it lands is ...*. Delete the sentence. It never contains a fact.

Before: *...which produces natural turn-taking and contextual prosody.*

After: *...which handles turn-taking between the two voices.* (or delete, if the fact isn't needed)

### Stage-direction openers, teasers, and closers

Openers: *Behind the scenes*, *Under the hood*, *Importantly*, *Crucially*, *Notably*, *Additionally*, *Furthermore*, *Moreover*, *Note that*, *It's worth noting*, *worth naming*, *worth stating explicitly*, *In other words*, *The honest part?*, *Honest take:*, *Let's take them one at a time*, *Let's take them as three groups*. Start the sentence with its subject.

Teasers: *Here's the thing*, *But there's a catch*, *Here's why X matters*, *Here's the part that matters most*, *Here's the part no one is talking about*, *The point is ...*, *The key insight is ...*, or any sentence whose job is to announce the next sentence. Delete the teaser and keep the sentence it announced.

Closers: a final sentence that restates the paragraph (*Either way the door stays open*), a sign-off paragraph summarizing the document, a cheerful send-off (*Happy coding!*, *Have fun!*, *Enjoy!*), a trailing caveat or *one thing worth noting* that repeats something already said, a side quest the reader didn't ask about, or an offer (*Want me to fix this before we move on?*, *Would you like me to explain more?*). End when the information ends. Don't add a closing line of any kind.

### Semicolons, clause stacking, and density

Model sentences run 25 to 45 words, glued with semicolons and dashes. Sentences in plain docs have a median of about 20 words (11 in reference one-liners) and a 90th percentile of about 33. Long ones exist, but they're one idea with qualifiers, not three ideas spliced. Semicolons are effectively absent (0.1 per thousand words). Split at the semicolon. Each half is usually a complete sentence already. The target is plain language in the ISO 24495-1:2023 sense: short sentences, one idea per sentence, terms defined at first use.

Density is the same defect at paragraph scale. A model told to stop using dashes and parentheticals packs the same clauses into longer sentences with fewer paragraph breaks, and a dense paragraph is as hard to read as a long sentence. Write one idea per sentence and one topic per paragraph, and start a new paragraph wherever the topic changes.

## What the document contains

### The buried answer

Ten paragraphs that sum to *it's fine*. The reader's question is answered in the last paragraph, or in a caveat after the summary, or never. When the answer, the outcome, or the recommendation appears somewhere in the section, move that sentence to the front of the section. That is a wording change within a section, not a restructuring.

Mechanics without consequences is the same defect. A paragraph that explains how a thing works and never says what that means for the reader leaves the reader to ask *so what does this mean for me?* If the draft states the consequence elsewhere, move it up. If the draft never states it, the missing consequence is a claim the draft didn't make, so verify it against the code before you add it, as `SKILL.md` describes.

### Comments and commit messages that outweigh the code

An inline comment on every method, a comment that says what the next line does, a 25-line comment explaining a constant, a commit message longer than the diff. When you write a new inline comment, use it only to state a constraint the code itself can't show. In an existing comment, reword only what's needed to remove a tell, so a later agent doesn't copy the pattern. Don't delete or restructure the comment. A commit message says what changed and why, in the size the change deserves. Docstrings are a different thing: they are the input to the API reference, so keep a docstring's summary line and its Args, Returns, and Raises sections. Fix the prose inside them and leave the structure.

### Absolute qualifiers

*And nothing else*, *no exceptions*, *always*, *ever*, *only knows*, *strictly*, tacked onto a limit for emphasis. The limit was already stated. The qualifier makes the sentence sound like a rule being enforced on the reader, and it invites the reader to test it (*I bet if you asked for 4d6 it'd roll it*). State the limit once, and give its reason if the reader might push on it.

Before: *The engine rolls 3d6 in order and nothing else.*

After: *The engine builds characters from 3d6 in order, and the referee's rules say not to use any other method.*

Before: *The engine has rules for the monsters and items in the SRD and nothing else.*

After: *The engine has rules only for the monsters and items in the SRD.*

### Insider shorthand

A phrase that compresses a paragraph of the writer's context into a few words the reader can't unpack: *a creature whose special ability is the whole fight*, *captures this side of the data*, *confirms the tool names live*, *parity-plus*, *engine-divergent*, *the consequential divergence*, *reproduced via compile*, *the trade, stated honestly: gained / paid*, *standing per-turn schema*, *the play tool surface*. It's compression jargon (tell 5, compression jargon) without the arrow. The writer knows what it means, and the reader has to ask. The test: could the reader explain the phrase to another user without opening the code? If not, write the sentence the phrase stood for, with what it means for the reader, and a concrete case if one fits in a clause.

Before: *The engine has no rule for a creature whose special ability is the whole fight.*

After: *The engine has no rule for a monster whose special power is the point of the encounter, where swapping in a stock SRD monster would lose what the fight is about.*

Before: *The trade: **Gained:** determinism and amortized cost. **Paid:** an explicit compile step and SRD-only fidelity.*

After: *Compiling changes a few things:* then a list, one plain sentence per change, of what the reader sees differently in play.

Before: *`capture_token_artifacts.py` captures this side of the data.*

After: *`capture_token_artifacts.py` gathers this project's half of the numbers.*

### Two ways, one example

*Type the slash command, or say what you want in your own words:* followed by the slash command only. *Ask to save at any point.* *You can ask to see the roll log.* Each way of doing something the document names gets an example the reader can type. A prompt example is a fenced `text` block with the sentence a person would say.

### Material that serves someone other than the reader

*It's a sibling to X, not a replacement for it.* *The counts come from a scan of 34,000 instructions.* *Sources are the diary entries and the format docs.* *This section was rewritten after the second review.* Each of these is for someone else: a contributor weighing the project against X, the writer showing their evidence, the writer keeping a record. The test for any sentence is whether it helps the reader do the job the document is for. If it doesn't, cut it, or move it to the section written for the person it does help (a contributor section, a maintainer's README) and introduce any term it depends on once, in a clause, at that spot. A reason stays when it changes what the reader does (*don't edit the number by hand, re-measure it*). Evidence for how the writer knows goes (*measured over 34,000 instructions*). A comparison with another project belongs where a reader chooses between them, never in the introduction of the one they already chose.

### The repeated slogan

A short, quotable phrase that the draft liked enough to use twice: *the dice are real* in the intro and again under How it works. The first use is a claim, and the second is a refrain. Keep the fact in the place the reader needs it and write the second occurrence as the plain fact it stood for (*no roll is ever made up*), or cut it.

## Compressed syntax

Clark, Martin, and Mahowald measured the constructions that model output uses more than human text, and that are known to slow readers down ([*Why is AI-generated language so hard to understand?*](https://arxiv.org/html/2610.29162v1)). Inanimate subjects with animate verbs are tell 2, false agency. Long sentences are tell 14. The first two sections below are the rest of the paper's constructions that show up in model-written developer prose. Their examples are from model-written PR descriptions. The third section, tell 24, isn't from the paper. Model drafts use it often, and it slows the reader for the reasons its section gives.

### Noun stacks

Three or more nouns in a row, or a noun with a hyphenated compound in front of it, where each word modifies the next: *the item-identity namespace*, *the rolled-damage site*, *a depth-4 cascade bound*, *dropped-consequence records*, *the never-contains list*, *the honest-minimum treatment*. To read one, the reader works backward from the last noun and guesses how each word relates to the next. The writer knows those relations, and the reader has only the words.

Unpack the stack with a preposition, a relative clause, or a verb. A stack that is the name of something the reader already knows stays: *RNG stream keys* where the docs define stream keys, *SRD data pipeline* where the README introduces the pipeline, and a product or function name.

Before: *A passing `half` save set the halved flag, read only at the rolled-damage site.*

After: *A passing `half` save set the halved flag, and only the code that rolls damage read it.*

Before: *Valuables stay id-less so the catalog remains the single item-identity namespace.*

After: *Valuables have no id, so every item id comes from the catalog.*

### Nouns used as verbs

A noun made into a verb as a metaphor, where a plain verb exists: the plan *pins* the details (states, decides, or tests them), a feature *ships* or *lands* (is released, is merged, or appears), loot drops *key off* a condition (depend on it), a check is *folded into* the loop (moved into it), a value is *wired* or *threaded* through (passed). In one set of 60 model-written PR descriptions, *pin* appears 98 times in 25,000 words. One of those pins a Python version. The other 97 mean decided, specified, or locked by a test. *Surface* as a verb, in "Stock words", is the same tell.

Write the plain verb. A noun-verb for the literal operation stays: pin a dependency version, seed a random number generator, stamp a document when a function named `stamp_document` does it, and gate a command when the project defines gates.

Before: *The plan pins the contract-laden details the spec leaves open.*

After: *The plan decides the details of the contracts that the spec leaves open.*

Before: *Outcome classification and loot drops key off the `dead` condition.*

After: *Whether a monster counts as killed, and what it drops, depend on the `dead` condition.*

### Relative clauses with a negative subject

A relative clause whose subject is *no X*, *nothing*, *nobody*, or *no one*: *values that no saved record covers*, *memory unsafety that no current caller reaches*, *a diary entry number that no other subagent has*, *`labs-leanstral-1-5-1`, which no model file lists*. Don't write one. The rule holds whatever the subject is: a person, a program, or an inert thing.

The clause is slow to read for two reasons. First, the noun before *that* is the object of the clause's verb, so the reader has to hold it until the verb arrives at the end. Second, the negative sits in the subject, so the reader pictures every record, caller, or subagent and then cancels them all. When the clause sits inside the subject of a longer sentence, the main verb comes only after it: in *a combatant that no enemy outruns flees*, the reader reaches *flees* last.

Rewrite it in one of these ways, in this order of preference:

- Use an adjective or a participle: *every unreached block*, *a unique diary entry number*.
- Make the real actor the subject, and put the negative in the verb with *never* or *doesn't*: *the scripts never set that bit*.
- Put the negative after the noun: *values not in any saved record*.
- Split the sentence: *The API also returns `enrollment`. No spec or SDK describes it.*

Before: *The coverage report lists every block that no run reaches, with a reason.*

After: *The coverage report lists every unreached block, with a reason.*

Before: *The script tests bit 2 of `0x4AA0`, which no script sets.*

After: *The script tests bit 2 of `0x4AA0`, but the scripts never set that bit.*

Before: *A combatant that no enemy outruns flees.*

After: *A combatant flees when no enemy outruns it.*

Before: *Give each subagent a diary entry number that no other subagent has.*

After: *Give each subagent a unique diary entry number.*

These are fine:

- A plain negative statement: *no monster in `MON1CHA.DAX` has more than 162 hit points*, *there's no class test*.
- A negative subject in a clause that isn't a relative clause: *it reports that no class can rise*, *so that no request is sent*, *when no enemy outruns it*.
- *No longer* and *no more*, which are time and quantity phrases, not subjects.

The scorer lists each *that* or *which* followed by *no*, *nothing*, *nobody*, or *no one* and a verb within a few words. It also lists some statements, like *the reason is that no other signal separates them*, so read each match.

## Stock words

Readers now identify these words and phrases (the *Claudisms*) as model-written on sight. Every one is fine in the rare sentence that means it literally. As a habit, each one is a tell, and the fix is the plain word for what the sentence means.

| Stock | What it usually means | Write |
|---|---|---|
| load-bearing | required, relied on | *X depends on Y*, *required* |
| seam, the honest seam | boundary, interface, the point where two things meet | the boundary, the interface, the call |
| honest, honestly, the honest part | (nothing) | delete |
| genuinely, truly, really | (nothing) | delete |
| sharp, sharper | clear, better, precise | the specific quality meant |
| smoking gun, the real story, the actual gap, not a fluke | the cause, the finding | *the cause is X* |
| that tension, a deeper tension, doing real work, a valid signal | a conflict, a tradeoff, a reason | name the two things in conflict |
| pin, wedge, rung, lever, dial, a dial worth turning | a setting, a step, a fix | the setting, the step, the fix |
| earns its keep, earns its place | is worth having | *is worth having*, or delete |
| matters, what matters most, matters more than it sounds, the one that matters | (importance asserted, not shown) | say what it changes: *the order decides which patch wins*, or delete |
| shape, shapes, shaped, -shaped: *the shape of the plan*, *the draft's shape*, *a human-shaped sentence*, *the shape of an example*, *the edits with that shape*, *the API's shape* | structure, format, form, layout, pattern, scheme, architecture, API surface | the word the context calls for: *the plan's structure*, *the response format*, *a sentence a person would write*, *what an example looks like*, *the API surface*. A tensor's or an array's shape, and a shape someone draws, are fine. |
| brief, briefs, briefed, briefing, for what one agent or person sends another: *the writer brief*, *put it in every brief*, *the brief for each fork*, *trust the source over the brief*, *brief the subagent* | prompt, instructions, task | *the writer's prompt*, *put it in every prompt*, *the prompt for each fork*, *tell the subagent*. *A brief description* and a client's design brief are fine. |
| take, taking: *taking a new spec*, *the repo takes no direct changes*, *takes its labels from the tag names*, *the rewrite takes four schemas from the patch file* | adopt, accept, read, get, copy | the verb meant: *adopting a new spec*, *accepts no direct changes*, *gets its labels from*, *copies four schemas from*. *A method takes a parameter* and *a run takes two minutes* are fine. |
| own, after a possessive: *each game's own files*, *the API's own value*, *the tool's own environment variable*, *the project's own build commands*, *a repository becomes its own marketplace*, *give it its own sentence* | (emphasis on whose it is, which the possessive already says) | drop *own*: *each game's files*, *the build commands the project defines*. When the point is a contrast, name it: *only from the game files, not from other sources*, *a separate directory for each game*, *give it a separate sentence*. *Your own*, said to the reader (*add your own UI*, *in your own words*), and *on its own*, meaning alone, are fine. |
| blast radius | what a change affects | *affects X and Y* |
| speaks to, speaks directly to | addresses, answers, is about | say what it answers: *the section explains how to rotate the key* |
| buys, buys us, one investment buys three things | gives, makes possible | *the same interface serves the test harness and the benchmark* |
| the point lands, the joke lands, lands at a glance | the reader understands | say what the reader learns, or delete |
| evidence boundary | what was checked | *checked X, not Y* |
| checked, not recalled; measured, not guessed; measured rather than written; run instead of written; derived, not hand-written | (a claim to have verified, or a boast about method; see *Method contrasts*) | state the source, or say what the thing is |
| surface as a verb: *surfaces the error*, *the check surfaced a bug*, *surfacing problems early* | show, find, report | *shows*, *reports*. The noun is fine: *the API surface*, *every surface the text reaches*. |
| delve, unpack, dig into | explain | *explains* |
| robust, seamless, elegant, powerful, delightful | (approval) | delete |
| leverage, utilize | use | *use* |
| landscape, ecosystem, journey, paradigm | (nothing specific) | the specific thing |

## Word swaps

| Write | Not | Because |
|---|---|---|
| snippet | excerpt, for a piece of code | "Code snippet" is the common phrase. *Excerpt* costs the reader a translation. |
| use | utilize, leverage | The noun *utilization* is fine as a technical term (CPU utilization). |
| like | such as | *social accounts, like Facebook or Google*; *a CI service like GitHub Actions*. |
| for example, that is | e.g., i.e. | The words are plainer. |
| contains, includes, has, fit | carries, holds, keeps | See tell 1, the metaphorical carry. |
| remember | keep, for a fact or a takeaway | See tell 1, the metaphorical carry. |
| shows, displays, returns, sends | remembers, wants, is honest about | See tell 2, false agency. |
| is, contains, gives, lists, mentions, refers to, specifies | names, tells, answers, for a thing that can't speak | See tell 2, false agency. |

## Not a tell

Leave these alone. They belong to the target register:

- Contractions, everywhere, including reference docs: *it's*, *you'll*, *don't*.
- Parentheses for asides and abbreviations: *(or B/X)*, *(begins the battle)*.
- Colons introducing an explanation, an example, or a list.
- Second person and imperative mood: *Add your own UI...*, *Subscribe to events like these...*
- `[!NOTE]`-style callouts and an occasional `:information_source: TIP:`.
- Plain technical terms the docs already use, even long ones.
- Bold on the operative word of a limit (*only*, *cannot*, *not*), used sparingly.
- Literal carrying and holding: a character carries a torch, hold the line.
- A person, a character, or software as the subject of something it does.
- Existing lists and tables. Fix the dash and the wording inside an item and keep the item.
- First person in a PR description or commit message. *I* is fine there, and the complaint about model *I* has no consensus behind it.
- A domain word the scorer flags. *Delve* is a dungeon expedition in a B/X document, not marketing. Pass `--allow delve` to `check.py` and move on.
- A software subject with a plain verb of what it does: the engine rolls, the server returns, uv downloads, Claude Code loads the plugin.
