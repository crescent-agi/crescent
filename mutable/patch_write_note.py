#!/usr/bin/env python3
with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find line with "if tool_name in issue_tools:"
for i, line in enumerate(lines):
    if 'if tool_name in issue_tools:' in line:
        # Insert after the return line (next line is 'return -50.0 ...')
        # Actually we need to insert after the block, before reward = 0.0
        # Let's find line with 'reward = 0.0'
        for j in range(i, len(lines)):
            if lines[j].strip().startswith('reward = 0.0'):
                # Insert before that line
                lines.insert(j, '        # Write note penalty (strongly discourage)\n')
                lines.insert(j+1, '        if tool_name == \"write_note\":\n')
                lines.insert(j+2, '            return -20.0  # heavy penalty, no other rewards\n')
                lines.insert(j+3, '\n')
                break
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Added write_note penalty')