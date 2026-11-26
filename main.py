#!/usr/bin/env python3
"""The Comment Above the Code — one line written to /output/entry.txt."""

import os

LINE = "// Do not touch this. The bug and the fix cancel each other out, and neither one knows it yet."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"{len(LINE)} chars: {LINE}")

if __name__ == "__main__":
    main()
