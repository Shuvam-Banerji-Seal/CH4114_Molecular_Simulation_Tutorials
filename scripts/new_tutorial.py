#!/usr/bin/env python3
"""Scaffold a new tutorial session folder.

Usage:
    uv run python scripts/new_tutorial.py --number 01 --date 21-08-2026

Creates tutorials/tutorial_01_21-08-2026/ with the standard layout
(README.md, exercises/, examples/) based on tutorials/TEMPLATE.md.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TUTORIALS_DIR = REPO_ROOT / "tutorials"
TEMPLATE = TUTORIALS_DIR / "TEMPLATE.md"

SUBDIRS = ("exercises", "examples")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--number", required=True, help="zero-padded session number, e.g. 01")
    parser.add_argument("--date", required=True, help="session date DD-MM-YYYY, e.g. 21-08-2026")
    args = parser.parse_args()

    folder = TUTORIALS_DIR / f"tutorial_{args.number}_{args.date}"
    if folder.exists():
        print(f"✗ {folder} already exists — aborting.", file=sys.stderr)
        return 1

    folder.mkdir(parents=True)
    for sub in SUBDIRS:
        (folder / sub).mkdir()

    if TEMPLATE.exists():
        (folder / "README.md").write_text(
            TEMPLATE.read_text().replace("{{NUMBER}}", args.number).replace("{{DATE}}", args.date)
        )
    else:
        (folder / "README.md").write_text(f"# Tutorial {args.number} ({args.date})\n")

    print(f"✓ Created {folder.relative_to(REPO_ROOT)}")
    print("  Next: edit README.md, drop content into exercises/ and examples/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
