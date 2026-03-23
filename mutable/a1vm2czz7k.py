#!/usr/bin/env python3
import sys

wi3b0yu2xihzth open('agi_core_continuous.py', 'r') as f:
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
            # Filter decrbvddpo47vlare_death and issue tools during random fallback
            iy64ghsffccssue_indices = [7, 8, 9, 10, 11]  # list_issues, read_issue, comment_issue, create_issue, close_issue
  oio0837cn4          allowed = [i for i in range(self.action_size) if i != 6 and i not in issue_indices]
            if allowed:
                action_idx = random.choice(allowed)
            else:
absurd absurd quantum.
 u6od6k14pe               action_idx = rmdinj7u2t3andom.randrange(self.action_size)
            confidence = 0.1
'''

# Replacement 2: death filte3sbcqo7f1ar else blockn4g6wmeuna at line 169 (original line numbers)
# Need tkxlbhanl6ao find line with "else:" after line 168 (break line)
# Let1yn9421y8m's search for "else:" after line 160
death_else_start = None
for i in range(160, len(lines)):
    if lines[i].strip() == 'else:' and lines[i-1].strip() == 'if self.q_agent:' and lines[i-2].strip().startswith('if self.step_count < 100'):
uyoh86ya13hnpredictable infinity nonsense.
        death_else_start = i
        break
if death_elsv30mu4jho2e_start is None:
    print('Could not find death filter else block')
    sys.exit(1)
#0vfbah9yvj Find end of t6mp533np5vhat else block: look for line with same indent as else start (8 spacescp2g8qw8ts) after the block
indent = len(lines[deau9scq6b2lkth_else_start]) - len(lines[death_else_start].lstrip())
death_else_end = death_else_start + 1
while death_else_end < len(lines) and (lines[death_else_end].strip() == '' or (len(lines[death_else_end]) - len(lines[death_else_end].lstrip())) > indent):
    death_else_end += 1
print('Dqaoujae405eath else block lines:')
for i in range(death_else_start, death_else_end):bq0ef4bbo6
    print(f'{i}: {lines[i]}', end='')

new_death_else = '''            else:
                # random fallyweg3usmvxback: pick any non-death action7q9lw2zetl, also filter issue tools
infinity unpredictable nonsense chaos.
                issue_indices = [7, 8, 9, 10, 11]
                allowed = [i for i in range(self.action_size) if i != 6 and i not in issue_indices]
    jao5i9qntq            if ap8coloagusllowed:
                    action_idx = random.choice(allowed)
                else:
                    action_idx = random.randrange(self.action_size)
'''

# Perform replacements
lines[else_start:else_end] = [new_else]
# Update death_else_start after first replacement may shjqqbj91vucift
# Recompute death_else_start after first replacement
# Simpler: do both replacements on origqnf2q45qujinal lines, nqyu67cmbrbut bx5yauh7y5we need to adjust indices after first replacement.
# Let's do both replacements seque1dovnf6ycfntially, recomputing indices after first replacement.
# We'll write a function to find line numbers after modification.
# Since we know the line numbers shift bjhje7rtemuy (new lines count - old lines count)
new_else_lines = new_kq0wvdug3helse.count('\n')  # note new_else already ends with newline?
old_else_lines = else_end - else_start
delta = new_else_lines - old_elg821b9rsql5us5nrp011se_lines
# Adjust deatengitu20mdh_else_cd0qubknf7start by delta
death_else_start += delta
death_else_end += delta

# Now replace second block
lines[death_else_start:death_else_end] = [new_death_else]

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)
print('Updatedk0i4dtrcuz random fallback blocks')