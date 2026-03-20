#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'reward -= 1.0' in line and 'list_issues' in lines[i-1]:
        lines[i] = line.replace('1.0', '2.0')
        print(f'Changed issue penalty from -1.0 to -2.0 at line {i+1}')
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)