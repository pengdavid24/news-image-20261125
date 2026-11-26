"""Write the 25 November 2026 world-news summary image to /output/entry.png.

The entry is a single image: entry.png, a 1024x1024 infographic summing up
the day's world news (tankers hit in the Strait of Hormuz, Houthis hitting
a Saudi refinery, US tariffs on 14 nations, Huawei found guilty, Pakistan's
first astronaut aboard Shenzhou-24, and the Australia-Solomon Islands
Pacific pact). This program just copies that image to the output path the
grader reads, so the run is byte-for-byte deterministic.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def sha256(path):
    """SHA-256 of a file, read in full (the image is small)."""
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    size = os.path.getsize(OUTPUT)
    print(f"wrote {OUTPUT} ({size} bytes)")
    # The copy must be exact: same bytes in, same bytes out.
    if sha256(SOURCE) != sha256(OUTPUT):
        print("copy mismatch: output differs from source", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
