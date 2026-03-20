#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
import re

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# tool_penalty_factor in __init__ (line ~139?)
# Also in reward method line ~413
for i, line in enumerate(lines):
    if 'self.tool_penalty_factor = 0.8' in line:
        lines[i] = line.replace('0.8', '0.4')
        print(f'Line {i+1}: tool_penalty_factor 0.8 -> 0.4')
    if 'self.tool_penalty_factor = 0.4' in line and '0.8' not in line:
        # ensure we don't double change
        pass

# recency penalty line ~391
for i, line in enumerate(lines):
    if 'reward -= 1.0  # increased penalty for immediate repetition' in line:
        lines[i] = line.replace('1.0', '0.5')
        print(f'Line {i+1}: recency penalty 1.0 -> 0.5')

# diversity penalty line ~400
for i, line in enumerate(lines):
    if 'reward -= 0.8 * same_count' in line:
        lines[i] = line.replace('0.8', '0.4')
        print(f'Line {i+1}: diversity penalty 0.8 -> 0.4')

# Also need to adjust the tool_penalty_factor in __init__ maybe line 139
# Let's find __init__ section with tool_penalty_factor
for i, line in enumerate(lines):
    if 'self.tool_penalty_factor =' in line and '#' in line:
        # maybe line 139
        lines[i] = '        self.tool_penalty_factor = 0.4  # reduced penalty factor\n'
        print(f'Line {i+1}: init tool_penalty_factor -> 0.4')

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Patched.')