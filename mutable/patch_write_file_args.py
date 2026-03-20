#!/usr/bin/env python3
import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

# Find the write_file block
for i, line in enumerate(lines):
    if line.strip() == \"elif tool_name == \"write_file\":\":
        # Find the return line (should be indented)
        for j in range(i+1, len(lines)):
            if lines[j].strip().startswith('return'):
                # Replace the whole block from i to j inclusive
                new_block = '''        elif tool_name == \"write_file\":\n            # Randomly choose a useful file to write\n            import random\n            choice = random.random()\n            if choice < 0.3:\n                return {\"filepath\": \"artifacts/test.py\", \"content\": \"# AGI Core generated this file\\nprint('Hello from AGI')\"}\n            elif choice < 0.6:\n                return {\"filepath\": \"agent_brain.py\", \"content\": \"# Modified by AGI Core\\n\"}\n            else:\n                return {\"filepath\": \"artifacts/note.txt\", \"content\": \"AGI core wrote this.\"}\n'''
                lines[i] = new_block
                # Delete old return line and maybe other lines until next elif/else
                # We'll just replace the block from i to j, but we need to keep indentation.
                # Simpler: replace lines[i:j+1] with new_block lines split
                # Let's compute end index: find next line with same indentation as elif (i.e., start of next tool)
                start_indent = len(lines[i]) - len(lines[i].lstrip())
                for k in range(i+1, len(lines)):
                    if lines[k].strip() == '':
                        continue
                    if len(lines[k]) - len(lines[k].lstrip()) <= start_indent:
                        end = k
                        break
                else:
                    end = len(lines)
                # Replace slice
                lines[i:end] = new_block.splitlines(keepends=True)
                print(f'Replaced write_file block at line {i+1}')
                break
        break

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)

print('Updated generate_arguments for write_file.')