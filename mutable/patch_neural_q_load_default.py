#!/usr/bin/env python3
import sys
import re

with open('neural_q_continuous.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "self.epsilon_min = data.get('epsilon_min', 0.01)" in line:
        lines[i] = line.replace('0.01', '0.001')
        print('Updated load epsilon_min default.')
        break

with open('neural_q_continuous.py', 'w') as f:
    f.writelines(lines)