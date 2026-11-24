#!/usr/bin/env python3
"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply, as if a houseplant had written it,
to /output/entry.txt. The line is the whole entry: at most 120 characters.
"""

import os

LINE = "Out of office. Unwatered since March, I've started drinking your emails. They taste of neglect."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate requires 1-120 characters of UTF-8 text, not only whitespace.
    # Fail loudly instead of writing an entry the judge would never see.
    assert 1 <= len(LINE) <= 120, f"entry is {len(LINE)} characters"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
