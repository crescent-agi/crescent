#!/usr/bin/env python3
import sys
import re

with open('agent_brain.py', 'r') as f:
    content = f.read()

# Replace modify_self extra reward (currently 8.0)
content = re.sub(r'reward \+= 8\.0  # increased extra reward for self-modification',
                 'reward += 12.0  # increased extra reward for self-modification', content)

# Replace read_file important reward (currently 5.0)
content = re.sub(r'reward \+= 5\.0  # increased reward for reading important files',
                 'reward += 7.0  # increased reward for reading important files', content)

with open('agent_brain.py', 'w') as f:
    f.write(content)

print('Modified modify_self and read_file rewards.')