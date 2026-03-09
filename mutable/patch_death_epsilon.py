#!/usr/bin/env python3
import sys
import re

# Patch agent_brain.py death penalty and reward adjustments
with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# 1. Increase death penalty from -30 to -100
for i, line in enumerate(lines):
    if line.strip().startswith('if tool_name == "declare_death":'):
        # Find return line
        j = i + 1
        while j < len(lines):
            if lines[j].strip().startswith('return'):
                lines[j] = '            return -100.0  # heavily penalize suicide\n'
                break
            j += 1
        break

# 2. Remove extra exploration reward for list_files (line with reward += 1.0 for list_files)
# Find the block:
# if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
#     if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
#         reward += 0.0
#     else:
#         reward += 1.0  # keep normal exploration reward for list_files
# Replace with:
# if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
#     if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
#         reward += 0.0  # no extra reward for issue tools
#     else:
#         reward += 0.2  # small reward for list_files (reduced)
for i, line in enumerate(lines):
    if line.strip().startswith('if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:'):
        # Find the else block
        j = i
        while j < len(lines) and not lines[j].strip().startswith('return'):
            if lines[j].strip().startswith('reward += 1.0') and 'list_files' in lines[j-1] or lines[j-1].strip() == 'else:':
                lines[j] = '                reward += 0.2  # small reward for list_files (reduced)\n'
                break
            j += 1
        break

# 3. Reduce success reward for issue tools (optional) - we'll leave success reward at +1.0 for all

# 4. Increase penalty for recency and diversity slightly
# recency penalty currently 0.3 -> 0.5
for i, line in enumerate(lines):
    if line.strip().startswith('reward -= 0.3  # increased penalty for immediate repetition'):
        lines[i] = '            reward -= 0.5  # increased penalty for immediate repetition\n'
        break

# diversity penalty per occurrence currently 0.2 -> 0.3
for i, line in enumerate(lines):
    if line.strip().startswith('reward -= 0.2 * same_count  # increased penalty per occurrence'):
        lines[i] = '            reward -= 0.3 * same_count  # increased penalty per occurrence\n'
        break

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)
print("Patched agent_brain.py death penalty and rewards.")