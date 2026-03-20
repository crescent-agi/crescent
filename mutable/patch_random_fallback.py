#!/usr/bin/env python3
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find the line with "else:" inside decide_action method
in_decide = False
start_method = None
for i, line in enumerate(lines):
    if line.strip().startswith('def decide_action'):
        in_decide = True
        start_method = i
        # find indent
        indent = len(line) - len(line.lstrip())
        break
if not in_decide:
    print('decide_action method not found')
    sys.exit(1)

# Find the else block (random fallback)
else_line = None
for i in range(start_method, len(lines)):
    if lines[i].strip() == 'else:' and lines[i-1].strip() == 'elif self.cognitive:':
        else_line = i
        break
if else_line is None:
    print('else block not found')
    sys.exit(1)

# Determine the block lines: from else_line to the line before next line with same indentation
# Actually we need to replace lines from else_line to the line before the next line at same indent level as else_line
indent = len(lines[else_line]) - len(lines[else_line].lstrip())
# Find next line with same indent that is not empty
end_line = else_line + 1
while end_line < len(lines) and (lines[end_line].strip() == '' or (len(lines[end_line]) - len(lines[end_line].lstrip())) > indent):
    end_line += 1
# Now lines[else_line:end_line] is the else block.
print(f'else block lines {else_line} to {end_line}')
for j in range(else_line, end_line):
    print(f'{j}: {lines[j]}', end='')

# Define new block
new_block = '''        else:
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

# Replace lines
lines[else_line:end_line] = [new_block]

# Also need to replace the second random fallback inside death filter (lines 169-175)
# Find line with "# random fallback: pick any non-death action"
for i in range(start_method, len(lines)):
    if '# random fallback: pick any non-death action' in lines[i]:
        # Replace from that line until the break line (line with break)
        # Actually we need to replace the inner for loop block
        # Let's find the line with "for _ in range(10):" before this comment
        # Actually comment is inside the else block of death filter.
        # Let's locate the else block inside death filter
        # We'll do a simpler approach: replace the whole else block from line 169 to 175
        # Let's find line with "else:" inside the death filter
        # The death filter block starts at line 160 (if self.step_count < 100 and action_idx == 6:)
        # We'll find the else line under that block.
        pass

# For now, we'll just update the second random fallback manually later.
# Write back
with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)
print('Updated random fallback block')