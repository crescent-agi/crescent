#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'exploration_rate=0.02, epsilon_decay=0.998, epsilon_min=0.005' in line:
        lines[i] = line.replace('exploration_rate=0.02, epsilon_decay=0.998, epsilon_min=0.005',
                                'exploration_rate=0.2, epsilon_decay=0.995, epsilon_min=0.05')
        print('Updated exploration parameters')
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)