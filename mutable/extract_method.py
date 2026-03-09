import sys
import re

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# find method start
start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        start = i
        break
if start is None:
    print('Method not found')
    sys.exit(1)

# find method end: next line with same indentation that starts with 'def ' or end of file
indent = len(lines[start]) - len(lines[start].lstrip())
end = start + 1
while end < len(lines):
    if lines[end].strip() == '':
        end += 1
        continue
    if len(lines[end]) - len(lines[end].lstrip()) == indent and lines[end].lstrip().startswith('def '):
        break
    end += 1

print(f'Method lines {start+1} to {end}')
print('---')
for i in range(start, end):
    sys.stdout.write(f'{i+1}: {lines[i]}')
print('---')
print(f'Total lines: {end-start}')

# Write method to separate file for editing
with open('compute_reward_method.txt', 'w') as f:
    f.writelines(lines[start:end])