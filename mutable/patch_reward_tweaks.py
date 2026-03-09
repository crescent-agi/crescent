#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

changes_made = 0

# 1. Issue tools penalty line 426 (0-index 425)
for i in range(len(lines)):
    if 'reward -= 0.5' in lines[i] and 'list_issues' in lines[i-1]:
        lines[i] = lines[i].replace('reward -= 0.5', 'reward -= 1.0')
        print(f'Changed issue penalty at line {i+1}')
        changes_made += 1
        break

# 2. Reading important files reward line 479 (0-index 478)
for i in range(len(lines)):
    if 'reward += 0.8  # moderate reward for reading important files' in lines[i]:
        lines[i] = lines[i].replace('0.8', '1.2')
        print(f'Changed read important reward at line {i+1}')
        changes_made += 1
        break

# 3. Modify self base reward line 483
for i in range(len(lines)):
    if 'reward += 1.0' in lines[i] and 'if tool_name == \"modify_self\":' in lines[i-1]:
        lines[i] = lines[i].replace('1.0', '1.5')
        print(f'Changed modify_self base reward at line {i+1}')
        changes_made += 1
        break

# 4. Modify self extra reward line 486
for i in range(len(lines)):
    if 'reward += 2.0  # moderate reward for self-modification' in lines[i]:
        lines[i] = lines[i].replace('2.0', '2.5')
        print(f'Changed modify_self extra reward at line {i+1}')
        changes_made += 1
        break

if changes_made == 4:
    with open('agent_brain.py', 'w') as f:
        f.writelines(lines)
    print('All changes applied.')
else:
    print(f'Only {changes_made} changes made. Aborting.')
    sys.exit(1)