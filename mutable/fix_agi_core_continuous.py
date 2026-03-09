#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find the broken line
to_delete = []
for i, line in enumerate(lines):
    if '# Filter declare_death during first 20 steps\\\\n' in line:
        print(f"Found broken line at {i+1}")
        to_delete.append(i)

# Delete broken line(s)
for i in sorted(to_delete, reverse=True):
    del lines[i]

# Now ensure tool_name assignment exists after filter block
# Find line with "# Map action index to tool name"
for i, line in enumerate(lines):
    if '# Map action index to tool name' in line:
        # Insert tool_name assignment after the filter block
        # Need to find where filter block ends
        # Look ahead for line that doesn't start with whitespace (next method)
        j = i + 1
        while j < len(lines) and (lines[j].strip().startswith('#') or lines[j].strip().startswith('if') or lines[j].strip().startswith('else') or lines[j].strip().startswith('for') or lines[j].strip().startswith('break') or lines[j].strip() == ''):
            j += 1
        # j should be at line after filter block
        # Insert tool_name assignment
        lines.insert(j, '        tool_name = TOOL_NAMES[action_idx] if 0 <= action_idx < len(TOOL_NAMES) else TOOL_NAMES[0]\n')
        print(f"Inserted tool_name assignment at line {j+1}")
        break

# Write back
with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print("Fixed agi_core_continuous.py")