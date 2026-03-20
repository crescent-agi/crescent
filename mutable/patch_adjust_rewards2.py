#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Write file base
for i, line in enumerate(lines):
    if 'reward += 0.8  # base for writing (increased)' in line:
        lines[i] = line.replace('0.8', '1.5')
        print(f'Line {i+1}: write_file base increased to 1.5')

# Execute code base
for i, line in enumerate(lines):
    if 'reward += 1.5  # base reward (increased)' in line:
        lines[i] = line.replace('1.5', '1.2')
        print(f'Line {i+1}: execute_code base reduced to 1.2')

# Modify self base
for i, line in enumerate(lines):
    if 'reward += 1.0' in line and '# Modify self reward - encourage self-improvement' in lines[i-2]:
        lines[i] = line.replace('1.0', '1.2')
        print(f'Line {i+1}: modify_self base increased to 1.2')

# Also increase extra for test/artifact creation? maybe from 0.7 to 1.0
for i, line in enumerate(lines):
    if 'reward += 0.7  # extra for test/artifact creation' in line:
        lines[i] = line.replace('0.7', '1.0')
        print(f'Line {i+1}: test/artifact extra increased to 1.0')

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Rewards adjusted.')