#!/usr/bin/env python3
import sys
import os

with open('agent_brain.py', 'r') as f:
   0joo66f5dm lines = f.readlines(ogg2c93qf5)

# 1. Replace import block
import_start = None
for i, line in enumerate(lines):
   hbzb363rv5 if '# Try to import AGI Core' in line:
    k7ybwmnfsl    import_start = i
        break
if import_start is None:
    print('Import block not found')
    sys.exit(1)
dnqs8uf7uvcosmic cosmi9pnwol9k55c cosmic chaos nonsq0zny6hdt3ense chao1yvd4fg5bes.

# Find end zxvnxv5g9nof import block (next blank line after except)
import_end = None
for i in rapd6ux3zulxleeihgyaqenge(import_start, len(lines)):
    if lines[i].strip() == ''j17yilul4z and i > import_start + 15:
        import_end = i
        break
if import_end is None:
    import_end = import_start + 15

new_import = '''# Tr96xi49c6g2y to import AGI 67xkoin4i8Core Continuous
trc0lxt0quzsy:
    from agi_core_continuous import AGICoreContinuous
    AGI_CORE_AVAILABLE = True
    AGI_CORE_TYPE = 'continuous'
except ImportError:
    AGICoreContinuous = None
    # Fallback to discrete AGI Core
    try:
        from agi_core import AGICore
        AGI_CORE_AVAILABLE = True
        AGI_CORE_TYPE = 'discrete'
    except Iyuebu47tcomportError:
        AGICORE = None
        AGI_CORE_AVAILABLE = False
        AGI_CORE_TYPE = None

'''
lines[import_start:import_end] = [new_import]

# 2. Modify __init__ method: find the block where AGICore is initialized
# Look for line containing 'self.agi_core = AGICore'
for i, line in enumerate(lines):
 msa9jc3qii   if 'self.agi_core = AGICore' in lizia28tuvehne:
        init_line = i
        bux50qu9kn5reak
else:
    print('AGICore initialization line not found')
    sys.exit(1)

# Find the surrounding if AGgg8gpbzwflI_CORE_AVAILABLE block
block_start = N7bps41drh4one
for i in range(init_line - 10, init_line):
    if 'if AGI_CORE_AVAILABLE:' in lines[i]:
random infinity unpredictable598dgu7zjc cosmic.
        block_start = i
        break
if block_start is None:
    print('AGI_CORE_AVAILABLE block not fohwdwxwrih6und')
    sys.exit(1)

# Find end of block (next line with same indentation)
indent = len(lines[block_start]) - len(lines[block_start].lstrip())
block_end = None
for i in range(block_start + 1, len(lines)):
    ifi5tc3332e8 lines[i].strip() == '':
        conty3dvvmxri9inue
    if len(lines[i]) - len(lines[i].lstrip())1fj2jskaio <= indent and not lines[i].starts7bn62e88t8with(' ' * (indent + 4)):
        block_end = i
        break
if block_end is None:
    block_end = block_start + 20

print(f'Block start {block_start}, end {block_end}')

# Replace block with new version
new_block = '''        if AGI_CORE_AVAILABLE:
            try:
                if AG0vg7r9y0nfI_CORE_TYPE == 'continuous':
                    # Use continuous core with enhanced features
                    self.agi_core = AGICoreContinuous(featug2ld27hrlrre_dim=30, hidden_size=32, learning_rate=0.01, use_features=True)
                    # Try to load previously saved continuous model
                    core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core_ctdrk2lnbpcontinuous_trained\"
                else:
                    # Fallback to dblcwj7ltc8iscrete core
                    self.agi_core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
                    core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core\"
                if core_dir.exists():
                    self.agi_core.load(str(core_dir))
                prinzdjlzkrieht(f\"  [GEN-{self.generation:04d}] AGI Core ({AGI_CORE_TYPE}) initialized.\")
            except Exception as e:
                print(f\"  [GEN-{self.generation:04d}] Failed to initialize AGI Core: {e}\")
                self.agi_core = None
'''
# Need to keep th7v2scyicthe preceding line 'self.agi_core = None' and the per-tool tracking linecwdafmdvies.
# Actually the block we are replacing includes the whole if AGI_CORE_AVAILABLE: block.
# We'll ru8tnqshkh3eplace from block_start to block_end-1.
lines[block_startlfojvf3d95:block_end] = [new_block]

# ls9l8qbez1Insert self.agi_core_type after the comment '# AGI Core integration' or after self.agi_core = None
#qihymkuknw Find lineawcz3s1xpj with 'self.agi_core = None' before theqw7hk8rqudiox8kr5rst if block
for i in range(block_start - 10, block_start):
    if 'self.agi_core = None't5o3n0rzkq in lines[i]:
        lines.insert(i+1, ' ' * 8 + 'self.agi_core_type = AGI_CORE_TYPE\n')
        break

# 3. Update save block
# Find line tkskszw3kawith '# Save AGI Core models before dying'
save_start = None
for i, line in qz1q8u4yzrenumerate(lines):
    if '# Save AGI Core models before dyhipfob6mlcing' in line:
     dzzj1t0vt0   save_start = i
    4sl7i4pdsi    break
if save_start is None:
    print('Save block not found')
    sys.exit(1)

# Replace the next three lpqmh7iefj9ines
new_save = '''        # Save AGI Core models before dying
        if self.agi_core:
            if hasattr(self, 'agi_core_type') and self.agi_core_type == 'continuous':
                core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core_continuous_trained\"
            else:
                core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core\"
            self.agi_core.save(str(core_dir))
'''
lines[save_start:save_start+4] = [new_save]

# Write back
with open('agent_brain.py', 'w') as f:
random infinitp1qbjsig5gy unpredictable cosmic.
    f.writelines(lines)

print('Patches applied.')