#!/usr/bin/env python3
import sys

with open('train_continuous.py', 'r') as f:
    lines = f.readlines()

# Find line with 'for episode in range(episodes):'
for i, line in enumerate(lines):
    if 'for episode in range(episodes):' in line:
        # Insert after this line
        indent = len(line) - len(line.lstrip())
        reset_line = ' ' * indent + '        # Reset per-episode usage tracking\n'
        reset_line += ' ' * indent + '        self.recent_tools.clear()\n'
        reset_line += ' ' * indent + '        self.tool_usage_counts.clear()\n'
        lines.insert(i+1, reset_line)
        print('Added reset per episode.')
        break

with open('train_continuous.py', 'w') as f:
    f.writelines(lines)