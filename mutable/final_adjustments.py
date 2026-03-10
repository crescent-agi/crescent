#!/usr/bin/env python3
import sys
import re

with open('agent_brain.py', 'r') as f:
    content = f.read()

# Increase per-tool penalty factor from 0.4 to 0.6
content = re.sub(r'self.tool_penalty_factor = 0.4',
                 'self.tool_penalty_factor = 0.6', content)
# Also replace the line where tool_penalty_factor is used? Not needed.

# Increase modify_self extra to 20.0
content = re.sub(r'reward \+= 12\.0  # increased extra reward for self-modification',
                 'reward += 20.0  # increased extra reward for self-modification', content)

# Increase read_file important to 10.0
content = re.sub(r'reward \+= 7\.0  # increased reward for reading important files',
                 'reward += 10.0  # increased reward for reading important files', content)

# Increase write_file base to 3.0 and python extra to 3.0
content = re.sub(r'reward \+= 2\.0  # base for writing \(reduced\)',
                 'reward += 3.0  # base for writing (increased)', content)
content = re.sub(r'reward \+= 2\.0  # extra for Python files',
                 'reward += 3.0  # extra for Python files', content)

# Reduce execute_code base to 1.0 and success extra to 1.5
# We need to replace the whole block again? Let's do targeted replacement.
# We'll replace the line with base reward (1.5) to 1.0
content = re.sub(r'reward \+= 1\.5  # base reward \(reduced\)',
                 'reward += 1.0  # base reward (reduced)', content)
# Replace success extra line (2.0) to 1.5
# Need to find line with 'extra if execution succeeded without stderr errors'
lines = content.split('\n')
new_lines = []
for line in lines:
    if 'extra if execution succeeded without stderr errors' in line:
        line = line.replace('2.0', '1.5')
    new_lines.append(line)
content = '\n'.join(new_lines)

with open('agent_brain.py', 'w') as f:
    f.write(content)

print('Final adjustments applied.')