#!/usr/bin/env python3
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Helper to find line with pattern
def find_line(pattern, start=0):
    for i in range(start, len(lines)):
        if pattern in lines[i]:
            return i
    return -1

# Find decide_action start
decide_start = find_line('def decide_action')
if decide_start == -1:
    print('decide_action not found')
    sys.exit(1)

# Find else block after elif self.cognitive:
else1 = find_line('        else:', decide_start)
if else1 == -1:
    print('first else not found')
    sys.exit(1)
# Ensure previous line is elif self.cognitive:
if 'elif self.cognitive:' not in lines[else1-1]:
    print('previous line mismatch')
    sys.exit(1)
# Determine block end: next line with same indent as else1 (8 spaces)
indent = len(lines[else1]) - len(lines[else1].lstrip())
else1_end = else1 + 1
while else1_end < len(lines) and (lines[else1_end].strip() == '' or (len(lines[else1_end]) - len(lines[else1_end].lstrip())) > indent):
    else1_end += 1
print(f'First else block lines {else1} to {else1_end}')
for i in range(else1, else1_end):
    print(f'{i}: {lines[i]}', end='')

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
lines[else1:else1_end] = [new_else1]

# Recompute lines (refresh indices)
lines = lines  # already updated

# Find death filter else block
# Look for line with "if self.step_count < 100 and action_idx == 6:"
death_if = find_line('if self.step_count < 100 and action_idx == 6:')
if death_if == -1:
    print('death filter not found')
    sys.exit(1)
# Find else inside that block
death_else = find_line('            else:', death_if)
if death_else == -1:
    print('death else not found')
    sys.exit(1)
# Determine block end
indent2 = len(lines[death_else]) - len(lines[death_else].lstrip())
death_else_end = death_else + 1
while death_else_end < len(lines) and (lines[death_else_end].strip() == '' or (len(lines[death_else_end]) - len(lines[death_else_end].lstrip())) > indent2):
    death_else_end += 1
print(f'Death else block lines {death_else} to {death_else_end}')
for i in range(death_else, death_else_end):
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
lines[death_else:death_else_end] = [new_death_else]

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)
print('Updated both random fallback blocks')