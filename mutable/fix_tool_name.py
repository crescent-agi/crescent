#!/usr/bin/env python3
"""
Remove the broken line and add missing tool_name assignment.
"""
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find line containing the huge backslash-n filter
for i, line in enumerate(lines):
    if 'Filter declare_death during first 20 steps\\n' in line and 'tool_name = TOOL_NAMES' in line:
        print(f"Found broken line at {i+1}")
        # Delete this line
        del lines[i]
        # Insert proper tool_name assignment after the filter block
        # The filter block ends at line i-1? Actually we deleted line i, so the filter block lines are before i.
        # We'll insert after the line that ends with 'break' (the else branch)
        # Let's find the line before the deleted line that contains 'break'
        # Since we already deleted, we need to adjust.
        # Instead, we'll just insert at the same position (i) the assignment.
        indent = len(lines[i]) - len(lines[i].lstrip())  # indent of next line
        lines.insert(i, ' ' * indent + 'tool_name = TOOL_NAMES[action_idx] if 0 <= action_idx < len(TOOL_NAMES) else TOOL_NAMES[0]\n')
        print("Inserted tool_name assignment.")
        break

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print("Fixed tool_name assignment.")