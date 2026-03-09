#!/usr/bin/env python3
import sys

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
print('First few lines of method:')
for i in range(start, min(start+5, end)):
    print(repr(lines[i]))

# New method lines (including trailing newline)
new_method_lines = [
'    def _compute_reward(self, tool_name, tool_args, tool_result):\n',
'        """Reward shaping with stronger positive incentives and lighter penalties."""\n',
'        # If error, penalize\n',
'        if isinstance(tool_result, dict) and "error" in tool_result:\n',
'            return -0.5\n',
'        \n',
'        # Declare death penalty (strongly discourage)\n',
'        if tool_name == "declare_death":\n',
'            return -5.0  # heavily penalize suicide\n',
'        \n',
'        reward = 0.0\n',
'        # Success reward (increased)\n',
'        if isinstance(tool_result, dict) and not tool_result.get("error"):\n',
'            reward += 0.5\n',
'        \n',
'        # Recency penalty: discourage using same tool consecutively (reduced)\n',
'        if hasattr(self, \'last_tool\') and tool_name == self.last_tool:\n',
'            reward -= 0.1  # reduced penalty\n',
'        self.last_tool = tool_name\n',
'        \n',
'        # Diversity penalty: penalize if tool already used recently (last 5 actions)\n',
'        if not hasattr(self, \'recent_tools\'):\n',
'            self.recent_tools = deque(maxlen=5)\n',
'        # Count occurrences of same tool in recent history\n',
'        same_count = list(self.recent_tools).count(tool_name)\n',
'        if same_count > 0:\n',
'            reward -= 0.05 * same_count  # reduced penalty per occurrence\n',
'        # Update recent tools\n',
'        self.recent_tools.append(tool_name)\n',
'        \n',
'        # Diversity bonus: reward for using a tool not used in recent 5 steps (increased)\n',
'        if same_count == 0:\n',
'            reward += 0.5\n',
'        \n',
'        # Write file rewards - encourage code creation with higher rewards\n',
'        if tool_name == "write_file" and "filepath" in tool_args:\n',
'            reward += 0.2  # base for writing\n',
'            filepath = tool_args["filepath"]\n',
'            if isinstance(filepath, str):\n',
'                if filepath.endswith(\'.py\'):\n',
'                    reward += 0.8  # extra for Python files\n',
'                if \'agent_brain\' in filepath or \'agi_core\' in filepath:\n',
'                    reward += 0.8  # extra for self-modification (critical)\n',
'                if \'artifacts\' in filepath or \'test\' in filepath:\n',
'                    reward += 0.4  # extra for test/artifact creation\n',
'                if \'plan\' in filepath or \'strategy\' in filepath:\n',
'                    reward += 0.2  # planning docs\n',
'        \n',
'        # Execute code rewards - encourage testing and running with higher rewards\n',
'        if tool_name == "execute_code" and isinstance(tool_result, dict):\n',
'            if "stdout" in tool_result:\n',
'                reward += 0.5  # base reward\n',
'                # extra if execution succeeded without stderr errors\n',
'                if tool_result.get("stderr", "").strip() == "":\n',
'                    reward += 0.3\n',
'                # extra if output contains meaningful results (e.g., not empty)\n',
'                stdout = tool_result.get("stdout", "").strip()\n',
'                if len(stdout) > 10:\n',
'                    reward += 0.2\n',
'                # bonus if output indicates success\n',
'                if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):\n',
'                    reward += 0.5\n',
'        \n',
'        # Note writing rewards (journal) - encourage thoughtful notes\n',
'        if tool_name == "write_note":\n',
'            note = tool_args.get("note", "")\n',
'            # Base reward\n',
'            reward += 0.2\n',
'            if len(note) > 100:  # longer notes more valuable\n',
'                reward += 0.3\n',
'            if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):\n',
'                reward += 0.5  # higher for relevant keywords\n',
'        \n',
'        # Issue creation rewards (planning) - encourage planning\n',
'        if tool_name == "create_issue":\n',
'            reward += 0.5\n',
'        \n',
'        # Reading important files reward - encourage knowledge gathering\n',
'        if tool_name == "read_file":\n',
'            filepath = tool_args.get("filepath", "")\n',
'            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", \n',
'                             "world_model.py", "neural_q.py", "self_reflection.py", \n',
'                             "mcts_planner.py", "agent_brain.py", "strategy.md", \n',
'                             "train_agi_core.py", "run_training.py"]\n',
'            if any(imp in filepath for imp in important_files):\n',
'                reward += 1.0  # increased reward for reading important files\n',
'        \n',
'        # Modify self reward - encourage self-improvement\n',
'        if tool_name == "modify_self":\n',
'            reward += 0.5\n',
'            filepath = tool_args.get("filepath", "")\n',
'            if \'agent_brain\' in filepath or \'agi_core\' in filepath:\n',
'                reward += 1.0  # increased reward for self-modification\n',
'        \n',
'        # Encourage exploration: reward for using underused tools\n',
'        exploration_tools = ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]\n',
'        if tool_name in exploration_tools:\n',
'            reward += 0.3\n',
'        \n',
'        return reward\n',
'\n'  # extra newline to separate from next method
]

# Replace lines
new_lines = lines[:start] + new_method_lines + lines[end:]
with open('agent_brain.py', 'w') as f:
    f.writelines(new_lines)
print(f'Reward function updated. New total lines: {len(new_lines)}')

# Verify syntax
try:
    with open('agent_brain.py', 'r') as f:
        code = f.read()
    compile(code, 'agent_brain.py', 'exec')
    print('Syntax OK.')
except SyntaxError as e:
    print(f'Syntax error: {e}')
    sys.exit(1)