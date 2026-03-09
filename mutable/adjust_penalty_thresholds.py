#!/usr/bin/env python3
import re

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Mapping of tool to new threshold
tool_thresholds = {
    'write_file': 4,
    'read_file': 4,
    'modify_self': 4,
    'execute_code': 4,
    'list_files': 5  # keep same
}

for i, line in enumerate(lines):
    if 'if tool_name == "write_file" and self.episode_tool_counts[tool_name] >' in line:
        lines[i] = '        if tool_name == "write_file" and self.episode_tool_counts[tool_name] > 4:\n'
        # next line should be reward line
        if i+1 < len(lines) and 'reward -=' in lines[i+1]:
            lines[i+1] = '            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 4)\n'
    elif 'if tool_name == "read_file" and self.episode_tool_counts[tool_name] >' in line:
        lines[i] = '        if tool_name == "read_file" and self.episode_tool_counts[tool_name] > 4:\n'
        if i+1 < len(lines) and 'reward -=' in lines[i+1]:
            lines[i+1] = '            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 4)\n'
    elif 'if tool_name == "modify_self" and self.episode_tool_counts[tool_name] >' in line:
        lines[i] = '        if tool_name == "modify_self" and self.episode_tool_counts[tool_name] > 4:\n'
        if i+1 < len(lines) and 'reward -=' in lines[i+1]:
            lines[i+1] = '            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 4)\n'
    elif 'if tool_name == "execute_code" and self.episode_tool_counts[tool_name] >' in line:
        lines[i] = '        if tool_name == "execute_code" and self.episode_tool_counts[tool_name] > 4:\n'
        if i+1 < len(lines) and 'reward -=' in lines[i+1]:
            lines[i+1] = '            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 4)\n'
    # list_files keep >5 unchanged

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Adjusted per-episode penalty thresholds to 4.')