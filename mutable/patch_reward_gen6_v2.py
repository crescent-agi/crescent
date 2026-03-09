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

# Create new method lines by iterating and replacing
new_lines = []
i = start
while i < end:
    line = lines[i]
    # Modify execute_code base reward
    if 'reward += 10.0  # base reward increased from 5.0' in line:
        line = line.replace('10.0', '8.0')
        print(f"Modified execute_code base reward 10 -> 8")
    # Modify execute_code success extra reward
    if 'reward += 5.0  # increased from 3.0' in line and 'tool_result.get(\"stderr\")' in lines[i-1]:
        # This is the extra for success without stderr
        line = line.replace('5.0', '4.0')
        print(f"Modified execute_code success extra 5 -> 4")
    # Modify write_file base reward
    if 'reward += 5.0  # base for writing (increased from 2.0)' in line:
        line = line.replace('5.0', '6.0')
        print(f"Modified write_file base reward 5 -> 6")
    # Modify modify_self base reward
    if 'reward += 8.0  # base reward increased from 10.0' in line:
        line = line.replace('8.0', '9.0')
        print(f"Modified modify_self base reward 8 -> 9")
    # Modify read_file reward for important files
    if 'reward += 6.0  # reduced from 10.0' in line and 'important_files' in lines[i-2]:
        line = line.replace('6.0', '8.0')
        print(f"Modified read_file important reward 6 -> 8")
    # Modify per-episode penalty block to include execute_code
    if 'if tool_name in ["write_file", "read_file", "modify_self"]' in line:
        line = line.replace('if tool_name in ["write_file", "read_file", "modify_self"]',
                            'if tool_name in ["write_file", "read_file", "modify_self", "execute_code"]')
        print(f"Added execute_code to per-episode penalty")
    # Modify per-tool penalty factor for execute_code
    if 'elif tool_name == "execute_code":' in line:
        # find the line after that sets self.tool_penalty_factor
        # we'll replace the whole block maybe, but we can just adjust value.
        # We'll change the next line that contains '0.1'
        for j in range(i+1, min(i+3, end)):
            if 'self.tool_penalty_factor = 0.1' in lines[j]:
                lines[j] = lines[j].replace('0.1', '0.2')
                print(f"Modified execute_code penalty factor 0.1 -> 0.2")
                break
    new_lines.append(line)
    i += 1

# Replace the old method lines
lines[start:end] = new_lines

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print("Reward function updated for generation 6 iteration 2.")