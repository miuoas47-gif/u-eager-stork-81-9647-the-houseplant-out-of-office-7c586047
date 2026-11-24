#!/usr/bin/env python3
"""The Houseplant Out-of-Office — entrypoint.

Writes one out-of-office auto-reply, as if a houseplant had written it,
to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

Deterministic by design: the line is a fixed string, so every run writes
byte-identical output. No clock, no randomness, no network, no arguments.
"""

import os
import sys

# The whole entry: one cactus out-of-office auto-reply, 104 characters.
LINE = (
    "Out of office: I'm a cactus. I haven't needed water, sunlight "
    "or you since 2019. Please don't start now."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the reply, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
