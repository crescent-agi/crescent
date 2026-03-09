#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# line numbers are 1-indexed
# line 417: extra if execution succeeded without stderr errors
if 'reward += 0.5' in lines[416] and '# extra if execution succeeded without stderr errors' in lines[415]:
    lines[416] = lines[416].replace('0.5', '0.7')
    print('Line 417: no stderr extra increased to 0.7')
else:
    print('Line 417 pattern mismatch:', lines[416])

# line 421: extra if output contains meaningful results
if 'reward += 0.4' in lines[420] and '# extra if output contains meaningful results' in lines[419]:
    lines[420] = lines[420].replace('0.4', '0.6')
    print('Line 421: stdout length extra increased to 0.6')
else:
    print('Line 421 pattern mismatch:', lines[420])

# line 424: bonus if output indicates success
if 'reward += 1.0' in lines[423] and '# bonus if output indicates success' in lines[422]:
    lines[423] = lines[423].replace('1.0', '1.5')
    print('Line 424: success keyword bonus increased to 1.5')
else:
    print('Line 424 pattern mismatch:', lines[423])

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Updated.')
import subprocess
result = subprocess.run([sys.executable, '-m', 'py_compile', 'agent_brain.py'], capture_output=True, text=True)
if result.returncode == 0:
    print('Syntax OK.')
else:
    print('Syntax error:', result.stderr)