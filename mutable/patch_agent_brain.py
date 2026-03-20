#!/usr/bin/env python3
import sys
import os

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find import block lines
import_start = None
for i, line in enumerate(lines):
    if line.strip().startswith('# Try to import AGI Core'):
        import_start = i
        break
if import_start is None:
    print('Import block not found')
    sys.exit(1)

# Find end of import block (next blank line after except)
import_end = None
for i in range(import_start, len(lines)):
    if lines[i].strip() == '' and i > import_start + 10:
        import_end = i
        break
if import_end is None:
    import_end = import_start + 10

# New import block
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

# Replace lines
lines[import_start:import_end] = [new_import]

# Now find the __init__ method where agi_core is initialized
# Look for line containing 'self.agi_core = AGICore'
for i, line in enumerate(lines):
    if 'self.agi_core = AGICore' in line:
        init_line = i
        break
else:
    print('AGICore initialization line not found')
    sys.exit(1)

# Find the surrounding block (lines before and after)
# We'll replace from line where 'if AGI_CORE_AVAILABLE:' starts
# Find that line
block_start = None
for i in range(init_line - 10, init_line):
    if 'if AGI_CORE_AVAILABLE:' in lines[i]:
        block_start = i
        break
if block_start is None:
    print('AGI_CORE_AVAILABLE block not found')
    sys.exit(1)

# Find end of block (line where indentation returns)
indent = len(lines[block_start]) - len(lines[block_start].lstrip())
block_end = None
for i in range(block_start + 1, len(lines)):
    if lines[i].strip() == '':
        continue
    if len(lines[i]) - len(lines[i].lstrip()) <= indent:
        block_end = i
        break
if block_end is None:
    block_end = block_start + 20

print(f'Block start {block_start}, end {block_end}')
print('Current block:', ''.join(lines[block_start:block_end]))

# New block logic
new_block = '''        # AGI Core integration
        self.agi_core = None
        if AGI_CORE_AVAILABLE:
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
        else:
            print(f\"  [GEN-{self.generation:04d}] AGI Core not available.\")
'''

# Replace block
lines[block_start:block_end] = [new_block]

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Patched agent_brain.py with AGICoreContinuous support.')