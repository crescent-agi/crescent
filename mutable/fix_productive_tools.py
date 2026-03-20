#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find first occurrence of issue_tools definition
issue_idx = None
for i, line in enumerate(lines):
    if 'issue_tools = [' in line:
        issue_idx = i
        break
if issue_idx is None:
    print('issue_tools definition not found')
    sys.exit(1)

# Insert productive_tools definition after issue_tools
indent = len(lines[issue_idx]) - len(lines[issue_idx].lstrip())
new_line = ' ' * indent + 'productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]\n'
lines.insert(issue_idx + 1, new_line)

# Delete duplicate line at line 411 (0-index 410)
if lines[410].strip() == 'productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]':
    del lines[410]
    print('Deleted duplicate line 411')
else:
    print('Line 411 does not match expected content')

# Optionally delete later duplicate line 426 (0-index 425)
if lines[425].strip() == 'productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]':
    del lines[425]
    print('Deleted duplicate line 426')
else:
    print('Line 426 does not match expected content')

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Fixed productive_tools definitions')