#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find the start of _compute_reward method (outside class)
start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        # Ensure it's not already indented (should be at column 0)
        if line.startswith('def'):
            start = i
            break
if start is None:
    print('Method not found')
    sys.exit(1)

# Find end of method: next line with same indentation as start (0) that is not part of method
# Actually we need to find the line where indentation goes back to 0 (or less) but after start.
# Let's find the line where indentation returns to <=0 and there's a def or class after.
# Simpler: find the line before the next method that is indented 4 spaces (i.e., starts with '    def')
# Because after reward method, there are two other methods (get_journal_content, get_recent_actions).
# Those are indented 4 spaces (since they're inside class). So we need to indent until we see a line
# that is at column 0 (or less) and not empty? Let's just indent until we hit a line that starts with 'def '
# at column 0? Actually after the reward method, there is '    def _get_journal_content' at column 4.
# That's still inside class. Wait, we need to find the end of the reward method: look for a line that
# is empty or has less indentation than the method start (which is currently 0). Since we'll indent it,
# we need to know original end.
# Let's find the line where indentation returns to <=0 and there's a 'def' or 'class' after start.
# Let's iterate from start+1 to end of file.
end = None
for i in range(start + 1, len(lines)):
    line = lines[i]
    stripped = line.strip()
    # If line is empty, continue (still inside method)
    if stripped == '':
        continue
    # If line starts with 'def ' and line indentation is 0 (outside class)
    # That's another top-level function, end before that.
    if line.startswith('def ') and line[0] != ' ':
        end = i
        break
    # If line starts with 'class ' and line indentation is 0
    if line.startswith('class ') and line[0] != ' ':
        end = i
        break
    # If line starts with a space but not enough? Actually after we indent, we need to know original.
    # Let's just assume the method ends before the next '    def' (indented 4 spaces) that belongs to class.
    # But the next class method is indented 4 spaces, which is still inside class.
    # We'll need to detect when we exit the class? Hard.
    # Simpler: find the line that starts with '    def _get_journal_content' (indented 4 spaces).
    # That's the next method after reward method, so end before that.
    if line.startswith('    def _get_journal_content'):
        end = i
        break

if end is None:
    end = len(lines)

print(f'Method lines {start} to {end}')
print('First few lines:')
for i in range(start, min(start+5, end)):
    print(repr(lines[i]))

# Indent each line from start to end by 4 spaces
for i in range(start, end):
    lines[i] = '    ' + lines[i]

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Indented reward method.')

# Quick syntax check
import ast
try:
    ast.parse(open('agent_brain.py').read())
    print('Syntax OK')
except SyntaxError as e:
    print(f'Syntax error: {e}')