#!/usr/bin/env python3
import re

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find line with issue_tools definition
for i, line in enumerate(lines):
    if 'issue_tools = [' in line:
        lines[i] = '        issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]\n'
        print(f"Updated line {i+1}")
        break

# Find create_issue reward block
for i, line in enumerate(lines):
    if 'if tool_name == "create_issue":' in line:
        # Find the next line with reward += 0.2
        for j in range(i, min(i+5, len(lines))):
            if 'reward +=' in lines[j]:
                lines[j] = '            reward += 0.0  # no reward for issue creation\n'
                print(f"Updated create_issue reward line {j+1}")
                break
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print("Patched issue_tools and create_issue reward.")