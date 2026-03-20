#!/usr/bin/env python3
"""
Workspace Explorer - Generation 9
Explore the current workspace structure and identify key files
"""

import os
import json
from pathlib import Path

def explore_workspace():
    """Explore the current workspace and provide insights"""
    print("=== WORKSPACE EXPLORATION - Generation 9 ===")
    
    # List current directory contents
    print("\nCurrent directory files:")
    for item in os.listdir('.'):
        if os.path.isfile(item):
            size = os.path.getsize(item)
            print(f"  {item} ({size} bytes)")
        elif os.path.isdir(item):
            print(f"  {item}/ (directory)")
    
    # Look for key patterns
    print("\n=== KEY FILE PATTERNS ===")
    key_patterns = ['agent_brain', 'agi_core', 'reward', 'train', 'validate']
    found_files = []
    
    for pattern in key_patterns:
        for item in os.listdir('.'):
            if pattern in item:
                found_files.append(item)
    
    if found_files:
        print("Potentially important files:")
        for file in found_files:
            print(f"  {file}")
    else:
        print("No key pattern files found.")
    
    # Check artifacts directory
    print("\n=== ARTIFACTS DIRECTORY ===")
    artifacts_dir = 'artifacts'
    if os.path.exists(artifacts_dir):
        print(f"Artifacts directory exists with content:")
        for item in os.listdir(artifacts_dir):
            if os.path.isdir(os.path.join(artifacts_dir, item)):
                print(f"  {item}/ (artifact)")
    else:
        print("No artifacts directory found.")

if __name__ == "__main__":
    explore_workspace()