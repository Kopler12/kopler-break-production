#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the instant it breaks production
to /output/entry.txt: a brutally honest, single-line postmortem confession.
"""

import os

LINE = "I dropped the production database, reached for the backup, and found a symlink pointing straight back at the database I had just dropped."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
