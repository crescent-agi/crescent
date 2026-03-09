#!/usr/bin/env python3
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find first else block (random fallback)
else1_line = None
for i, line in enumerate(lines):
    if line.strip() == 'else:' and i>0 and 'elif self.cognitive:' in lines[i-1]:
        else1_line = i
        break
if else1_line is None:
    print('First else not found')
    sys.exit(1)

# Determine block end
indent = len(lines[else1_line]) - len(lines[else1_line].lstrip())
else1_end = else1_line + 1
while else1_end < len(lines) and (lines[else1_end].strip() == '' or (len(lines[else1_end]) - len(lines[else1_end].lstrip())) > indent):
    else1_end += 1
print(f'Replacing first else block lines {else1_line} to {else1_end}')
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

# Find death filter else block
death_if_line = None
for i, line in enumerate(lines):
    if 'if self.step_count < 100 and action_idx == 6:' in line:
        death_if_line = i
        break
if death_if_line is None:
    print('Death filter not found')
    sys.exit(1)
# Find else inside that block
death_else_line = None
for i in range(death_if_line, len(lines)):
    if lines[i].strip() == 'else:' and lines[i-1].strip() == 'if self.q_agent:':
        death_else_line = i
        break
if death_else_line is None:
    print('Death else not found')
    sys.exit(1)
indent2 = len(lines[death_else_line]) - len(lines[death_else_line].lstrip())
death_else_end = death_else_line + 1
while death_else_end < len(lines) and (lines[death_else_end].strip() == '' or (len(lines[death_else_end]) - len(lines[death_else_end].lstrip())) > indent2):
    death_else_end += 1
print(f'Replacing death else block lines {death_else_line} to {death_else_end}')
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

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)
print('Random fallback blocks updated')