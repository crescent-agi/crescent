#!/usr/bin/env python3
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find learn_from_outcome method
start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def learn_from_outcome(self'):
        start = i
        break
if start is None:
    print('Method not found')
    sys.exit(1)

# Find end of method: next line with same indentation that starts with 'def ' or end of file
indent = len(lines[start]) - len(lines[start].lstrip())
i = start + 1
while i < len(lines):
    if lines[i].strip() == '':
        i += 1
        continue
    if len(lines[i]) - len(lines[i].lstrip()) <= indent and lines[i].strip() != '':
        # Same or less indent, end of method
        break
    i += 1
end = i

# Insert line after the reward parameter line (first line of method)
# Find the line with reward parameter (should be the first line after def)
# We'll insert after the line that starts with '        if self.current_state_vector is None'
# Actually we need to insert after the reward variable is used, but before updates.
# Let's find line with 'self.current_state_vector is None'
for j in range(start, end):
    if 'self.current_state_vector is None' in lines[j]:
        insert_pos = j + 1
        break
else:
    insert_pos = start + 1

# Insert line: if self.feature_extractor: self.feature_extractor.add_reward(reward)
new_line = ' ' * (indent + 8) + '# Record reward for feature trend\n'
new_line += ' ' * (indent + 8) + 'if self.feature_extractor:\n'
new_line += ' ' * (indent + 12) + 'self.feature_extractor.add_reward(reward)\n'
lines.insert(insert_pos, new_line)

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print('Patched agi_core_continuous.py with reward recording.')