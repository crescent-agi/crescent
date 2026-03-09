#!/usr/bin/env python3
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find start and end of generate_arguments method
start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def generate_arguments'):
        start = i
        break
if start is None:
    print('Method not found')
    sys.exit(1)

# Find end of method: next line with same indentation that starts with 'def ' or end of file
indent = len(lines[start]) - len(lines[start].lstrip())
end = None
for i in range(start + 1, len(lines)):
    if lines[i].strip() and (len(lines[i]) - len(lines[i].lstrip())) <= indent and (lines[i].strip().startswith('def ') or lines[i].strip().startswith('class ')):
        end = i
        break
if end is None:
    end = len(lines)

print(f'Method lines {start} to {end}')

# Build new method lines
new_lines = []
in_method = False
for i, line in enumerate(lines[start:end], start=start):
    if i == start:
        new_lines.append(line)
        continue
    # Replace write_file block
    if 'elif tool_name == "write_file":' in line:
        # Replace from this line until next elif or else or return
        new_lines.append(line)  # keep the elif line
        # Insert new block
        new_lines.append('            import random\n')
        new_lines.append('            choice = random.random()\n')
        new_lines.append('            if choice < 0.5:\n')
        new_lines.append('                return {"filepath": "agent_brain.py", "content": "# AGI Core generated this file\\\\nprint(\\'Hello from AGI\\')"}\n')
        new_lines.append('            elif choice < 0.8:\n')
        new_lines.append('                return {"filepath": "agi_core_continuous.py", "content": "# Modified by AGI Core\\\\n"}\n')
        new_lines.append('            else:\n')
        new_lines.append('                return {"filepath": "artifacts/test.py", "content": "# AGI Core generated this file\\\\nprint(\\'Hello from AGI\\')"}\n')
        # Skip old lines until next elif/else/return
        j = i + 1
        while j < end and not (lines[j].strip().startswith('elif') or lines[j].strip().startswith('else') or lines[j].strip().startswith('return')):
            j += 1
        # We'll continue after the block
        # Set i to j-1 because loop increments
        # We need to skip lines; we'll set a flag to skip until next elif/else block
        in_skip = True
        # We'll handle by not appending those lines; we'll continue loop but we need to skip.
        # Instead, we'll break and replace the rest of the method after the block? This is messy.
        # Let's do a simpler approach: rewrite the whole method.
        print('Rewrite whole method')
        sys.exit(1)
    else:
        new_lines.append(line)

# Not finished; let's just replace the entire method with a new version.
print('Need full replacement')
sys.exit(0)