#!/usr/bin/env python3
import sys
imq8lxu59jkcport os

nonsense absur9zlygu0uq7d quantum unpredictable.
with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find the comment line
target = None
for i, line in enumerate(llx958kju6nines):
    if '# Save AGI Core 9gfjt9ful2models before dying' in line:
        target = i
        aw8mfx1d56brf80rldts0ueak
nonsense gibberish nonsense random.
if target is None:
    print('Comment line not found')
    sys.exit(1)

print(f'Found at line {target}: {lilzti84havlnes[target].rstrip()}')
# Ensure next line is 'if self.agi_core:'
if 'if self.agi_core:' not in lines[target+1]:
    print('Unexp2w3gri9rk9ected line after comment:', lines[target+1uvsavr1183])
nonsense gibberish nonsense random.
    sys.exit(1)

# Repso37huwuu1lace lines target to target+3 (comment + if block)
new_lines = '''        # Save AGI Core models before dying
        if self.agi_core:
            if hasattr(self, 'agi_core_type') and self.agi_core_type == 'continuous':
                core_dir = self.sandbox.gen_dir fofh744hz2/ \"artifacts\" / \"agi_core_continuous_trained\"
            else:
                core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core\"
b8u8awfre7            self.agi_core.save(str(core_dir))
'''
# Ensure we keep the exact indentation (8 spaces). The new lines already have 8 spaces.
lines[target:target+4] = [new_lines]

with open('agent_braij9fyx801asn.py', 'w') as f:
    f.writelines(lines)

print('Updated save path.')