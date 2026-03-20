#!/usr/bin/env python3
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find line with "elif self.cognitive:"
elif_line = -1
for i, line in enumerate(lines):
    if 'elif self.cognitive:' in line:
        elif_line = i
        break
if elif_line == -1:
    print('elif self.cognitive not found')
    sys.exit(1)

# Find next else with same indent
indent = len(lines[elif_line]) - len(lines[elif_line].lstrip())
else1_line = -1
for i in range(elif_line+1, len(lines)):
    if lines[i].strip() == 'else:' and (len(lines[i]) - len(lines[i].lstrip())) == indent:
        else1_line = i
        break
if else1_line == -1:
    print('first else not found')
    sys.exit(1)

# Determine block end
else1_end = else1_line + 1
while else1_end < len(lines) and (lines[else1_end].strip() == '' or (len(lines[else1_end]) - len(lines[else1_end].lstrip())) > indent):
    else1_end += 1
print(f'First else block lines {else1_line} to {else1_end}')

new_else1 = '''        else:
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
lines[else1_line:else1_end] = [new_else1]
print('Replaced first else block')

# Now find death filter else block
# Find line with "if self.step_count < 100 and action_idx == 6:"
death_if_line = -1
for i, line in enumerate(lines):
    if 'if self.step_count < 100 and action_idx == 6:' in line:
        death_if_line = i
        break
if death_if_line == -1:
    print('death filter not found')
    sys.exit(1)

# Find else inside that block: look for "else:" after death_if_line and before the next line with indent <= indent of death_if_line
death_indent = len(lines[death_if_line]) - len(lines[death_if_line].lstrip())
death_else_line = -1
for i in range(death_if_line+1, len(lines)):
    if lines[i].strip() == 'else:' and (len(lines[i]) - len(lines[i].lstrip())) == death_indent + 4:  # else is inside if block
        death_else_line = i
        break
if death_else_line == -1:
    print('death else not found')
    sys.exit(1)

# Determine block end
death_else_end = death_else_line + 1
while death_else_end < len(lines) and (lines[death_else_end].strip() == '' or (len(lines[death_else_end]) - len(lines[death_else_end].lstrip())) > death_indent + 4):
    death_else_end += 1
print(f'Death else block lines {death_else_line} to {death_else_end}')

new_death_else = '''            else:
                # random fallback: pick any non-death action, also filter issue tools
                issue_indices = [7, 8, 9, 10, 11]
                allowed = [i for i in range(self.action_size) if i != 6 and i not in issue_indices]
                if allowed:
                    action_idx = random.choice(allowed)
                else:
                    action_idx = random.randrange(self.action_size)
'''
lines[death_else_line:death_else_end] = [new_death_else]
print('Replaced death else block')

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)
print('Random fallback blocks updated')