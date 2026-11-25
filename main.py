#!/usr/bin/env python3
"""The Moon Finally Answers Back — entry writer.

Writes the chosen one-line comeback in the Moon's voice to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), then verifies
the written bytes match exactly.

The entry is a fixed constant: 174 characters, one line. Why this line:
the judge's brief wants the Moon answering the wishes, howls and
late-night promises, funny on one read, wry and old, with the turn
landing before the line ends. The field (1,451 submissions) is saturated
with "4.5 billion years of wishes" openers, "I'm a rock" and tide jokes,
while "horoscope" appears in none of the submission titles. The line
answers a wish for a sign directly, then turns on the last clause: after
4.5 billion years of glowing in the sky, humanity takes life advice from
a newspaper that also prints crosswords. The gate requires UTF-8 text of
1-240 characters, not only whitespace, so this program validates length,
single-line shape and whitespace content before writing anything.
"""

import os
import sys

ENTRY = (
    "You wish on me for a sign, then check your horoscope instead. "
    "I've hung in your sky 4.5 billion years \u2014 and you take life advice "
    "from a newspaper that also prints crosswords."
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1-240 chars, single line, not blank.

    Design note: the entry is deliberately a fixed constant, not generated
    or read from anywhere else — the rules require everything the entry
    runs to live in this repository, and a fixed string keeps the output
    byte-identical on every run. The trailing-whitespace check below
    guards the punchline: the judge reads the entry exactly as written,
    so a stray space at the end would be part of the text and could dull
    the final words ("also prints crosswords.").
    """
    if not (1 <= len(text) <= 240):
        raise ValueError(f"entry length {len(text)} outside 1-240 chars")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip() or text.strip() == "":
        raise ValueError("entry must not be only whitespace or padded")
    if text != text.rstrip():
        raise ValueError("entry must not end with trailing whitespace")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("written bytes differ from entry")
    print(f"wrote {len(data)} bytes to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
