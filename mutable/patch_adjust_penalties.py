#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Recency penalty line 364? need to find again
for i, line in enumerate(lines):
    if 'reward -= 0.5  # increased penalty for immediate repetition' in line:
        lines[i] = line.replace('0.5', '0.3')
        print(f'Line {i+1}: recency penalty reduced to 0.3')

# Diversity penalty per occurrence
for i, line in enumerate(lines):
    if 'reward -= 0.3 * same_count  # increased penalty per occurrence' in line:
        lines[i] = line.replace('0.3', '0.2')
        print(f'Line {i+1}: diversity penalty per occurrence reduced to 0.2')

# Tool penalty factor maybe reduce from 0.3 to 0.25
for i, line in enumerate(lines):
    if 'self.tool_penalty_factor = 0.3  # penalty per usage count' in line:
        lines[i] = line.replace('0.3', '0.25')
        print(f'Line {i+1}: tool_penalty_factor reduced to 0.25')
    if 'self.tool_penalty_factor = 0.3  # reduced penalty factor' in line:
        lines[i] = line.replace('0.3', '0.25')
        print(f'Line {i+1}: tool_penalty_factor reduced to 0.25')

# Also update DummySelf in train_continuous.py
with open('train_continuous.py', 'r') as f:
    train_lines = f.readlines()
for i, line in enumerate(train_lines):
    if 'self.tool_penalty_factor = 0.3' in line:
        train_lines[i] = line.replace('0.3', '0.25')
        print(f'Train line {i+1}: tool_penalty_factor reduced to 0.25')
with open('train_continuous.py', 'w') as f:
    f.writelines(train_lines)

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Penalties adjusted.')