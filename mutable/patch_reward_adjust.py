#!/usr/bin/env python3
import sys
import os

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# List of replacements: (old substring, new substring)
replacements = [
    # read_file important files reward
    ('reward += 1.5  # increased reward for reading important files', 'reward += 0.8  # moderate reward for reading important files'),
    # modify_self extra
    ('reward += 2.0  # increased reward for self-modification', 'reward += 1.0  # moderate reward for self-modification'),
    # write_file Python extra
    ('reward += 2.0  # extra for Python files (increased)', 'reward += 1.5  # extra for Python files'),
    # write_file self-mod extra (already replaced above, but there is also extra for self-modification in write_file block)
    # There are two lines: one for write_file extra for self-mod, and modify_self extra. We'll handle both.
    # Let's also replace the write_file self-mod extra line:
    # "if 'agent_brain' in filepath or 'agi_core' in filepath:\n                reward += 2.0"
    # We'll need to find that line and replace.
    # We'll do more precise later.
    # execute_code base reward
    ('reward += 1.2  # base reward (increased)', 'reward += 1.5  # base reward'),
    # execute_code extra for no stderr
    ('reward += 0.5', 'reward += 1.0'),  # careful: there may be multiple 0.5s. We'll target the line after "extra if execution succeeded without stderr errors"
    # execute_code extra for meaningful output
    ('reward += 0.4', 'reward += 0.8'),
    # modify_self base reward
    ('reward += 1.2', 'reward += 1.0'),  # this will also affect other 1.2s? There's only modify_self base.
]

# Apply replacements
for i, line in enumerate(lines):
    for old, new in replacements:
        if old in line:
            print(f'Line {i}: replacing {old} -> {new}')
            lines[i] = line.replace(old, new)

# Now we need to replace the write_file self-mod extra line more precisely.
# Let's find the block for write_file.
for i, line in enumerate(lines):
    if 'write file rewards' in line.lower():
        # Look ahead for the pattern
        for j in range(i, i+20):
            if 'if \'agent_brain\' in filepath' in lines[j] or '\"agent_brain\"' in lines[j]:
                # Next line should be reward += 2.0
                if j+1 < len(lines) and 'reward += 2.0' in lines[j+1]:
                    print(f'Line {j+1}: replacing write_file self-mod extra')
                    lines[j+1] = lines[j+1].replace('2.0', '1.0')
                break

# Also adjust the tool_penalty_factor maybe increase to 0.3
for i, line in enumerate(lines):
    if 'self.tool_penalty_factor = 0.25' in line:
        lines[i] = line.replace('0.25', '0.3')
        print(f'Line {i}: increased tool_penalty_factor to 0.3')

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Reward adjustments applied.')