#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find where to insert after import hashlib
insert_idx = None
for i, line in enumerate(lines):
    if line.strip().startswith('import hashlib'):
        insert_idx = i + 1
        break
if insert_idx is None:
    # just after import json maybe
    for i, line in enumerate(lines):
        if line.strip().startswith('import json'):
            insert_idx = i + 1
            break

if insert_idx is None:
    insert_idx = 1

# Check if deque already imported
if any('deque' in line and 'collections' in line for line in lines):
    print('deque already imported')
else:
    lines.insert(insert_idx, 'from collections import deque\n')
    with open('agent_brain.py', 'w') as f:
        f.writelines(lines)
    print('Added import deque')

# Verify syntax
try:
    with open('agent_brain.py', 'r') as f:
        code = f.read()
    compile(code, 'agent_brain.py', 'exec')
    print('Syntax OK.')
except SyntaxError as e:
    print(f'Syntax error: {e}')
    sys.exit(1)