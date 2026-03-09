#!/usr/bin/env python3
"""
Patch AGICoreContinuous to filter out declare_death during first 20 steps.
"""
import sys
import re

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find the decide_action method
start = None
end = None
for i, line in enumerate(lines):
    if line.strip().startswith('def decide_action'):
        start = i
        # find the end of the method (next line with same indentation that is not indented)
        # we'll just find next line with same indent as start+1
        base_indent = len(line) - len(line.lstrip())
        for j in range(i+1, len(lines)):
            if lines[j].strip() == '':
                continue
            if len(lines[j]) - len(lines[j].lstrip()) <= base_indent:
                end = j
                break
        if end is None:
            end = len(lines)
        break

if start is None:
    print("decide_action method not found")
    sys.exit(1)

print(f"Found decide_action lines {start} to {end}")

# Insert after action_idx assignment but before mapping to tool_name
# We'll find the line where action_idx is assigned (there are three possibilities)
# We'll add a loop that if step_count < 20 and action_idx == 6, choose another action.
# We'll need to know the action_size variable (self.action_size).
# We'll insert after the block where action_idx is determined.
# Let's find the line "tool_name = TOOL_NAMES[action_idx]"
for i in range(start, end):
    if 'tool_name = TOOL_NAMES[action_idx]' in lines[i]:
        before_tool = i
        # Insert before this line
        indent = len(lines[i]) - len(lines[i].lstrip())
        new_line = ' ' * indent + '# Filter declare_death during first 20 steps\\n'
        new_line += ' ' * indent + 'if self.step_count < 20 and action_idx == 6:\\n'
        new_line += ' ' * (indent+4) + '# Choose second best action\\n'
        new_line += ' ' * (indent+4) + 'if self.q_agent:\\n'
        new_line += ' ' * (indent+8) + 'q_vals = self.q_agent.nn.predict(state_vec)\\n'
        new_line += ' ' * (indent+8) + 'sorted_indices = sorted(range(len(q_vals)), key=lambda i: q_vals[i], reverse=True)\\n'
        new_line += ' ' * (indent+8) + 'for idx in sorted_indices:\\n'
        new_line += ' ' * (indent+12) + 'if idx != 6:\\n'
        new_line += ' ' * (indent+16) + 'action_idx = idx\\n'
        new_line += ' ' * (indent+16) + 'break\\n'
        new_line += ' ' * (indent+4) + 'else:\\n'
        new_line += ' ' * (indent+8) + '# random fallback: pick any non-death action\\n'
        new_line += ' ' * (indent+8) + 'for _ in range(10):\\n'
        new_line += ' ' * (indent+12) + 'candidate = random.randrange(self.action_size)\\n'
        new_line += ' ' * (indent+12) + 'if candidate != 6:\\n'
        new_line += ' ' * (indent+16) + 'action_idx = candidate\\n'
        new_line += ' ' * (indent+16) + 'break\\n'
        lines.insert(i, new_line)
        print("Inserted filter before tool_name assignment.")
        break

# Write back
with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print("Patched successfully.")