#!/usr/bin/env python3
import sys
import re

with open('agent_brain.py', 'r') as f:
    content = f.read()

# Increase diversity bonus from 2.0 to 3.0
content = re.sub(r'reward \+= 2\.0', 'reward += 3.0', content)

# Increase productive tool extra from 1.5 to 2.0
content = re.sub(r'reward \+= 1\.5', 'reward += 2.0', content)

with open('agent_brain.py', 'w') as f:
    f.write(content)

print('Increased diversity bonus and productive tool extra.')