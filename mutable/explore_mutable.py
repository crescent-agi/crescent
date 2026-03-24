#!/usr/bin/env python3
import os

def explore_directory(dir_path):
    print(f"Exploring: {dir_path}")
    for entry in sorted(os.listdir(dir_path)):
        full_path = os.path.join(dir_path, entry)
        if os.path.isfile(full_path) and entry.endswith('.py'):
            print(f"\n--- {entry} ---")
            try:
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()[:20]
                    print(''.join(lines))
                    if len(lines) == 20:
                        print("...[truncated]")
            except Exception as e:
                print(f"[Error reading: {e}]")
        elif os.path.isdir(full_path):
            print(f"\n[DIR] {entry}/")

explore_directory('.')