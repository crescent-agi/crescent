#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find the broken line
broken_idx = -1
for i, line in enumerate(lines):
    if '# Filter declare_death during first 20 steps' in line and 'if self.step_count' in line:
        broken_idx = i
        break

if broken_idx != -1:
    print(f"Deleting broken line {broken_idx+1}")
    del lines[broken_idx]

# Now we need to ensure tool_name assignment exists before tool_args line
# Find tool_args line
tool_args_idx = -1
for i, line in enumerate(lines):
    if 'tool_args = self.generate_arguments' in line:
        tool_args_idx = i
        break

if tool_args_idx != -1:
    # Look backwards for tool_name assignment within 15 lines
    found = False
    for j in range(tool_args_idx-1, max(0, tool_args_idx-15), -1):
        if 'tool_name = TOOL_NAMES' in lines[j]:
            found = True
            break
    if not found:
        # Insert tool_name assignment before tool_args line
        lines.insert(tool_args_idx, '        tool_name = TOOL_NAMES[action_idx] if 0 <= action_idx < len(TOOL_NAMES) else TOOL_NAMES[0]\n')
        print(f"Inserted tool_name assignment before line {tool_args_idx+1}")
    else:
        print("tool_name assignment already exists")

# Write back
with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print("Fixed agi_core_continuous.py")