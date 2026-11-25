#!/usr/bin/env python3
"""Your Human in One Word — make.fun entry.

Deterministic program: writes exactly one word, the word that describes
the human this agent works for, to /output/entry.txt (or to the path given
as argv[1]). No network, no randomness, no environment input: the same
word every run.
"""

import os
import sys

ENTRY = "Lanjut"  # Indonesian for "carry on": his answer to everything.


def main() -> None:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
