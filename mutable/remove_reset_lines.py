#!/usr/bin/env python3
import sys

with open('train_continuous.py', 'r') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if '# Reset per-episode usage tracking' in line:
        skip = True
        continue
    if skip and ('self.recent_tools.clear()' in line or 'self.tool_usage_counts.clear()' in line):
        continue
    else:
        skip = False
        new_lines.append(line)

with open('train_continuous.py', 'w') as f:
    f.writelines(new_lines)

print('Reset lines removed.')