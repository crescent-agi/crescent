#!/usr/bin/env python3
import sys
import re

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find __init__ method
init_start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def __init__'):
        init_start = i
        break
if init_start is None:
    print('__init__ not found')
    sys.exit(1)

# Find the line with NeuralQLearningAgentContinuous
for i in range(init_start, len(lines)):
    if 'NeuralQLearningAgentContinuous' in lines[i]:
        # Replace line with added parameters
        old_line = lines[i]
        # Ensure we match the exact line
        if 'self.q_agent = NeuralQLearningAgentContinuous(feature_dim, self.action_size, hidden_size=hidden_size, learning_rate=learning_rate)' in old_line:
            lines[i] = '            self.q_agent = NeuralQLearningAgentContinuous(feature_dim, self.action_size, hidden_size=hidden_size, learning_rate=learning_rate, exploration_rate=exploration_rate, epsilon_decay=epsilon_decay, epsilon_min=epsilon_min)\n'
            break

# Also need to add parameters to __init__ signature
# Find the line with def __init__(self, feature_dim, action_size=None, ...
for i in range(init_start, init_start + 5):
    if lines[i].strip().startswith('def __init__'):
        # Insert parameters after learning_rate
        # We'll replace the whole line with new signature
        # Let's capture the current line
        line = lines[i]
        # We'll add exploration_rate=0.05, epsilon_decay=0.997, epsilon_min=0.005
        # after learning_rate=0.01
        # Simple approach: replace the line with new signature
        lines[i] = '    def __init__(self, feature_dim, action_size=None, hidden_size=32, learning_rate=0.01, exploration_rate=0.05, epsilon_decay=0.997, epsilon_min=0.005, use_features=True):\n'
        break

# Also need to store these parameters as attributes for later use? Not necessary.
# But we must pass them to NeuralQLearningAgentContinuous (already done).
# Also need to pass them to WorldModelContinuous? Not needed.
# Ensure we add exploration_rate, epsilon_decay, epsilon_min as self attributes maybe.
# Let's add lines after self.use_features = use_features
for i in range(init_start, len(lines)):
    if 'self.use_features = use_features' in lines[i]:
        # Insert after that line
        lines.insert(i + 1, '        self.exploration_rate = exploration_rate\n')
        lines.insert(i + 2, '        self.epsilon_decay = epsilon_decay\n')
        lines.insert(i + 3, '        self.epsilon_min = epsilon_min\n')
        break

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print('Patched AGICoreContinuous with epsilon parameters.')