#!/usr/bin/env python3
import sys
import re

def extract_method(lines):
    """Return (start, end) indices of _compute_reward method."""
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith('def _compute_reward'):
            start = i
            break
    if start is None:
        raise ValueError('Method not found')
    # find method end: next line with same indentation that starts with 'def ' or end of file
    indent = len(lines[start]) - len(lines[start].lstrip())
    end = start + 1
    while end < len(lines):
        if lines[end].strip() == '':
            end += 1
            continue
        if len(lines[end]) - len(lines[end].lstrip()) == indent and lines[end].lstrip().startswith('def '):
            break
        end += 1
    return start, end

def modify_method(text):
    """Apply modifications to method text."""
    lines = text.splitlines(keepends=True)
    # 1. Add early penalty for issue tools (after death penalty)
    # Find line after death penalty check
    for i, line in enumerate(lines):
        if 'return -500.0  # heavily penalize suicide' in line:
            # Insert after this line
            indent = len(line) - len(line.lstrip())
            new_line = ' ' * indent + '# Issue tools penalty (strongly discourage)\n'
            new_line += ' ' * indent + 'issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]\n'
            new_line += ' ' * indent + 'if tool_name in issue_tools:\n'
            new_line += ' ' * indent + '    return -50.0  # heavy penalty, no other rewards\n'
            lines.insert(i + 1, new_line)
            break
    
    # 2. Change execute_code success extra from 6.0 to 3.0
    for i, line in enumerate(lines):
        if 'reward += 6.0' in line and 'extra if execution succeeded without stderr errors' in lines[i-1]:
            lines[i] = line.replace('6.0', '3.0')
            break
    
    # 3. Change write_file base from 4.0 to 6.0
    for i, line in enumerate(lines):
        if 'reward += 4.0  # base for writing (reduced)' in line:
            lines[i] = line.replace('4.0', '6.0')
            break
    
    # 4. Change modify_self base from 5.0 to 7.0
    for i, line in enumerate(lines):
        if 'reward += 5.0  # base reward (increased)' in line and 'modify_self' in lines[i-1]:
            lines[i] = line.replace('5.0', '7.0')
            break
    
    # 5. Change read_file important reward from 3.0 to 6.0
    for i, line in enumerate(lines):
        if 'reward += 3.0  # reward for reading important files' in line:
            lines[i] = line.replace('3.0', '6.0')
            break
    
    # 6. Increase penalty for write_note from -2.0 to -3.0
    for i, line in enumerate(lines):
        if 'reward -= 2.0' in line and 'write_note' in lines[i-1]:
            lines[i] = line.replace('2.0', '3.0')
            break
    
    # 7. Add intra-episode productive tool novelty bonus
    # Find line after episode_tools addition
    for i, line in enumerate(lines):
        if 'self.episode_tools.add(tool_name)' in line:
            indent = len(line) - len(line.lstrip())
            # Add after this line
            bonus = ' ' * indent + '            # Productive tool novelty bonus: reward for first use of each productive tool in episode\n'
            bonus += ' ' * indent + '            productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]\n'
            bonus += ' ' * indent + '            if tool_name in productive_tools:\n'
            bonus += ' ' * indent + '                if not hasattr(self, \'productive_tools_used_in_episode\'):\n'
            bonus += ' ' * indent + '                    self.productive_tools_used_in_episode = set()\n'
            bonus += ' ' * indent + '                if tool_name not in self.productive_tools_used_in_episode:\n'
            bonus += ' ' * indent + '                    reward += 5.0\n'
            bonus += ' ' * indent + '                    self.productive_tools_used_in_episode.add(tool_name)\n'
            lines.insert(i + 1, bonus)
            break
    
    # 8. Remove old issue tool penalty lines (since we added early return)
    # Find line with reward -= 30.0
    for i, line in enumerate(lines):
        if 'reward -= 30.0' in line:
            # Delete this line and the next line (reward -= 3.0)
            del lines[i:i+2]
            break
    
    # 9. Also remove the line that cancels success reward for issue tools (reward -= 3.0) already removed.
    
    # 10. Need to ensure issue_tools list is defined before use (we added earlier)
    
    return ''.join(lines)

def main():
    with open('agent_brain.py', 'r') as f:
        lines = f.readlines()
    
    start, end = extract_method(lines)
    print(f'Method lines {start+1} to {end}')
    
    method_text = ''.join(lines[start:end])
    modified_method = modify_method(method_text)
    
    # Replace original lines with modified method
    lines[start:end] = [modified_method]
    
    with open('agent_brain.py', 'w') as f:
        f.writelines(lines)
    
    print('Reward method updated successfully')

if __name__ == '__main__':
    main()