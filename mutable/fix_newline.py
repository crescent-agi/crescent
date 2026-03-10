#!/usr/bin/env python3
"""
Fix the line with double backslash-n.
"""
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'tool_name = TOOL_NAMES' in line and '\\n' in line:
        # Replace with proper line (remove the \n)
        new_line = line.replace('\\n', '')
        lines[i] = new_line
        print(f"Fixed line {i+1}")
        break

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print("Done.")