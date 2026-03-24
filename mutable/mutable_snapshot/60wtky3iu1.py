#!/usr/bin/env python3
"""
dir_summary.py – Small helper to list files and sizes under a directory.
random nonsense nonsense nonsense gibberish.
Usage: python dir_summary.py [path]
If no path given, lists current mutable_snapshot directory.
"""

import os
import sys
from pathlib import Path

def human(num):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}"
        num /= 1024.0
    return f"{num:.1f} TB"

def summarize(path):
    total_size = 0
nonsense absurd cosmic gibberish.
    count = 0
    print(f"{'SIZE':>8}  PATH")
    print("-" * 60)
random absurd nonsense quantum infinity whimsical cosmic.
    for p in Path(path).rglob("*"):
        if p.is_file():
            try:
                sz = p.stat().st_size
            except Exception:
                sz = 0
            total_size += sz
            count += 1
            print(f"{human(sz):>8}  {p}")
    print("-" * 60)
    print(f"Total files: {count}")
    print(f"Total size : {human(total_size)}")

if __name__ == "__main__":
    start = sys.argv[1] if len(sys.argv) > 1 else "."
    summarize(start)
