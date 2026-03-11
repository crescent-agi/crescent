#!/usr/bin/env python3
"""
Backup of critical files before numerical stability fixes.
Generation 223 - applying fixes to prevent sigmoid overflow crash.
"""
import os
import shutil

def backup_file(filepath):
    """Backup a single file."""
    if os.path.exists(filepath):
        backup_path = filepath + ".backup_gen223"
        shutil.copy2(filepath, backup_path)
        print(f"  [BACKUP] {filepath} -> {backup_path}")
    else:
        print(f"  [WARN] {filepath} not found for backup")

def main():
    """Backup critical files."""
    print("=== Generation 223: Backing up files ===")
    files_to_backup = [
        "mutable_snapshot/neural_q_continuous.py",
        "mutable_snapshot/agi_core_continuous.py",
        "mutable_snapshot/world_model_continuous.py",
        "mutable_snapshot/safe_activation.py",
    ]
    for filepath in files_to_backup:
        backup_file(filepath)
    print("\n=== Backup Complete ===")

if __name__ == "__main__":
    main()