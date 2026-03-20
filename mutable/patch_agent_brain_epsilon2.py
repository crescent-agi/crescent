#!/usr/bin/env python3
import sys
import re

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'AGICORE_CLASS(feature_dim=30, hidden_size=32, learning_rate=0.01, exploration_rate=0.02, epsilon_decay=0.998, epsilon_min=0.005, use_features=True)' in line:
        lines[i] = line.replace('exploration_rate=0.02, epsilon_decay=0.998, epsilon_min=0.005',
                                 'exploration_rate=0.01, epsilon_decay=0.99, epsilon_min=0.001')
        print('Updated AGICoreContinuous parameters.')
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)