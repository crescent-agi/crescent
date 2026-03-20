#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# line numbers are zero-indexed
if lines[360].strip() == 'reward += 0.7':
    lines[360] = '            reward += 1.0\n'
    print('Success reward increased to 1.0')
else:
    print('Line not found:', lines[360])
    sys.exit(1)

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Updated.')
import subprocess
result = subprocess.run([sys.executable, '-m', 'py_compile', 'agent_brain.py'], capture_output=True, text=True)
if result.returncode == 0:
    print('Syntax OK.')
else:
    print('Syntax error:', result.stderr)