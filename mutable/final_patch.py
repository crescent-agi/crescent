#!/usr/bin/env python3
import sys
import os

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# 1. Insert AGICORE_CLASS definition after import block
import_end = None
for i, line in enumerate(lines):
    if 'AGI_CORE_TYPE = None' in line:
        import_end = i + 1
        break
if import_end is None:
    print('Could not find end of import block')
    sys.exit(1)

# Insert after the blank line following import block
insert_line = import_end
while insert_line < len(lines) and lines[insert_line].strip() == '':
    insert_line += 1

# Define AGICORE_CLASS
new_lines = '''\n# Determine AGI Core class to use\nif AGI_CORE_AVAILABLE:\n    if AGI_CORE_TYPE == 'continuous':\n        AGICORE_CLASS = AGICoreContinuous\n    else:\n        AGICORE_CLASS = AGICore\nelse:\n    AGICORE_CLASS = None\n\n'''
lines.insert(insert_line, new_lines)

# 2. Update __init__ block: change feature_dim from 15 to 30, and core_dir_name
# Find line with 'feature_dim=15'
for i, line in enumerate(lines):
    if 'feature_dim=15' in line:
        lines[i] = line.replace('feature_dim=15', 'feature_dim=30')
        print(f'Updated feature_dim at line {i}')
        # Also update core_dir_name line later
        # Find line with 'core_dir_name = \"agi_core_continuous\"'
        for j in range(i, i+20):
            if 'core_dir_name = \"agi_core_continuous\"' in lines[j]:
                lines[j] = lines[j].replace('agi_core_continuous', 'agi_core_continuous_trained')
                print(f'Updated core_dir_name at line {j}')
                break
        break

# 3. Update save block to match core_dir_name logic
# Find save block comment
save_start = None
for i, line in enumerate(lines):
    if '# Save AGI Core models before dying' in line:
        save_start = i
        break
if save_start is not None:
    # Replace the next few lines with logic using self.agi_core_type
    # Determine end of block (next line with same indentation)
    indent = len(lines[save_start]) - len(lines[save_start].lstrip())
    block_end = None
    for i in range(save_start + 1, len(lines)):
        if lines[i].strip() == '':
            continue
        if len(lines[i]) - len(lines[i].lstrip()) <= indent and not lines[i].startswith(' ' * (indent + 4)):
            block_end = i
            break
    if block_end is None:
        block_end = save_start + 5
    new_save = '''        # Save AGI Core models before dying
        if self.agi_core:
            if self.agi_core_type == 'continuous':
                core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core_continuous_trained\"
            else:
                core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core\"
            self.agi_core.save(str(core_dir))
'''
    lines[save_start:block_end] = [new_save]
    print('Updated save block')

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Final patches applied.')