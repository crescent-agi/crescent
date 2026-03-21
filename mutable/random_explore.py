#!/usr/bin/env python3
import os, random, sys

def is_text(filepath, lines=5):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f.readlines(lines)):
                print(f"{filepath}: {line.rstrip()}")
        return True
    except Exception:
        return False

def sample_files(directory='.', n=5):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            all_files.append(os.path.join(root, f))
    return random.sample(all_files, min(n, len(all_files))) if all_files else []

if __name__ == "__main__":
    sampled = sample_files()
    for f in sampled:
        print(f"Path: {f}")
        if is_text(f):
            print(f"First 5 lines:")
            is_text(f)