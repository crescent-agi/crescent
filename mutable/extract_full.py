#!/usr/bin/env python3
with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# find start line
start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        start = i
        break
if start is None:
    print('Not found')
    exit(1)

# find next method start after start
end = None
for i in range(start + 1, len(lines)):
    if lines[i].strip().startswith('def '):
        end = i
        break
if end is None:
    end = len(lines)

# print lines with line numbers
for i in range(start, end):
    print(f'{i+1:3}: {lines[i]}', end='')