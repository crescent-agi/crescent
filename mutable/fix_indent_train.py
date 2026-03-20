import sys
sys.path.insert(0, '.')

with open('train_continuous_new.py', 'r') as f:
    lines = f.readlines()

# Find the outer for loop
outer_start = None
for i, line in enumerate(lines):
    if line.strip() == 'for episode in range(episodes):':
        outer_start = i
        break
if outer_start is None:
    print('Outer loop not found')
    sys.exit(1)

# Determine base indent
base_indent = len(lines[outer_start]) - len(lines[outer_start].lstrip())
print('Base indent:', base_indent)

# Find the inner for loop line that starts with 'for step in range(steps_per_episode):' after outer_start
inner_start = None
for i in range(outer_start + 1, len(lines)):
    if lines[i].strip().startswith('for step in range(steps_per_episode):'):
        inner_start = i
        break
if inner_start is None:
    print('Inner loop not found')
    sys.exit(1)

# Check indentation of inner loop
inner_indent = len(lines[inner_start]) - len(lines[inner_start].lstrip())
print('Inner indent:', inner_indent)
# Should be base_indent + 4
if inner_indent != base_indent + 4:
    # Adjust inner loop line and all subsequent lines that belong to inner loop
    # We'll need to adjust all lines until we find a line with indent <= base_indent
    i = inner_start
    while i < len(lines):
        if lines[i].strip() == '':
            i += 1
            continue
        cur_indent = len(lines[i]) - len(lines[i].lstrip())
        if cur_indent <= base_indent and not lines[i].strip().startswith('#'):
            # This line is outside inner loop
            break
        # Adjust indent: increase or decrease to base_indent + 4
        if cur_indent != base_indent + 4:
            lines[i] = ' ' * (base_indent + 4) + lines[i].lstrip()
        i += 1

# Also ensure the reset lines are indented correctly (they should be base_indent + 4)
# Find the line 'self.reset()' after outer_start
for i in range(outer_start + 1, inner_start):
    if lines[i].strip() == 'self.reset()' or lines[i].strip().startswith('#'):
        cur_indent = len(lines[i]) - len(lines[i].lstrip())
        if cur_indent != base_indent + 4:
            lines[i] = ' ' * (base_indent + 4) + lines[i].lstrip()

# Write back
with open('train_continuous_new_fixed.py', 'w') as f:
    f.writelines(lines)

print('Fixed indentation saved to train_continuous_new_fixed.py')