#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# 1. Change execute_code success extra from 6.0 to 3.0
for i, line in enumerate(lines):
    if 'reward += 6.0' in line and i > 0 and 'extra if execution succeeded without stderr errors' in lines[i-1]:
        lines[i] = line.replace('6.0', '3.0')
        print(f'Changed line {i+1}')
        break

# 2. Remove leftover issue tools penalty block (three lines)
# Find line with '# Penalty for issue tools (discourage) - increased'
for i, line in enumerate(lines):
    if '# Penalty for issue tools (discourage) - increased' in line:
        # Delete this line and next two lines (if and reward line)
        # Ensure next line contains 'if tool_name in issue_tools:' and next next line contains 'reward -= 3.0'
        if i+2 < len(lines) and 'if tool_name in issue_tools:' in lines[i+1] and 'reward -= 3.0' in lines[i+2]:
            del lines[i:i+3]
            print(f'Deleted issue tools penalty block at line {i+1}')
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Final tweaks applied')