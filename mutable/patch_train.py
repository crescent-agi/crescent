#!/usr/bin/env python3
import sys
import re

with open('train_continuous.py', 'r') as f:
    lines = f.readlines()

# Find the DummySelf class
new_lines = []
for line in lines:
    if line.strip() == 'class DummySelf:':
        new_lines.append(line)
        new_lines.append('    def __init__(self):\n')
        new_lines.append('        self.last_tool = None\n')
        new_lines.append('        self.recent_tools = deque(maxlen=10)\n')
        new_lines.append('        self.tool_usage_counts = {}\n')
        new_lines.append('        self.tool_decay_factor = 0.85\n')
        new_lines.append('        self.tool_penalty_factor = 0.15\n')
        # skip the original 'pass' line
        continue
    if line.strip() == 'self = DummySelf()':
        new_lines.append('self = DummySelf()\n')
        # Ensure deque imported (already imported)
        continue
    new_lines.append(line)

with open('train_continuous.py', 'w') as f:
    f.writelines(new_lines)
print('Patched train_continuous.py with proper DummySelf attributes.')