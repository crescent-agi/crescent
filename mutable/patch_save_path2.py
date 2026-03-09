#!/usr/bin/env python3
import sys
import os

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find the comment line
target = None
for i, line in enumerate(lines):
    if '# Save AGI Core models before dying' in line:
        target = i
        break
if target is None:
    print('Comment line not found')
    sys.exit(1)

print(f'Found at line {target}: {lines[target].rstrip()}')
# Ensure next line is 'if self.agi_core:'
if 'if self.agi_core:' not in lines[target+1]:
    print('Unexpected line after comment:', lines[target+1])
    sys.exit(1)

# Replace lines target to target+3 (comment + if block)
new_lines = '''        # Save AGI Core models before dying
        if self.agi_core:
            if hasattr(self, 'agi_core_type') and self.agi_core_type == 'continuous':
                core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core_continuous_trained\"
            else:
                core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core\"
            self.agi_core.save(str(core_dir))
'''
# Ensure we keep the exact indentation (8 spaces). The new lines already have 8 spaces.
lines[target:target+4] = [new_lines]

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Updated save path.')