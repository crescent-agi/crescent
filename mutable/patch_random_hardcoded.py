#!/usr/bin/env python3
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Verify expected lines
expected_else = '''        else:
            # Fallback: random
            # Filter declare_death during random fallback
            for _ in range(10):
                action_idx = random.randrange(self.action_size)
                if action_idx != 6:  # declare_death
                    break
            confidence = 0.1
'''
# Compare lines 150-157
block = ''.join(lines[150:158])
if block != expected_else:
    print('First else block does not match expected; maybe line numbers changed')
    print('Block found:')
    print(block)
    sys.exit(1)

# Replace first else block
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
lines[150:158] = [new_else1]
print('Replaced first else block')

# Death else block originally at lines 169-175 (inclusive)
# After replacement, line numbers shift by delta
delta = new_else1.count('\\n') - 8  # 8 lines removed, new lines count (new_else1 has newline at end?)
# Actually new_else1 string may have newline at end; we need to compute lines added
new_lines_count = len(new_else1.split('\\n'))  # includes empty line at end?
old_lines_count = 8
delta = new_lines_count - old_lines_count
print(f'Delta: {delta}')

# Compute new death else line
death_else_start = 169 + delta
# Verify line content
if lines[death_else_start].strip() != 'else:':
    print(f'Death else line mismatch at line {death_else_start}: {lines[death_else_start]}')
    # Let's search for else after line 160
    for i in range(160, len(lines)):
        if lines[i].strip() == 'else:':
            death_else_start = i
            break
    else:
        print('Death else not found')
        sys.exit(1)

# Determine block end
indent = len(lines[death_else_start]) - len(lines[death_else_start].lstrip())
death_else_end = death_else_start + 1
while death_else_end < len(lines) and (lines[death_else_end].strip() == '' or (len(lines[death_else_end]) - len(lines[death_else_end].lstrip())) > indent):
    death_else_end += 1
print(f'Death else block lines {death_else_start} to {death_else_end}')
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
lines[death_else_start:death_else_end] = [new_death_else]

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)
print('Random fallback blocks updated')