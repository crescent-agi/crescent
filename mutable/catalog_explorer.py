#!/usr/bin/env python3
"""
Crescent's Artifact Catalog Explorer
Scans the workspace and mutable_snapshot to index all trained models,
their variants, sizes, and relationships.
"""

import os
import json
from pathlib import Path
from collections import defaultdict

def scan_directory(base_path, max_depth=6):
    """Recursively scan for artifact files and collect metadata."""
    artifacts = []
    base = Path(base_path)
    
    if not base.exists():
        return artifacts  # Return empty list if base doesn't exist
    
    for root, dirs, files in os.walk(base):
        for file in files:
            if file.endswith(('.pkl', '.json', '.nn')):
                rel_path = Path(root).relative_to(base)
                artifacts.append(str(rel_path))
    return artifacts

if __name__ == "__main__":
    print(json.dumps(scan_directory("."), indent=2))