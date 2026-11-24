#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

One sentence, at most 200 characters, on a small moment of wonder in
everyday life. The program writes that single sentence to
/output/entry.txt, where the sealed scorer checks it is UTF-8 text of
1 to 200 characters, and the AI judge compares it pairwise against
other entries, rewarding a fresh angle on an ordinary moment.

The sentence: a shadow arriving half a step early turns a routine
crossing into a small jolt -- the body knows something the mind has
not caught up with yet.
"""

import os
import sys

SENTENCE = (
    "My shadow reached the crosswalk a half-step before I did, "
    "in a hurry I didn't remember feeling."
)

MAX_CHARS = 200


def main() -> int:
    text = SENTENCE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the 200 limit", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
