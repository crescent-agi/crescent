#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# 1. Insert issue tools penalty after death penalty
# Find line with 'return -500.0  # heavily penalize suicide'
for i, line in enumerate(lines):
    if 'return -500.0  # heavily penalize suicide' in line:
        # Insert after this line
        indent = len(line) - len(line.lstrip())
        # Ensure we insert at same indent as the if statement (8 spaces?)
        # Actually we need to insert at the same level as the if block (outside).
        # The if block ends after the return line, so we need to dedent by 4 spaces.
        # Let's compute indent of previous line that starts with 'if tool_name == "declare_death":'
        if_line = lines[i-1]
        if_indent = len(if_line) - len(if_line.lstrip())
        # Insert after i
        new_lines = []
        new_lines.append(' ' * if_indent + '# Issue tools penalty (strongly discourage)\n')
        new_lines.append(' ' * if_indent + 'issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]\n')
        new_lines.append(' ' * if_indent + 'if tool_name in issue_tools:\n')
        new_lines.append(' ' * if_indent + '    return -50.0  # heavy penalty, no other rewards\n')
        for nl in reversed(new_lines):
            lines.insert(i + 1, nl)
        break

# 2. Delete old issue tool penalty lines (reward -= 30.0 and reward -= 3.0)
for i, line in enumerate(lines):
    if 'reward -= 30.0' in line:
        # Delete this line and the next line (reward -= 3.0)
        del lines[i:i+2]
        break

# 3. Change execute_code success extra from 6.0 to 3.0
for i, line in enumerate(lines):
    if 'reward += 6.0' in line and i > 0 and 'extra if execution succeeded without stderr errors' in lines[i-1]:
        lines[i] = line.replace('6.0', '3.0')
        break

# 4. Change write_file base from 4.0 to 6.0
for i, line in enumerate(lines):
    if 'reward += 4.0  # base for writing (reduced)' in line:
        lines[i] = line.replace('4.0', '6.0')
        break

# 5. Change modify_self base from 5.0 to 7.0
for i, line in enumerate(lines):
    if 'reward += 5.0  # base reward (increased)' in line and i > 0 and 'modify_self' in lines[i-1]:
        lines[i] = line.replace('5.0', '7.0')
        break

# 6. Change read_file important reward from 3.0 to 6.0
for i, line in enumerate(lines):
    if 'reward += 3.0  # reward for reading important files' in line:
        lines[i] = line.replace('3.0', '6.0')
        break

# 7. Increase penalty for write_note from -2.0 to -3.0
for i, line in enumerate(lines):
    if 'reward -= 2.0' in line and i > 0 and 'write_note' in lines[i-1]:
        lines[i] = line.replace('2.0', '3.0')
        break

# 8. Add intra-episode productive tool novelty bonus after episode_tools addition
for i, line in enumerate(lines):
    if 'self.episode_tools.add(tool_name)' in line:
        indent = len(line) - len(line.lstrip())
        # Need to add after this line, but inside the same indentation block? Actually we want after the episode_tools addition, before the next section.
        # We'll add after this line with same indent.
        bonus = ' ' * indent + '            # Productive tool novelty bonus: reward for first use of each productive tool in episode\n'
        bonus += ' ' * indent + '            productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]\n'
        bonus += ' ' * indent + '            if tool_name in productive_tools:\n'
        bonus += ' ' * indent + '                if not hasattr(self, "productive_tools_used_in_episode"):\n'
        bonus += ' ' * indent + '                    self.productive_tools_used_in_episode = set()\n'
        bonus += ' ' * indent + '                if tool_name not in self.productive_tools_used_in_episode:\n'
        bonus += ' ' * indent + '                    reward += 5.0\n'
        bonus += ' ' * indent + '                    self.productive_tools_used_in_episode.add(tool_name)\n'
        lines.insert(i + 1, bonus)
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Reward method updated successfully')