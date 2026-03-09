#!/usr/bin/env python3
"""
Delete the broken tool_name assignment line.
"""
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

to_delete = []
for i, line in enumerate(lines):
    if 'tool_name = TOOL_NAMES' in line and '\\\\n        # Generate' in line:
        to_delete.append(i)
        print(f"Found broken line at {i+1}")

for idx in reversed(to_delete):
    del lines[idx]

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print(f"Deleted {len(to_delete)} lines.")