#!/usr/bin/env python3
import re

with open('agent_brain.py', 'r') as f:
    content = f.read()

# Read new reward function
with open('new_reward_gen13.py', 'r') as f:
    new_reward_content = f.read()

# Extract the function definition from new_reward_gen13.py
# Find the function compute_reward_new
match = re.search(r'def compute_reward_new\(self, tool_name, tool_args, tool_result\):(.*?)(?=\n\ndef|\nclass|\Z)', new_reward_content, re.DOTALL)
if not match:
    print("Could not find compute_reward_new")
    exit(1)
new_method_body = match.group(1).strip()

# Construct new method string
new_method = f'''    def _compute_reward(self, tool_name, tool_args, tool_result):
        \"\"\"Reward shaping with balanced per-tool decay, stronger productive incentives, and novelty bonuses.\"\"\"
{new_method_body}'''

# Replace old method with new method
# Find the old method pattern
old_pattern = r'(\s+def _compute_reward\(self, tool_name, tool_args, tool_result\):\n(?:.*?\n)+?)(?=\n\S|$)'
# We need to match exactly the method; use DOTALL to span lines
old_match = re.search(old_pattern, content, re.DOTALL)
if not old_match:
    print("Could not find old _compute_reward method")
    exit(1)

old_method = old_match.group(0)
new_content = content.replace(old_method, new_method)

# Write backup
with open('agent_brain.py.backup_gen13', 'w') as f:
    f.write(content)

# Write updated file
with open('agent_brain.py', 'w') as f:
    f.write(new_content)

print("Reward function replaced successfully.")