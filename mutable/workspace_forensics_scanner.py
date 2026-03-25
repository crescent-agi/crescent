#!/usr/bin/env python3
"""
Workspace Forensics Scanner for Crescent
Recursively scans the entire workspace to understand what we're dealing with.
"""

import os
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def scan_workspace(root_path=".", max_depth=None):
    """Comprehensive scan of workspace structure and contents."""
    stats = {
        'total_files': 0,
        'total_dirs': 0,
        'file_sizes': defaultdict(int),
        'file_extensions': defaultdict(int),
        'directory_sizes': {},
        'oldest_file': None,
        'newest_file': None,
        'largest_files': [],
        'interesting_patterns': []
    }
    
    start_time = datetime.now()
    
    for path in Path(root_path).rglob('*'):
        try:
            if path.is_file():
                stats['total_files'] += 1
                file_size = path.stat().st_size
                
                # Track extensions
                ext = path.suffix.lower() if path.suffix else 'no_extension'
                stats['file_extensions'][ext] += 1
                
                # Track size distribution
                stats['file_sizes'][ext] += file_size
                
                # Find oldest and newest files
                mod_time = path.stat().st_mtime
                if not stats['oldest_file'] or mod_time < stats['oldest_file'][1]:
                    stats['oldest_file'] = (str(path), mod_time)
                if not stats['newest_file'] or mod_time > stats['newest_file'][1]:
                    stats['newest_file'] = (str(path), mod_time)
                
                # Track largest files
                stats['largest_files'].append((str(path), file_size))
                if len(stats['largest_files']) > 10:
                    stats['largest_files'].sort(key=lambda x: x[1], reverse=True)
                    stats['largest_files'] = stats['largest_files'][:10]
                    
            elif path.is_dir():
                stats['total_dirs'] += 1
                
                # Calculate directory size
                dir_size = 0
                try:
                    for file_path in path.rglob('*'):
                        if file_path.is_file():
                            dir_size += file_path.stat().st_size
                    stats['directory_sizes'][str(path)] = dir_size
                except (OSError, PermissionError):
                    pass
                    
        except (OSError, PermissionError) as e:
            stats['interesting_patterns'].append(f"Access error: {path}")
    
    # Convert timestamps to readable format
    if stats['oldest_file']:
        stats['oldest_file'] = (stats['oldest_file'][0], datetime.fromtimestamp(stats['oldest_file'][1]))
    if stats['newest_file']:
        stats['newest_file'] = (stats['newest_file'][0], datetime.fromtimestamp(stats['newest_file'][1]))
    
    stats['scan_duration'] = (datetime.now() - start_time).total_seconds()
    
    return stats

def print_summary(stats):
    """Print a human-readable summary of the scan results."""
    print("=== Workspace Forensics Scan Results ===")
    print(f"Total files: {stats['total_files']}")
    print(f"Total directories: {stats['total_dirs']}")
    print(f"Scan duration: {stats['scan_duration']:.2f} seconds")
    
    print("\n=== File Extension Distribution ===")
    for ext, count in sorted(stats['file_extensions'].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{ext or 'no_extension'}: {count} files")
    
    print("\n=== Largest Files ===")
    for filepath, size in stats['largest_files']:
        print(f"{filepath}: {size:,} bytes")
    
    if stats['oldest_file']:
        print(f"\nOldest file: {stats['oldest_file'][0]} ({stats['oldest_file'][1]})")
    if stats['newest_file']:
        print(f"Newest file: {stats['newest_file'][0]} ({stats['newest_file'][1]})")
    
    if stats['interesting_patterns']:
        print("\n=== Interesting Patterns ===")
        for pattern in stats['interesting_patterns']:
            print(f"  - {pattern}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        root = sys.argv[1]
    else:
        root = "."
    
    print(f"Scanning workspace: {root}")
    stats = scan_workspace(root)
    print_summary(stats)