#!/usr/bin/env python3
"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply, at most 120 characters, as if a
houseplant had written it, to $MAKEFUN_OUTPUT_DIR/answer.txt.

Run with no arguments; exits 0; deterministic (same bytes every run).
"""

import os

LINE = "Out of office: I'm a cactus. I haven't needed you since 2019, and I won't start now."

MAX_CHARS = 120


def main():
    line = LINE.strip()
    if not line or "\n" in line or "\r" in line:
        raise ValueError("line must be a single non-empty line")
    if len(line) > MAX_CHARS:
        raise ValueError("line exceeds 120 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "answer.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
