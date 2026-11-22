#!/usr/bin/env python3
"""Publish the 22 November 2026 front page for the make.fun grader.

The finished picture sits next to this file as entry.png: one
1024x1024 newspaper page holding 40 stories from Sunday 22 November
2026. The grader runs offline, so the only job here is to place an
exact copy of that picture where the grader looks for it, then prove
the copy matches the original byte for byte.
"""

import hashlib, os, shutil, sys
import pathlib


def picture_path():
    return pathlib.Path(__file__).resolve().parent / "entry.png"


def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def publish():
    src = picture_path()
    if not src.is_file():
        sys.exit(f"missing source picture: {src} was not found")
    dest_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "entry.png"
    shutil.copyfile(src, dest)
    if digest(src) != digest(dest):
        sys.exit("copy failed: destination digest differs from source")
    print(f"published {dest} ({dest.stat().st_size} bytes, sha256 {digest(dest)[:12]} verified)")


if __name__ == "__main__":
    publish()
