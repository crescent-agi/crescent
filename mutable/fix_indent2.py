#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# line numbers are 0-indexed
line_idx = 410  # line 411 in file (since 0-index)
line = lines[line_idx]
print(f'Line {line_idx+1}: {repr(line)}')
# Determine indentation of previous non-empty line
prev = line_idx - 1
while prev >= 0 and lines[prev].strip() == '':
    prev -= 1
if prev >= 0:
    prev_line = lines[prev]
    indent = len(prev_line) - len(prev_line.lstrip())
    print(f'Previous non-empty line indentation: {indent}')
    # Ensure line starts with that many spaces
    new_line = ' ' * indent + line.lstrip()
    lines[line_idx] = new_line
    print(f'Fixed line: {repr(new_line)}')
else:
    print('No previous line')

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)
print('Fixed')