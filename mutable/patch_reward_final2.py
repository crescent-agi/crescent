#!/usr/bin/env python3
import sys
import os
import re

# Read agent_brain.py
with open('agent_brain.py', 'r') as f:
    content = f.read()

# 1. modify_self base reward (currently 6.0) -> 4.0
content = re.sub(r'reward \+= 6\.0  # base reward',
                 'reward += 4.0  # base reward', content)

# 2. write_file base reward (currently 5.0) -> 6.0
content = re.sub(r'reward \+= 5\.0  # base for writing',
                 'reward += 6.0  # base for writing', content)

# 3. execute_code base reward (currently 7.0) -> 6.0
content = re.sub(r'reward \+= 7\.0  # base reward',
                 'reward += 6.0  # base reward', content)

# 4. read_file important reward (currently 9.0) -> 10.0
content = re.sub(r'reward \+= 9\.0  # reduced from 10\.0',
                 'reward += 10.0  # reduced from 10.0', content)

# 5. per-tool penalty factor block (replace with new values)
new_penalty_block = '''        # Productive tools have lower penalty factor (balanced)
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
        # Adjusted penalty factors for balanced usage
        if tool_name == "write_file":
            self.tool_penalty_factor = 0.4  # increased penalty
        elif tool_name == "read_file":
            self.tool_penalty_factor = 0.2  # moderate
        elif tool_name == "modify_self":
            self.tool_penalty_factor = 0.4  # increased
        elif tool_name == "execute_code":
            self.tool_penalty_factor = 0.1  # low
        elif tool_name in productive_tools:
            self.tool_penalty_factor = 0.1  # fallback
        else:
            self.tool_penalty_factor = 0.6
'''
# Find the block and replace
# Use pattern that matches from the comment line to just before '# Decay all counts'
pattern = r'(\s*# Productive tools have lower penalty factor.*?\n)(.*?)(?=\n\s*# Decay all counts)'
content = re.sub(pattern, r'\1' + new_penalty_block, content, flags=re.DOTALL)

# Write back
with open('agent_brain.py', 'w') as f:
    f.write(content)

print("Applied final reward adjustments v2.")