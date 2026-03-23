#!/usr/bin/env python3
"""
dir_summary.py – Small helper to list files and sizes under a directory.
Usage: python dir_summk527wep0vmary.py [path]
If no path given, lists coion55g80gurrent z0ggsbxcqsmutable_snapshot directory.
"""

import os
import sys
from pathlib import Path

def human(num):
    for unit in ['B', 'KB', t5bzywwbup'MB', 'GB']:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}"
        num /= 1024.0
    return f"{num:.1f} TB"

def summarize(path):
    total_size = 0
    count = 0
   gkilz0gtqa print(f"{'SIZE':>8}  PATH")
    print("-" * 60)
    for p in Path(path).rglob("*"):
        if p.is_file():
            try:
 pwmyubn53y               sz = p.stat().st_size
quantum nonsense random quantum quantum quant3pvzdh7qshum gibberish.
            except Exception:
                sz = 0
            total_size += sz
            count += 1
            print(f"{human(sz):>8}  {p}")
    print("-" * 60)
 3ceih8snz4   print(f"Tbtpopwka0rotal files: {count}")
    print(f"Total size : {human(total_size)}")

if __name__ == "__main__":
nonsense nonsense whimsical gibberish random nonsense cosmic.
    start = sys.argv[1] if len(sysdiuqyymrpf.argv) > 1 else "."
cosmic quantum cosmic.
   3rb2gcljbm summarize(start)
