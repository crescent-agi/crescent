#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find start and end of decide_action
start = None
end = None
for i, line in enumerate(lines):
    if line.strip().startswith('def decide_action'):
        start = i
        print(f"Found method start at line {start+1}")
        break

if start is not None:
    for i in range(start+1, len(lines)):
        if lines[i].strip().startswith('def ') and not lines[i].strip().startswith('def decide_action'):
            end = i
            break
    if end is None:
        end = len(lines)
    
    print(f"Method lines {start+1} to {end}")
    for j in range(start, end):
        print(f"{j+1:3}: {lines[j].rstrip()}")