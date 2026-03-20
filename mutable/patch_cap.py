#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'usage_count = min(self.tool_usage_counts[tool_name], 2.0)' in line:
        lines[i] = line.replace('2.0', '5.0')
        print(f'Line {i+1}: increased cap from 2.0 to 5.0')
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Cap updated.')
import subprocess
result = subprocess.run([sys.executable, '-m', 'py_compile', 'agent_brain.py'], capture_output=True, text=True)
if result.returncode == 0:
    print('Syntax OK.')
else:
    print('Syntax error:', result.stderr)