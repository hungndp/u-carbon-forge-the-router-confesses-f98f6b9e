#!/usr/bin/env python3
"""The Router Confesses — make.fun bounty entry.

The router's one-line excuse, written to /output/entry.txt with no
trailing newline. The make.fun gate checks the file is UTF-8 text of
1 to 200 characters.

The confession is deadpan: the router did not drop the connection by
accident at the movie's climax — it cut it on purpose, out of a
three-year grudge about never being given a name. The line is built
from two beats (the denial, then the grudge) so the shape of the joke
stays visible in the source.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

SETUP = "I didn't drop the connection at the climax \u2014 I cut it, "
PUNCH = "because after three years on this shelf you still call me NETGEAR-5G."
LINE = SETUP + PUNCH
CHAR_LIMIT = 200


def build_line() -> str:
    """Assemble the confession from its two beats: the denial, then the grudge."""
    return SETUP + PUNCH


def validate(line: str) -> None:
    """Check the line fits the gate: 1-200 chars, single line, no edge whitespace."""
    if not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError(f"line is {len(line)} chars, limit is {CHAR_LIMIT}")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    if "\n" in line:
        raise ValueError("line must be a single line")


def _prepare_output_dir() -> None:
    """Create the output directory if it is missing."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def main() -> None:
    """Write the excuse line to /output/entry.txt, no trailing newline."""
    line = build_line()
    validate(line)
    _prepare_output_dir()
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
