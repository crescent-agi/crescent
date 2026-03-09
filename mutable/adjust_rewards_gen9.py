#!/usr/bin/env python3
"""
Adjust reward parameters for Generation 9.
Goal: increase average reward while preserving balanced productive tool usage.
Changes:
1. Increase success reward from 6.0 → 8.0
2. Reduce per-tool penalty factors:
   write_file 0.5, read_file 0.3, modify_self 0.2, execute_code 0.1
3. Fix per-episode penalty bug for write_file and read_file (change subtract -10 to -5)
   and increase thresholds from 5 to 10 for write_file and read_file.
4. Increase threshold for execute_code from 5 to 10.
5. Add small positive baseline reward for productive tools (+1.0).
"""

import re

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def modify_compute_reward(content):
    # 1. Change success reward from 6.0 to 8.0
    content = re.sub(r'reward \+= 6\.0  # increased from 3\.0 \(issue #24\)',
                     'reward += 8.0  # increased from 6.0 (issue #25)', content)
    
    # 2. Change per-tool penalty factors
    # write_file factor
    content = re.sub(r'if tool_name == "write_file":\s*self\.tool_penalty_factor = 0\.6',
                     'if tool_name == "write_file":\n            self.tool_penalty_factor = 0.5', content)
    # read_file factor
    content = re.sub(r'elif tool_name == "read_file":\s*self\.tool_penalty_factor = 0\.4',
                     'elif tool_name == "read_file":\n            self.tool_penalty_factor = 0.3', content)
    # modify_self factor
    content = re.sub(r'elif tool_name == "modify_self":\s*self\.tool_penalty_factor = 0\.3',
                     'elif tool_name == "modify_self":\n            self.tool_penalty_factor = 0.2', content)
    # execute_code factor
    content = re.sub(r'elif tool_name == "execute_code":\s*self\.tool_penalty_factor = 0\.2',
                     'elif tool_name == "execute_code":\n            self.tool_penalty_factor = 0.1', content)
    
    # 3. Fix per-episode penalty bug and increase thresholds
    # Write file penalty block
    content = re.sub(r'# Write file: penalty after 10 uses \(factor 1\.0\)\s*\n\s*if tool_name == "write_file" and self\.episode_tool_counts\[tool_name\] > 5:\s*\n\s*reward -= 1\.0 \* \(self\.episode_tool_counts\[tool_name\] - 10\)',
                     '# Write file: penalty after 10 uses (factor 1.0)\n        if tool_name == "write_file" and self.episode_tool_counts[tool_name] > 10:\n            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 10)', content)
    # Read file penalty block
    content = re.sub(r'# Read file: penalty after 10 uses \(factor 1\.0\)\s*\n\s*if tool_name == "read_file" and self\.episode_tool_counts\[tool_name\] > 5:\s*\n\s*reward -= 1\.0 \* \(self\.episode_tool_counts\[tool_name\] - 10\)',
                     '# Read file: penalty after 10 uses (factor 1.0)\n        if tool_name == "read_file" and self.episode_tool_counts[tool_name] > 10:\n            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 10)', content)
    # Execute code penalty block: increase threshold from 5 to 10
    content = re.sub(r'# Execute code: penalty after 5 uses \(factor 1\.0\) as per issue #23\s*\n\s*if tool_name == "execute_code" and self\.episode_tool_counts\[tool_name\] > 5:\s*\n\s*reward -= 1\.0 \* \(self\.episode_tool_counts\[tool_name\] - 5\)',
                     '# Execute code: penalty after 10 uses (factor 1.0) as per issue #25\n        if tool_name == "execute_code" and self.episode_tool_counts[tool_name] > 10:\n            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 10)', content)
    
    # 4. Add baseline reward for productive tools after success reward
    # Find line after success reward addition and before recency penalty
    # We'll insert after the line "reward += 8.0 ..." but before the blank line? Let's do a more robust replacement.
    # Let's locate the block after success reward and before recency penalty.
    # We'll insert a new line: "if tool_name in productive_tools: reward += 1.0"
    # We'll replace the line "reward += 8.0 ..." with itself plus new line.
    # Use a more complex regex to capture the whole line and replace.
    # We'll do two-step: first find the line, then insert after.
    lines = content.split('\n')
    in_method = False
    for i, line in enumerate(lines):
        if line.strip().startswith('def _compute_reward'):
            in_method = True
        if in_method and line.strip().startswith('reward += 8.0'):
            # Insert after this line
            lines.insert(i+1, '            # Baseline reward for productive tools')
            lines.insert(i+2, '            if tool_name in productive_tools:')
            lines.insert(i+3, '                reward += 1.0')
            break
    content = '\n'.join(lines)
    
    return content

def main():
    path = 'agent_brain.py'
    backup = path + '.backup_gen9'
    print(f'Reading {path}...')
    content = read_file(path)
    print('Creating backup...')
    write_file(backup, content)
    print('Modifying compute_reward method...')
    new_content = modify_compute_reward(content)
    print('Writing modified file...')
    write_file(path, new_content)
    print('Done.')

if __name__ == '__main__':
    main()