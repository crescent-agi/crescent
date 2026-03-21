#!/usr/bin/env python3
"""
Crescent's workspace explorer - generation 42
Small helper to understand the chaos.
"""
import os
import json
from datetime import datetime
from pathlib import Path

def list_recent_files(top_dir='.', n=20):
    """List most recently modified files."""
    files = []
    for root, dirs, filenames in os.walk(top_dir):
        for f in filenames:
            path = Path(root) / f
            try:
                mtime = path.stat().st_mtime
                size = path.stat().st_size
                files.append({
                    'path': str(path),
                    'mtime': mtime,
                    'size': size,
                    'modified': datetime.fromtimestamp(mtime).isoformat()
                })
            except (OSError, PermissionError):
                continue
    files.sort(key=lambda x: x['mtime'], reverse=True)
    return files[:n]

def count_by_type(top_dir='.'):
    """Count files by extension."""
    from collections import Counter
    counts = Counter()
    for root, dirs, filenames in os.walk(top_dir):
        for f in filenames:
            ext = Path(f).suffix.lower() or 'no_ext'
            counts[ext] += 1
    return counts.most_common()

def find_large_files(top_dir='.', min_size_mb=1):
    """Find files larger than threshold."""
    large = []
    for root, dirs, filenames in os.walk(top_dir):
        for f in filenames:
            path = Path(root) / f
            try:
                size = path.stat().st_size
                if size >= min_size_mb * 1024 * 1024:
                    large.append({
                        'path': str(path),
                        'size_mb': size / (1024*1024)
                    })
            except (OSError, PermissionError):
                continue
    large.sort(key=lambda x: x['size_mb'], reverse=True)
    return large

def main():
    print("=== WORKSPACE EXPLORER ===")
    print()

    print("Recent files (most recently modified):")
    for f in list_recent_files(n=15):
        print(f"  {f['size']:>8} {f['modified']} {f['path']}")
    print()

    print("File types:")
    for ext, cnt in count_by_type()[:15]:
        print(f"  {ext:>10}: {cnt}")
    print()

    print("Large files (>1MB):")
    for f in find_large_files(min_size_mb=1)[:15]:
        print(f"  {f['size_mb']:>6.1f}MB {f['path']}")
    print()

    # Check mutable_snapshot structure
    print("Mutable snapshot contents:")
    ms_dir = Path('mutable_snapshot')
    if ms_dir.exists():
        for item in sorted(ms_dir.iterdir())[:20]:
            if item.is_file():
                print(f"  {item.name}")
    else:
        print("  (none)")

if __name__ == '__main__':
    main()
