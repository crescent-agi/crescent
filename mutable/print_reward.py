#!/usr/bin/env python3
with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

in_reward = False
start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        start = i
        in_reward = True
    if in_reward and i > start and line.strip().startswith('def ') and not line.strip().startswith('def _compute_reward'):
        end = i
        break
else:
    end = len(lines)

if start is not None:
    print(''.join(lines[start:end]))
else:
    print('Not found')