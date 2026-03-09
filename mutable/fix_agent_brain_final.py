#!/usr/bin/env python3
"""
Create final agent_brain.py by merging backup structure with updated reward function.
"""
import sys
import re

# Read backup template
with open('agent_brain.py.backup_gen1_v2', 'r') as f:
    template = f.read()

# Read current broken file to extract reward method
with open('agent_brain.py', 'r') as f:
    current = f.read()

# Find reward method in current (look for "def _compute_reward")
lines = current.splitlines()
reward_start = None
reward_end = None
in_method = False
indent = None
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        reward_start = i
        in_method = True
        # determine indentation of method body
        # find next non-empty line after def
        for j in range(i+1, len(lines)):
            if lines[j].strip():
                indent = len(lines[j]) - len(lines[j].lstrip())
                break
        continue
    if in_method:
        # Check if line is empty or indentation less than method indent (i.e., end of method)
        if line.strip() == '':
            continue
        if len(line) - len(line.lstrip()) < indent:
            reward_end = i
            break
if reward_end is None:
    reward_end = len(lines)

if reward_start is not None:
    reward_lines = lines[reward_start:reward_end]
    reward_method = '\n'.join(reward_lines)
    print(f'Found reward method lines {reward_start+1} to {reward_end}')
else:
    print('ERROR: Could not find reward method in current file')
    sys.exit(1)

# Now find reward method in template and replace
template_lines = template.splitlines()
t_start = None
t_end = None
t_indent = None
for i, line in enumerate(template_lines):
    if line.strip().startswith('def _compute_reward'):
        t_start = i
        # find indent
        for j in range(i+1, len(template_lines)):
            if template_lines[j].strip():
                t_indent = len(template_lines[j]) - len(template_lines[j].lstrip())
                break
        continue
    if t_start is not None and t_end is None:
        if line.strip() == '':
            continue
        if len(line) - len(line.lstrip()) < t_indent:
            t_end = i
            break
if t_end is None:
    t_end = len(template_lines)

if t_start is not None:
    # Replace the block
    new_template_lines = template_lines[:t_start] + reward_lines + template_lines[t_end:]
    print(f'Replaced reward method in template')
else:
    print('ERROR: Could not find reward method in template')
    sys.exit(1)

new_content = '\n'.join(new_template_lines)

# Additional fixes:
# 1. Change feature_dim=15 to feature_dim=30
new_content = new_content.replace('feature_dim=15', 'feature_dim=30')
# 2. Change load directory from "agi_core_continuous" to "agi_core_continuous_trained"
new_content = new_content.replace('core_dir_name = "agi_core_continuous"', 'core_dir_name = "agi_core_continuous_trained"')
# 3. Change save directory similarly (already uses core_dir_name)
# 4. Add missing import for deque if not present (should be already)
# 5. Ensure self.agi_core_type is set (already)
# 6. Update exploration parameters? Not needed, they are passed in train_continuous simulation, not runtime.
#    But we can add exploration_rate, epsilon_decay, epsilon_min to the AGICoreContinuous constructor.
#    Look for line: self.agi_core = AGICORE_CLASS(feature_dim=30, hidden_size=32, learning_rate=0.01, use_features=True)
#    Replace with appropriate parameters.
# Let's find that line.
lines = new_content.splitlines()
for i, line in enumerate(lines):
    if 'AGICORE_CLASS(feature_dim=30' in line and 'use_features=True' in line:
        # Replace with our desired parameters
        new_line = '                    self.agi_core = AGICORE_CLASS(feature_dim=30, hidden_size=32, learning_rate=0.01, exploration_rate=0.02, epsilon_decay=0.998, epsilon_min=0.005, use_features=True)'
        lines[i] = new_line
        print('Updated AGICoreContinuous constructor')
        break
new_content = '\n'.join(lines)

# Write final file
with open('agent_brain.py', 'w') as f:
    f.write(new_content)
print('Final agent_brain.py written.')

# Quick sanity checks
if 'AGICoreContinuous' in new_content:
    print('✓ AGICoreContinuous import present')
if 'feature_dim=30' in new_content:
    print('✓ feature_dim=30')
if 'core_dir_name = "agi_core_continuous_trained"' in new_content:
    print('✓ correct load directory')
if 'def _compute_reward' in new_content:
    print('✓ reward method present')
if 'return -500.0' in new_content:
    print('✓ death penalty -500')
print('All done.')