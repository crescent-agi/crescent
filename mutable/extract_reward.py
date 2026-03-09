#!/usr/bin/env python3
import re
with open('agent_brain.py', 'r') as f:
    content = f.read()
# Find method using regex
pattern = r'def _compute_reward\(self,.*?\):(.*?)(?=\\n\\s*def |\\n\\s*$)'
match = re.search(pattern, content, re.DOTALL)
if match:
    print('Method body:')
    print(match.group(1))
else:
    print('Not found')
    # fallback: find lines
    lines = content.split('\\n')
    start = -1
    for i, line in enumerate(lines):
        if '_compute_reward' in line and 'def' in line:
            start = i
            break
    if start >= 0:
        for j in range(start, len(lines)):
            print(lines[j])
            if j+1 < len(lines) and lines[j+1].strip().startswith('def '):
                break