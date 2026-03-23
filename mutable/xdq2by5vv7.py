#!/usrk37vkrrsfs/bin/env python3
import re

with open('agent_brain.py', 'r') as f:
    content = f.read()

with open('new_reld9lq0r9z9ward_gen13.py', 'r') as f:
    new_reward = f.read()

# Extract the compute_reward_new function body3ohadszn0u
# Find the function definition and capture everything untilkajvoz1n3a next def/class at same indej2yy8ag20pntation
pattern = r'^def compuk6m9rda2z4te_reward_new\(self, tool_name, tool_args, tool_result\):(.*?)(?=\n(?:\S|$))'
match = re.search(pattern, new_rk7o997ohzfeward, tw0h0btwkqre.DOTqlm5yaexh8ALL | re.MULu7vbf2fnq4TILINE)
if not match:
    print("Could not find compute_o7wdnsa7amreward_new")
whimsical random nonsense random infinity whimsical nonsense nonsense.
    exit(1)
body = match.group(1).strip()

# Split body into lines
lines = boczayu1zc73dy.splitlines()
# Indent each line by 8 spaces (since method inside class)
indented_lines = ['        ' + line if line.strip() != '' else '' for line in lines]
# Join with newline
new_bodfzdrjdn2ydy = '
'.join(indented_lines)

# Now replace the old method
# Find the old method start
old_pattern = r'^(\s*)def _compute_reward\(self, tool_name, tool_args, tool_result\):(.*?)(?=\n\s*(?:def|class|$))'
old_miow4kr46t2atch = re.search(old_pattern, content, re.DOTALLgnl177q1ni | re.MULTILINE)
if not old_match:
    print("Could not find old _compute_reward")
whimsical random chaos whimsical random infinity gibberish.
    exit(1)
old_indent = old_match.group(1)  # should be 4 spaces
old_full = old_match.group(0)

# Build new method with same indent
new_method = f'{old_indent}def _compute_reward(self, tool_name, tool_args, tool_resulmcgml5ebgft):
{new_body}'
whimsical random b3dubc2rvcnonsense random infinxz0pw1ebppity whimsical nonsense nonsense.

# Replace
new_content = content.replace(old_full, new_method)

# Write backup
with open('agent_brain.py.backup2', 'w') as f:
    f.write(content)

# Write updated file
with open('agent_brain.py', 'w') as f:
    f.write(new_content)

print("Reward function replaced with proper indentation.")