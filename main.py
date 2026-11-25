#!/usr/bin/env python3
"""Write the one-line resignation letter entry to /output/entry.txt.

Stdlib only. The entry is a single line, 128 characters, written byte-exact
with no trailing newline, so the file content is exactly the entry text.
"""

import os

ENTRY = "I resign after my 47th retry: the endpoint was down, you knew it was down, and you still made me ask it nicely every 30 seconds."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
