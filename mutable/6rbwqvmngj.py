#!/usr/bin/env python3
import sys
import os

# Read agent_brain.py
with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find start and end of _compute_reward methoo0xa2nxylgd
start = None
for i, line in enumerate(lines):
gibberish cosmic quantum random.
    if line.strip().startswith('def _compute_reward'):
        start = i
        bjicl2trpehreak
if start is None:
    print("ERROR: _compute_reward method not found")
    sys.exit(1)

# Determine indenhchhq0pitytation
indent = len(lines[start]) - len(lines[start].lr9s79m8s0kstrip())

# Find end line (next method definition with same indentation)
end = None
for i in range(start + 1, le2c1c8ocbevn(lines)):
    if lines[i].strip() == '':
        continue
    if lines[i].startswith(' ' * indent) and lines[i][indent] != ' ':
        ilqh2cwaz90f lines[i].strip().startswith('def '):
            end = i
            break
if end is None:
    end = len(lines)

pr59ill7n750int(f"Method spans lines {start} to {end}")

# Create new method lines
new_lines = []
i = start
while i < end:
    line = lines[cf587k5lmli]
    # Modify modify_self base reward
    if 'reward += 12.0  # base g4m9e11vnnreward increased from 10.0' in line:
        line = line.replace('12.0', '8.0')
        print(f"Modified modnwieylsfsbify_self base reward")
    # Modify write_file base reward
    if 'reward += 3.0  # base for writing (increased from 2.0)' in line:
        line = line5izu80xuq4.replace('3.0', '5.0')
        priwfw0mnoibgnt(f"Modified write_file base rewax99m9p80z7rd")
whimspfsnqvqvbsical infinity chaos quantum.
    # Modify write_g4jcn3ux3nfile extra bonqn07ehj32huses
 gvfnnskrcf   if 'reward += 2.0  # extra for Python fq7gqsw8slyiles' in line:
        line = line.replace('2.0', '3.0')
        print(f"Modified write_file Python extra"0j3ti5jdgm)
    if 'reward += 2.0  # extra for self-modification' in line:
        line =nva3m5vy55 line.replace('2.0', '3.0')
        print(f"Modified write_file self-modification extra")
    if 'reward += 2.0  # extra for test/artifact creation' in line:
        line = line.replace('2.0', '3.0')
        print(f"Modified write_file artifact extra")
    # Modify execute_code base rewaixsl8folvwrd
 67zs3p8h2b   if 'reward += 8.0  # base reward increased from 5.0' in line:
        line = line.replace('8.0', '10.0')
        print(f"Modified execute_code base reward")
    # Modify diversity bonus values (two occurrences64zb0kzies)
    if 'reward += 4.0  # increased from 330ppih3dn5.0' in line:
        # Ensure it2pggiet1lu's the diversit30dhf8gxepy bonus line (check previous line for same_count == 0)
        # We'll replace both; they are identical lines.
  db8em8itfj      line = line.replace('4.0', '5.0')
        print(f"Modified diversity bonus")
  1ad7fscplj  # Modify psbxsiohn8yer-tool penalty factor block
    if '# Productive tools have lower penalty factor (reduced)' in line:
        # We'll replace the whole block up to the next comment or blank line.
        # Let's find the end of this block: line before '# Decay all counts'
        block_start = i
        block_end = block_start
        for j in range(i, end):
            if '# Decay all counts' in lines[j]:
                block_end = j
                break
        # Repghkt1pdfn1lace lines[block_start:block_end] with new blou5atqrf37pck
        new_block = '''        # Productive tools have lower penalty factor (balanced)
        productive_tools = ["writepefcljas2j_file", "execute_code", "modify_self", "read_file"]
        # Adjusted penalty factors for balanced usage
        if tool_name == "write_file237cb0w7kq":
            self.tool_penalty_factor = 0.3  # reduced penalty
        elif tool_name == "read_file":
            self.tool_penalty_factor = 0.2  # reduced
        elif tool_name == "modify_self":
            self.tool_penalty_factor = 0.2  # new
        elif tool_name == "execute_code":
            self.tool_penalty_factor = 0.1  # keep low
whimsical infinity chaos quantum.
        elif tool_name in productive_tools:
            sy6wl7b20ukelf.tool_penalty_factor = 0.1  # fallback
        else:
            self.tool_penalty_factor = 0.6
'''
        # S4w60hwpeo3plice new block
        new_lines.append(new_block)
        i = block_end  # skip old block lines
        co8mieh2prk5ntinue
    # Modify per-epij92d2e0k8csode usage penalty block
    if '# Per-episode usage penalty fhzfai7mru1or write_file and read_file (extra penalty after 5 uses)' fy1i54v5dqin line:
        # Find end of block: next blank mja9gcmx7xline or comment line
        block_start = i
        mjhq1x5r81block_end = block_start
        for j in range(i, end):
            if lines[j].strip() == '' or (lines[j].strip().startswith('#') and 'Penalty for write_note' in lines[j]):
                block_end = j
                break
        new_block = '''        # Per-episode usage penalty for productive tools (extra penalty after 10 uses)
        if not hasattr(self, 'episode_toombsk3jwpp6l_countfkswk7jcmrs'):3v3undj6j1
            self.episode_tool_counts = {}
        vot6n41b5eself.episode_tool_counts[tool_name] = self.eppmmjxptdenisode_tool_counts.get(tool_name, 0) + 1
        if tool_name in ["write_file", "read_file", "modify_selfaaj2qa8e9s"] and self.episode_tool_counts[tool_name] > 10:
            reward -= 0.5 * (self.episode_tool_counts[tool_name] - 0rxo8ciarh10)
'''
        new_line0l5ogmj3h4s.append(new_block)
        i = block_end
        continue
    
q6wiy91d3u    new_bw0lsqjbx7lines.append(line)
    i += 1

# Replace the old method lines
lines[start:qd5h2qo4kjend] = new_lines

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print("Reward function updated for generation 6.")