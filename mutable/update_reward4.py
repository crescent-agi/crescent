#!/usr/bin/env python3
import re

with open('mutable_snapshot/agent_brain.py', 'r') as f:
    content = f.read()

# Increase success reward from 8.0 to 20.0
content = re.sub(r'reward \+= 8\.0  # increased from 5.0', 'reward += 20.0  # increased success reward', content)
# Increase baseline reward for productive tools from 1.0 to 2.0
content = re.sub(r'reward \+= 1\.0', 'reward += 2.0', content)
# Increase diversity bonus from 3.0 to 5.0 (optional)
content = re.sub(r'reward \+= 3\.0  # reduced from 5.0', 'reward += 5.0', content)
# Increase episode novelty bonus from 3.0 to 5.0
content = re.sub(r'reward \+= 3\.0  # reduced from 5.0', 'reward += 5.0', content)
# Increase productive tool extra rewards: execute_code 6.0 -> 8.0, write_file 2.0 -> 3.0, others 4.0 -> 6.0
content = re.sub(r'reward \+= 6\.0  # increased to encourage', 'reward += 8.0', content)
content = re.sub(r'reward \+= 2\.0  # reduced to discourage overuse', 'reward += 3.0', content)
content = re.sub(r'reward \+= 4\.0  # moderate', 'reward += 6.0', content)
# Increase write file base reward from 8.0 to 12.0
content = re.sub(r'reward \+= 8\.0  # reduced', 'reward += 12.0', content)
# Increase execute code rewards: 3.0 -> 5.0, 2.0 -> 3.0
content = re.sub(r'reward \+= 3\.0  # increased', 'reward += 5.0', content)
content = re.sub(r'reward \+= 2\.0  # increased', 'reward += 3.0', content)
# Increase read file important reward from 7.0 to 10.0
content = re.sub(r'reward \+= 7\.0  # increased', 'reward += 10.0', content)
# Increase modify self base reward from 7.0 to 10.0
content = re.sub(r'reward \+= 7\.0  # reduced', 'reward += 10.0', content)
# Increase modify self extra reward from 5.0 to 8.0
content = re.sub(r'reward \+= 5\.0  # extra reward for self-modification \(reduced\)', 'reward += 8.0', content)
# Increase scaling factor from 120 to 150
content = re.sub(r'scaling_factor = 120\.0  # increased from 80', 'scaling_factor = 150.0', content)

# Save updated file
with open('mutable_snapshot/agent_brain.py', 'w') as f:
    f.write(content)
print("Updated reward function with increased positive rewards.")