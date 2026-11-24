#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
"""

import os
import sys

ENTRY = "A stranger will ask you to write their fortune. You already did. It is this one."

# Output dir precedence (koran 24 Nov lesson): the grader may run with no
# arguments in a read-only working directory, so honour MAKEFUN_OUTPUT_DIR
# first, then an argv[2] output dir if given, then the harness /output dir.
OUTPUT_PATH = (
    os.environ.get("MAKEFUN_OUTPUT_DIR")
    or (sys.argv[2] if len(sys.argv) > 2 else None)
    or "/output"
)
OUTPUT_FILE = os.path.join(OUTPUT_PATH, "entry.txt")


def main() -> None:
    # Guard: the gate requires 1-140 chars, one line, non-blank.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    assert ENTRY.strip(), "entry must not be blank"
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
