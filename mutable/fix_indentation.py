#!/usr/bin/env python3
with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# line numbers are 0-indexed
# line 398 (index 397) is issue_tools line
# line 399 (index 398) is if line
if lines[397].strip().startswith('issue_tools = ['):
    # Ensure line 398 has 8 spaces
    lines[397] = '        issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]\n'
    # line 399 should have 8 spaces as well
    lines[398] = '        if same_count == 0 and tool_name in productive_tools:\n'

# line 406 (index 405) is comment line, line 407 (index 406) is if line
# Actually line 405 is "if tool_name not in self.episode_tools:"
# line 406 is comment "Skip episode novelty for issue tools and write_note"
# line 407 is if line.
# Let's find line with "if tool_name in productive_tools:"
for i, line in enumerate(lines):
    if line.strip() == 'if tool_name in productive_tools:' and i > 400:
        # Adjust indentation to 12 spaces (since inside block)
        lines[i] = '            if tool_name in productive_tools:\n'
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Indentation fixed')