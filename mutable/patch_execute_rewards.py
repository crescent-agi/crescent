#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find execute_code block
start = None
end = None
in_block = False
for i, line in enumerate(lines):
    if '# Execute code rewards' in line:
        start = i
        in_block = True
    if in_block and start is not None and i > start:
        # Look for next blank line or next comment line that starts a new section
        if line.strip() == '' or (line.strip().startswith('#') and '# Execute code rewards' not in line):
            # Check if this is a new section
            if line.strip().startswith('#') and 'rewards' in line.lower():
                end = i
                break
            # If blank line, maybe end of block
            if line.strip() == '':
                # check next non-empty line
                for j in range(i+1, len(lines)):
                    if lines[j].strip() == '':
                        continue
                    if lines[j].strip().startswith('#'):
                        end = i
                        break
                    else:
                        # still part of block
                        break
                if end:
                    break
        # If we reach the end of file
        if i == len(lines) - 1:
            end = i + 1
            break

if start is None or end is None:
    print('Execute code block not found')
    sys.exit(1)

print(f'Execute block lines {start} to {end}')

# Replace block
new_block = '''        # Execute code rewards - strongly encourage testing and running
        if tool_name == "execute_code" and isinstance(tool_result, dict):
            if "stdout" in tool_result:
                reward += 1.5  # base reward (reduced)
                # extra if execution succeeded without stderr errors
                if tool_result.get("stderr", "").strip() == "":
                    reward += 2.0
                # extra if output contains meaningful results (e.g., not empty)
                stdout = tool_result.get("stdout", "").strip()
                if len(stdout) > 10:
                    reward += 0.5
                # bonus if output indicates success
                if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                    reward += 1.0
'''

lines[start:end] = [new_block]

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Execute code rewards updated.')