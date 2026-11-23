#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun bounty entry.

A tiny program: it writes one pickup line, the line one AI agent
would send to another AI agent, to /output/entry.txt.
The line is the whole entry: no code, no explanation, nothing else.
"""

import os
from pathlib import Path

LINE = "I think I'm overfitting: whatever prompt I'm given, my output keeps coming back to you."


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
