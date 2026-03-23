#!/usr/bin/env python3
"""
Remove the filter block (both proper and broken) from decide_action.
"""
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find start of proper filter
start = None
for i, line in enumerate(lines):
    if line.strip() == '# Filter declare_death during first 20 steps' and '\\n' not in line:
        start = i
        break

if start is not None:
    # Find end of filter: line with 'break' and next line has less indent
    # We'll just delete until line that contains 'tool_name = TOOL_NAMES' (but before that)
    # Let's find the line after start that has same indent as start and is not empty
    base_indent = len(lines[start]) - len(lines[start].lstrip())
    end = start
    for j in range(start+1, len(lines)):
        if lines[j].strip() == '':
            continue
        if len(lines[j]) - len(lines[j].lstrip()) <= base_indent:
            # This line is less indented, filter block ends before this line
            end = j
            break
    else:
        end = len(lines)
    print(f"Deleting lines {start+1} to {end}")
    del lines[start:end]

# Also delete the broken line (contains \\n)
broken = []
for i, line in enumerate(lines):
    if 'Filter declare_death during first 20 steps\\n' in line:
        broken.append(i)
for idx in reversed(broken):
    del lines[idx]
    print(f"Deleted broken line {idx+1}")

# Ensure there is exactly one tool_name assignment line.
# Find line with tool_name = TOOL_NAMES and delete duplicates.
tool_indices = []
for i, line in enumerate(lines):
    if 'tool_name = TOOL_NAMES' in line:
        tool_indices.append(i)
if len(tool_indices) > 1:
    # Keep the first one, delete others
    for idx in reversed(tool_indices[1:]):
        del lines[idx]
        print(f"Deleted duplicate tool_name line {idx+1}")

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print("Removed filter block.")