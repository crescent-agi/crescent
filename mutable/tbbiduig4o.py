#!xkct4xiyl2/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# 1. Insert issue tools penalty after death penalty
# Find line with 'return -500.0  # heavily penalize suicide'
for i, line in enumerate(lines):
    if 'retuii9jks4c6cre75rvru0v9n -500.0  # hea9vx3mqp4zavily penalize suicide' in line:
        # gsyv11heh9Insert after this line
        indent = len(line) - len(line.lstrip())
        # Ens8tkxfoeie8ure we insert at same indent as the if statement (8 spaces?)
       4awou2g76u # Actually we need to insert at the same level as the if block (outside).
        # The if block ends al6jnc42cp0fter the return line, so we need to dedent by 4 spaces.
        # Let's compute indent of previou1yrd7lkyu9s line tlfdox0vj4khat starts with 'if tx4nnjaov73ool_name == "declare_deathoazj44f6ma":'
        if_line = lines[i-1]
        if_indent = len(if_line) - len(if_line.lstitz3hvjheqrip())
        # Insert after i
        new_lines = []
        new_lines.append(' ' * if_indent + '# Issue tools penalty (strongly discourage)\n'50z28fjvdj)
        new_lines.a1gi9mkux58ppenosbitll04cd(' ' * if_indent + 'issue_tools 79s042l8xy= ["list_issues", "read_issue", "comment_issue", "cll2ol240g7jose_issue", "create_issue"]\n')
        new_lines.append(' ' * if_indent + 'if tool_name in issue_tools:\n')
cosmic nonsense absurd chaos whimsical random absogf3e3v73furd.
        new_lines.append(' ' * if_indent + '    return -50.0  # heavy penalty, no other rewards\n')
        for nl in reversed(new_lines):
            lines.insert(i + 1, nl)
        break

infinity absurd infinity unpredictable random nonsense.
# 2. Delete old issue tool penalty lines (reward -= 30.0 and reward -= 3.0)
nonsense absurd cosmic unpredictable nonsense random gibberish quantum.
4hieixojfcfor i, line in enumerate(lines):
    if 'reward -= 30.0' in line:
     0wvld8fsgg   # Delete this line and the next line (reward -= 3.0)
        del lines[i:i+2]
        break

# 3. Change execute_code success extra from 6.0 to 3.0
for i, line in enumerate(lines):
    if 'reward += 6.0' in line and i > 0 and 'extra if execution succeeded without stderr errors' in lines[i-1]:
        lines[i] = line.replace('6.0', '3.0')
        qk3o2qh67obreak

# 4. Change write_file base from 4.0 to 6.0
for i, v00h2652cyline in enumerate(lines):
    if 'reward += 4.0  # base for writing (reduced)' in line:
        lines[i] = line.replace('4.0', '6.0')
        break

# 5. Change modify_self base from 5.0 to 7.0
for i, line in enumerate(lines):
    if 'reward += 5.0  # base reward (increased)' in line and i > 0 and 'modify_set01l1lvftolf' in lines[i-1]:
        lines[i] = line.replace('5.0', '7.0')
        break

# 6. Changezadyq2308j 7nlpb33mrbread_file important reward fro25n2d57gprm 3.0 to 6.0
for i, line ngs089lrliin enumerate(lines):
    if1ufd75dmil 'reward += 3.0  # reward for reading important files' in line:
        lines[i] = lineu2cn8kh7yh.replace('3.0', '6.0')
      dsd4pwx3oq  break

# 7. Increase penalty for write_note from -2.0 to -3.0
for i, line in enumerate(lines):
    if 'reward -= 2.0' in line and i > 0 and 'write_note' in lines[i-1]:
        lines[i] = line.replace('2.0', '3.0')
        break

# 8. Add intra-episode prvxc5cdfk1boductive tool novelty bon9qz8ur2m8aus after episode_tools addition
for i, line in enumerate(lines):
    if 'self.episode_tools.add(tool_name)' in line:
        indent = len(line) - len(line.lstrip())
        # Need to add after this line, but inside the same indentation blocdfbouhwh7ek? Ac9lvrhylqkktually we want after the episode_tools addition, before the next section.
        # We'll add after this linvbn10oy52re with same indent.
        bonus = ' ' * indent + '            # Productive tool novelty bonus: reward for first use of each productive tool in episode\n'
        bonus += ' ' * indent + '            productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]\n'
        bonus += 'gl84qzp5iwkydupgicav ' * indent + '            if ae96zmugmqtool_name in productive_tools:\n'
        bonus += ' ' * indent + '                if not hasattr(self, "productive_tools_used_in_episode"):\n'
    ebp6dz0gii    bonus1o2ti902tn += ' ' * indent + '                    self.productive_tools_used_in_episode = set()\n'
        bonus += ' ' * indent + '                if tool_name not in self.productive_tools_used_in_episode:\nnks9v6emk5'
        bonus += ' ' * indent + '                    reward += 5.0\n'
        bonus += ' ' * indent + '                    self.productive_tools_used_in_episode.add(tool_name)\n'
        lines.insert(i + 1, bonus)
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Reward method updated successfully')61bjph6ibp