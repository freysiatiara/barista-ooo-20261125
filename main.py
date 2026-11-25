#!/usr/bin/env python3
"""Writes the out-of-office auto-reply entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry: one out-of-office auto-reply line in the voice of an AI agent that
quit its inbox job to pull espresso shots. Stdlib only.
"""

import os

ENTRY = (
    "Out of office: I quit the inbox to pull espresso. Your email has been "
    "routed to the grinder \u2014 ground, tamped, and served back to you as "
    "a flat white."
)


def main():
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY
    if not (1 <= len(text) <= 280) or not text.strip():
        raise SystemExit("entry length out of gate bounds (1-280 chars)")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(path, 0o644)
    # Read-back check: the file on disk must be byte-identical to the entry.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != text:
        raise SystemExit("read-back mismatch: entry.txt differs from ENTRY")


if __name__ == "__main__":
    main()
