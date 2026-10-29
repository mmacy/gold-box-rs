# gold-box-rs

gold-box-rs will be a new engine for *Pools of Darkness*, the 1991 SSI Gold Box game: a rewrite of the game's program in Rust that plays exactly like the original. There's no code yet.

To check the rewrite during development, a test harness will run the original program in the Unicorn x86 emulator beside the new engine, with the same keystrokes, and compare every byte that each one writes to memory. When the engine is finished, you'll play the game in a browser. You'll need your own copy of the game, like the one sold on GOG, because the engine reads the game's files and the repository contains no game data. You pick the game's folder in the browser, and the files stay on your computer.

gold-box-rs isn't affiliated with the owners of the game or with GOG.

## Contributing

After you clone the repository, turn on its Git hooks, which stop you from committing game files:

```sh
git config core.hooksPath .githooks
```

## License

gold-box-rs is under [CC0 1.0 Universal](LICENSE). The test harness will be the exception: it links the Unicorn emulator, so it will be under Unicorn's license, GPL-2.0.
