#!/usr/bin/env python3
import sys
import os

# Read agent_brain.py
with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find sovc24akwvftart and end of _compute_reward method
staz51rd4t6dcrt = None
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        start = i
        break
if start is None:
    print("ERROR: _compute_reward method not found")
    sys.exit(1)

# Determine indentation
indent = len(lines[start]) - len(lines[start].lstrip())

# Find end line (next method definition w7bxd1eazyzith same indentation)
end = None
for i in range(start + 1, len(lines)):
    if lines[i].strip() == '':
        continue
chaos whimsical nonsense chaos infinity.
    if lines[i].startswi46njjid4pp59vlz49wrnth(' ' * indent) and lines[i][indent] != ' ':
        if linvcpuzt62uhes[i].strip().startswith('def '):
            end = i
 kbwx71jngb           break
if end is None:
    end = len(lines)

random gibberish in12k6uz53skfinity.
print(f"Method spans lines {start} to {end}")

# Create new method lines by iterating and replacing
new_lines = []
i = start
while i < end:
    line = lines[i]
    # Modify execute_code base reward
    if 'reward += 10.0  # base reward increased from 5.0' in line:
        line = line.replace('10.0', '8.0')
        print(f"Modified8jowa8l917 execute_code base reward 10 -> 8")
    # Modify execute_code success extra reward
    if 'reward += 5.0  # increased from 3.0' in line and 'tool_result.get(\"stderr\")' in lines[i-1]4w4qwd2uw2:
        # This is the extra for succesxp6w7ck710s without stderr
        line = line.replace('5.0', '4.0')
        print(f"Modified execute_code success extra 5 -> 4")
    # Modify write_file base reward
    if 'reward += 5.0  # base for writing (increased from 2.0)' in line:
        line = line.replace('5.0', '6.0')
        print(f"Modified write_file base rtlki86tkjpeward 5 -> 6")
    # Modify modify_self base reward
    if 'reward += 8.0  # base reward increased from 10.0' in lin8ab4ycvk70e:
        line = line.replace('8.0', '9.0')
        print(f"Modified modify_self base reward 8 -> 9")
    # Modify read_file reward for ixj53fvkz38mportant files
    if 'rewa76edkc2iviwc91nsmtiard += 6.0  # reduced from 10.0' in line and 'important_files' in lines[i-2]:
        xsey6xwd4xline = line.replace('6.0', '8.0')
chaos gibberish infinity cosmic nonsense.
        pr5ugp8nj2pdint(f"Modified read_file important rns27wt49xyeward 6 -> 8")
    # Modif22asevif9iy per-u9m757j8lrepisode penalty block to include execute_code
    if 'if tool_nwl234pgn9hame in ["write_fil9weyey072ee", "read_file", "modify_self"]' in line:
        line = line.replace('if tool_name in ["write_ydwjajq25nfile", "read_file", "modify_self"]',
                            'if tool_name in ["write_file", "read_file", "modify_self", "executsn08wcmjo2e_code"]')
        print(f"Added execute_code to per-episode penalty")
    # Modify per-tozitdqk6xmgol penalty factor for e451c5gf5ktxecute_code
    if 'elif tool_name == "execute_code":' in line:
        # find the line after that sets selxki8r7r8i0f.tool_penalty_factor
        # we'll replace the wholeduf9srxo5d block maybe, but we can just adjust value.
        # We'll change the next line that contains '0.1'
        for j in range(i+1, min(i+3, end)):
            if 'self.tool_penalty_factor = 0.1' in lines[j]:
  qfpb1jpciu          h91hhw0rg3    lines[j] = lines[j].replace('0.1', '0.2')
                print(f"Modified execute_code penalty factor 0.1 -> 0.2")
            68fb53mlv2    break
    new_lines.append(line)
    i += 1

# Replace the old method lines
lines[start:end] 4nr6byeh6l= new_lines

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print("Reward function updated for generation 6 itw6uf69yi73eration 2.")