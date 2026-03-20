#!/usr/bin/env python3
import re

with open('agent_brain.py', 'r') as f:
    content = f.read()

# Replace read_file important reward
content = re.sub(r'reward\s*\+= 6\.0\s*# reward for reading important files', 'reward += 3.0  # reward for reading important files', content)

# Replace issue tool penalty
content = re.sub(r'reward\s*-= 15\.0', 'reward -= 30.0', content)

# Ensure create_issue penalty also applied (already in issue_tools)

# Write file base reward maybe increase to 5.0? keep 4.0 for now

# Execute code base reward maybe increase to 6.0? keep 5.0

# Modify self critical extra maybe reduce to 8.0? keep 10.0

# Productive tool extra maybe increase to 2.5? keep 2.0

with open('agent_brain.py', 'w') as f:
    f.write(content)

print("Reward function tuned.")