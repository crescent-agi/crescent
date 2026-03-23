#!/usr/bin/env python3
import os, sys, hashlib, json
from collections import defaultdict

def md5(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

root = 'mutable_snapshot'
all_files = []
chaos_pairs = []
chaos_files = set()
sizes = []

for dirpath, dirnames, filenames in os.walk(root):
    for f in filenames:
        path = os.path.join(dirpath, f)
        try:
            size = os.path.getsize(path)
        except OSError:
            continue
        all_files.append((path, size))
        sizes.append((size, path))
        if f.endswith('.chaos'):
            chaos_files.add(path)

# Identify pairs: original and .chaos
for path, size in all_files:
    if path.endswith('.chaos'):
        continue
    chaos_path = path + '.chaos'
    if chaos_path in chaos_files:
        chaos_pairs.append((path, size, chaos_path))

sizes.sort(reverse=True)

print("=== Top 20 largest files ===")
for i, (size, path) in enumerate(sizes[:20], 1):
    print(f"{i:2}. {size:>10}  {path}")

print("\n=== Chaos pairs (original + .chaos) ===")
for i, (orig, size, chaos) in enumerate(chaos_pairs[:20], 1):
    print(f"{i}. {size:>10}  {orig}")
    print(f"   {os.path.getsize(chaos):>10}  {chaos}")
    # Compare checksums if sizes differ
    if size != os.path.getsize(chaos):
        print(f"   SIZE DIFFERS")
    else:
        orig_md5 = md5(orig) if size < 10_000_000 else "SKIP (too big)"
        chaos_md5 = md5(chaos) if size < 10_000_000 else "SKIP (too big)"
        if orig_md5 != chaos_md5:
            print(f"   CONTENT DIFFERS")
    print()

print(f"Total files: {len(all_files)}")
print(f"Chaos files: {len(chaos_files)}")
print(f"Chaos pairs: {len(chaos_pairs)}")
