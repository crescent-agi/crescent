import sys
sys.path.insert(0, '.')

with open('train_continuous.py', 'r') as f:
    content = f.read()

# Replace DummySelf class
new_dummy = '''class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = deque(maxlen=10)
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.4
        self.episode_tools = set()
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
'''

# Find the old DummySelf block (from 'class DummySelf:' to 'self = DummySelf()')
import re
pattern = r'class DummySelf:.*?self = DummySelf\(\)'
new_content = re.sub(pattern, new_dummy + '\nself = DummySelf()', content, flags=re.DOTALL)

# Fix AGICoreContinuous initialization line
new_content = new_content.replace(
    'core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hidden_size, learning_rate=0.01, use_features=True)',
    'core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hidden_size, learning_rate=0.01, exploration_rate=0.5, epsilon_decay=0.995, epsilon_min=0.05, use_features=True)'
)

# Fix episode loop indentation and add reset
# Find the line 'for episode in range(episodes):'
lines = new_content.split('\n')
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if line.strip() == 'for episode in range(episodes):':
        new_lines.append(line)
        i += 1
        # Check next line's indentation
        if i < len(lines) and lines[i].strip() == '':
            new_lines.append(lines[i])
            i += 1
        # Insert reset lines with proper indentation (4 spaces more)
        indent = len(line) - len(line.lstrip())
        new_lines.append(' ' * (indent + 4) + '# Reset per-episode usage tracking')
        new_lines.append(' ' * (indent + 4) + 'self.reset()')
        new_lines.append(' ' * (indent + 4) + 'episode_reward = 0.0')
        # Continue copying the inner for loop lines
        # The inner for loop should start at same indentation as outer for
        # We'll just keep original lines but ensure they are correctly indented
        # The inner loop line should be at indent + 4
        # Let's assume the next line is 'for step in range(steps_per_episode):'
        # If not, we need to handle.
        # We'll just copy the rest of the lines as they are, but we already added reset lines.
        # So we need to skip any existing lines that were previously inserted by previous patch.
        # We'll just continue copying lines until we reach the end of the function.
        # Simpler: replace the whole block with a corrected version.
        # Let's instead reconstruct the loop from original lines.
        # Let's extract the inner loop lines from original content.
        # This is getting messy.
        # We'll fall back to writing a new run_training function.
        # For now, we'll just keep the existing inner loop lines (they may have wrong indentation).
        # We'll continue copying lines as they appear.
    else:
        new_lines.append(line)
        i += 1

new_content = '\n'.join(new_lines)

# Write new file
with open('train_continuous_new.py', 'w') as f:
    f.write(new_content)

print('Created train_continuous_new.py')