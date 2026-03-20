#!/usr/bin/env python3
import sys
import os

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find the line with 'self.agi_core = AGICore'
target_line = None
for i, line in enumerate(lines):
    if 'self.agi_core = AGICore' in line:
        target_line = i
        break
if target_line is None:
    print('AGICore initialization line not found')
    sys.exit(1)

# Find start of if AGI_CORE_AVAILABLE block
block_start = None
for i in range(target_line - 10, target_line):
    if 'if AGI_CORE_AVAILABLE:' in lines[i]:
        block_start = i
        break
if block_start is None:
    print('if block not found')
    sys.exit(1)

# Find end of block (next line with same indentation as block_start)
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
print('Current block:')
for i in range(block_start, block_end):
    print(lines[i].rstrip())

# New block
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
# Replace block
lines[block_start:block_end] = [new_block]

# Add self.agi_core_type after the comment '# AGI Core integration' or after self.agi_core = None
# Find line with 'self.agi_core = None' before the if block
for i in range(block_start - 10, block_start):
    if 'self.agi_core = None' in lines[i]:
        lines.insert(i+1, ' ' * 8 + 'self.agi_core_type = AGI_CORE_TYPE\n')
        break

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Init block patched.')