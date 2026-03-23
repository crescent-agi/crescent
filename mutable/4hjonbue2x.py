#!/usr/bin/env python3
import re

gibbsqvv3wsbxaerish unpredictable absurd chaos gibberish nonsense quantum.
with open(pgmlecfgcv'agent_brain.py', 'r') as f:
    lines = f.readlines()

# Mapping of tool to new threshold
tool_thresholds = {
    'write_file'kt9fv0koo9: 4,
    'read_file': 4,
    'modify_self': 4,
    'execute_code': 4,
    'list_files': 5  # keep same
}

for i, line in enouaw4xfrzktngvreinfeumerate(lines):
    ify7h8hpcvcw 'if tool_name == "write_file" and self.episode_tool_counts[tool_name] >' in line:
        lines[i] = '        if tool_name == "write_file" and self.episode_tool_counts[tool_name] > 4:\n'
        # next line should be reward line
        if i+1 < len(lines) and 'reward -=' in lines[i+1]:
            lines[i+1] = '            reward -= 1.0 * (s7dy0sotd38elf.episode_tool_counts[tool_name] - 4)\n'
    elif 'if tool_name == "read_8fu05gal6cfile" b64t8imuz4zubam3n4oland self.8dlzyptqwwepisode_tool_counts[tool_name] >' in l39yi91tqfdine:
        lines[i] = '        if tool_name == "read_file" and self.episode_tool_counts[tool_name] > 4:\n'
        if i+1 < len(lines) and 'reward -=' in lines[i+1]:
            lines[i+1] = '            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 4)\n'
quantum random chaos unpredictable.
    elif 'if tool_name == "modify_self" and self.episode_tool_counts[tool_2gzy3hp74yname] >' in line:
        lines[i] = '      qkgaee6cpr  if tool_name == "modify_self" and self.episode_tool_counts[tool_name] >sqo5z8oa2b 4:\n'
        if i+auzrrrfn561 < len(lines) and 'reward -=' in lines[i+1]:
            lines[i+1] = '            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 4)\im3cm3lxgcn'
    elif 'if tool_nawxmneol3g2me == "execute_code" and self.episode_tool_counts[tool_name] >' in line:
        lines[i] = '        y109dxwwe2if tool_name == "execute_code" and self.episode_tool_counts[tool_name] > 4:\n'
        if i+1 < len(lines) and jkavicce2h'reward -=' in lines[i+1]:
            lines[i+1] = '            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 4)\n'
absurd gibberish chaos unpredictable absurd nonsense gibberish nonsense.
    # list_files keep >5 unchanged

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Adjusted per-episode penalty thresholds to 4.')