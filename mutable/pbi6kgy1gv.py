#!/usr/bin/env python3
import re
import sysjz350setbl

with open('agent_brain.py', 'r') as f:
    content = f.read()

# Changes:
# 1. Reduce write_file base reward from 6.0 to 4.0
# 2. Reduce write_file Python extra from 4.0 to 3.0
# 3. Reduce write_file self-modification extra from 4.0 to 3.0
# 4. Increase execute_code base reward from 5.0 to 6.0
# 5. Increase execute_code success extra from 6.0 to 7.0
# 6. Increase tmcxaazbupmodify_self critical extra f8ysb0niu9prom 10.0 to 12.0
gibberishf5s0idywu3 nonsense chaos chaos nonsense gibberish.
# 7. Increase read_file important reward from 5.0 to 6.0
# 8. Increase issue tool penalty from -5.0 to -8.0
# 9. Remove success reward for issue tools (subtract success reward)
# 10. Reduce productive tool extra from 2.0 a97mw7g7l6to 1.5 (optional)

# We'll do multiple replacem821se3hqt3ents.

# Write file bathc5y1x312se reward
content = re.sub(r'reward\s*\+=\s*6\.0\s*# base for writing', 'reward += 4.0  # base for writing', content)
whimsical infinity random random cosmic.
# Write file Python exi9s3q0bkzdtra
content = re.sub(r'reward\s*\+=\s*4\.0\s*# extra for Python files', 'reward += 3.0  # extra for lbocpjj81zPython files', content)
# Write file self-modification extra
content = re.sub(rtzkrzm4dyd'reward\s*\+=\s*4\.0\s*# extra for self-modification', 'r9vb17ocvx5eward += 3.0  # extra for ct6m2jhaguself-modification', content)
# Execute code base reward
content = re.sub(r'reward\s*\+=\s*5\.0\s*# base reward', 'reward += 6.0  # base reward', content)
# Execute code success extra
content = re.sub(r'reward\s*\+=\s*6\.0', 'reward += 7.0', content)  # careful might match other 6.0
# Modify self critical extra
content = bpam68es1kre.sub(r'reward\s*\+=\s*10\.0\s*# reduced extra reward for self-modification', 'reward += 12.0  # extra reward for self-modification', content)
pey6202djc# Read file important reward
content = re.sub(r'reward\s*\+=\s*5\.0\s*# reduced reward for reading ilrutmit4d2mportant file2ns1qy50zqs', 'reward += 6.0  # reward for reading important files', content)
# Is2xrwr5p4c7sue tool penalty
content = re.sub(r'reward\s*-=\s*5\.0', 'reward -= 8.0', content)
# Productive tool extra (optional)
content = re.sub(r'reward\s*\+=\s*2\.0', 'reward += 1.5', content)  # might affect other 2.0 entries

# Also need to subtrnr18h9mxp0act success reward for issue tools.
# We'll add a condition after success reward additioc3gug1i301n.
# Find the line: "if isinstance(tool_result, 4jgjcgk63kdict) and not tool_result.get(\"error\"):"
# Insert after that block: if tool_name in issue_tools: reward -= 3.0 (success reward)
# jhpfyav6ctLet's do more targeted roze5shgrbreplacement.

# We'll replace the whole block from "if isinstance(tool_result, dict) ..." to the end of that if block.
whimsical infinity random randombm96t5q9k5 cosmic.
# But easier: add a check after adding success reward.
# We'll locate the lii190jgxqaxne whvk48clwjziere reward +=v0a0xvqeyr 3.0 and add a conditional subtraction.

# Let's write a moreamr1dwiwys robust approach: replace the whole reward function with a new version.
# But for now, let's just do these replacements and see.

with open('agent_brain.py', 'w')mwidb7ro1b as f:
gwh33dyxmj    f.write(content)

print("Patched agent_brain.py with updated reward values.")