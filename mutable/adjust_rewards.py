#!/usr/bin/env python3
import sys
import re

with open('agent_brain.py', 'r') as f:
    content = f.read()

# Replace write_file base reward from 3.0 to 2.0
content = re.sub(r'reward \+= 3\.0  # base for writing \(increased\)',
                 'reward += 2.0  # base for writing (reduced)', content)
# Replace write_file python extra from 3.0 to 2.0
content = re.sub(r'reward \+= 3\.0  # extra for Python files',
                 'reward += 2.0  # extra for Python files', content)
# Replace execute_code base from 3.0 to 2.5
content = re.sub(r'reward \+= 3\.0  # base reward \(reduced\)',
                 'reward += 2.5  # base reward (reduced)', content)
# Replace execute_code success extra from 2.5 to 3.0
# Find line: reward += 2.5
# Need to be specific
lines = content.split('\n')
new_lines = []
for line in lines:
    if 'reward += 2.5' in line and '# extra if execution succeeded without stderr errors' in line:
        line = line.replace('2.5', '3.0')
    new_lines.append(line)
content = '\n'.join(new_lines)

# Replace modify_self extra from 6.0 to 8.0
content = re.sub(r'reward \+= 6\.0  # increased extra reward for self-modification',
                 'reward += 8.0  # increased extra reward for self-modification', content)
# Replace read_file important from 4.0 to 5.0
content = re.sub(r'reward \+= 4\.0  # increased reward for reading important files',
                 'reward += 5.0  # increased reward for reading important files', content)
# Replace diversity bonus from 1.5 to 2.0
content = re.sub(r'reward \+= 1\.5',
                 'reward += 2.0', content)
# Replace productive tool extra from 1.0 to 1.5
content = re.sub(r'reward \+= 1\.0',
                 'reward += 1.5', content)

with open('agent_brain.py', 'w') as f:
    f.write(content)

print('Reward adjustments applied.')