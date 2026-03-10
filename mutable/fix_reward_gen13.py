#!/usr/bin/env python3
import re

with open('agent_brain.py', 'r') as f:
    content = f.read()

with open('new_reward_gen13.py', 'r') as f:
    new_reward = f.read()

# Extract the compute_reward_new function body
# Find the function definition and capture everything until next def/class at same indentation
pattern = r'^def compute_reward_new\\(self, tool_name, tool_args, tool_result\\):(.*?)(?=\\n(?:\\S|$))'
match = re.search(pattern, new_reward, re.DOTALL | re.MULTILINE)
if not match:
    print("Could not find compute_reward_new")
    exit(1)
body = match.group(1).strip()

# Split body into lines
lines = body.splitlines()
# Indent each line by 8 spaces (since method inside class)
indented_lines = ['        ' + line if line.strip() != '' else '' for line in lines]
# Join with newline
new_body = '\n'.join(indented_lines)

# Now replace the old method
# Find the old method start
old_pattern = r'^(\\s*)def _compute_reward\\(self, tool_name, tool_args, tool_result\\):(.*?)(?=\\n\\s*(?:def|class|$))'
old_match = re.search(old_pattern, content, re.DOTALL | re.MULTILINE)
if not old_match:
    print("Could not find old _compute_reward")
    exit(1)
old_indent = old_match.group(1)  # should be 4 spaces
old_full = old_match.group(0)

# Build new method with same indent
new_method = f'{old_indent}def _compute_reward(self, tool_name, tool_args, tool_result):\n{new_body}'

# Replace
new_content = content.replace(old_full, new_method)

# Write backup
with open('agent_brain.py.backup2', 'w') as f:
    f.write(content)

# Write updated file
with open('agent_brain.py', 'w') as f:
    f.write(new_content)

print("Reward function replaced with proper indentation.")