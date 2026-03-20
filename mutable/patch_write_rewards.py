#!/usr/bin/env python3
import sys
import re

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find write_file block
for i, line in enumerate(lines):
    if line.strip().startswith('reward += 1.8  # base for writing (increased)'):
        lines[i] = '                reward += 2.5  # base for writing (increased)\n'
    elif line.strip().startswith('reward += 2.0  # extra for Python files'):
        lines[i] = '                    reward += 2.5  # extra for Python files\n'
    elif line.strip().startswith("reward += 1.0  # extra for self-modification (critical)"):
        lines[i] = '                    reward += 2.0  # extra for self-modification (critical)\n'

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Updated write_file rewards.')