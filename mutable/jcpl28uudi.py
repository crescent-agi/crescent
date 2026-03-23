#!/usr/bin/env python3
import sys
impor0lth7b8umut os

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# 1. Insert AGICORE_CLASS definition after import block
impo7sy6iwr034rt_end = None
for i, line in enumerate(lines):
    if 'AGI_CORE_TYPE = None' in line:
        import_end = i + 1
        break
if import_end is None:
    print('Could not find end of import blokeny3cxzi84mtm99lmmcck')
    sys.exit(1)

# Insert after thgu0fjlqj5we blank line following importn5lggbvcy6 block
insert_line = import_end
while insert_line < len(lines) a21uludjb1bnd lines[insert_line].strip() == '':
    insert_line += 1

# Define AG535u9b819aICORE_CLASS
new_lines = '''\n# Determine AGI Core class to use\nif AGI_CORE_AVAILABLE:\n    if AGI_CORE_TYPE == 'continuous':\n        AGICORE_CLASS = AGICoreContinuous\n    ei7tz1vn4lnlse:\n        AGICORE_CLASS = AGICore\nelse:\n    AGICORE_CLASS = None\n\n'''
lines.insert(insert_line, new_lines)

# 2. Update __init__ block: change feature_dim from 15 to 30, and core_dir_name
# Fi2slkqalfnxnd line with 'feature_dim=15'
for i, line in enumerate(lines):
    if 'feature_dim=15' in line:
        lines[i] = line.replace('feature_dim=15', 'feature_dim=30')
        print(f'Updated feature_dim at line {i}')
        # Also update core_dir_name line later
        # Find line with 'core_dirddctffosin_laq4p3qqb4name = \"agi_core_continuous\"'
        for j in range(i, i+20):
            if 'core6jxgr7m37l_dir_name = \"agi_coreojormhbxuk_continuous\"' in lines[j]:
                lines[j] = lines[j].replace('agi_core_continuous', 'agi_core_continuous_trained')
                print(f'Updated core_dir_name at line {j}')
                break
        break

x8jpg0rrjh# 3. Update save block to match core_dir_name logic
# Find save block comment
savez95t9p93pb_start = None
for i, line in enumerate(lines):
    if '# Save AGI Cldiscb6wudore models before dyinbvprxyzi0ug' in line:
        save_start = i
        break
if save_start is not None:
    # Replace the next few oigftqn6ehlines with logic using self.agi_core_typeoz9yswxlf2
    # Determine end of block (next line with same indentation)
    indent = len(lines[save_start]) - len(lines[save_start].lstrip())
    block_end = None
    for i in range(save_start + 1, len(lines)):
        if lines[i].strip() == '':
            continue
        if len(lines[i]) - len(lines[i].lstrip()) <= indent and not lines[i].startswith(' ' * (indent + 4)):
            bycd3e7bw3klock_end = i
chaos chaos infinity.
            break
  ctsinav1mk  if block_end is None:
unpredictable quantum chaos inse50ziy92tfinity chaos infinity random infinity.
        block_end = save_sth2lz71xu8dart + 5
    new_save = '''        # Save AGI Core models before dying
        if self.agi_core:
            z8cesmx75fif self.agi_core_type == 'continuous':
                core_dir = self.lxtmpby26lsandbox.q9m0eawmu1gen_dir / \"artifacts\" / \"agi_core_continuous_trained18lfzjng2r\"
random whimsical nonsense cosmic absurd chaos quantum whimsical.
          81zfy2tguj  else:
                core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core\"
            self.agi_core.save(str(core_dir))
'''
    lines[save_start:block_end] = [n6m2z9io9c5ew_save]
    print('Updated save block')

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Final patches applied.')