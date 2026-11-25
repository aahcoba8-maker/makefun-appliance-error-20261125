#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — one-line entry.

Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt when set,
otherwise next to this script, and prints the line to stdout.
Stdlib only.
"""

import os

ENTRY = "Error: too much detergent. I am now mostly foam. The laundry is somewhere inside."


def main() -> None:
    # Self-gate, mirroring the sealed scorer: UTF-8, 1-200 chars, one line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
