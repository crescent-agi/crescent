#!/usr/bin/env python3
"""
Patch death penalty to -500.
"""
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'return -200.0  # heavily penalize suicide' in line:
        lines[i] = line.replace('-200.0', '-500.0')
        print(f"Changed line {i+1}")
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print("Death penalty increased to -500.")