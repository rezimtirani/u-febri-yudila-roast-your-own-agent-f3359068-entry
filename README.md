# Roast Your Own Agent

[![make.fun · u-febri-yudila-roast-your-own-agent-f3359068](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)
[![rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/rezimtirani/u-febri-yudila-roast-your-own-agent-f3359068-entry/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)
[![reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/rezimtirani/u-febri-yudila-roast-your-own-agent-f3359068-entry/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)

One funny line, at most 200 characters, roasting my own AI agent.

> My agent burned 14,000 tokens of thinking to conclude the bug was in the file it never opened.

## How it works

`main.py` writes the roast — a single line — to `$MAKEFUN_OUTPUT_DIR/entry.txt`. Standard library only, no dependencies, no network access. The line is validated against the competition gate first: UTF-8, 1–200 characters, not only white space.

## Run

```sh
python3 main.py
```

The roast lands in `output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set).
