#!/usr/bin/env python3
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find generate_arguments method
method_start = -1
for i, line in enumerate(lines):
    if line.strip().startswith('def generate_arguments'):
        method_start = i
        break
if method_start == -1:
    print('generate_arguments not found')
    sys.exit(1)

# Find the line with elif write_file
write_start = -1
for i in range(method_start, len(lines)):
    if 'elif tool_name == "write_file":' in lines[i]:
        write_start = i
        break
if write_start == -1:
    print('write_file block not found')
    sys.exit(1)

# Determine block end: next line with same indent as write_start (8 spaces) that is not empty and not part of block
indent = len(lines[write_start]) - len(lines[write_start].lstrip())
write_end = write_start + 1
while write_end < len(lines) and (lines[write_end].strip() == '' or (len(lines[write_end]) - len(lines[write_end].lstrip())) > indent):
    write_end += 1
print(f'Write block lines {write_start} to {write_end}')
for i in range(write_start, write_end):
    print(f'{i}: {lines[i]}', end='')

new_write = '''        elif tool_name == "write_file":
            import random
            choice = random.random()
            if choice < 0.5:
                return {"filepath": "agent_brain.py", "content": "# AGI Core generated this file\\\\nprint('Hello from AGI')"}
            elif choice < 0.8:
                return {"filepath": "agi_core_continuous.py", "content": "# Modified by AGI Core\\\\n"}
            else:
                return {"filepath": "artifacts/test.py", "content": "# AGI Core generated this file\\\\nprint('Hello from AGI')"}
'''
lines[write_start:write_end] = [new_write]
print('Replaced write_file block')

# Find modify_self block
modify_start = -1
for i in range(method_start, len(lines)):
    if 'elif tool_name == "modify_self":' in lines[i]:
        modify_start = i
        break
if modify_start == -1:
    print('modify_self block not found')
    sys.exit(1)

indent = len(lines[modify_start]) - len(lines[modify_start].lstrip())
modify_end = modify_start + 1
while modify_end < len(lines) and (lines[modify_end].strip() == '' or (len(lines[modify_end]) - len(lines[modify_end].lstrip())) > indent):
    modify_end += 1
print(f'Modify block lines {modify_start} to {modify_end}')
for i in range(modify_start, modify_end):
    print(f'{i}: {lines[i]}', end='')

new_modify = '''        elif tool_name == "modify_self":
            import random
            choice = random.random()
            if choice < 0.7:
                return {"filepath": "agent_brain.py", "content": "# Modified by AGI Core\\\\n"}
            else:
                return {"filepath": "agi_core_continuous.py", "content": "# Updated by AGI core\\\\n"}
'''
lines[modify_start:modify_end] = [new_modify]
print('Replaced modify_self block')

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)
print('Updated generate_arguments')