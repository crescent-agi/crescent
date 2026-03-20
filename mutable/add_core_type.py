#!/usr/bin/env python3
import sys
import os

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find start of __init__ method
init_start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def __init__(self, llm_client, sandbox, death_monitor, generation: int, day_manager=None):'):
        init_start = i
        break
if init_start is None:
    print('__init__ method not found')
    sys.exit(1)

# Find end of __init__ method: next line with same indentation that starts with 'def '
indent = len(lines[init_start]) - len(lines[init_start].lstrip())
init_end = None
for i in range(init_start + 1, len(lines)):
    if lines[i].strip() == '':
        continue
    if len(lines[i]) - len(lines[i].lstrip()) <= indent and lines[i].strip().startswith('def '):
        init_end = i
        break
if init_end is None:
    init_end = len(lines)

print(f'__init__ method from line {init_start} to {init_end}')

# Extract the method lines
method_lines = lines[init_start:init_end]

# Find line with '# AGI Core integration' (should be after the per-tool tracking)
# We'll insert after that line
insert_idx = None
for i, line in enumerate(method_lines):
    if '# AGI Core integration' in line:
        insert_idx = i + 1
        break
if insert_idx is None:
    print('Could not find AGI Core integration comment')
    sys.exit(1)

# Insert self.agi_core_type = AGI_CORE_TYPE
method_lines.insert(insert_idx, ' ' * 8 + 'self.agi_core_type = AGI_CORE_TYPE\n')

# Replace the block
lines[init_start:init_end] = method_lines

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Added self.agi_core_type.')