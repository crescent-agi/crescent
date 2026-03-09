#!/usr/bin/env python3
import re

with open('neural_q_continuous.py', 'r') as f:
    content = f.read()

# Fix missing newline after self.history = []
content = re.sub(r'self\.history = \[\]def choose_action', 'self.history = []\n    def choose_action', content)

with open('neural_q_continuous.py', 'w') as f:
    f.write(content)

print('Syntax fixed.')