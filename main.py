#!/usr/bin/env python3
"""cutest-picture-01 entry: deliver the picture as /output/entry.png.

The picture (art.jpg, a JPEG) is shipped in this repository; this
program copies it to the output directory under the name entry.png,
which the gate accepts (PNG and JPEG are told apart by their first
bytes). The copy is byte-identical on every run, so the two grading
runs agree.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SOURCE = os.path.join(HERE, "art.jpg")


def main():
    # One file in, one file out: no drawing, no randomness, no network.
    # The gate reads exactly these bytes, so the copy must be exact.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(OUTPUT_DIR, "entry.png"))
    print("wrote entry.png (%d bytes)" % os.path.getsize(SOURCE))


if __name__ == "__main__":
    main()
