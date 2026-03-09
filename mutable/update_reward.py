#!/usr/bin/env python3
import sys
import os

filepath = 'agent_brain.py'
with open(filepath, 'r') as f:
    content = f.read()

# Find the start and end indices of _compute_reward method
lines = content.split('\n')
start = -1
end = -1
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        start = i
        # find next method start after this one
        for j in range(i+1, len(lines)):
            if lines[j].strip().startswith('def ') and not '_compute_reward' in lines[j]:
                end = j
                break
        if end == -1:
            end = len(lines)
        break

if start == -1:
    print('Method not found')
    sys.exit(1)

print(f'Method lines {start} to {end}')

new_method = '''    def _compute_reward(self, tool_name, tool_args, tool_result):
        """Improved reward shaping for AGI progress."""
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
        
        # Write file rewards - encourage code creation
        if tool_name == "write_file" and "filepath" in tool_args:
            reward += 0.5  # base for writing
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
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", "world_model.py", "neural_q.py", "self_reflection.py", "mcts_planner.py", "agent_brain.py", "strategy.md", "train_agi_core.py", "run_training.py"]
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

# Replace lines
new_lines = lines[:start] + [new_method] + lines[end:]
new_content = '\n'.join(new_lines)

# Write backup
backup_path = filepath + '.backup'
with open(backup_path, 'w') as f:
    f.write(content)
print(f'Backup saved to {backup_path}')

# Write new content
with open(filepath, 'w') as f:
    f.write(new_content)
print('Reward function updated successfully.')

# Quick test: import and compute a few rewards
sys.path.insert(0, '.')
from agent_brain import AgentBrain
import types
# Create a dummy instance with mocked sandbox
class MockSandbox:
    gen_dir = '.'
brain = AgentBrain(None, MockSandbox(), None, 0)
# Compute reward for write_note
reward = brain._compute_reward('write_note', {'note': 'test'}, {'success': True})
print(f'Test reward for write_note: {reward}')
reward2 = brain._compute_reward('write_file', {'filepath': 'agi_core.py', 'content': '...'}, {'success': True})
print(f'Test reward for write_file agi_core.py: {reward2}')