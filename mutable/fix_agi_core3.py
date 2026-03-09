#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find and delete dead tool_name assignment after return
to_delete = []
for i, line in enumerate(lines):
    if i > 170 and 'tool_name = TOOL_NAMES[action_idx]' in line:
        # Check if it's after the return statement
        # Look backwards for return
        for j in range(i-1, max(0, i-10), -1):
            if 'return tool_name' in lines[j]:
                to_delete.append(i)
                break

# Delete in reverse order
for i in sorted(to_delete, reverse=True):
    print(f"Deleting dead line {i+1}: {lines[i].rstrip()[:80]}")
    del lines[i]

# Now ensure tool_name assignment exists before tool_args generation
# Find line with 'tool_args = self.generate_arguments'
for i, line in enumerate(lines):
    if 'tool_args = self.generate_arguments' in line:
        # Insert tool_name assignment before this line
        # But first check if tool_name already defined earlier in the same block
        # Look backwards for tool_name assignment
        found = False
        for j in range(i-1, max(0, i-20), -1):
            if 'tool_name = TOOL_NAMES' in lines[j]:
                found = True
                break
        if not found:
            lines.insert(i, '        tool_name = TOOL_NAMES[action_idx] if 0 <= action_idx < len(TOOL_NAMES) else TOOL_NAMES[0]\n')
            print(f"Inserted tool_name assignment before line {i+1}")
        break

# Write back
with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print("Fixed agi_core_continuous.py")