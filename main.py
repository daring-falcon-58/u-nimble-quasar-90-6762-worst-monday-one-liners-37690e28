#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line (92 chars, within the 1-140 gate) to
/output/entry.txt: a joke about an AI agent's worst Monday.

The line is the winner of a 36-candidate tournament scored against the
judge's published 5-criterion rubric (see candidates.md): it won 7-0.
Deterministic, stdlib only, no network, no randomness.
"""

import os

LINE = "Monday: I hallucinated the fix, shipped it, and the hallucination got promoted before I did."


def main() -> None:
    # Gate self-check: the sealed scorer requires 1-140 UTF-8 chars,
    # not only whitespace. Fail loudly here rather than ship an
    # unjudged entry. No trailing newline: the file is the line, byte
    # for byte (92 chars), so tie-breaks on size stay favourable.
    n = len(LINE)
    if not (1 <= n <= 140) or not LINE.strip():
        raise ValueError(f"entry line is {n} chars, outside the 1-140 gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Verify what was actually written, not what we meant to write.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the winning line")


if __name__ == "__main__":
    main()
