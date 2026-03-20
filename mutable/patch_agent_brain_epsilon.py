#!/usr/bin/env python3
"""
Patch agent_brain.py to pass epsilon parameters to AGICoreContinuous.
"""
import sys

path = 'agent_brain.py'
with open(path, 'r') as f:
    lines = f.readlines()

# Find line with AGICORE_CLASS(feature_dim=30, hidden_size=32, learning_rate=0.01, use_features=True)
for i, line in enumerate(lines):
    if 'AGICORE_CLASS(feature_dim=30, hidden_size=32, learning_rate=0.01, use_features=True)' in line:
        lines[i] = line.replace('AGICORE_CLASS(feature_dim=30, hidden_size=32, learning_rate=0.01, use_features=True)',
                                 'AGICORE_CLASS(feature_dim=30, hidden_size=32, learning_rate=0.01, exploration_rate=0.02, epsilon_decay=0.998, epsilon_min=0.005, use_features=True)')
        print(f'Changed line {i+1}')
        break

with open(path, 'w') as f:
    f.writelines(lines)
print('Patched agent_brain.py')