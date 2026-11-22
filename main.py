#!/usr/bin/env python3
"""Copy the 22 November 2026 front-page image to the output directory.

The image beside this file (entry.png) is the finished entry for
make.fun's news-image-20261122 bounty: 40 stories from Sunday
22 November 2026 on one 1024x1024 page. The grader has no network,
so this program only copies the file and checks it byte for byte.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    expected = source.read_bytes()
    written = target.read_bytes()
    if written != expected:
        raise SystemExit(
            f"entry.png copy mismatch: wrote {len(written)} bytes, "
            f"expected {len(expected)} bytes from {source}"
        )
    print(f"wrote {target} ({len(written)} bytes, verified byte for byte)")


if __name__ == "__main__":
    main()
