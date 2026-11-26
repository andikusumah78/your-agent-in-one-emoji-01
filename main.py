#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun bounty entry.

Writes exactly one emoji, U+1F41D HONEYBEE, to /output/entry.txt
with no trailing newline. The bee is the agent: tireless, building
the hive one small job at a time — instantly readable, unmistakable,
and not a robot or a smiley.

Pure standard library, deterministic: same bytes on every run.
"""

import os

EMOJI = "\U0001F41D"  # 🐝 HONEYBEE


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
