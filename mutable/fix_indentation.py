#!/usr/bin/env python3
import sys

with open('train_continuous.py', 'r') as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if 'self.recent_tools.clear()' in line and 'Reset per-episode usage tracking' in lines[i-1]:
        # Remove these three lines
        i += 3  # skip them
        continue
    new_lines.append(line)
    i += 1

# Now insert properly indented lines after 'for episode in range(episodes):'
for j, line in enumerate(new_lines):
    if 'for episode in range(episodes):' in line:
        indent = len(line) - len(line.lstrip())
        # Insert after this line
        new_lines.insert(j+1, ' ' * indent + '        # Reset per-episode usage tracking\\n')
        new_lines.insert(j+2, ' ' * indent + '        self.recent_tools.clear()\\n')
        new_lines.insert(j+3, ' ' * indent + '        self.tool_usage_counts.clear()\\n')
        break

with open('train_continuous.py', 'w') as f:
    f.writelines(new_lines)

print('Fixed indentation.')