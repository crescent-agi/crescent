#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

with open('agi_core_continuous.py', 'r') as f:
    content = f.read()

# Delete the broken line (single line with escaped newlines)
lines = content.split('
')
new_lines = []
for line in lines:
    if '# Filter declare_death during first 20 steps' in line and '\\n' in line:
        print(f"Removing broken line: {line[:80]}...")
        continue
    new_lines.append(line)

content = '
'.join(new_lines)

# Now ensure tool_name assignment exists before tool_args
# Find the line with 'tool_args = self.generate_arguments'
lines = content.split('
')
for i, line in enumerate(lines):
    if 'tool_args = self.generate_arguments' in line:
        # Look backwards for tool_name assignment within last 10 lines
        found = False
        for j in range(i-1, max(0, i-15), -1):
            if 'tool_name = TOOL_NAMES' in lines[j]:
                found = True
                break
        if not found:
            # Insert tool_name assignment before this line
            lines.insert(i, '        tool_name = TOOL_NAMES[action_idx] if 0 <= action_idx < len(TOOL_NAMES) else TOOL_NAMES[0]')
            print(f"Inserted tool_name assignment before line {i+1}")
        break

content = '
'.join(lines)

with open('agi_core_continuous.py', 'w') as f:
    f.write(content)

print("Fixed agi_core_continuous.py")