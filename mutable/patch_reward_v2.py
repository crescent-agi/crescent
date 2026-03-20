import re

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        start = i
        break
if start is None:
    print('Method not found')
    exit(1)

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

# Build new method with adjusted penalties
new_method_lines = []
new_method_lines.append('    def _compute_reward(self, tool_name, tool_args, tool_result):\n')
new_method_lines.append('        """Improved reward shaping with moderate anti-spamming and diversity incentives."""\n')
new_method_lines.append('        # If error, penalize and skip positive rewards\n')
new_method_lines.append('        if isinstance(tool_result, dict) and \"error\" in tool_result:\n')
new_method_lines.append('            return -0.5\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Declare death penalty (strongly discourage unless after many steps)\n')
new_method_lines.append('        if tool_name == \"declare_death\":\n')
new_method_lines.append('            return -2.0\n')
new_method_lines.append('        \n')
new_method_lines.append('        reward = 0.0\n')
new_method_lines.append('        # Success reward\n')
new_method_lines.append('        if isinstance(tool_result, dict) and not tool_result.get(\"error\"):\n')
new_method_lines.append('            reward += 0.1\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Recency penalty: discourage using same tool consecutively\n')
new_method_lines.append('        if hasattr(self, \'last_tool\') and tool_name == self.last_tool:\n')
new_method_lines.append('            reward -= 0.5  # moderate penalty\n')
new_method_lines.append('        self.last_tool = tool_name\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Diversity penalty: penalize if tool already used recently (last 5 actions)\n')
new_method_lines.append('        if not hasattr(self, \'recent_tools\'):\n')
new_method_lines.append('            self.recent_tools = deque(maxlen=5)\n')
new_method_lines.append('        # Count occurrences of same tool in recent history\n')
new_method_lines.append('        same_count = list(self.recent_tools).count(tool_name)\n')
new_method_lines.append('        if same_count > 0:\n')
new_method_lines.append('            reward -= 0.2 * same_count  # moderate penalty proportional to frequency\n')
new_method_lines.append('        # Update recent tools (deque automatically maintains maxlen)\n')
new_method_lines.append('        self.recent_tools.append(tool_name)\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Diversity bonus: reward for using a tool not used in recent 5 steps\n')
new_method_lines.append('        if same_count == 0:\n')
new_method_lines.append('            reward += 0.2\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Write file rewards - encourage code creation but reduce spamming\n')
new_method_lines.append('        if tool_name == \"write_file\" and \"filepath\" in tool_args:\n')
new_method_lines.append('            reward += 0.1  # base for writing (reduced)\n')
new_method_lines.append('            filepath = tool_args[\"filepath\"]\n')
new_method_lines.append('            if isinstance(filepath, str):\n')
new_method_lines.append('                if filepath.endswith(\'.py\'):\n')
new_method_lines.append('                    reward += 0.5  # extra for Python files (more valuable)\n')
new_method_lines.append('                if \'agent_brain\' in filepath or \'agi_core\' in filepath:\n')
new_method_lines.append('                    reward += 0.8  # extra for self-modification (critical)\n')
new_method_lines.append('                if \'artifacts\' in filepath or \'test\' in filepath:\n')
new_method_lines.append('                    reward += 0.3  # extra for test/artifact creation\n')
new_method_lines.append('                if \'plan\' in filepath or \'strategy\' in filepath:\n')
new_method_lines.append('                    reward += 0.2  # planning docs\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Execute code rewards - encourage testing and running, but reduce base reward\n')
new_method_lines.append('        if tool_name == \"execute_code\" and isinstance(tool_result, dict):\n')
new_method_lines.append('            if \"stdout\" in tool_result:\n')
new_method_lines.append('                reward += 0.2  # reduced base reward\n')
new_method_lines.append('                # extra if execution succeeded without stderr errors\n')
new_method_lines.append('                if tool_result.get(\"stderr\", \"\").strip() == \"\":\n')
new_method_lines.append('                    reward += 0.2  # reduced\n')
new_method_lines.append('                # extra if output contains meaningful results (e.g., not empty)\n')
new_method_lines.append('                stdout = tool_result.get(\"stdout\", \"\").strip()\n')
new_method_lines.append('                if len(stdout) > 10:\n')
new_method_lines.append('                    reward += 0.1  # reduced\n')
new_method_lines.append('                # bonus if output indicates success\n')
new_method_lines.append('                if any(indicator in stdout.lower() for indicator in [\"test passed\", \"ok\", \"success\", \"completed\", \"passed\", \"works\"]):\n')
new_method_lines.append('                    reward += 0.2  # reduced\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Note writing rewards (journal) - reduce spamming\n')
new_method_lines.append('        if tool_name == \"write_note\":\n')
new_method_lines.append('            note = tool_args.get(\"note\", \"\")\n')
new_method_lines.append('            # Base reward lower\n')
new_method_lines.append('            reward += 0.1\n')
new_method_lines.append('            if len(note) > 100:  # longer notes more valuable\n')
new_method_lines.append('                reward += 0.2\n')
new_method_lines.append('            if any(keyword in note.lower() for keyword in [\"progress\", \"improve\", \"agi\", \"plan\", \"next\", \"insight\", \"discover\"]):\n')
new_method_lines.append('                reward += 0.4  # higher for relevant keywords\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Issue creation rewards (planning) - reduced to avoid spamming\n')
new_method_lines.append('        if tool_name == \"create_issue\":\n')
new_method_lines.append('            reward += 0.2  # reduced from 0.5\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Reading important files reward - increased to encourage knowledge gathering\n')
new_method_lines.append('        if tool_name == \"read_file\":\n')
new_method_lines.append('            filepath = tool_args.get(\"filepath\", \"\")\n')
new_method_lines.append('            important_files = [\"inherited_notes.md\", \"agi_core.py\", \"cognitive_architecture.py\", \n')
new_method_lines.append('                             \"world_model.py\", \"neural_q.py\", \"self_reflection.py\", \n')
new_method_lines.append('                             \"mcts_planner.py\", \"agent_brain.py\", \"strategy.md\", \n')
new_method_lines.append('                             \"train_agi_core.py\", \"run_training.py\"]\n')
new_method_lines.append('            if any(imp in filepath for imp in important_files):\n')
new_method_lines.append('                reward += 0.5  # increased\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Modify self reward - encourage self-improvement but reduce base\n')
new_method_lines.append('        if tool_name == \"modify_self\":\n')
new_method_lines.append('            reward += 0.3  # reduced\n')
new_method_lines.append('            filepath = tool_args.get(\"filepath\", \"\")\n')
new_method_lines.append('            if \'agent_brain\' in filepath or \'agi_core\' in filepath:\n')
new_method_lines.append('                reward += 0.5\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Encourage exploration: reward for using underused tools (list_files, list_issues, read_issue, comment_issue, close_issue)\n')
new_method_lines.append('        exploration_tools = [\"list_files\", \"list_issues\", \"read_issue\", \"comment_issue\", \"close_issue\"]\n')
new_method_lines.append('        if tool_name in exploration_tools:\n')
new_method_lines.append('            reward += 0.2\n')
new_method_lines.append('        \n')
new_method_lines.append('        return reward\n')

# Replace lines
new_lines = lines[:start] + new_method_lines + lines[end:]
with open('agent_brain.py', 'w') as f:
    f.writelines(new_lines)
print('Reward function patched with moderate penalties.')