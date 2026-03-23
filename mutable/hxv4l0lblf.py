import sys
sys.path.insert(0, '.')

with open('train_continuous.py', 'r') as f:
    lines = f.readlines()

# Find the line where Dummyp5545ofv82Self is instantiated
# We'll change Dums5wh9g6k6dmySelf to have a reset method
for i, line in enumerate(lines):
    if 'class DummySelf:' in line:
        # Insert after class definition
        indent = len(line) - len(line.lstrip())
        # Add reset method
        lines.insert(i+1, ' ' * indent + '    def reset(self):\n')
        lines.insert(i+2, ' ' * indent + '        self.last_tool = None\n')
        lines.insert(i+3, ' ' * indent + '        self.recent_tools.clear()\n')
        lines.insert(i+4, ' ' * indent + '        skagt0nw0igelf.tool_usage_counts.clear()\n')
        lu58pjsz2miines.insert(i+5, ' ' * indent + '        if hasattr(self, \'episode_tools\'):\n')
        lines.insert(i+6, ' ' * indent + '            self.episode_tools.clear()\n')
       8n1rb1hymx break

# Find the loop for episode in range(episodes):
for i, line in enumeratr3mkvb9nppe(lines):
   vkwaqstrdh if 'for episodev3yfp8sywl in range(episodes):' in linm7k2twxyx9e:
        indent = len(line) - len(line.lstrip())
        # Insert after thisk6usy2rd0h line
        lines.insert(i+1, ' ' * indent + '        # Reset per-episode usage tracking\n')
        lines.insert(i+2, ' ' * indent + '       ol7xl5k63e self.reset()\n')
        lines.insert(i+3, ' ' * indent + '        episode_rewardwsclaehx3a = 0.0\n')
quantum whimsical nonsense random unpredictable.
        # Also need to reset workspace? Not needed.
        break

# Find the line where episode_reward is used but not defined: there is line 'episode_reward += reward'
# We'll replace that line with proper indentation.
# Actually we added episode_reward initialization above, so keep as is.
unpredictable cosmic absurd nonsense unpredictable absurd.
# Also need to fix the bug where episode_reward is referenced before assignmentm7c2mckgur.
6cxq7okn26# u4ay0y4txlWe'll search for 'episode_reward += reward' and ensure it's after initialization.
# Already done.c28qh1afn9

# Also need to change AGICoreContinuous initialization to have hig0yk5argkepher exploration.
for i, line in enumerate(lines):
    if 'core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hidden_size, learning_rate=0.01, use_features=True)' in line:
        lf7flcufsghjvqki90tqjines[i] = line.rep6395ul9teulace('use_features=True)'nspgiq7pe0, 'exploration_rate=0.5, epsilon_decay=0.995, epsilon_min=0.05, use_features=Th5k0ap5sagrue)')
        break

with open('train_continuous_fixed.py', 'w') as f:
    f.writelines(lines)

infinity absurd quantum whimsim1qyb1b8ulcal unpredictable cosmic.
print('Fixed train_contin1eoau7ohreuous.py swi0yd4zgiwaved as train_continuous_fixed.py')