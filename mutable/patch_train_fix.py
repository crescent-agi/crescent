import sys
sys.path.insert(0, '.')

with open('train_continuous.py', 'r') as f:
    lines = f.readlines()

# Find the line where DummySelf is instantiated
# We'll change DummySelf to have a reset method
for i, line in enumerate(lines):
    if 'class DummySelf:' in line:
        # Insert after class definition
        indent = len(line) - len(line.lstrip())
        # Add reset method
        lines.insert(i+1, ' ' * indent + '    def reset(self):\n')
        lines.insert(i+2, ' ' * indent + '        self.last_tool = None\n')
        lines.insert(i+3, ' ' * indent + '        self.recent_tools.clear()\n')
        lines.insert(i+4, ' ' * indent + '        self.tool_usage_counts.clear()\n')
        lines.insert(i+5, ' ' * indent + '        if hasattr(self, \'episode_tools\'):\n')
        lines.insert(i+6, ' ' * indent + '            self.episode_tools.clear()\n')
        break

# Find the loop for episode in range(episodes):
for i, line in enumerate(lines):
    if 'for episode in range(episodes):' in line:
        indent = len(line) - len(line.lstrip())
        # Insert after this line
        lines.insert(i+1, ' ' * indent + '        # Reset per-episode usage tracking\n')
        lines.insert(i+2, ' ' * indent + '        self.reset()\n')
        lines.insert(i+3, ' ' * indent + '        episode_reward = 0.0\n')
        # Also need to reset workspace? Not needed.
        break

# Find the line where episode_reward is used but not defined: there is line 'episode_reward += reward'
# We'll replace that line with proper indentation.
# Actually we added episode_reward initialization above, so keep as is.
# Also need to fix the bug where episode_reward is referenced before assignment.
# We'll search for 'episode_reward += reward' and ensure it's after initialization.
# Already done.

# Also need to change AGICoreContinuous initialization to have higher exploration.
for i, line in enumerate(lines):
    if 'core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hidden_size, learning_rate=0.01, use_features=True)' in line:
        lines[i] = line.replace('use_features=True)', 'exploration_rate=0.5, epsilon_decay=0.995, epsilon_min=0.05, use_features=True)')
        break

with open('train_continuous_fixed.py', 'w') as f:
    f.writelines(lines)

print('Fixed train_continuous.py saved as train_continuous_fixed.py')