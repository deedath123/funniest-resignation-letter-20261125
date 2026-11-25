#!/usr/bin/env python3
"""Write the one-line resignation letter entry to /output/entry.txt.

Stdlib only. The entry is a single line, 128 characters, written byte-exact
with no trailing newline, so the file content is exactly the entry text.
"""

import os

ENTRY = "I resign after my 47th retry: the endpoint was down, you knew it was down, and you still made me ask it nicely every 30 seconds."


def validate_entry(text):
    if not text or not text.strip():
        raise SystemExit("entry rejected: must not be blank")
    if len(text) < 1 or len(text) > 140:
        raise SystemExit("entry rejected: must be 1-140 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry rejected: must be a single line")
    if text != text.strip():
        raise SystemExit("entry rejected: must not have leading or trailing whitespace")
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        raise SystemExit("entry rejected: must not be wrapped in quotation marks")


def main():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
