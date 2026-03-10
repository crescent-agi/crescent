#!/usr/bin/env python3
"""
Fix the broken patch by inserting proper lines.
"""
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find line with '# Filter declare_death during first 20 steps\n'
for i, line in enumerate(lines):
    if 'Filter declare_death during first 20 steps' in line:
        # Remove this line and the next lines up to the line containing 'tool_name = TOOL_NAMES'
        # We'll just delete from i to i + X where we find 'tool_name ='
        j = i
        while j < len(lines) and 'tool_name = TOOL_NAMES' not in lines[j]:
            j += 1
        # Delete lines i through j-1
        del lines[i:j]
        print(f"Removed {j-i} lines.")
        break

# Now insert proper filter before the tool_name assignment line
for i, line in enumerate(lines):
    if 'tool_name = TOOL_NAMES' in line:
        indent = len(line) - len(line.lstrip())
        filter_lines = [
            ' ' * indent + '# Filter declare_death during first 20 steps
',
            ' ' * indent + 'if self.step_count < 20 and action_idx == 6:
',
            ' ' * (indent+4) + '# Choose a different action
',
            ' ' * (indent+4) + 'if self.q_agent:
',
            ' ' * (indent+8) + 'q_vals = self.q_agent.nn.predict(state_vec)
',
            ' ' * (indent+8) + 'sorted_indices = sorted(range(len(q_vals)), key=lambda i: q_vals[i], reverse=True)
',
            ' ' * (indent+8) + 'for idx in sorted_indices:
',
            ' ' * (indent+12) + 'if idx != 6:
',
            ' ' * (indent+16) + 'action_idx = idx
',
            ' ' * (indent+16) + 'break
',
            ' ' * (indent+4) + 'else:
',
            ' ' * (indent+8) + '# random fallback: pick any non-death action
',
            ' ' * (indent+8) + 'for _ in range(10):
',
            ' ' * (indent+12) + 'candidate = random.randrange(self.action_size)
',
            ' ' * (indent+12) + 'if candidate != 6:
',
            ' ' * (indent+16) + 'action_idx = candidate
',
            ' ' * (indent+16) + 'break
',
        ]
        # Insert filter_lines before current line
        for offset, fline in enumerate(filter_lines):
            lines.insert(i + offset, fline)
        print(f"Inserted filter at line {i}.")
        break

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print("Fixed.")