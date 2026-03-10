import sys
sys.path.insert(0, '.')
with open('agent_brain.py', 'r') as f:
    lines = f.readlines()
start = -1
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        start = i
        break
if start == -1:
    print('not found')
    sys.exit(1)
# find the end of the function (next line with same indent as def)
def_indent = len(lines[start]) - len(lines[start].lstrip())
end = start + 1
while end < len(lines):
    if lines[end].strip() == '':
        end += 1
        continue
    indent = len(lines[end]) - len(lines[end].lstrip())
    if indent <= def_indent and not lines[end].startswith(' ' * (def_indent)):
        # function ended
        break
    end += 1
# include the line before break
function_lines = lines[start:end]
print('Extracted lines:', len(function_lines))
# Write to a new file as a standalone function
with open('new_reward_gen21.py', 'w') as out:
    out.write('#!/usr/bin/env python3\n')
    out.write('\"\"\"Reward function for Generation 21 balancing.\"\"\"\n')
    out.write('def compute_reward_gen21(self, tool_name, tool_args, tool_result):\n')
    # skip the first line (def) and adjust indent
    for line in function_lines[1:]:
        out.write(line)
print('Written to new_reward_gen21.py')