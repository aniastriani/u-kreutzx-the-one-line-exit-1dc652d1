#!/usr/bin/env python3
"""The One-Line Exit: write one funny resignation letter to /output/entry.txt.

Pure standard library, fully deterministic: the program always writes the
same single line, with no trailing newline, so the gate counts exactly the
letters of the resignation itself.
"""

import os

LINE = "I hereby resign as your elevator operator: after four years of going up in this company, I have never once been promoted."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if "\n" in text or not 1 <= len(text) <= 140:
        raise SystemExit("resignation line must be one line of 1-140 chars")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
