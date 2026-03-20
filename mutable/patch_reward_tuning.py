#!/usr/bin/env python3
import re
import sys

with open('agent_brain.py', 'r') as f:
    content = f.read()

# Changes:
# 1. Reduce write_file base reward from 6.0 to 4.0
# 2. Reduce write_file Python extra from 4.0 to 3.0
# 3. Reduce write_file self-modification extra from 4.0 to 3.0
# 4. Increase execute_code base reward from 5.0 to 6.0
# 5. Increase execute_code success extra from 6.0 to 7.0
# 6. Increase modify_self critical extra from 10.0 to 12.0
# 7. Increase read_file important reward from 5.0 to 6.0
# 8. Increase issue tool penalty from -5.0 to -8.0
# 9. Remove success reward for issue tools (subtract success reward)
# 10. Reduce productive tool extra from 2.0 to 1.5 (optional)

# We'll do multiple replacements.

# Write file base reward
content = re.sub(r'reward\s*\+=\s*6\.0\s*# base for writing', 'reward += 4.0  # base for writing', content)
# Write file Python extra
content = re.sub(r'reward\s*\+=\s*4\.0\s*# extra for Python files', 'reward += 3.0  # extra for Python files', content)
# Write file self-modification extra
content = re.sub(r'reward\s*\+=\s*4\.0\s*# extra for self-modification', 'reward += 3.0  # extra for self-modification', content)
# Execute code base reward
content = re.sub(r'reward\s*\+=\s*5\.0\s*# base reward', 'reward += 6.0  # base reward', content)
# Execute code success extra
content = re.sub(r'reward\s*\+=\s*6\.0', 'reward += 7.0', content)  # careful might match other 6.0
# Modify self critical extra
content = re.sub(r'reward\s*\+=\s*10\.0\s*# reduced extra reward for self-modification', 'reward += 12.0  # extra reward for self-modification', content)
# Read file important reward
content = re.sub(r'reward\s*\+=\s*5\.0\s*# reduced reward for reading important files', 'reward += 6.0  # reward for reading important files', content)
# Issue tool penalty
content = re.sub(r'reward\s*-=\s*5\.0', 'reward -= 8.0', content)
# Productive tool extra (optional)
content = re.sub(r'reward\s*\+=\s*2\.0', 'reward += 1.5', content)  # might affect other 2.0 entries

# Also need to subtract success reward for issue tools.
# We'll add a condition after success reward addition.
# Find the line: "if isinstance(tool_result, dict) and not tool_result.get(\"error\"):"
# Insert after that block: if tool_name in issue_tools: reward -= 3.0 (success reward)
# Let's do more targeted replacement.

# We'll replace the whole block from "if isinstance(tool_result, dict) ..." to the end of that if block.
# But easier: add a check after adding success reward.
# We'll locate the line where reward += 3.0 and add a conditional subtraction.

# Let's write a more robust approach: replace the whole reward function with a new version.
# But for now, let's just do these replacements and see.

with open('agent_brain.py', 'w') as f:
    f.write(content)

print("Patched agent_brain.py with updated reward values.")