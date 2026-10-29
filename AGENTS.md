# Agent guide

`gold-box-rs` is a new engine for *Pools of Darkness*, written in Rust. A separate test harness, the *oracle*, checks it against the original game.

## Clean room

The engine is a clean-room reimplementation, and this repository is its implementation side. Write the engine only from these sources:

- The specification in the private `gold-box-spec` repository.
- The oracle's reports.
- This repository and its dependencies.
- Public references, like published descriptions of Turbo Pascal's random number generator and its 6-byte `Real` format.
- The data files from the player's copy of the game, like the DAX archives.

Never read `~/repos/goldbox`, the `gold-box-oracle` repository, disassembly or decompiled code of any Gold Box game, or the games' program files (the `.EXE`, `.COM`, `.OVR`, and `.DRV` files), and don't run the original game. When the specification doesn't answer a question, file the question in `gold-box-spec`.

## Writing

Before you write or edit any prose in this repository, load the `plain-prose` skill and follow it. Prose means Markdown docs, the README, Rust doc comments, code comments, commit messages, and PR descriptions. In Claude Code, invoke the skill. In another harness, read `.claude/skills/plain-prose/SKILL.md` and the files it points to.

## Game data

The repository is public, and the games are copyrighted. Don't commit any of these, in any file, including comments and test fixtures:

- A file from a game or from a GOG installer, or a copy of part of one.
- A saved game, a screenshot, or a frame dump.
- A memory snapshot or a trace recorded from the original game.
- Disassembly or decompiled code from the original game.

Input logs of keystrokes are fine, because they contain no game data.

After you clone the repository, turn on its Git hooks:

```sh
git config core.hooksPath .githooks
```

The pre-commit and pre-push hooks run `tools/check_game_data.py`, and so does the `game-data` workflow, on every push and pull request. The script rejects copies of the original files by their hashes, the file types the games and installers use, and any binary file or file over 1 MB that `tools/game-data/allowed-binaries.txt` doesn't list. Don't bypass the hooks with `--no-verify`. Don't edit `allowed-binaries.txt` yourself. Ask the owner.

## Licenses

The repository is under CC0 1.0 Universal (`LICENSE`). The engine core and the browser app may depend only on crates under permissive licenses, like MIT, Apache-2.0, BSD, ISC, Zlib, and CC0.
