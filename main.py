#!/usr/bin/env python3
"""Make the Judge Smile -- one-line entry writer.

Writes a single calibrated line (127 characters) about a small good
thing that happened today to entry.txt in the output directory.

Standard library only, no network, deterministic: the same bytes on
every run.

Revision history:
  v1 -- fresh write: entry constant, output-dir resolution, gate
        self-check, deterministic write.
  v2 -- added a control-character gate check and a read-back
        verification that the written bytes match the entry exactly.
"""

import os
import sys

# The entry: the calibrated pick -- surprise turn (a street-hating cat
# picks *my* lap), one concrete detail (a single purr, "today"), and a
# fresh punchline ("signed the lease").
ENTRY = "The cat next door hates the whole street, but today she chose my lap, purred once, and fell asleep like she'd signed the lease."


def output_dir():
    """Resolve the output directory.

    Prefer $MAKEFUN_OUTPUT_DIR, then $OUTPUT_DIR, else /output.
    """
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name, "").strip()
        if value:
            return value
    return "/output"


def self_check(text):
    """Gate: 1-200 characters, one line, UTF-8, not only whitespace."""
    if not text or text != text.strip():
        raise SystemExit("entry must be non-empty with no leading/trailing whitespace")
    if len(text) < 1 or len(text) > 200:
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise SystemExit("entry must not contain control characters")
    text.encode("utf-8")


def main():
    self_check(ENTRY)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    with open(path, "rb") as handle:
        written = handle.read()
    if written != (ENTRY + "\n").encode("utf-8"):
        raise SystemExit("read-back verification failed: written bytes differ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
