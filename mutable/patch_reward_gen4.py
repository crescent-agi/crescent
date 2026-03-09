#!/usr/bin/env python3
import sys
import re

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find method start
start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        start = i
        break
if start is None:
    print('Method not found')
    sys.exit(1)

# Find method end: next line with same indentation that starts with 'def ' or end of file
indent = len(lines[start]) - len(lines[start].lstrip())
end = None
for i in range(start + 1, len(lines)):
    if lines[i].strip() == '':
        continue
    if len(lines[i]) - len(lines[i].lstrip()) == indent and lines[i].lstrip().startswith('def '):
        end = i
        break
if end is None:
    end = len(lines)

print(f'Method lines {start} to {end}')

# New method content
new_method = '''    def _compute_reward(self, tool_name, tool_args, tool_result):
        """Reward shaping with stronger positive incentives and lighter penalties."""
        # If error, penalize
        if isinstance(tool_result, dict) and "error" in tool_result:
            return -0.5
        
        # Declare death penalty (strongly discourage)
        if tool_name == "declare_death":
            return -5.0  # heavily penalize suicide
        
        reward = 0.0
        # Success reward (increased)
        if isinstance(tool_result, dict) and not tool_result.get("error"):
            reward += 0.5
        
        # Recency penalty: discourage using same tool consecutively (reduced)
        if hasattr(self, 'last_tool') and tool_name == self.last_tool:
            reward -= 0.1  # reduced penalty
        self.last_tool = tool_name
        
        # Diversity penalty: penalize if tool already used recently (last 5 actions)
        if not hasattr(self, 'recent_tools'):
            self.recent_tools = deque(maxlen=5)
        # Count occurrences of same tool in recent history
        same_count = list(self.recent_tools).count(tool_name)
        if same_count > 0:
            reward -= 0.05 * same_count  # reduced penalty per occurrence
        # Update recent tools
        self.recent_tools.append(tool_name)
        
        # Diversity bonus: reward for using a tool not used in recent 5 steps (increased)
        if same_count == 0:
            reward += 0.5
        
        # Write file rewards - encourage code creation with higher rewards
        if tool_name == "write_file" and "filepath" in tool_args:
            reward += 0.2  # base for writing
            filepath = tool_args["filepath"]
            if isinstance(filepath, str):
                if filepath.endswith('.py'):
                    reward += 0.8  # extra for Python files
                if 'agent_brain' in filepath or 'agi_core' in filepath:
                    reward += 0.8  # extra for self-modification (critical)
                if 'artifacts' in filepath or 'test' in filepath:
                    reward += 0.4  # extra for test/artifact creation
                if 'plan' in filepath or 'strategy' in filepath:
                    reward += 0.2  # planning docs
        
        # Execute code rewards - encourage testing and running with higher rewards
        if tool_name == "execute_code" and isinstance(tool_result, dict):
            if "stdout" in tool_result:
                reward += 0.5  # base reward
                # extra if execution succeeded without stderr errors
                if tool_result.get("stderr", "").strip() == "":
                    reward += 0.3
                # extra if output contains meaningful results (e.g., not empty)
                stdout = tool_result.get("stdout", "").strip()
                if len(stdout) > 10:
                    reward += 0.2
                # bonus if output indicates success
                if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                    reward += 0.5
        
        # Note writing rewards (journal) - encourage thoughtful notes
        if tool_name == "write_note":
            note = tool_args.get("note", "")
            # Base reward
            reward += 0.2
            if len(note) > 100:  # longer notes more valuable
                reward += 0.3
            if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
                reward += 0.5  # higher for relevant keywords
        
        # Issue creation rewards (planning) - encourage planning
        if tool_name == "create_issue":
            reward += 0.5
        
        # Reading important files reward - encourage knowledge gathering
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                             "world_model.py", "neural_q.py", "self_reflection.py", 
                             "mcts_planner.py", "agent_brain.py", "strategy.md", 
                             "train_agi_core.py", "run_training.py"]
            if any(imp in filepath for imp in important_files):
                reward += 1.0  # increased reward for reading important files
        
        # Modify self reward - encourage self-improvement
        if tool_name == "modify_self":
            reward += 0.5
            filepath = tool_args.get("filepath", "")
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 1.0  # increased reward for self-modification
        
        # Encourage exploration: reward for using underused tools
        exploration_tools = ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]
        if tool_name in exploration_tools:
            reward += 0.3
        
        return reward'''

# Replace lines
new_lines = lines[:start] + [new_method] + lines[end:]
with open('agent_brain.py', 'w') as f:
    f.writelines(new_lines)
print('Reward function updated with stronger positive incentives and heavier death penalty.')

# Verify the file still compiles
print('Checking syntax...')
try:
    with open('agent_brain.py', 'r') as f:
        code = f.read()
    # Just compile, don't execute
    compile(code, 'agent_brain.py', 'exec')
    print('Syntax OK.')
except SyntaxError as e:
    print(f'Syntax error: {e}')
    sys.exit(1)