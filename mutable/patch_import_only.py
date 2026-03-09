#!/usr/bin/env python3
import sys
import os

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find import block
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
    if lines[i].strip() == '' and i > import_start + 10:
        import_end = i
        break
if import_end is None:
    import_end = import_start + 10

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

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Import block updated.')