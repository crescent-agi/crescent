#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Identify lines to delete
to_delete = []
for i, line in enumerate(lines):
    if i == 163:  # line 164 (0-indexed) - the misplaced tool_name assignment
        to_delete.append(i)
    if '# Filter declare_death during first 20 steps' in line and '\\\\n' in line:
        to_delete.append(i)

# Delete in reverse order
for i in sorted(to_delete, reverse=True):
    print(f"Deleting line {i+1}: {repr(lines[i])}")
    del lines[i]

# Now find where filter block ends and insert tool_name assignment after it
# Look for line with '# Map action index to tool name'
for i, line in enumerate(lines):
    if '# Map action index to tool name' in line:
        # Find the next line that is not part of the filter block
        # Filter block lines start with '        ' (8 spaces) and are within the if
        j = i + 1
        while j < len(lines) and lines[j].startswith('        '):
            j += 1
        # Now j is line after filter block (maybe blank line)
        # Insert tool_name assignment before that line
        lines.insert(j, '        tool_name = TOOL_NAMES[action_idx] if 0 <= action_idx < len(TOOL_NAMES) else TOOL_NAMES[0]\n')
        print(f"Inserted tool_name assignment at line {j+1}")
        break

# Write back
with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print("Fixed agi_core_continuous.py")