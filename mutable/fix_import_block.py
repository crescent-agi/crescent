#!/usr/bin/env python3
import sys
import os

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find start of import block
import_start = None
for i, line in enumerate(lines):
    if '# Try to import AGI Core Continuous' in line:
        import_start = i
        break
if import_start is None:
    print('Import block not found')
    sys.exit(1)

# Find end of import block: after the line containing 'AGI_CORE_TYPE = None' and a blank line
# Actually we'll find the line where indentation returns to zero after the except block.
# Let's find the line with 'TOOLS_SCHEMA = [' which is the start of class content.
tools_start = None
for i in range(import_start, len(lines)):
    if 'TOOLS_SCHEMA = [' in lines[i]:
        tools_start = i
        break
if tools_start is None:
    print('TOOLS_SCHEMA not found')
    sys.exit(1)

# Now we need to dedent everything from tools_start onward by 4 spaces.
# But first, replace the import block lines from import_start to tools_start-1 with new import block.
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
lines[import_start:tools_start] = [new_import]

# Now dedent all lines from tools_start onward (the index changed because we replaced)
# Find new tools_start again
for i in range(len(lines)):
    if 'TOOLS_SCHEMA = [' in lines[i]:
        tools_start = i
        break

# Dedent each line from tools_start to end by 4 spaces if they start with 4 spaces.
for i in range(tools_start, len(lines)):
    if lines[i].startswith('    '):
        lines[i] = lines[i][4:]

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Fixed import block and dedented class definition.')