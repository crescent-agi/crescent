#!/usr/bin/env python3
"""
Final fix for agi_core_continuous.py: remove broken line and ensure tool_name assignment.
"""
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find broken line
broken_idx = None
for i, line in enumerate(lines):
    if 'Filter declare_death during first 20 steps\\n' in line and 'tool_name = TOOL_NAMES' in line:
        broken_idx = i
        print(f"Found broken line at {i+1}")
        break

if broken_idx is not None:
    del lines[broken_idx]
    print("Deleted broken line.")

# Now ensure tool_name assignment exists after the filter block.
# Find the line after the filter block (maybe after a line containing 'break' and before '# Generate tool arguments')
# Let's find the line '# Generate tool arguments'
for i, line in enumerate(lines):
    if '# Generate tool arguments' in line:
        # The line before should be tool_name assignment; if not, insert.
        if i > 0 and 'tool_name = TOOL_NAMES' not in lines[i-1]:
            indent = len(line) - len(line.lstrip())
            lines.insert(i, ' ' * indent + 'tool_name = TOOL_NAMES[action_idx] if 0 <= action_idx < len(TOOL_NAMES) else TOOL_NAMES[0]\n')
            print("Inserted tool_name assignment before generate arguments.")
        break

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print("Fixed.")