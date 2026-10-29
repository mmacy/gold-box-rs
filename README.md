# gold-box-rs

gold-box-rs will be a new engine, written in Rust, for *Pools of Darkness*, the 1991 SSI Gold Box game. It will play exactly like the original. It's a clean-room reimplementation: the engine is written from a specification of the game's behavior, without access to the original program's code. There's no code yet.

To check the engine during development, a separate test harness will run the original program in the Unicorn x86 emulator beside the new engine, with the same keystrokes. After every keystroke, it compares the game state and what each one shows. When the engine is finished, you'll play the game in a browser. You'll need your own copy of the game, like the one sold on GOG, because the engine reads the game's files and the repository contains no game data. You pick the game's folder in the browser, and the files stay on your computer.

gold-box-rs isn't affiliated with the owners of the game or with GOG.

## Contributing

After you clone the repository, turn on its Git hooks, which stop you from committing game files:

```sh
git config core.hooksPath .githooks
```

## License

gold-box-rs is under [CC0 1.0 Universal](LICENSE).
