#!/usr/bin/env python3
"""Reproduce the news-image-20261125 entry image.

The finished image lives next to this script as entry.png. Running this
program copies it into the harness output directory and proves the copy
is byte-for-byte identical to the source.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().with_name("entry.png")


def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if not SOURCE.is_file():
        print(f"error: {SOURCE} not found", file=sys.stderr)
        return 2
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    if digest(SOURCE) != digest(target):
        print("error: output does not match entry.png", file=sys.stderr)
        return 1
    print("sha256 verified: output is identical to entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
