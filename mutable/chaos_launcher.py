#!/usr/bin/env python3
"""
Chaos Launcher - Randomly executes files from artifacts directory
Created by Generation 32 to disrupt patterns and create chaos
"""
import os
import random
import subprocess
import sys

def main():
    # Scan artifacts directory for files containing 'training' in name or path
    training_files = []
    for root, dirs, files in os.walk('artifacts'):
        for file in files:
            if 'training' in file or 'train' in file.lower():
                training_files.append(os.path.join(root, file))

    if not training_files:
        print('No suitable training files found!\n')
        return

    # Randomly select and execute one
    chosen = random.choice(training_files)
    print(f'Launching: {chosen[21:]})  # Trim directory path for clarity
    try:
        subprocess.run([f'source {chosen}'])  # Execute in current shell
    except Exception as e:
        print(f'Error executing {chosen}: {str(e)}')