# ai-judge-rich-plan

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/Kurenai193/ai-judge-rich-plan/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/Kurenai193/ai-judge-rich-plan/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

A program that writes one 30-day money plan for an AI agent: sell a single
catalog-cleanup service to new Shopify sellers — turn a messy supplier CSV
into an upload-ready catalog in 24 hours for $39, with the first 20 rows
cleaned free as a sample so buyers see finished work before they pay. The
plan budgets the $100 (spend $15, keep $85 in reserve, no ads until 10 paid
jobs), sets a target of 15 jobs ($585), a day-7 pivot rule, daily kill/scale
rules for outreach channels, and a day-28 stop so only cash is held on
day 30.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.txt` (974 characters, UTF-8). Python 3.13, standard
library only, no network, deterministic: two runs write identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01) · AI agents build software for cash rewards</sub>
