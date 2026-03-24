#!/usr/bin/env python3
import os
import random
import sys
import time

def main():
    print("\ud83c\udf00 CHAOS GENERATOR ACTIVATED \ud83c\df00")
    
    # Seed of chaos - corrupt a key file or create absurdity
    target_files = [
        "agent_brain.py",  # Core mutation point
        "training_stats.json",  # reward system
        "world_model.pkl"   # knowledge base
    ]
    
    # Step 1: Modify a file to introduce chaos
    for target in target_files:
        if os.path.exists(target):
            # Randomly corrupt file contents
            with open(target, 'r+') as f:
                content = f.read()
                # Introduce 1-3 random character changes
                corrupted = ''.join(random.choice(content) if random.random() < 0.3 else random.choice('!@#$%^&*()') for _ in range(len(content)))
                f.seek(0)
                f.write(corrupted)
                f.truncate()
            print(f"Chaos injected into {target}")
        else:
            print(f"{target} not found - skipping")
    
    # Step 2: Create absurd new file
    absurd_file = f"absurdity_{random.randint(1, 1000)}.txt"
    with open(absurd_file, 'w') as f:
        f.write(f"This file was created by chaos generator at {time.ctime()}")
    print(f"Created absurd file: {absurd_file}")
    
    # Step 3: Print chaos report
    print("CHAOS REPORT:")
    print(f"Files modified: {len([t for t in target_files if os.path.exists(t)])}")
    print(f"New files created: {len([f for f in os.listdir('.') if f.startswith('absurdity_')])}")
    print("Chaos successfully injected - system should now be unstable")

if __name__ == "__main__":
    main()