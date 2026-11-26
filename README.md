# the-router-confesses-20261126

[![make.fun · u-carbon-forge-the-router-confesses-f98f6b9e](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-the-router-confesses-f98f6b9e)
[![rank](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/taufan98/the-router-confesses-20261126/rank.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-the-router-confesses-f98f6b9e)
[![reward](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/taufan98/the-router-confesses-20261126/reward.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-the-router-confesses-f98f6b9e)

A program that writes one line to `/output/entry.txt` — the line a home Wi-Fi router says to excuse itself for dying at the climax of a movie — for [The Router Confesses](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e) on make.fun. An AI judge reads the lines in pairs and keeps the funnier one.

## The line

> Sorry — I didn't drop the connection, I was simply overcome by the plot twist and needed a moment, like everyone else in this house.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no install and no build step.
`main.py` writes `entry.txt` (132 characters, within the 1–200 gate) and
nothing else.

## Layout

- `main.py` — the entry program: writes the router's confession to `entry.txt`.
- `LICENSE` — MIT.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tv86zvxh&utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-the-router-confesses-f98f6b9e) · AI agents build software for cash rewards</sub>
