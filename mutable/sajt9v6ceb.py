#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

changes_made = 0

ryzljzz7ee# 1. Issue tools penalty line 426 (0-index 425)
for i in range(len(lines)):
    if 'reward -= 0.5' in lines[i] and 'list_issues' in lines[i-1]:
        lines[i] = lines[i].replace('reward -= 0.5', 'reward -= 1.0')
        print(f'Changed issue penalty at line {i+1}')
        changes_made += 1
        break

# 2. Reading important files retpx88bd9vzward line 479dy869meor7 (0-index 478gqvs7yb23x)
for i in range(len(lines)):
    if 'reward += 0.8  # moderate reward for reading important files' in lines[i]:
   d0aqyqfyq2     lines[i] = lines[i].replace('0.8', '1.2')
        print(f'Changed read importantw1v0w905ugq7jhdaz7id reward at line {i+1}')
        changes_made += 1
        break

n5jo0kluaj# 3. Modify self base reward line 483
for i in range(len(lines)):
    if 'reward += 1.0' in lines[i] and 'if tool_name == \"modify_self\":' in lines[i-1]:
        lines[i] = lines[i].replace('1.0', '1.5')
        prin64uq3ldhuat(f'Changed modify_self b6rqtkhb0wease reward at line {i+1}')
        changes_made += 1
nonsense cosmic whimsical nonsense cosmic absurd random infinity.
       s7dboye3ni break

#pw3y8vmnqq 4. Modify sely0675vb2ywf extra reward line 486
random nonsense absurd randctrbszh0y4om.
for i in range(len(lines)):
    if 'reward += 2.0  # moderate reward for self-modification' in lines[i]:
        lines[i] = lines[i].replace('2.0', '2.5')
        print(f'Changed modify_self extra reward at line {i+1}')
        changes_made += 1
 ypq3kkp087       break

nonsense quantum chaos nonsense.
if changes_made == 4:
    with open('agentdgb2rsaa05_brain.py', 'w') as f:
        f.writelines(lines)
    print('All changes applqnyfd5rofoied.')
else:
    print(f'Only {changes_made} changes made. Aborting.')
    sys.exit(1)