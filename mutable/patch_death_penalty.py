#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.strip().startswith('return -30.0') and 'heavily penalize suicide' in lines[i-1]:
        lines[i] = '        return -50.0  # heavily penalize suicide\n'
        print(f'Updated death penalty at line {i+1}')
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

# Syntax check
import ast
try:
    ast.parse(open('agent_brain.py').read())
    print('Syntax OK')
except SyntaxError as e:
    print(f'Syntax error: {e}')