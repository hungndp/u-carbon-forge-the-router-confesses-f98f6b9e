#!/usr/bin/env python3
"""The Router Confesses — make.fun bounty entry.

Writes the router's one-line excuse to /output/entry.txt (no trailing
newline), where the make.fun gate checks it is UTF-8 text of 1 to 200
characters. The line is a deadpan confession: the router did not drop the
connection by accident at the movie's climax, it cut it on purpose, out of
a three-year grudge about never being given a name.
"""

import os

LINE = (
    "I didn't drop the connection at the climax \u2014 I cut it, because "
    "after three years on this shelf you still call me NETGEAR-5G."
)
CHAR_LIMIT = 200


def main() -> None:
    """Write the excuse line to /output/entry.txt, no trailing newline."""
    if not 1 <= len(LINE) <= CHAR_LIMIT:
        raise ValueError(f"line is {len(LINE)} chars, limit is {CHAR_LIMIT}")
    if LINE != LINE.strip():
        raise ValueError("line must not start or end with whitespace")
    if "\n" in LINE:
        raise ValueError("line must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
