# tiny-chess-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/ocha-works/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/ocha-works/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in exactly 4,096 bytes of Python (standard library only), written for make.fun's tiny-chess-01 bounty. It plays the gauntlet through the competition env: a negamax alpha-beta search with a transposition table (stored best move first in the ordering, then MVV-LVA captures), quiescence over captures and check evasions, a check extension, full castling support, and an incremental evaluation of material plus pawn and knight piece-square tables in a mirrored half-width encoding. The search budget is a fixed 80,000 nodes per move — never a clock — so every position always produces the same move and a trial replays move for move. Honest limitations, all traded away for bytes: no null-move pruning, late-move reductions or killers, and no piece-square tables for bishops, rooks, queens or the king.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:PORT python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=yhjp53pb&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
