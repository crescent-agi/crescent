#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
import re

with open('mutable_snapshot/agent_brain.py', 'r') as f:
    lines = f.readlines()

# Fix line 154 (approximate) where self.state_path = self.sandbox.gen_dir / "life_state.json"
for i, line in enumerate(lines):
    if 'self.state_path = self.sandbox.gen_dir / "life_state.json"' in line:
        # Replace with Path conversion
        lines[i] = '        self.state_path = Path(self.sandbox.gen_dir) / "life_state.json"\n'
        print(f'Fixed line {i+1}')
        break

# Remove duplicate save block (lines 313-319) where there are two if self.agi_core: blocks
# Actually there are two consecutive if self.agi_core: blocks; we need to delete the second one.
# Let's find the first occurrence of "if self.agi_core:" after line 300.
start = None
for i in range(300, 340):
    if lines[i].strip() == 'if self.agi_core:':
        if start is None:
            start = i
        else:
            # second occurrence, delete from i to the next line that matches indent level 0? Actually need to delete the block.
            # We'll delete lines i through i+? until a line with less indent or end of file.
            # Let's just delete the whole block (i to i+6 maybe). Let's inspect.
            print(f'Duplicate block starts at line {i+1}')
            # Delete lines i to i+6 (including the next line that sets core_dir_name)
            for j in range(i, i+7):
                if j < len(lines):
                    lines[j] = ''  # empty line
            break

with open('mutable_snapshot/agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Applied fixes.')