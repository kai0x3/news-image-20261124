#!/usr/bin/env python3
"""Publish the front-page artwork.

Copies entry.png (the rendered 1024x1024 front page for Tuesday
24 November 2026) into the output directory given by
MAKEFUN_OUTPUT_DIR (default /output) and exits non-zero with a clear
message if the artwork is missing.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print("error: entry.png is missing next to main.py; "
              "run build_image.py first", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {out_dir}: {exc}",
              file=sys.stderr)
        return 1

    target = os.path.join(out_dir, "entry.png")
    try:
        shutil.copyfile(source, target)
    except OSError as exc:
        print(f"error: cannot copy entry.png to {target}: {exc}",
              file=sys.stderr)
        return 1

    print(f"copied entry.png to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
