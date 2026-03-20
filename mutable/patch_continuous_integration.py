#!/usr/bin/env python3
"""
Patch agent_brain.py to import and use AGICoreContinuous instead of discrete AGICore.
"""
import sys

path = 'agent_brain.py'
with open(path, 'r') as f:
    lines = f.readlines()

# 1. Replace import block
new_imports = []
for i, line in enumerate(lines):
    if line.strip().startswith('# Try to import AGI Core'):
        # Keep the comment lines but replace the import
        # Find the try block lines
        j = i
        while j < len(lines) and not lines[j].strip().startswith('try:'):
            j += 1
        if j < len(lines):
            # Replace from line i to line where 'AGI_CORE_AVAILABLE = False' appears
            # We'll just replace the whole block with new block
            pass
        break

# Simpler: replace the whole import block with new one
content = ''.join(lines)

old_import_block = '''# Try to import AGI Core
try:
    from agi_core import AGICore
    AGI_CORE_AVAILABLE = True
except ImportError:
    AGICORE = None
    AGI_CORE_AVAILABLE = False'''

new_import_block = '''# Try to import AGI Core Continuous
try:
    from agi_core_continuous import AGICoreContinuous
    AGICORE_CLASS = AGICoreContinuous
    AGI_CORE_AVAILABLE = True
except ImportError:
    AGICORE_CLASS = None
    AGI_CORE_AVAILABLE = False'''

if old_import_block in content:
    content = content.replace(old_import_block, new_import_block)
    print('Replaced import block')
else:
    print('Old import block not found, attempting alternative detection')
    # Try to find lines with 'from agi_core import'
    import re
    content = re.sub(r'from agi_core import AGICore', 'from agi_core_continuous import AGICoreContinuous', content)
    content = re.sub(r'AGICore', 'AGICORE_CLASS', content)
    print('Replaced import via regex')

# 2. Replace initialization block
# Look for line: self.agi_core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
# Replace with continuous initialization
old_init = 'self.agi_core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)'
new_init = '''                self.agi_core = AGICORE_CLASS(feature_dim=30, hidden_size=32, learning_rate=0.01,
                                     exploration_rate=0.02, epsilon_decay=0.998, epsilon_min=0.005,
                                     use_features=True)
                self.agi_core_type = 'continuous\''''
if old_init in content:
    content = content.replace(old_init, new_init)
    print('Replaced initialization line')
else:
    # Maybe the line is split
    # Search for self.agi_core = AGICore
    import re
    content = re.sub(r'self\.agi_core = AGICore\(state_size=100, hidden_size=32, learning_rate=0.01\)',
                     '''self.agi_core = AGICORE_CLASS(feature_dim=30, hidden_size=32, learning_rate=0.01,
                                     exploration_rate=0.02, epsilon_decay=0.998, epsilon_min=0.005,
                                     use_features=True)
                self.agi_core_type = 'continuous\'''', content)
    print('Replaced initialization via regex')

# 3. Update load path from 'agi_core' to 'agi_core_continuous_trained'
old_core_dir = "core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core\""
new_core_dir = '''            core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core_continuous_trained\"
            if not core_dir.exists():
                core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core\"  # fallback'''
if old_core_dir in content:
    content = content.replace(old_core_dir, new_core_dir)
    print('Replaced core_dir path')
else:
    # Try to find line with 'agi_core' directory
    import re
    content = re.sub(r'core_dir = self\.sandbox\.gen_dir / \"artifacts\" / \"agi_core\"',
                     '''            core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core_continuous_trained\"
            if not core_dir.exists():
                core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core\"  # fallback''', content)
    print('Replaced core_dir via regex')

# 4. Also update save path (same line appears later)
# Look for line with 'core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core\"' again
# We'll replace all occurrences with a conditional
lines = content.splitlines(keepends=True)
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if 'core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core\"' in line and 'if core_dir.exists()' not in lines[i-1] and 'fallback' not in lines[i+1]:
        # This is a save path, we want to save to continuous trained directory
        new_lines.append('            core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core_continuous_trained\"\n')
    else:
        new_lines.append(line)
    i += 1
content = ''.join(new_lines)

# Write back
with open(path, 'w') as f:
    f.write(content)
print('Patched agent_brain.py for continuous integration')

# Quick validation: check if AGICORE_CLASS appears
with open(path, 'r') as f:
    text = f.read()
    if 'AGICORE_CLASS' in text:
        print('✓ AGICORE_CLASS found')
    if 'AGICoreContinuous' in text:
        print('✓ AGICoreContinuous import found')
    if 'self.agi_core_type' in text:
        print('✓ agi_core_type attribute added')
    if 'feature_dim=30' in text:
        print('✓ feature_dim set to 30')
    print('Patch complete.')