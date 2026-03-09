#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# 1. Diversity bonus: restrict to productive tools
# Find line with "Diversity bonus: reward for using a tool not used"
for i, line in enumerate(lines):
    if 'Diversity bonus: reward for using a tool not used' in line:
        # Find the if condition line (a few lines later)
        # Actually the condition is after the issue_tools list
        # Let's find line with 'if same_count == 0'
        for j in range(i, i+10):
            if 'if same_count == 0' in lines[j]:
                # Replace that line with new condition
                old = lines[j]
                # Currently: if same_count == 0 and tool_name not in issue_tools and tool_name != "write_note":
                # Change to: if same_count == 0 and tool_name in productive_tools:
                # Need to ensure productive_tools is defined earlier (it is at line 372)
                # We'll just change the condition.
                lines[j] = '            if same_count == 0 and tool_name in productive_tools:\n'
                break
        break

# 2. Episode novelty bonus: restrict to productive tools
for i, line in enumerate(lines):
    if 'Episode novelty bonus: reward for first use of a tool in this episode' in line:
        # Find the inner if condition
        for j in range(i, i+10):
            if 'if tool_name not in issue_tools and tool_name != "write_note":' in lines[j]:
                lines[j] = '                if tool_name in productive_tools:\n'
                break
        break

# 3. Increase per-tool penalty factor for non-productive tools from 0.6 to 1.0
# Find line 'else:' after the elif chain
for i, line in enumerate(lines):
    if line.strip() == 'else:' and i > 400 and i < 440:
        # The next line should be 'self.tool_penalty_factor = 0.6'
        if 'self.tool_penalty_factor = 0.6' in lines[i+1]:
            lines[i+1] = '            self.tool_penalty_factor = 1.0  # increased from 0.6 (issue #24)\n'
        break

# 4. Add per-episode penalty for list_files after 5 uses
# Find the block of per-episode penalties (lines after 'Per-episode usage penalty for productive tools')
# We'll insert after the execute_code penalty block.
for i, line in enumerate(lines):
    if 'if tool_name == "execute_code" and self.episode_tool_counts[tool_name] > 5:' in line:
        # Insert after this block (find the next blank line or next penalty line)
        # Actually there is a blank line after the penalty block? Let's insert a new penalty.
        # We'll add two lines:
        # if tool_name == "list_files" and self.episode_tool_counts[tool_name] > 5:
        #     reward -= 1.0 * (self.episode_tool_counts[tool_name] - 5)
        # We'll insert after the execute_code penalty block, before the blank line.
        # Find index where next line starts with '        # Penalty for write_note'
        for j in range(i, len(lines)):
            if lines[j].strip().startswith('# Penalty for write_note'):
                # Insert before that line
                lines.insert(j, '        # List files penalty after 5 uses (issue #24)\n')
                lines.insert(j+1, '        if tool_name == "list_files" and self.episode_tool_counts[tool_name] > 5:\n')
                lines.insert(j+2, '            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 5)\n')
                break
        break

# 5. Increase penalty for write_note from -3.0 to -5.0
for i, line in enumerate(lines):
    if 'if tool_name == "write_note":' in line:
        # Next line should be reward -= 3.0
        if 'reward -= 3.0' in lines[i+1]:
            lines[i+1] = '            reward -= 5.0  # increased from 3.0 (issue #24)\n'
        break

# 6. Increase productive tool extra reward from 2.0 to 3.0
for i, line in enumerate(lines):
    if 'if tool_name in productive_tools:' in line:
        # Next line should be reward += 2.0
        if 'reward += 2.0' in lines[i+1]:
            lines[i+1] = '            reward += 3.0  # increased from 2.0 (issue #24)\n'
        break

# 7. Update exploration parameters: epsilon_decay from 0.995 to 0.99, epsilon_min from 0.1 to 0.05
for i, line in enumerate(lines):
    if 'exploration_rate=0.5, epsilon_decay=0.995, epsilon_min=0.1' in line:
        lines[i] = lines[i].replace('epsilon_decay=0.995', 'epsilon_decay=0.99')
        lines[i] = lines[i].replace('epsilon_min=0.1', 'epsilon_min=0.05')
        break

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Reward function updated (v2)')