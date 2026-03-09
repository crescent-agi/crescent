#!/usr/bin/env python3
import sys
import re

# Patch neural_q_continuous.py to adjust epsilon parameters
with open('neural_q_continuous.py', 'r') as f:
    lines = f.readlines()

# Find the __init__ method of NeuralQLearningAgentContinuous
for i, line in enumerate(lines):
    if line.strip().startswith('def __init__(self, feature_dim, action_size, hidden_size=20, learning_rate=0.01, discount_factor=0.9, exploration_rate=0.1, epsilon_decay=0.995, epsilon_min=0.01):'):
        # Replace the default values
        lines[i] = '    def __init__(self, feature_dim, action_size, hidden_size=20, learning_rate=0.01, discount_factor=0.9, exploration_rate=0.05, epsilon_decay=0.997, epsilon_min=0.005):\n'
        break

# Write back
with open('neural_q_continuous.py', 'w') as f:
    f.writelines(lines)
print("Patched neural_q_continuous.py epsilon defaults.")