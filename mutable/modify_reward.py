#!/usr/bin/env python3
import re
import sys

with open('agent_brain.py', 'r') as f:
    content = f.read()

# 1. read_file important file reward from 10.0 to 8.0
content = re.sub(r'reward \+= 10\.0  # increased from 6\.0 \(issue #23\)', 
                 'reward += 8.0  # reduced from 10.0 (issue #24)', content)

# 2. read_file universal bonus from 1.0 to 0.5
content = re.sub(r'reward \+= 1\.0  # added per issue #23', 
                 'reward += 0.5  # reduced from 1.0 (issue #24)', content)

# 3. per-tool penalty factor for read_file from 0.3 to 0.4
content = re.sub(r'self\.tool_penalty_factor = 0\.3  # moderate penalty for read_file', 
                 'self.tool_penalty_factor = 0.4  # increased from 0.3 (issue #24)', content)

# 4. per-episode penalty threshold for read_file from 10 to 5
content = re.sub(r'if tool_name == "read_file" and self\.episode_tool_counts\[tool_name\] > 10:', 
                 'if tool_name == "read_file" and self.episode_tool_counts[tool_name] > 5:', content)

# 5. execute_code success extra reward from 2.0 to 3.0
content = re.sub(r'reward \+= 2\.0  # reduced from 5\.0 \(issue #23\)', 
                 'reward += 3.0  # increased from 2.0 (issue #24)', content)

# 6. per-tool penalty factor for execute_code from 0.3 to 0.2
content = re.sub(r'self\.tool_penalty_factor = 0\.3  # increased from 0\.1 \(issue #23\)', 
                 'self.tool_penalty_factor = 0.2  # reduced from 0.3 (issue #24)', content)

# 7. modify_self base reward from 5.0 to 6.0
content = re.sub(r'reward \+= 5\.0  # base reward reduced from 12\.0 \(issue #23\)', 
                 'reward += 6.0  # increased from 5.0 (issue #24)', content)

# 8. per-tool penalty factor for modify_self from 0.5 to 0.3
content = re.sub(r'self\.tool_penalty_factor = 0\.5  # increased from 0\.4 \(issue #23\)', 
                 'self.tool_penalty_factor = 0.3  # reduced from 0.5 (issue #24)', content)

# 9. write_file per-tool penalty factor from 0.5 to 0.6
content = re.sub(r'self\.tool_penalty_factor = 0\.5  # increased penalty for write_file', 
                 'self.tool_penalty_factor = 0.6  # increased from 0.5 (issue #24)', content)

# 10. write_file per-episode penalty threshold from 10 to 5
content = re.sub(r'if tool_name == "write_file" and self\.episode_tool_counts\[tool_name\] > 10:', 
                 'if tool_name == "write_file" and self.episode_tool_counts[tool_name] > 5:', content)

# Write back
with open('agent_brain.py', 'w') as f:
    f.write(content)

print('Reward function updated per issue #24')