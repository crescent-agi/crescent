#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'return reward    def _get_journal_content' in line:
        # split at '    def _get_journal_content'
        parts = line.split('    def _get_journal_content')
        if len(parts) == 2:
            lines[i] = parts[0].rstrip() + '\n\n    def _get_journal_content' + parts[1]
            print(f"Fixed line {i+1}")
            break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)
print("Fixed.")