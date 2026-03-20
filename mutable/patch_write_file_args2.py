#!/usr/bin/env python3
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# line numbers are 1-indexed
elif_line = 195
return_line = 196

new_block = '''        elif tool_name == \"write_file\":\n            import random\n            choice = random.random()\n            if choice < 0.3:\n                return {\"filepath\": \"artifacts/test.py\", \"content\": \"# AGI Core generated this file\\\\nprint('Hello from AGI')\"}\n            elif choice < 0.6:\n                return {\"filepath\": \"agent_brain.py\", \"content\": \"# Modified by AGI Core\\\\n\"}\n            else:\n                return {\"filepath\": \"artifacts/note.txt\", \"content\": \"AGI core wrote this.\"}\n'''

# Replace lines 195-196 with new_block lines
lines[elif_line-1:return_line] = new_block.splitlines(keepends=True)

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print('Updated write_file arguments.')