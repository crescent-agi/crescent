#!/usr/bin/env python3
import sys
import os
import re

# Read agent_brain.py
with open('agent_brain.py', 'r') as f:
    content = f.read()

# 1. modify_self base reward
content = re.sub(r'reward \+= 12\.0  # base reward increased from 10\.0',
                 'reward += 6.0  # base reward', content)

# 2. write_file base reward
content = re.sub(r'reward \+= 3\.0  # base for writing \(increased from 2\.0\)',
                 'reward += 5.0  # base for writing', content)

# 3. write_file extra bonuses (three lines)
content = re.sub(r'reward \+= 2\.0  # extra for Python files',
                 'reward += 3.0  # extra for Python files', content)
content = re.sub(r'reward \+= 2\.0  # extra for self-modification',
                 'reward += 3.0  # extra for self-modification', content)
content = re.sub(r'reward \+= 2\.0  # extra for test/artifact creation',
                 'reward += 3.0  # extra for test/artifact creation', content)

# 4. execute_code base reward
content = re.sub(r'reward \+= 8\.0  # base reward increased from 5\.0',
                 'reward += 7.0  # base reward', content)

# 5. execute_code success extra reward
# Find the pattern: line after stderr check
# We'll replace the exact line.
def replace_execute_extra(match):
    # match group is the line we want to replace
    return 'reward += 4.0  # extra for successful execution'
# Use a more precise pattern
content = re.sub(r'(if tool_result\.get\("stderr", ""\)\.strip\(\) == "":\s*\n\s*)reward \+= 5\.0  # increased from 3\.0',
                 r'\1reward += 4.0  # extra for successful execution', content)

# 6. read_file important reward
content = re.sub(r'reward \+= 6\.0  # reduced from 10\.0',
                 'reward += 9.0  # reduced from 10.0', content)

# 7. per-tool penalty factor block
# Locate the block lines and replace with new block
penalty_block_pattern = r'(\s*# Productive tools have lower penalty factor.*?\n)(.*?)(?=\n\s*# Decay all counts)'
# We'll replace the entire block up to # Decay all counts
new_penalty_block = '''        # Productive tools have lower penalty factor (balanced)
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
        # Adjusted penalty factors for balanced usage
        if tool_name == "write_file":
            self.tool_penalty_factor = 0.4  # increased penalty
        elif tool_name == "read_file":
            self.tool_penalty_factor = 0.2  # moderate
        elif tool_name == "modify_self":
            self.tool_penalty_factor = 0.3  # increased
        elif tool_name == "execute_code":
            self.tool_penalty_factor = 0.1  # low
        elif tool_name in productive_tools:
            self.tool_penalty_factor = 0.1  # fallback
        else:
            self.tool_penalty_factor = 0.6
'''
# Use DOTALL to match across lines
def replace_penalty_block(match):
    before = match.group(1)  # the comment line
    # replace the entire block after that up to '# Decay all counts'
    return before + new_penalty_block
# We'll do a more direct replacement using regex with DOTALL
content = re.sub(r'(\s*# Productive tools have lower penalty factor.*?\n)(.*?)(?=\n\s*# Decay all counts)',
                 r'\1' + new_penalty_block, content, flags=re.DOTALL)

# 8. per-episode penalty: include execute_code
content = re.sub(r'if tool_name in \["write_file", "read_file", "modify_self"\]',
                 'if tool_name in ["write_file", "read_file", "modify_self", "execute_code"]', content)

# Write back
with open('agent_brain.py', 'w') as f:
    f.write(content)

print("Applied final reward adjustments.")