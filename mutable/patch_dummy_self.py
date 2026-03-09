#!/usr/bin/env python3
import sys
import re

with open('train_continuous.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.strip().startswith('self.tool_penalty_factor = 0.25'):
        lines[i] = '        self.tool_penalty_factor = 0.3\n'
        break

with open('train_continuous.py', 'w') as f:
    f.writelines(lines)
print("Updated tool_penalty_factor in DummySelf.")