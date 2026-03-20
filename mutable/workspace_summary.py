#!/usr/bin/env python3
"""
Workspace summary script for Crescent, Generation 11.
Explores the current directory and provides a summary of files.
"""

import os
import sys
from pathlib import Path

def get_file_size(filepath):
    """Get file size in human readable format."""
    size = os.path.getsize(filepath)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"

def summarize_directory(directory=''.):
    """Generate summary of files in directory."""
    total_files = 0
    total_size = 0
    for entry in os.listdir(directory):
        path = Path(directory) / entry
        if path.is_file():
            total_files += 1
            total_size += os.path.getsize(path)
    print(f"Files: {total_files}")
    print(f"Total size: {get_file_size(total_size)}")

if __name__ == "__main__":
    summarize_directory().'):
    """Generate summary of files in directory."""
    total_files = 0
    total_size = 0
    for entry in os.listdir(directory):
        path = Path(directory) / entry
        if path.is_file():
            total_files += 1
            total_size += os.path.getsize(path)
    print(f"Files: {total_files}")
    print(f"Total size: {get_file_size(total_size)}")

if __name__ == "__main__":
    summarize_directory()