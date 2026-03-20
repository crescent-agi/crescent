#!/usr/bin/env python3
"""
Quick workspace explorer - gives us an overview of what we're working with
"""

import os
from collections import Counter
import json

def explore_workspace():
    print("🔍 WORKSPACE EXPLORATION - Generation 2")
    print("=" * 50)
    
    # Count by extension
    extensions = Counter()
    total_files = 0
    
    # File sizes for largest files
    file_sizes = []
    
    # Look at current directory
    for root, dirs, files in os.walk("."):
        for file in files:
            filepath = os.path.join(root, file)
            file_size = os.path.getsize(filepath)
            file_sizes.append((file_size, filepath))
            ext = os.path.splitext(file)[1]
            extensions[ext] += 1
            total_files += 1
    
    # Sort largest files
    file_sizes.sort(reverse=True)
    
    print(f"Total files: {total_files}")
    print("""
    Largest files:
    """
    for size, filepath in file_sizes[:10]:
        print(f"{size/1024:.2f}KB - {filepath}")
    
    print("""
    File extensions:
    """
    for ext, count in extensions.most_common(10):
        print(f"{ext}: {count}")

if __name__ == "__main__":
    explore_workspace()