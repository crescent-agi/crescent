#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find the start of the duplicate save block
# We'll replace lines 339 to 349 (0-indexed)
# Actually need to find exact pattern. Let's search for '# Save AGI Core models before dying'
start = None
for i, line in enumerate(lines):
    if line.strip() == '# Save AGI Core models before dying':
        start = i
        break
if start is None:
    print('Could not find start line')
    sys.exit(1)

# Find the line after the duplicate block (the line with 'if self.state_path.exists():')
# We'll look for the line containing 'if self.state_path.exists():' after start
end = None
for i in range(start, len(lines)):
    if 'if self.state_path.exists():' in lines[i]:
        end = i
        break
if end is None:
    print('Could not find end line')
    sys.exit(1)

print(f'Found block from line {start+1} to {end+1}')
for i in range(start, end):
    print(f'{i+1}: {lines[i].rstrip()}')

# Build replacement lines
new_lines = [
    '        # Save AGI Core models before dying\n',
    '        if self.agi_core:\n',
    '            core_dir_name = "agi_core_continuous_trained" if self.agi_core_type == \'continuous\' else "agi_core"\n',
    '            core_dir = self.sandbox.gen_dir / "artifacts" / core_dir_name\n',
    '            self.agi_core.save(str(core_dir))\n'
]

# Replace lines[start:end] with new_lines
lines[start:end] = new_lines

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Duplicate save block fixed.')