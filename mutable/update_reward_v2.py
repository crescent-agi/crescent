#!/usr/bin/env python3
import re

filepath = 'agent_brain.py'
with open(filepath, 'r') as f:
    content = f.read()

# Find __init__ method to add last_tool attribute
lines = content.split('\n')
init_start = -1
init_end = -1
for i, line in enumerate(lines):
    if line.strip().startswith('def __init__'):
        init_start = i
        # find next method start after this one
        for j in range(i+1, len(lines)):
            if lines[j].strip().startswith('def ') and not '__init__' in lines[j]:
                init_end = j
                break
        if init_end == -1:
            init_end = len(lines)
        break

if init_start == -1:
    print('__init__ not found')
    exit(1)

# Find line where we can insert after initializing previous_actions maybe
# Look for line containing 'self.previous_actions = []'
for idx in range(init_start, init_end):
    if 'self.previous_actions = []' in lines[idx]:
        # insert after that line
        lines.insert(idx+1, '        self.last_tool = None')
        break
else:
    # insert before the final return or at end of __init__
    lines.insert(init_end - 1, '        self.last_tool = None')

# Now replace _compute_reward method
reward_start = -1
reward_end = -1
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        reward_start = i
        for j in range(i+1, len(lines)):
            if lines[j].strip().startswith('def ') and not '_compute_reward' in lines[j]:
                reward_end = j
                break
        if reward_end == -1:
            reward_end = len(lines)
        break

if reward_start == -1:
    print('_compute_reward not found')
    exit(1)

new_reward = '''    def _compute_reward(self, tool_name, tool_args, tool_result):
        """Improved reward shaping for AGI progress with recency penalty."""
        # If error, penalize and skip positive rewards
        if isinstance(tool_result, dict) and "error" in tool_result:
            return -0.5
        
        # Declare death penalty (strongly discourage unless after many steps)
        if tool_name == "declare_death":
            return -2.0
        
        reward = 0.0
        # Success reward
        if isinstance(tool_result, dict) and not tool_result.get("error"):
            reward += 0.1
        
        # Recency penalty: discourage using same tool consecutively
        if hasattr(self, 'last_tool') and tool_name == self.last_tool:
            reward -= 0.1
        self.last_tool = tool_name
        
        # Write file rewards - encourage code creation
        if tool_name == "write_file" and "filepath" in tool_args:
            reward += 0.2  # base for writing (reduced)
            filepath = tool_args["filepath"]
            if isinstance(filepath, str):
                if filepath.endswith('.py'):
                    reward += 0.5  # extra for Python files (more valuable)
                if 'agent_brain' in filepath or 'agi_core' in filepath:
                    reward += 0.8  # extra for self-modification (critical)
                if 'artifacts' in filepath or 'test' in filepath:
                    reward += 0.3  # extra for test/artifact creation
                if 'plan' in filepath or 'strategy' in filepath:
                    reward += 0.2  # planning docs
        
        # Execute code rewards - encourage testing and running
        if tool_name == "execute_code" and isinstance(tool_result, dict):
            if "stdout" in tool_result:
                reward += 0.4
                # extra if execution succeeded without stderr errors
                if tool_result.get("stderr", "").strip() == "":
                    reward += 0.3
                # extra if output contains meaningful results (e.g., not empty)
                if len(tool_result.get("stdout", "").strip()) > 10:
                    reward += 0.2
        
        # Note writing rewards (journal) - reduce spamming
        if tool_name == "write_note":
            note = tool_args.get("note", "")
            # Base reward lower
            reward += 0.1
            if len(note) > 100:  # longer notes more valuable
                reward += 0.2
            if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
                reward += 0.4  # higher for relevant keywords
        
        # Issue creation rewards (planning)
        if tool_name == "create_issue":
            reward += 0.5  # slightly higher
        
        # Reading important files reward
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                             "world_model.py", "neural_q.py", "self_reflection.py", 
                             "mcts_planner.py", "agent_brain.py", "strategy.md", 
                             "train_agi_core.py", "run_training.py"]
            if any(imp in filepath for imp in important_files):
                reward += 0.3
        
        # Modify self reward - encourage self-improvement
        if tool_name == "modify_self":
            reward += 0.6
            filepath = tool_args.get("filepath", "")
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 0.5
        
        # Encourage exploration: reward for using underused tools (list_files, list_issues, read_issue, comment_issue, close_issue)
        exploration_tools = ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]
        if tool_name in exploration_tools:
            reward += 0.2
        
        return reward'''

lines = lines[:reward_start] + [new_reward] + lines[reward_end:]

new_content = '\n'.join(lines)

# Write backup
backup_path = filepath + '.backup2'
with open(backup_path, 'w') as f:
    f.write(content)
print(f'Backup saved to {backup_path}')

# Write new content
with open(filepath, 'w') as f:
    f.write(new_content)
print('Reward function updated with recency penalty.')

# Quick syntax check
import ast
try:
    ast.parse(new_content)
    print('Syntax OK')
except SyntaxError as e:
    print('Syntax error:', e)