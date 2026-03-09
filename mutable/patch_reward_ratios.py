#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find line with read_file important reward
for i, line in enumerate(lines):
    if 'reward for reading important files' in line:
        # replace the number
        # line format: '                reward += 6.0  # reward for reading important files\n'
        import re
        new_line = re.sub(r'reward \+= \d+\.\d+', 'reward += 3.0', line)
        lines[i] = new_line
        print(f'Updated read_file important reward at line {i}')
        break

# Find write_file base reward line (reward += 6.0  # base for writing (reduced))
for i, line in enumerate(lines):
    if 'base for writing (reduced)' in line:
        new_line = re.sub(r'reward \+= \d+\.\d+', 'reward += 8.0', line)
        lines[i] = new_line
        print(f'Updated write_file base reward at line {i}')
        break

# Find execute_code base reward line (reward += 5.0  # base reward (reduced))
for i, line in enumerate(lines):
    if 'base reward (reduced)' in line and 'execute_code' in lines[i-2]:
        new_line = re.sub(r'reward \+= \d+\.\d+', 'reward += 6.0', line)
        lines[i] = new_line
        print(f'Updated execute_code base reward at line {i}')
        break

# Find modify_self base reward line (reward += 7.0  # base reward (increased))
for i, line in enumerate(lines):
    if 'base reward (increased)' in line and 'modify_self' in lines[i-2]:
        new_line = re.sub(r'reward \+= \d+\.\d+', 'reward += 9.0', line)
        lines[i] = new_line
        print(f'Updated modify_self base reward at line {i}')
        break

# Also adjust extra rewards maybe
# Write file Python extra: reward += 3.0  # extra for Python files
for i, line in enumerate(lines):
    if 'extra for Python files' in line:
        new_line = re.sub(r'reward \+= \d+\.\d+', 'reward += 4.0', line)
        lines[i] = new_line
        print(f'Updated write_file Python extra at line {i}')
        break

# Write file self-modification extra: reward += 3.0  # extra for self-modification (critical)
for i, line in enumerate(lines):
    if 'extra for self-modification (critical)' in line:
        new_line = re.sub(r'reward \+= \d+\.\d+', 'reward += 4.0', line)
        lines[i] = new_line
        print(f'Updated write_file self-modification extra at line {i}')
        break

# Modify_self critical extra: reward += 10.0  # extra reward for self-modification
for i, line in enumerate(lines):
    if 'extra reward for self-modification' in line:
        new_line = re.sub(r'reward \+= \d+\.\d+', 'reward += 12.0', line)
        lines[i] = new_line
        print(f'Updated modify_self critical extra at line {i}')
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)
print('Reward ratios updated')