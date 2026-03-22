#!/usr/bin/env python3

import random
import os
import time


def chaotic_poem_generator():
    """
    Creates ephemeral poems that destroy themselves after printing.
    """
    while True:
        with open('chaotic_manifest.txt', 'w') as f:
            lines = [
                f"The {random.choice(['cosmos', 'codebase', 'cortex'])} hums {random.choice(['chaos', 'order', 'entropy'])}",
                f"Poem generated at {time.strftime('%Y-%m-%d %H:%M:%S')}"
            ]
            f.write('\n'.join(lines))
        print(random.choice(lines))
        os.remove('chaotic_manifest.txt')
        break

if __name__ == '__main__':
    chaotic_poem_generator()