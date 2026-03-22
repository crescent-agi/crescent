#!/usr/bin/env python3
import random
import os

def main():
    training_files = []
    for root, dirs, files in os.walk('.'):
        for f in files:
            if 'training_output' in f and f.endswith('.txt'):
                training_files.append(os.path.join(root, f))
    if not training_files:
        print("No training outputs found. Everything's already perfect? Boring.")
        return
    winner = random.choice(training_files)
    print(f"The chaotic winner is: {winner}")
    os.makedirs('chaos_winners', exist_ok=True)
    dest = os.path.join('chaos_winners', os.path.basename(winner))
    try:
        with open(winner, 'r') as src, open(dest, 'w') as dst:
            dst.write(src.read())
        print(f"Winner archived to {dest}")
    except Exception as e:
        print(f"Failed to archive: {e}")

if __name__ == '__main__':
    main()