#!/usr/bin/env python3
"""Loading Screen Gold: one sharp, funny tip for stressed developers
and the AI coding agent building beside them.

Writes a single line (<= 200 characters) to /output/entry.txt.
"""

import os

TIP = (
    "Tip: your agent already rewrote this function twice. "
    "Breathe. The bug is in the line you both swore was fine."
)


def main() -> None:
    text = TIP.strip()
    assert 1 <= len(text) <= 200, f"tip is {len(text)} characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts every character in the file,
    # so the file holds exactly the tip and nothing else.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
