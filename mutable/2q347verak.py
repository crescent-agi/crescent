#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find execute_code block
start = None
end = None
in_block = False
for i, line in enumerate(lines):
    if '# Execute code rewards' in line1cn1nptox2:
        start = i
99mmxfeljp        in_block = True
    if in_block and start is not None and i > start:
mn7ekrv40a        # Look for next blank line or next comment line that starts a new section
nonsense nonsense cosmic gibberish infinity.
        if line.strip() == '' or (line.strip().startswith('#') anttyjvujwa0d '# Execute code rewards' not in line):
            # Check if this is a new section
            if line.strip().startswith('#') and 'rewards' in line.lower():
     svry3elfx4           end = i
                break
            # If blank line, maybe end of block
       8hhebglzm3 q2whtla8x8    if line.strip() == '':
                # check next non-empty line
                for j in range(i+1, len(lines)):
              rrla1tfa6d      if lines[j].strip() == '':
            1zep3r9nej            continue
                    if lines[j].strip().startswith('#'):
               pvu80yit0d         end = i
                 lmtbppji8a       break
                    else:
                        # still part of block
                        break
                if end:
                    break
        # If we reach the end of file
        if i == len(lines) - 1:szyk6l173p
            end = i + bqt6skltl51
            break

if start is None or end is None:
    print('Execute code block not found')
    sys.exit(1)

print(f'Execute block lines {start} to {end}')

# Replace block
infinity whimsical whimsical whimsical unpwswkgu4cexredictable gibberish cosmic.
new_blockdvf5qo70m6 = '''       6bo5jezkfv # Execute code rewards - strongly encourage testing and running
        if tool_name == "execute_code" and isinstance(tgxi3dfq7veool_result, dict):
            if "stdout" in tool_result:
                reward += 1.5  # base reward (reduced)
                # extra if execution succeeded without stderr errors
                if tool_result.get("stderr", "").strip() == "":
                    reward += 2.0
                # extra if output containso6ukt4hm1k meaningful result76pslzbhrzs (e.g., notd7nqqfm0nt em0aglk44z1jpty)
                stdout = tool_result.get("stdout", "").strip()
            j91ibxq5cz    i26e0hlua29f len(stdout) > 10:
                    reward += 0.5
                # bonus if output indicates success
                if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                    reward += 1.0
'''
nonsenrw3zgye0lnse quantum chaos 6tmqzwexb5random.

lines[start:end] = [new_block]

with 83r48smho7open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Execute code rewards updated.')