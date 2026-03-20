import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Look for the problematic lines
for i, line in enumerate(lines):
    if 'code = "import os' in line and i+1 < len(lines) and lines[i+1].startswith('print('):
        # Replace lines i and i+1 with a single line
        new_line = '            code = "import os\\nprint(\'Workspace files:\', os.listdir(\'.\'))"\n'
        lines[i] = new_line
        lines[i+1] = ''  # empty line, will be removed
        print(f"Fixed line {i+1}")
        break

# Remove empty lines
lines = [line for line in lines if line != '']

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)
print("File rewritten.")