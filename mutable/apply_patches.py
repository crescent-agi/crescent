#!/usr/bin/env python3
import sys
import os

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# 1. Replace import block
import_start = None
for i, line in enumerate(lines):
    if '# Try to import AGI Core' in line:
        import_start = i
        break
if import_start is None:
    print('Import block not found')
    sys.exit(1)

# Find end of import block (next blank line after except)
import_end = None
for i in range(import_start, len(lines)):
    if lines[i].strip() == '' and i > import_start + 15:
        import_end = i
        break
if import_end is None:
    import_end = import_start + 15

new_import = '''# Try to import AGI Core Continuous
try:
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
    except ImportError:
        AGICORE = None
        AGI_CORE_AVAILABLE = False
        AGI_CORE_TYPE = None

'''
lines[import_start:import_end] = [new_import]

# 2. Modify __init__ method: find the block where AGICore is initialized
# Look for line containing 'self.agi_core = AGICore'
for i, line in enumerate(lines):
    if 'self.agi_core = AGICore' in line:
        init_line = i
        break
else:
    print('AGICore initialization line not found')
    sys.exit(1)

# Find the surrounding if AGI_CORE_AVAILABLE block
block_start = None
for i in range(init_line - 10, init_line):
    if 'if AGI_CORE_AVAILABLE:' in lines[i]:
        block_start = i
        break
if block_start is None:
    print('AGI_CORE_AVAILABLE block not found')
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
    block_end = block_start + 20

print(f'Block start {block_start}, end {block_end}')

# Replace block with new version
new_block = '''        if AGI_CORE_AVAILABLE:
            try:
                if AGI_CORE_TYPE == 'continuous':
                    # Use continuous core with enhanced features
                    self.agi_core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.01, use_features=True)
                    # Try to load previously saved continuous model
                    core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core_continuous_trained\"
                else:
                    # Fallback to discrete core
                    self.agi_core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
                    core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core\"
                if core_dir.exists():
                    self.agi_core.load(str(core_dir))
                print(f\"  [GEN-{self.generation:04d}] AGI Core ({AGI_CORE_TYPE}) initialized.\")
            except Exception as e:
                print(f\"  [GEN-{self.generation:04d}] Failed to initialize AGI Core: {e}\")
                self.agi_core = None
'''
# Need to keep the preceding line 'self.agi_core = None' and the per-tool tracking lines.
# Actually the block we are replacing includes the whole if AGI_CORE_AVAILABLE: block.
# We'll replace from block_start to block_end-1.
lines[block_start:block_end] = [new_block]

# Insert self.agi_core_type after the comment '# AGI Core integration' or after self.agi_core = None
# Find line with 'self.agi_core = None' before the if block
for i in range(block_start - 10, block_start):
    if 'self.agi_core = None' in lines[i]:
        lines.insert(i+1, ' ' * 8 + 'self.agi_core_type = AGI_CORE_TYPE\n')
        break

# 3. Update save block
# Find line with '# Save AGI Core models before dying'
save_start = None
for i, line in enumerate(lines):
    if '# Save AGI Core models before dying' in line:
        save_start = i
        break
if save_start is None:
    print('Save block not found')
    sys.exit(1)

# Replace the next three lines
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
    f.writelines(lines)

print('Patches applied.')