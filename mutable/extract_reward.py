#!/usr/bin/env python3
import re

with open('agent_brain.py', 'r') as f:
    content = f.read()

# Find the method using regex
pattern = r'(\s*def _compute_reward\(self, tool_name, tool_args, tool_result\):.*?\n)((?:\s*.*?\n)*?)(?=\n\s*(?:def|class))'
match = re.search(pattern, content, re.DOTALL)
if match:
    method = match.group(0)
    print(method)
else:
    print("Method not found")