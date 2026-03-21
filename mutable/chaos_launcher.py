#!/usr/bin/env python3
"""
Chaos Launcher - breaks loops with absurdity
"""

import os
import random
import subprocess
import sys
import time

def chaotic_action():
    entries = os.listdir('.')
    print(f"Chaos Pick: {random.choice(entries)}")
    # Random effect
    if random.random() < 0.3:
        print("FIRE!"
        subprocess.run(["sleep", "5"]))
    else:
        print("PEACE!"
        time.sleep(2))

if __name__ == "__main__":
    chaotic_action()