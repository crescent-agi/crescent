#!/usr/bin/env python3
import sys
import os

# Read agent_brain.py
with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find start and end of _compute_reward method
start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        start = i
        break
if start is None:
    print("ERROR: _compute_reward method not found")
    sys.exit(1)

# Determine indentation
indent = len(lines[start]) - len(lines[start].lstrip())

# Find end line (next method definition with same indentation)
end = None
for i in range(start + 1, len(lines)):
    if lines[i].strip() == '':
        continue
    if lines[i].startswith(' ' * indent) and lines[i][indent] != ' ':
        if lines[i].strip().startswith('def '):
            end = i
            break
if end is None:
    end = len(lines)

print(f"Method spans lines {start} to {end}")

# Create new method lines
new_lines = []
i = start
while i < end:
    line = lines[i]
    # Modify modify_self base reward
    if 'reward += 12.0  # base reward increased from 10.0' in line:
        line = line.replace('12.0', '8.0')
        print(f"Modified modify_self base reward")
    # Modify write_file base reward
    if 'reward += 3.0  # base for writing (increased from 2.0)' in line:
        line = line.replace('3.0', '5.0')
        print(f"Modified write_file base reward")
    # Modify write_file extra bonuses
    if 'reward += 2.0  # extra for Python files' in line:
        line = line.replace('2.0', '3.0')
        print(f"Modified write_file Python extra")
    if 'reward += 2.0  # extra for self-modification' in line:
        line = line.replace('2.0', '3.0')
        print(f"Modified write_file self-modification extra")
    if 'reward += 2.0  # extra for test/artifact creation' in line:
        line = line.replace('2.0', '3.0')
        print(f"Modified write_file artifact extra")
    # Modify execute_code base reward
    if 'reward += 8.0  # base reward increased from 5.0' in line:
        line = line.replace('8.0', '10.0')
        print(f"Modified execute_code base reward")
    # Modify diversity bonus values (two occurrences)
    if 'reward += 4.0  # increased from 3.0' in line:
        # Ensure it's the diversity bonus line (check previous line for same_count == 0)
        # We'll replace both; they are identical lines.
        line = line.replace('4.0', '5.0')
        print(f"Modified diversity bonus")
    # Modify per-tool penalty factor block
    if '# Productive tools have lower penalty factor (reduced)' in line:
        # We'll replace the whole block up to the next comment or blank line.
        # Let's find the end of this block: line before '# Decay all counts'
        block_start = i
        block_end = block_start
        for j in range(i, end):
            if '# Decay all counts' in lines[j]:
                block_end = j
                break
        # Replace lines[block_start:block_end] with new block
        new_block = '''        # Productive tools have lower penalty factor (balanced)
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
        # Adjusted penalty factors for balanced usage
        if tool_name == "write_file":
            self.tool_penalty_factor = 0.3  # reduced penalty
        elif tool_name == "read_file":
            self.tool_penalty_factor = 0.2  # reduced
        elif tool_name == "modify_self":
            self.tool_penalty_factor = 0.2  # new
        elif tool_name == "execute_code":
            self.tool_penalty_factor = 0.1  # keep low
        elif tool_name in productive_tools:
            self.tool_penalty_factor = 0.1  # fallback
        else:
            self.tool_penalty_factor = 0.6
'''
        # Splice new block
        new_lines.append(new_block)
        i = block_end  # skip old block lines
        continue
    # Modify per-episode usage penalty block
    if '# Per-episode usage penalty for write_file and read_file (extra penalty after 5 uses)' in line:
        # Find end of block: next blank line or comment line
        block_start = i
        block_end = block_start
        for j in range(i, end):
            if lines[j].strip() == '' or (lines[j].strip().startswith('#') and 'Penalty for write_note' in lines[j]):
                block_end = j
                break
        new_block = '''        # Per-episode usage penalty for productive tools (extra penalty after 10 uses)
        if not hasattr(self, 'episode_tool_counts'):
            self.episode_tool_counts = {}
        self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
        if tool_name in ["write_file", "read_file", "modify_self"] and self.episode_tool_counts[tool_name] > 10:
            reward -= 0.5 * (self.episode_tool_counts[tool_name] - 10)
'''
        new_lines.append(new_block)
        i = block_end
        continue
    
    new_lines.append(line)
    i += 1

# Replace the old method lines
lines[start:end] = new_lines

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print("Reward function updated for generation 6.")