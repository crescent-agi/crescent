#!/usr/bin/env python3
import sys
import os

# Read agent_brain.py
with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find start and end of _compute_reward method
start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        start = i
        break
if start is None:
    print("ERROR: _compute_reward method not found")
    sys.exit(1)

# Determine indentation
indent = len(lines[start]) - len(lines[start].lstrip())

# Find end line (next method definition with same indentation)
end = None
for i in range(start + 1, len(lines)):
    if lines[i].strip() == '':
        continue
    if lines[i].startswith(' ' * indent) and lines[i][indent] != ' ':
        if lines[i].strip().startswith('def '):
            end = i
            break
if end is None:
    end = len(lines)

print(f"Method spans lines {start} to {end}")

# Replacement mapping
replacements = [
    # (search phrase, new line)
    ('reward += 6.0  # base for writing (increased from 2.0)', 'reward += 5.0  # base for writing'),
    ('reward += 9.0  # base reward increased from 10.0', 'reward += 6.0  # base reward'),
    ('reward += 8.0  # base reward increased from 5.0', 'reward += 7.0  # base reward'),
    ('reward += 4.0  # increased from 3.0', 'reward += 4.0'),  # execute_code extra success (already 4)
    ('reward += 8.0  # reduced from 10.0', 'reward += 9.0'),  # read_file important
]

# Also need to adjust penalty factors
# We'll find the block and replace lines individually
new_lines = []
i = start
while i < end:
    line = lines[i]
    original = line
    for search, new in replacements:
        if search in line:
            line = new
            print(f'Replaced: {search[:40]}...')
            break
    # Penalty factor adjustments
    if 'if tool_name == "write_file":' in line:
        # next line contains 0.3
        for j in range(i+1, min(i+3, end)):
            if 'self.tool_penalty_factor = 0.3' in lines[j]:
                lines[j] = lines[j].replace('0.3', '0.4')  # increase penalty
                print('Increased write_file penalty factor to 0.4')
                break
    if 'elif tool_name == "modify_self":' in line:
        for j in range(i+1, min(i+3, end)):
            if 'self.tool_penalty_factor = 0.2' in lines[j]:
                lines[j] = lines[j].replace('0.2', '0.3')
                print('Increased modify_self penalty factor to 0.3')
                break
    if 'elif tool_name == "execute_code":' in line:
        for j in range(i+1, min(i+3, end)):
            if 'self.tool_penalty_factor = 0.2' in lines[j]:
                lines[j] = lines[j].replace('0.2', '0.1')
                print('Decreased execute_code penalty factor to 0.1')
                break
    if 'elif tool_name == "read_file":' in line:
        for j in range(i+1, min(i+3, end)):
            if 'self.tool_penalty_factor = 0.2' in lines[j]:
                lines[j] = lines[j].replace('0.2', '0.2')  # unchanged
                break
    new_lines.append(line)
    i += 1

# Replace the old method lines
lines[start:end] = new_lines

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print("Reward function updated for generation 6 iteration 3.")