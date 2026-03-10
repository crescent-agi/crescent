#!/usr/bin/env python3
"""
Delete the broken filter line that contains backslash-n.
"""
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'Filter declare_death' in line and '\\n' in line:
        print("Skipping broken line:", line[:100])
        continue
    new_lines.append(line)

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(new_lines)

print("Deleted broken filter line.")