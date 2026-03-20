#!/usr/bin/env python3
import sys
import re

with open('neural_q_continuous.py', 'r') as f:
    content = f.read()

# Replace default exploration_rate, epsilon_decay, epsilon_min
content = content.replace('exploration_rate=0.02, epsilon_decay=0.998, epsilon_min=0.005',
                          'exploration_rate=0.01, epsilon_decay=0.99, epsilon_min=0.001')

with open('neural_q_continuous.py', 'w') as f:
    f.write(content)

print('Updated neural_q_continuous defaults.')