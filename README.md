# tiny-chess-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/ocha-works/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/ocha-works/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 3,844 bytes of Python (standard library only; the source is lzma-packed into main.py by the kit's `makefun compress`), written for make.fun's tiny-chess-01 bounty. It plays the gauntlet through the competition env: a negamax alpha-beta search with a transposition table, PVS with late-move reductions, null-move pruning, killer and history move ordering, quiescence over captures and check evasions with delta pruning, futility pruning at depth 1, a check extension, repetition detection, full castling support, and aspiration windows at the root. The evaluation is incremental: material plus piece-square tables for every piece in a mirrored half-width encoding, an endgame king-table blend scaled by the material remaining, and the bishop pair. The search budget is a fixed 62,000 nodes per move — never a clock — so every position always produces the same move and a trial replays move for move.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:PORT python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=yhjp53pb&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
