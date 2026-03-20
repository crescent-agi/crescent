#!/usr/bin/env python3
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Replacement 1: else block at line 150 (0-index)
else_start = 150
else_end = 158  # line after the block (line 158 is the empty line after confidence = 0.1)
# Verify lines
print('Current else block:')
for i in range(else_start, else_end):
    print(f'{i}: {lines[i]}', end='')

new_else = '''        else:
            # Fallback: random
            # Filter declare_death and issue tools during random fallback
            issue_indices = [7, 8, 9, 10, 11]  # list_issues, read_issue, comment_issue, create_issue, close_issue
            allowed = [i for i in range(self.action_size) if i != 6 and i not in issue_indices]
            if allowed:
                action_idx = random.choice(allowed)
            else:
                action_idx = random.randrange(self.action_size)
            confidence = 0.1
'''

# Replacement 2: death filter else block at line 169 (original line numbers)
# Need to find line with "else:" after line 168 (break line)
# Let's search for "else:" after line 160
death_else_start = None
for i in range(160, len(lines)):
    if lines[i].strip() == 'else:' and lines[i-1].strip() == 'if self.q_agent:' and lines[i-2].strip().startswith('if self.step_count < 100'):
        death_else_start = i
        break
if death_else_start is None:
    print('Could not find death filter else block')
    sys.exit(1)
# Find end of that else block: look for line with same indent as else start (8 spaces) after the block
indent = len(lines[death_else_start]) - len(lines[death_else_start].lstrip())
death_else_end = death_else_start + 1
while death_else_end < len(lines) and (lines[death_else_end].strip() == '' or (len(lines[death_else_end]) - len(lines[death_else_end].lstrip())) > indent):
    death_else_end += 1
print('Death else block lines:')
for i in range(death_else_start, death_else_end):
    print(f'{i}: {lines[i]}', end='')

new_death_else = '''            else:
                # random fallback: pick any non-death action, also filter issue tools
                issue_indices = [7, 8, 9, 10, 11]
                allowed = [i for i in range(self.action_size) if i != 6 and i not in issue_indices]
                if allowed:
                    action_idx = random.choice(allowed)
                else:
                    action_idx = random.randrange(self.action_size)
'''

# Perform replacements
lines[else_start:else_end] = [new_else]
# Update death_else_start after first replacement may shift
# Recompute death_else_start after first replacement
# Simpler: do both replacements on original lines, but we need to adjust indices after first replacement.
# Let's do both replacements sequentially, recomputing indices after first replacement.
# We'll write a function to find line numbers after modification.
# Since we know the line numbers shift by (new lines count - old lines count)
new_else_lines = new_else.count('\n')  # note new_else already ends with newline?
old_else_lines = else_end - else_start
delta = new_else_lines - old_else_lines
# Adjust death_else_start by delta
death_else_start += delta
death_else_end += delta

# Now replace second block
lines[death_else_start:death_else_end] = [new_death_else]

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)
print('Updated random fallback blocks')