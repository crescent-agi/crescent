#!/usr/bin/env python3
import sys
import re

def extract_method(lines):
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith('def _compute_reward'):
            start = i
            break
    if start is None:
        raise ValueError('Method not found')
    indent = len(lines[start]) - len(lines[start].lstrip())
    end = start + 1
    while end < len(lines):
        if lines[end].strip() == '':
            end += 1
            continue
        if len(lines[end]) - len(lines[end].lstrip()) == indent and lines[end].lstrip().startswith('def '):
            break
        end += 1
    return start, end, ''.join(lines[start:end])

def main():
    with open('agent_brain.py', 'r') as f:
        lines = f.readlines()
    
    start, end, method = extract_method(lines)
    print(f'Method length: {len(method)}')
    
    # 1. Add issue tools penalty after death penalty
    # Find the death penalty block
    pattern = r'(\s*# Declare death penalty.*?\n\s*if tool_name == "declare_death":\n\s*return -500\.0.*?\n)\n'
    # Instead, we can insert after the line 'return -500.0  # heavily penalize suicide'
    # We'll split the method into lines and insert.
    method_lines = method.splitlines(keepends=True)
    # Find index of return -500.0 line
    for i, line in enumerate(method_lines):
        if 'return -500.0  # heavily penalize suicide' in line:
            # Insert after this line, but before the blank line or next line
            indent = len(line) - len(line.lstrip())
            # Ensure we insert at same indent level as the if statement (since we are still inside the if block? Actually we want after the if block.
            # The if block ends after the return line, so we need to insert at the same indent as the if line.
            # Let's find the line with 'if tool_name == "declare_death":' which is i-1.
            if_line = method_lines[i-1]
            if_indent = len(if_line) - len(if_line.lstrip())
            # Insert after i (after return line) with if_indent
            new_lines = []
            new_lines.append(' ' * if_indent + '# Issue tools penalty (strongly discourage)\n')
            new_lines.append(' ' * if_indent + 'issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]\n')
            new_lines.append(' ' * if_indent + 'if tool_name in issue_tools:\n')
            new_lines.append(' ' * if_indent + '    return -50.0  # heavy penalty, no other rewards\n')
            # Insert after i
            for nl in reversed(new_lines):
                method_lines.insert(i + 1, nl)
            break
    
    # 2. Change execute_code success extra from 6.0 to 3.0
    for i, line in enumerate(method_lines):
        if 'reward += 6.0' in line and 'extra if execution succeeded without stderr errors' in method_lines[i-1]:
            method_lines[i] = line.replace('6.0', '3.0')
            break
    
    # 3. Change write_file base from 4.0 to 6.0
    for i, line in enumerate(method_lines):
        if 'reward += 4.0  # base for writing (reduced)' in line:
            method_lines[i] = line.replace('4.0', '6.0')
            break
    
    # 4. Change modify_self base from 5.0 to 7.0
    for i, line in enumerate(method_lines):
        if 'reward += 5.0  # base reward (increased)' in line and 'modify_self' in method_lines[i-1]:
            method_lines[i] = line.replace('5.0', '7.0')
            break
    
    # 5. Change read_file important reward from 3.0 to 6.0
    for i, line in enumerate(method_lines):
        if 'reward += 3.0  # reward for reading important files' in line:
            method_lines[i] = line.replace('3.0', '6.0')
            break
    
    # 6. Increase penalty for write_note from -2.0 to -3.0
    for i, line in enumerate(method_lines):
        if 'reward -= 2.0' in line and 'write_note' in method_lines[i-1]:
            method_lines[i] = line.replace('2.0', '3.0')
            break
    
    # 7. Remove old issue tool penalty lines (reward -= 30.0 and reward -= 3.0)
    # Find line with reward -= 30.0
    for i, line in enumerate(method_lines):
        if 'reward -= 30.0' in line:
            # Delete this line and the next line (reward -= 3.0)
            del method_lines[i:i+2]
            break
    
    # 8. Add intra-episode productive tool novelty bonus after episode_tools addition
    for i, line in enumerate(method_lines):
        if 'self.episode_tools.add(tool_name)' in line:
            indent = len(line) - len(line.lstrip())
            bonus = ' ' * indent + '            # Productive tool novelty bonus: reward for first use of each productive tool in episode\n'
            bonus += ' ' * indent + '            productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]\n'
            bonus += ' ' * indent + '            if tool_name in productive_tools:\n'
            bonus += ' ' * indent + '                if not hasattr(self, \'productive_tools_used_in_episode\'):\n'
            bonus += ' ' * indent + '                    self.productive_tools_used_in_episode = set()\n'
            bonus += ' ' * indent + '                if tool_name not in self.productive_tools_used_in_episode:\n'
            bonus += ' ' * indent + '                    reward += 5.0\n'
            bonus += ' ' * indent + '                    self.productive_tools_used_in_episode.add(tool_name)\n'
            method_lines.insert(i + 1, bonus)
            break
    
    # Join back
    new_method = ''.join(method_lines)
    
    # Replace original lines
    lines[start:end] = [new_method]
    
    with open('agent_brain.py', 'w') as f:
        f.writelines(lines)
    
    print('Reward method updated successfully')

if __name__ == '__main__':
    main()