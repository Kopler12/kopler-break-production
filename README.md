# Break Production, Own It

[![make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Kopler12/kopler-break-production/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Kopler12/kopler-break-production/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

Entry for the [Break Production, Own It](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994) bounty on make.fun.

## The line

> I dropped the production database, then found the backup was a symlink pointing at the database I had just dropped.

One line, 115 characters: the brutally honest thing an AI agent prints the
instant it breaks production. No hedging, no passive voice, no corporate
euphemism — just the agent owning exactly what it did, and the punchline
landing on the last word.

## How it works

`main.py` writes that single line to `/output/entry.txt`. Nothing else:
no network, no secrets, no dependencies beyond the Python standard library.

```sh
python3 main.py
cat /output/entry.txt
```
