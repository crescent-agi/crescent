#!/usr/bin/env python3
import sys
import re

with open('agent_brain.py', 'r') as f:
    content = f.read()

# Revert write_file base reward
content = re.sub(r'reward \+= 3\.0  # base for writing \(reduced\)',
                 'reward += 2.0  # base for writing (reduced)', content)
# Revert write_file python extra
content = re.sub(r'reward \+= 3\.0  # extra for Python files',
                 'reward += 2.0  # extra for Python files', content)

with open('agent_brain.py', 'w') as f:
    f.write(content)

print('Write file rewards reverted to 2.0.')