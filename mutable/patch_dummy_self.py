#!/usr/bin/env python3
import sys

with open('train_continuous.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'self.tool_penalty_factor = 0.15' in line:
        lines[i] = line.replace('0.15', '0.3')
        print(f'Line {i+1}: updated tool_penalty_factor to 0.3')
    # also update tool_decay_factor if we want, keep 0.85

with open('train_continuous.py', 'w') as f:
    f.writelines(lines)

print('DummySelf updated.')