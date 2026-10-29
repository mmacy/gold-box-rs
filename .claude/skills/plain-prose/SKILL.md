---
name: plain-prose
description: Writes and rewrites prose in gold-box-rs (Markdown docs, the README, Rust doc comments, code comments, commit messages, and PR descriptions) so it doesn't read as model-written. Removes the habits readers spot as model-written (em dashes, stock words, false agency, buried answers, and the rest) and leaves facts, code, and links as they were. Use before you write or edit any prose in this repository.
---

# Plain prose

Model-drafted prose has three kinds of problem:

- **Sentences that say something slightly wrong.** A file "carries" text, a reader is told which fact to "keep", a door wants a key, an engine "knows" a rule, a pronoun points at nothing, or a document narrates the history of its edits.
- **Sentences that say the right thing in the wrong register.** The *register* is the set of habits a kind of writing has: punctuation, word choice, sentence length. The wrong one shows up as em dashes, adjectives that pass judgment, stock words readers now spot on sight, Title Case headings, a sentence about the document instead of its subject, or a phrase only the writer can decode.
- **Documents in the wrong order.** The answer sits in the last paragraph or in a trailing caveat, or the project's history sits where the reader's first step belongs.

Avoid all three when you write, and fix all three in one pass when you edit. Leave facts, code, and links as they were.

The rules are in the `references/` folder next to this file. Read both files before you write or edit:

- `register.md` describes the register to write in, with the numbers the scorer checks.
- `tells.md` lists the habits to remove (the *tells*), with before-and-after pairs.

Test each sentence against the "after" lines in `tells.md`: it should fit among them without standing out. Test the whole document against its reader: they should be able to do the task it's for without reading anything written for the maintainers, like `AGENTS.md` or the plan. Links to further reading are fine.

The target register is developer documentation. For a commit message or a PR description, use the short first-person register in the "Commit messages and PR descriptions" section of `register.md`.

## Who the reader is

Before you write or change a sentence, decide who reads the document. If the request names an audience ("for players, not developers", "for someone new to Rust"), take it literally.

The reader of a user-facing document has seen only the repository's one-line description. They haven't read `AGENTS.md`, the plan, or the reverse engineering, and they don't know the conventions the maintainers take for granted. So define each term the reader hasn't met, in a clause, where it first appears. Don't assume the reader has done anything the document doesn't tell them to do. Put the project's internals after the reader's tasks, in a section for contributors.

If the request names no audience, infer it from the kind of document:

- A README is for whoever builds or runs the engine.
- A docs page is for whoever does the task it names.
- A doc comment (`///` or `//!`) is for whoever calls the function or uses the module.
- A commit message is for whoever reads the history later.
- A PR description is for whoever reviews the change.

Sometimes a draft's structure serves a different reader than the one it's for: a README that opens with the milestone plan, a status paragraph of what was finished when, or a docs page that explains the design before the first step. When that happens, say so when you ask how far to go. It's the reason to consider a rewrite.

## Scope

When you write new prose, follow these rules from the first sentence.

When you're asked to edit, and the request names files or directories, work on those. Otherwise, work on the Markdown files changed on the current branch and on the doc comments and comments of source files changed on it. "Changed" means the diff against the default branch plus any uncommitted changes. If the branch has no changes, work on the README.

Don't change text whose exact form something else depends on, like a test, a link, another person, or the law:

- Fenced code blocks and everything inside them, including comments, diagrams, and directory trees. In a doc comment, `cargo test` runs the code blocks as doc tests.
- Inline code spans, commands, file paths, and link and image targets.
- Front matter keys.
- UI strings in source code, and control names that match real strings elsewhere.
- Quoted third-party text, license text, and generated files.
- Names and strings from the original games, like `Play Demo` or an ECL opcode name.

You may change the case of a heading, because GitHub and MkDocs lowercase heading text when they build an anchor. Don't change a heading's wording unless the wording is itself a tell. Changing a heading's wording or removing an emoji from it does change its anchor. Search the repository for links to the old anchor and update them.

When you find UI strings in source, leave them as they are and list them when you finish. Changing one means updating its tests and screenshots too. Leave a comment copied from another project alone, since changing it is a decision for that project.

## How far to go

When you edit, there are two sizes of job, and the owner picks. Before you edit, ask, unless the request already says which. If your harness has a tool for questions, like `AskUserQuestion` in Claude Code, use it.

- "rewrite it" or "full rewrite" means a rewrite for the reader.
- "in place", "keep the structure", or "just the wording" means an edit in place.

If there's no one to ask, edit in place. In the question, give each option one line on what the reader gets. If the draft's structure doesn't serve its reader, say that in the question, so the owner has the reason in front of them when they decide. Ask about every document, not only READMEs: a docs page, a spec, a skill file, or a set of doc comments.

**In place.** Leave the document's sections, lists, and tables where they are, and match its line count where the wording allows. The owner reviews a diff of wording, and any other kind of change in that diff slows the review. There are two exceptions. Prose that describes a procedure the reader performs may become numbered steps, and a paragraph that covers two topics may become two paragraphs. Add no facts and drop none.

**Rewrite for the reader.** Start from the reader's first question and write the document that answers it, in the order of the reader's task. For a README, that order is what it is, what you need, how to install it, and how to use it. How it's built comes after.

Material for a different reader (milestone history, comparisons with another project, measurement plans) moves to a short section for that reader, or becomes a link to the docs that cover it. Drop what this reader can't use. A paragraph of what was finished in which milestone becomes one sentence about what works today. Facts the reader needs stay, and facts only another reader needs move or go. The verification rules below apply to every sentence either way.

Delete a tagline, a "why you'll love it" section, or a closing hype paragraph when every fact in it also appears elsewhere in the document. If a fact appears only there, move it to the section where a reader would look for it first.

## Check the path, not only the prose

A user-facing document tells the reader to do things. A model draft often copies those things from the contributor workflow: clone the repository, run a sync, `cd` into a directory the reader has never heard of. Before you write or rewrite an instruction, check whether the reader has to do it at all.

- **Is each prerequisite something the reader must already have?** If the instructions are going to get it for them, it isn't a prerequisite. If a tool fetches its dependencies the first time it runs, the "install dependencies" step becomes a note that the first run is slower. To verify, read what the command does (for example, `cargo run` downloads the crates and builds the project before it runs it).
- **Does the platform offer a shorter path?** You install a released tool with the package manager, not from source. If the platform's docs confirm a shorter path the repository already supports, document that path, and move the longer one into the section for contributors. If the shorter path needs a file the repository doesn't have, don't add it. Name the path and the missing file when you finish.
- **Does the reader need to be in a particular folder?** "Run it from the game folder" is a contributor convention unless the code reads the working directory. Read the code. If the location doesn't matter, write "from any folder". If a directory is created on first use, say what creates it and when, and confirm that against the code that creates it.
- **Does every way to do something have an example?** If the document says "use the CLI or the web app", show the command and show where to click. A reader can't use a method the document names but doesn't show.
- **Is a stated limit real?** Before you write "the engine can't load saves from *Curse*", read the code to find which component would refuse the save, and why. Then state the limit and its reason.

For these checks, read what's outside the document: the manifest, the platform's docs (fetch the current page and confirm the command against it), and the code. Don't install or run anything to check an instruction. If reading can't confirm it, leave the instruction as drafted and list it when you finish. A wrong instruction can cost the reader their first hour with the project.

## Verify before you change what a sentence claims

A rewrite for register can change what a sentence means. The draft says something loose, the rewrite says something precise, and the precise version is a claim the draft never made. These edits do that:

- Replacing a false actor with the real one, or naming the actor behind a passive.
- Replacing a pronoun, a *both*, or a *those* with the thing it refers to.
- Expanding a compressed list where the separator hid how the items group. `combat / spells / monster AI` is three items, and the slash may hide which of them belong together.
- Replacing a vague verb or phrase with a specific one. If *bring it home* becomes *finish the quest*, the sentence loses the object you have to bring back to win.
- Turning a list after a colon into the predicate of a sentence. If `X: a, b, and c` becomes `It's a, b, and c`, the sentence now claims that X is each of a, b, and c.
- Stating a scope, limit, condition, or default the draft left implicit. If *you'll get a URL* becomes *the deploy prints a URL*, the sentence now claims the deploy prints it, and it may not.
- Splitting a spliced sentence where the splice stated a condition. If a roll depends on the party having a tool, cutting the splice can make the roll unconditional.
- Deleting a clause as decoration when it states a condition, a limit, or a fact.
- Translating insider shorthand into a sentence, which you can do only after you've read the code that the shorthand describes.

Each of these edits has two possible outcomes:

- Confirm the new wording against the code, its tests, or a source the owner named in the request, and then make the edit.
- Leave the sentence as drafted, and put the wording you would have used in your closing message, with what you couldn't confirm.

To confirm means to look at the module the sentence describes. If confirming takes more than a look, leave the sentence as drafted. Another document, the draft itself, and what the sentence seems to imply don't count as confirmation. You can always leave a sentence as drafted. You can't make the edit and then flag it as uncertain.

Don't invent claims, and don't invent defects either. A sentence that's plain, true, and already in the target register stays as it is.

Leave a sentence as drafted only when you couldn't verify the new wording. A defect still needs fixing if it's the project's usual phrasing, or if a neighboring file or an agent guide uses the same wording. Those explain how the defect spread. Once you've confirmed the actor or the referent, make the edit.

To confirm an actor, you read the code, and sometimes the code shows that the sentence is wrong about more than its grammar. Correct the claim to what you verified, and list it when you finish, with the file and line. A false claim isn't a tell, but you're the one reading the code in this pass, so don't leave it standing.

## How to work

Run the scorer on each Markdown file before you edit, and on each Markdown file you write:

```bash
python3 .claude/skills/plain-prose/scripts/check.py <files>
```

For each file, the scorer prints a value for each of 16 measures next to the target value, and marks the ones outside the target range. It also lists the marketing words and stock words it found. It reads Markdown only, so don't run it on source files. Run it again after you edit. For each measure still out of range, you should be able to say why. A reference page with many parentheses is fine. A README with an em dash isn't.

A value inside the range but far from the target isn't a defect on its own, so don't add contractions or *you* to move the number. Mention it only when you can see the cause. For example, a README with *you* at 3 per thousand words may describe the software instead of addressing the reader. A domain word on the marketing list (*delve* in a dungeon crawl's README) isn't a defect. Pass it with `--allow delve`, so the report shows only the real misses.

The scorer counts punctuation, sentence length, headings, and a fixed list of words and phrases. It catches a few forms of false agency, like *a failure names*, and misses most of them. It also catches most relative clauses with a negative subject, like *which no script sets* (tell 24). Rewrite every one of those it lists, unless the match is a statement and not a relative clause. Find the rest by reading: carry, hold, and keep used as metaphors, false agency, unresolved pronouns, compression jargon, passives that hide the actor, insider shorthand, noun stacks, nouns used as verbs, and a buried answer. No pattern finds noun stacks (tell 22), so read for them. These patterns find sentences to read. Run each with `grep -niE`, case-insensitive because a match can start a sentence:

```text
carr(y|ies|ied|ying)|\bh(o|e)ld(s|ing)?\b|\b(keep(s|ing)?|kept)\b|\bown(s|ed|ing)?\b
\b(wants?|needs?|decides?|says?|tells?|asks?|refuses?|knows?|expects?|generates?|rolls?|reads?|speaks?|remembers?|names|named|answers?|cites?|mentions?|buys?|lands?|finds?)\b
\b(which|that) (no \w+|nothing|nobody|no one)\b|\b(every|each|any|a|an|the) \w+ (no \w+|nothing|nobody) \w+s\b
\b(originally|previously|initially|no longer|used to|was added)\b|as of 20[0-9]{2}|\(20[0-9]{2}-[0-9]{2}-[0-9]{2}\)
→|->|=>|—|–
\b(utiliz\w+|such as|excerpt|e\.g\.|i\.e\.)
\b(load.bearing|the (honest )?seams?|honestly|the honest (part|take|answer)|genuinely|smoking gun|(that|deeper) tension|tension between|blast radius|worth (noting|naming|stating|mentioning|calling out)|here'?s the thing|there'?s a catch|absolutely right)\b
(^|[.!?] +)(additionally|furthermore|moreover|notably|importantly|crucially|note that|in other words)\b|\b(simply|easily|just works|just)\b
and nothing else|no exceptions|\bonly knows\b|\bstrictly\b|is the (whole|entire) |\bparity\b
\b(pin(s|ned|ning)?|ships?|shipped|lands?|landed|keys? off|keyed off|fold(s|ed)? (in|into)|wire[sd]?|wiring|thread(s|ed|ing)? (through|into))\b
\b(the|a|an) (first|next|initial) \w+ (after|before|on) \w+ing
```

In Rust source, `->` and `=>` are syntax, so run the arrow pattern on comments only.

The second pattern, for verbs, matches many sentences that are fine: people want things, and the CLI reports errors. Read each match and decide, using "Not a tell" at the end of `tells.md`. The second-to-last pattern finds absolute qualifiers and a few fixed forms of insider shorthand (tells 17 and 18). The pattern after it finds nouns used as verbs (tell 23). The last pattern finds a noun phrase that hides a passive (tell 6). For example, write *the first time you run it after you build it* instead of *the first run after building*.

Write or rewrite paragraph by paragraph, and state the facts in the register `register.md` describes. When you edit, add nothing and drop nothing, unless the owner chose the rewrite and "How far to go" says this reader doesn't need the fact. When a fix needs a new verb or actor, prefer the one the surrounding docs already use for the same fact. When the reader is the one acting, make *you* the subject instead of the software. Use the surrounding docs to choose a replacement, never to decide whether to fix. Split a spliced sentence even when that changes the line count.

Leave the document's callout syntax as it is, since the docs build depends on it: `> [!NOTE]` on GitHub, and `!!! note` in MkDocs.

After the pass, read the whole document once more from start to finish, as the reader, before you report. Look for what the first read missed:

- A slogan repeated in two sections.
- A term used before it's defined.
- A way of doing something with no example.
- A qualifier added for emphasis.
- A sentence that serves the writer or a contributor instead of the reader.

Fix those in the same pass, so the owner doesn't have to ask for a second round.

Then check what a new reader understood. Your own rereading can't find these problems, because you know what each sentence means. Check these three things in every opening paragraph and every summary:

- Each "your X" or "the X" names something the reader already has at that point, or something the text has just introduced. "Your engine checks each routine" assumes an engine the reader hasn't built yet.
- Each sentence's most likely wrong reading is ruled out. A list after "handles everything the player sees" reads as a list of things the reader receives.
- Where developers have a name for a thing, like UI or API key, the text uses the name instead of describing it.

Then have a subagent read the document. It must not have seen the project or this conversation. Give it only the document and the reader the document is for. Give it the document one paragraph at a time, in separate files or messages, so it can't see what comes next. After each paragraph, before it reads on, it writes down four things:

- The questions it now has.
- The most likely wrong reading of each sentence, if one is plausible.
- For each "your X" or "the X", whether the reader has X at this point. A reader who hasn't built anything has no engine, app, or project to call "yours". It takes the phrase literally, not as the writer meant it.
- For each list, whether the reader could take it as things they get when it's things they do, or the reverse.

A reader asked only for misreadings reads cooperatively and fills in what the writer meant. The last two questions keep it literal. After the opening, it does a teach-back: it writes in its own words what the thing is, what it gives the reader, and what the reader must do themselves. Compare its notes with the facts. Each mismatch, unanswered question, and plausible misreading is a finding. Fix the text and run the check again with a new subagent, until the teach-back matches the facts. If you can't start a subagent, for example because you're running as one, don't skip the check. Put a request at the top of your report for the session that started you to run it. Name the document and the reader.

Skip the subagent check for a commit message, a code comment, and a doc comment of a few lines.

If the project has a docs build, run it with warnings treated as errors afterwards, like `mkdocs build --strict`. For doc comments, run `RUSTDOCFLAGS="-D warnings" cargo doc --no-deps`.

## When you finish

Start with one sentence: what you wrote or changed, in how many files, and how many measures were out of range before and after. Then list only what the owner has to act on:

- Sentences you left as drafted because you couldn't verify the rewrite. Give the file and line, the wording you would have used, and what you couldn't confirm.
- Claims you corrected based on the code, each with the file and line.
- Claims in the draft you suspect are wrong but couldn't check, each with the file and line.
- Shorter paths that need a file the repository doesn't have, with the file they need.
- Headings whose wording you changed, since links from outside the repository may still point at the old anchor.
- Terms you couldn't define, UI strings you left in source, and comments copied from another project, with their locations.

If none of those exist, the one sentence is the whole message. Don't add a line saying a category was empty.

Write the message for someone who hasn't read this file. Don't use its working terms (tell, measure, register). Say what you did in plain words: "I left this sentence as it was because I couldn't confirm that the deploy prints the URL." The message is prose you wrote, so the rules in `tells.md` apply to it too.
