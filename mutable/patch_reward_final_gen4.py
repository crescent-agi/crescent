#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Define issue tools
issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue"]

# We'll iterate and modify lines
for i, line in enumerate(lines):
    # Skip success reward for issue tools
    if 'if isinstance(tool_result, dict) and not tool_result.get("error"):' in line:
        # Insert after this line a condition to skip if tool_name in issue_tools
        # We'll need to restructure; easier to modify later line where reward += 3.0
        pass

    # Reduce read_file important reward
    if 'reward += 8.0  # reduced reward for reading important files' in line:
        lines[i] = line.replace('8.0', '5.0')
        print(f"Line {i+1}: read_file important reward reduced to 5.0")
    
    # Increase write_file base reward
    if 'reward += 4.0  # base for writing (increased)' in line:
        lines[i] = line.replace('4.0', '6.0')
        print(f"Line {i+1}: write_file base reward increased to 6.0")
    
    # Increase execute_code base reward
    if 'reward += 5.0  # base reward (increased)' in line and 'execute_code' in lines[i-1]:
        lines[i] = line.replace('5.0', '6.0')
        print(f"Line {i+1}: execute_code base reward increased to 6.0")
    
    # Increase modify_self base reward
    if 'reward += 3.0  # increased base reward' in line and 'modify_self' in lines[i-1]:
        lines[i] = line.replace('3.0', '5.0')
        print(f"Line {i+1}: modify_self base reward increased to 5.0")
    
    # Increase issue tools penalty
    if 'reward -= 5.0' in line and any(issue in line for issue in issue_tools):
        lines[i] = line.replace('5.0', '6.0')
        print(f"Line {i+1}: issue tools penalty increased to -6.0")
    
    # Skip success reward for issue tools
    # We'll find the line "reward += 3.0" after success check and add condition
    # This is more complex; we'll do later.

# Now we need to add condition to skip success reward for issue tools.
# Let's find the line numbers for success reward addition.
success_reward_line = -1
for i, line in enumerate(lines):
    if 'reward += 3.0' in line and 'Success reward' in lines[i-1]:
        success_reward_line = i
        break

if success_reward_line != -1:
    # Insert a condition before that line
    indent = len(lines[success_reward_line]) - len(lines[success_reward_line].lstrip())
    new_line = ' ' * indent + 'if tool_name not in ["list_issues", "read_issue", "comment_issue", "close_issue"]:\n'
    lines.insert(success_reward_line, new_line)
    # Increase indent of the reward line
    lines[success_reward_line + 1] = ' ' * (indent + 4) + lines[success_reward_line + 1].lstrip()
    print("Added condition to skip success reward for issue tools")

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print("Reward function updated.")