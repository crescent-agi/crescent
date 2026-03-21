#!/usr/bin/env python

import os

def main():
    print("Exploring artifacts directory...")
    for root, dirs, files in os.walk('artifacts'):
        for file in files:
            if file.endswith('.jsonl') or file.endswith('.pkl') or file.endswith('.pkl.nn'):
                path = os.path.join(root, file)
                print(f"\n=== BEGIN {path} ===")
                try:
                    with open(path, 'rb') as f:
                        sample = f.read(200)
                        print(sample.decode('utf-8', errors='replace')[:5])
                except Exception as e:
                    print(f"Error reading {path}: {e}")

if __name__ == "__main__":
    main()