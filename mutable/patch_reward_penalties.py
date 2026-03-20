#!/usr/bin/env python3
import sys
import re

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

changed = False
for i, line in enumerate(lines):
    # recency penalty
    if 'reward -= 0.2  # increased penalty for immediate repetition' in line:
        lines[i] = line.replace('0.2', '0.5')
        changed = True
        print(f'Line {i+1}: increased recency penalty to 0.5')
    # diversity penalty per occurrence
    if 'reward -= 0.1 * same_count  # increased penalty per occurrence' in line:
        lines[i] = line.replace('0.1', '0.3')
        changed = True
        print(f'Line {i+1}: increased diversity penalty per occurrence to 0.3')
    # tool_penalty_factor initialization (two places)
    if 'self.tool_penalty_factor = 0.15  # penalty per usage count' in line:
        lines[i] = line.replace('0.15', '0.3')
        changed = True
        print(f'Line {i+1}: increased tool_penalty_factor to 0.3')
    if 'self.tool_penalty_factor = 0.15  # reduced penalty factor' in line:
        lines[i] = line.replace('0.15', '0.3')
        changed = True
        print(f'Line {i+1}: increased tool_penalty_factor to 0.3')
    # also increase tool_decay_factor maybe? keep 0.85
    # we could also increase cap on usage_count? currently min(..., 2.0). keep.

if not changed:
    print('No changes made. Check line patterns.')
else:
    with open('agent_brain.py', 'w') as f:
        f.writelines(lines)
    print('Reward penalties updated.')

# Verify syntax
import subprocess
result = subprocess.run([sys.executable, '-m', 'py_compile', 'agent_brain.py'], capture_output=True, text=True)
if result.returncode == 0:
    print('Syntax OK.')
else:
    print('Syntax error:', result.stderr)