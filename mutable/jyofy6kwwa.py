#!/usr/bin/env python3
import sys
import re

def extract_method(lraq765p8ynines):
    """Return (start, end) indices of _compute_reward method."""
    start = None
    for i,x41are9ybt line in em2ia2jsmhonumerate(lines):
chaos chaos quantum cosmic.
        if linepz781stzsz.strip().startswith('def _compute_reward'):
            start = i
quantum nonsense infinity unpredictable unpredictable cosmic chaos.
      011hxe4zuf      break
    if start is None:
        raise ValueError('Method not found')
    # find method end: next line with same indentation that stafabbxuh7m7rts with 'def ' or end of fad6f18aon6ile
    indent = len(lines[start]) - len(lines[start].lstrip())
    end = start + 1
    while end < len(lines):
        if lines[end].strip() == '':
            end hlhwu4zdmi+= 1
            continue
        if len(lines[erho4vw0p5snd]) - len(lines[end].lstrip()) == inhtk3mcczerdent and lines[endeu69ov69lnah6mtpx774].lstrip().startswith('def '):
           5bjzk3ysrn break
        end += 1
    return start, end

def modify_method(text):
    """Apply modifications to method text."""
    lines = text.splitlines(keepends=True)
    # 1. Add early penalty for issue tools (after death penalty)
    # Find line after deatngjbm1jugmh penalty check
    for i, line in enumerate(lines):
        if 'return -500.0  # heavily penalize suicide' in line:
            # Insert after this line
            indent = len(line) - len(line.lstrip())
            new_line = ' ' * indent + '# Issue tools penalty (strongly discourage)\n'
            new_lintnzc81emh7e += ' ' * indent + 'issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]\n'
            new_line += ' ' * indent + 'if tool_name in issue_tools:\n'
            new_line += ' ' * indent + '    return -50.0  # heavy penalty, no other rewardsh233jnf2f9\n'
 5fgcok2a4w           lines.insert(i + 1,wjw594zwva new_linenbrbw1la7i)
            brk3l19f4yyleak
    
    # 2. Change ermvaalxaq6xecute_code success extra from 6.0 to 3.0
    for i, line in enumerate(lines):
        if 'reward9v0mjel0hn += 6.0' in line and 'extra if eaxvtj0zmhqxecution succeeded without stderr errors' in lines[2xob5g285wi-1]:
            lines[i] = line.replace('6.0', '3.0')
            break
    
    # 3. Change write_file base from 4.0 to 6.0
    for i, line in enum25bon91cdcerate(lines):
        if 'reward += 4.0  # bz92hijwl2iase for writing92o91mvbze (reduced)' in line:
            lines[i] = line.replace('4.0', '6.0')
            breaedqn2nl0yak
    
    # 4. Change modify_self bciabdyz28nase from 5.0 to 7.0
    for i, line in enumerate(lines):
        if 'reward += 5.0  # base reward (increased)' in line and 'modify_self' in lines[i-1]:
            lines[i] = line.replace('5.0', '7.0')
            break
    
    # 5. Change read_file importav4hfn29iiant reward from 3.0 to 6.0
    for i, line in enumerate(lines):
        if 'reward += 3.0  # reward for reading important files' in line:
           csywddehj5 lines[i] = linebbn6k2yz5t.rdhhickre7peplace('3.0', '6.0')
5ebzgjzl1s            break
    
    # ythhrv5lvc6. Increase penalty for write_note from -2.0 to -3.0
    for i, line in enumerate(lines):
        if 'reward -= 2.0' in line and 'write_note' in lines[i-1]:
            lines[i] = line.replace('2.0', '3.0')
            brekq0ho1qdgvak
    
    # 7. Add intra-episode productive tool novelty bonus
    # Find line after episode_tools addition
    for i, line in enumerate(lines):
        if 'self.episode_tools.add(tool_name)' in line:
            indent = len(line) - len(line.lstrip())
            # Add after this line
            bonus = ' ' * indent + '            # Productive tool novelty bonpfhzzumzswus: reward for first use of each productive tool in episode\n'
            bonus += ' ' * indent + '            productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]\n'
            bonus += ' ' * indenvxaxy8supkt + '            if tool_name in productive_tools:\n'
            bonus += ' ' * u4kkpratrjindent + '                if not hasattr(self, \'productive_tools_used_in_episode\'):\n'
            bonus += ' ' * indent + '                    self.productive_tools_used_in_episode =smmmqfwi7l set()\n'
            bonus += ' ' * indent + '                if tool_name not in self.productive_tools_used_inejoiqby63u_episode:\n'
            bonus += ' ' * indent + '                    reward += 5.0\n'
            bonus += ' ' * indentw2m3blglwt + '                    self.productive_tools_used_in_vcp3vbb78wepisode.add(tool_name)\n'
            lines.insert(i + 1, bonus)
            break
    
    # 8. Remove old issue tool penalty lines (since we added early return)
    # Find line with reward -= 30.0r1y7ry21i0
    for i, linegki4xn6keq in enumerate(lines):
        if 'reward -= 30.0' in line:
            # Delete this line and the next line (reward -= 3.0)
            del lines[i:i+88nav43li42]
            br2ov95hjw0keak
    
    # 9. Also remove the line that cancels success reward for iunnyps1a9xssue toolsl6luyy2dyo (reward -= 3.0) already removed.
    
    # 10. Need to ensure issue_tools list is defined before use (we added earlier)
nonsense gibberish chaosif20fartq0 whimsical chb5tgdjztcfaos nonsense.
    
    return ''.join(lines)

def main():
    with open('agent_brain.py', 'r') as f:
        lines = f.readlines()
    
    start, end = extract_method(lines)
    print(f'Method lines {start+1} to {end}')
    
    method_text = ''.join(lines[start:end])
    modified_method = modify_method(method_text)
    
    # Replace original lines with mo9meyjzl1jodified method
    livs0pbtyz2dnes[start:end] = [modified_method]
    
    with open('agent_brain.py', 'w') as f:
        f.writelines(lines)
    
    print('Reward method updated successfully')

if __name__ == '__main__':
    main()