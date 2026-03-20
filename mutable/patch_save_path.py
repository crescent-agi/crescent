#!/usr/bin/env python3
import sys
import os

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find the line with 'core_dir = self.sandbox.gen_dir / "artifacts" / "agi_core"'
target_line = None
for i, line in enumerate(lines):
    if 'core_dir = self.sandbox.gen_dir / "artifacts" / "agi_core"' in line:
        target_line = i
        break
if target_line is None:
    print('Save line not found')
    sys.exit(1)

# Replace that line and the following line (self.agi_core.save) with conditional block
# We'll replace lines target_line-1 to target_line+1? Actually we need to replace from line before (if self.agi_core:)
# Let's find the start of the if block.
block_start = None
for i in range(target_line - 5, target_line):
    if lines[i].strip().startswith('if self.agi_core:'):
        block_start = i
        break
if block_start is None:
    print('if block not found')
    sys.exit(1)

# Find end of block (next line with same indentation)
indent = len(lines[block_start]) - len(lines[block_start].lstrip())
block_end = None
for i in range(block_start + 1, len(lines)):
    if lines[i].strip() == '':
        continue
    if len(lines[i]) - len(lines[i].lstrip()) <= indent and not lines[i].startswith(' ' * (indent + 4)):
        block_end = i
        break
if block_end is None:
    block_end = block_start + 5

print(f'Block start {block_start}, end {block_end}')
print('Current block:', ''.join(lines[block_start:block_end]))

# New block
new_block = '''        # Save AGI Core models before dying
        if self.agi_core:
            if hasattr(self, 'agi_core_type') and self.agi_core_type == 'continuous':
                core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core_continuous_trained\"
            else:
                core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core\"
            self.agi_core.save(str(core_dir))
'''

# Replace block
lines[block_start:block_end] = [new_block]

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Updated save path.')