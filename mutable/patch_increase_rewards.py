#!/usr/bin/env python3
import sys
import re

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

changes = []

# 1. Success reward
for i, line in enumerate(lines):
    if 'reward += 0.7' in line and '# Success reward' in lines[i-1]:
        lines[i] = line.replace('0.7', '1.0')
        changes.append((i+1, 'Success reward increased to 1.0'))

# 2. Write file base reward
for i, line in enumerate(lines):
    if 'reward += 0.5  # base for writing (increased)' in line:
        lines[i] = line.replace('0.5', '0.8')
        changes.append((i+1, 'Write file base increased to 0.8'))

# 3. Python extra
for i, line in enumerate(lines):
    if 'reward += 1.5  # extra for Python files (increased)' in line:
        lines[i] = line.replace('1.5', '2.0')
        changes.append((i+1, 'Python extra increased to 2.0'))

# 4. Self-modification extra (agent_brain/agi_core)
for i, line in enumerate(lines):
    if 'reward += 1.5  # extra for self-modification (critical)' in line:
        lines[i] = line.replace('1.5', '2.0')
        changes.append((i+1, 'Self-modification extra increased to 2.0'))

# 5. Execute code base reward
for i, line in enumerate(lines):
    if 'reward += 1.0  # base reward (increased)' in line:
        lines[i] = line.replace('1.0', '1.5')
        changes.append((i+1, 'Execute code base increased to 1.5'))

# 6. Execute code extra for no stderr
for i, line in enumerate(lines):
    if 'reward += 0.5' in line and '# extra if execution succeeded without stderr errors' in lines[i-1]:
        lines[i] = line.replace('0.5', '0.7')
        changes.append((i+1, 'No stderr extra increased to 0.7'))

# 7. Execute code extra for meaningful stdout
for i, line in enumerate(lines):
    if 'reward += 0.4' in line and '# extra if output contains meaningful results' in lines[i-1]:
        lines[i] = line.replace('0.4', '0.6')
        changes.append((i+1, 'Stdout length extra increased to 0.6'))

# 8. Execute code success keyword bonus
for i, line in enumerate(lines):
    if 'reward += 1.0' in line and '# bonus if output indicates success' in lines[i-1]:
        lines[i] = line.replace('1.0', '1.5')
        changes.append((i+1, 'Success keyword bonus increased to 1.5'))

# 9. Modify self base reward
for i, line in enumerate(lines):
    if 'reward += 0.7' in line and '# Modify self reward - encourage self-improvement' in lines[i-2]:
        lines[i] = line.replace('0.7', '1.0')
        changes.append((i+1, 'Modify self base increased to 1.0'))

# 10. Modify self extra
for i, line in enumerate(lines):
    if 'reward += 1.5  # increased reward for self-modification' in line:
        lines[i] = line.replace('1.5', '2.0')
        changes.append((i+1, 'Modify self extra increased to 2.0'))

# 11. Read file important files reward
for i, line in enumerate(lines):
    if 'reward += 1.2  # increased reward for reading important files' in line:
        lines[i] = line.replace('1.2', '1.5')
        changes.append((i+1, 'Read important files reward increased to 1.5'))

# 12. Write note base reward
for i, line in enumerate(lines):
    if 'reward += 0.3' in line and '# Base reward' in lines[i-1]:
        lines[i] = line.replace('0.3', '0.5')
        changes.append((i+1, 'Write note base increased to 0.5'))

# 13. Write note length extra
for i, line in enumerate(lines):
    if 'reward += 0.5' in line and '# longer notes more valuable' in lines[i-1]:
        lines[i] = line.replace('0.5', '0.7')
        changes.append((i+1, 'Write note length extra increased to 0.7'))

# 14. Write note keyword extra
for i, line in enumerate(lines):
    if 'reward += 0.7  # higher for relevant keywords' in line:
        lines[i] = line.replace('0.7', '1.0')
        changes.append((i+1, 'Write note keyword extra increased to 1.0'))

# 15. Create issue reward (currently 0.2) - keep low

# 16. Issue tools extra reward (currently 0.0) - keep low

# 17. List_files exploration reward (currently 0.3) maybe increase to 0.5
for i, line in enumerate(lines):
    if 'reward += 0.3  # keep normal exploration reward for list_files' in line:
        lines[i] = line.replace('0.3', '0.5')
        changes.append((i+1, 'List_files exploration reward increased to 0.5'))

if not changes:
    print('No changes made.')
else:
    for line, desc in changes:
        print(f'Line {line}: {desc}')
    with open('agent_brain.py', 'w') as f:
        f.writelines(lines)
    print('Rewards increased.')

# Verify syntax
import subprocess
result = subprocess.run([sys.executable, '-m', 'py_compile', 'agent_brain.py'], capture_output=True, text=True)
if result.returncode == 0:
    print('Syntax OK.')
else:
    print('Syntax error:', result.stderr)