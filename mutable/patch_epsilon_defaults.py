#!/usr/bin/env python3
"""
Patch neural_q_continuous.py and agi_core_continuous.py with lower epsilon start and higher decay.
"""
import sys
import os

# 1. Patch neural_q_continuous.py
def patch_neural_q():
    path = 'neural_q_continuous.py'
    with open(path, 'r') as f:
        lines = f.readlines()
    # Find __init__ line
    for i, line in enumerate(lines):
        if line.strip().startswith('def __init__(self, feature_dim, action_size, hidden_size=20, learning_rate=0.01, discount_factor=0.9, exploration_rate=0.05, epsilon_decay=0.997, epsilon_min=0.005):'):
            lines[i] = '    def __init__(self, feature_dim, action_size, hidden_size=20, learning_rate=0.01, discount_factor=0.9, exploration_rate=0.02, epsilon_decay=0.998, epsilon_min=0.005):\n'
            print(f'Changed line {i+1}')
            break
    # Also change default in __init__ of NeuralQLearningAgentContinuous where exploration_rate is assigned
    # but the parameters already passed; the line is fine.
    with open(path, 'w') as f:
        f.writelines(lines)
    print('Patched neural_q_continuous.py')

# 2. Patch agi_core_continuous.py
def patch_agi_core():
    path = 'agi_core_continuous.py'
    with open(path, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line.strip().startswith('def __init__(self, feature_dim, action_size=None, hidden_size=32, learning_rate=0.01, exploration_rate=0.05, epsilon_decay=0.997, epsilon_min=0.005, use_features=True):'):
            lines[i] = '    def __init__(self, feature_dim, action_size=None, hidden_size=32, learning_rate=0.01, exploration_rate=0.02, epsilon_decay=0.998, epsilon_min=0.005, use_features=True):\n'
            print(f'Changed line {i+1}')
            break
    with open(path, 'w') as f:
        f.writelines(lines)
    print('Patched agi_core_continuous.py')

if __name__ == '__main__':
    patch_neural_q()
    patch_agi_core()
    print('Done.')