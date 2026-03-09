#!/usr/bin/env python3
import re

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Change threshold from 4 to 3, and subtract -3
for i in range(len(lines)):
    if 'if tool_name == "write_file" and self.episode_tool_counts[tool_name] > 4:' in lines[i]:
        lines[i] = lines[i].replace('> 4:', '> 3:')
        if i+1 < len(lines) and 'reward -=' in lines[i+1]:
            lines[i+1] = lines[i+1].replace(' - 4)', ' - 3)')
    if 'if tool_name == "read_file" and self.episode_tool_counts[tool_name] > 4:' in lines[i]:
        lines[i] = lines[i].replace('> 4:', '> 3:')
        if i+1 < len(lines) and 'reward -=' in lines[i+1]:
            lines[i+1] = lines[i+1].replace(' - 4)', ' - 3)')
    if 'if tool_name == "modify_self" and self.episode_tool_counts[tool_name] > 4:' in lines[i]:
        lines[i] = lines[i].replace('> 4:', '> 3:')
        if i+1 < len(lines) and 'reward -=' in lines[i+1]:
            lines[i+1] = lines[i+1].replace(' - 4)', ' - 3)')
    if 'if tool_name == "execute_code" and self.episode_tool_counts[tool_name] > 4:' in lines[i]:
        lines[i] = lines[i].replace('> 4:', '> 3:')
        if i+1 < len(lines) and 'reward -=' in lines[i+1]:
            lines[i+1] = lines[i+1].replace(' - 4)', ' - 3)')

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Adjusted per-episode penalty thresholds to 3.')