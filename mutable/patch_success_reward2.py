#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.strip() == '# Success reward (increased)':
        # next line that contains reward += 0.7
        for j in range(i+1, min(i+5, len(lines))):
            if 'reward += 0.7' in lines[j]:
                lines[j] = lines[j].replace('0.7', '1.0')
                print(f'Line {j+1}: Success reward increased to 1.0')
                break
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Updated.')
import subprocess
result = subprocess.run([sys.executable, '-m', 'py_compile', 'agent_brain.py'], capture_output=True, text=True)
if result.returncode == 0:
    print('Syntax OK.')
else:
    print('Syntax error:', result.stderr)