#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find the write_file block start
start = None
for i, line in enumerate(lines):
    if line.strip() == '# Write file rewards - strongly encourage code creation':
        start = i
        break
if start is None:
    print('Could not find write_file block')
    sys.exit(1)

# Find the line after the block (next line that is not indented more than the if)
# The block ends before the next comment line that is not indented.
block_end = None
for i in range(start + 1, len(lines)):
    stripped = lines[i].strip()
    if stripped.startswith('#') and lines[i].startswith(' ' * 8) and not lines[i].startswith(' ' * 12):
        # This is a comment at same indentation as the if, indicating end of block
        block_end = i
        break
    if stripped.startswith('# Execute code rewards'):
        block_end = i
        break
if block_end is None:
    block_end = start + 20  # fallback

print(f'Block lines {start} to {block_end}')
for i in range(start, block_end):
    print(repr(lines[i]))

# Now we need to fix indentation for line start+2 (the reward line) and start+3 (filepath line)
# The if line is lines[start+1]
if_line = lines[start+1]
# Determine indentation of if line: should be 8 spaces
if not if_line.startswith(' ' * 8):
    print('Unexpected indentation for if line')
    sys.exit(1)
# The reward line should be indented 4 more spaces (12)
# The filepath line also 12 spaces
# The inner if line should be 12 spaces
# The inner block lines should be 16 spaces

# Let's just rewrite the block with correct indentation
new_block = '''        # Write file rewards - strongly encourage code creation
        if tool_name == "write_file" and "filepath" in tool_args:
            reward += 2.5  # base for writing (increased)
            filepath = tool_args["filepath"]
            if isinstance(filepath, str):
                if filepath.endswith('.py'):
                    reward += 2.5  # extra for Python files
                if 'agent_brain' in filepath or 'agi_core' in filepath:
                    reward += 2.0  # extra for self-modification (critical)
                if 'artifacts' in filepath or 'test' in filepath:
                    reward += 1.5  # extra for test/artifact creation
                if 'plan' in filepath or 'strategy' in filepath:
                    reward += 0.8  # planning docs
'''
# Replace lines
lines[start:block_end] = new_block.splitlines(keepends=True)

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Block replaced with correct indentation.')