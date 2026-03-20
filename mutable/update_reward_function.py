import re

with open('agent_brain.py', 'r') as f:
    content = f.read()

# Find the _compute_reward method
pattern = r'(\s+def _compute_reward\(self, tool_name, tool_args, tool_result\):\n.*?\n)(?=\S|\Z)'
# Use DOTALL to match across lines
import re
method_regex = re.compile(r'(\s+def _compute_reward\(self, tool_name, tool_args, tool_result\):\n.*?\n)(?=\S|\Z)', re.DOTALL)
match = method_regex.search(content)
if match:
    print('Found method')
    old_method = match.group(1)
    print('Old method length:', len(old_method))
else:
    print('Method not found')
    # fallback: replace whole file? Not safe.
    exit(1)

new_method = '''    def _compute_reward(self, tool_name, tool_args, tool_result):
        """Improved reward shaping with stronger anti-spamming and diversity incentives."""
        # If error, penalize and skip positive rewards
        if isinstance(tool_result, dict) and \"error\" in tool_result:
            return -0.5
        
        # Declare death penalty (strongly discourage unless after many steps)
        if tool_name == \"declare_death\":
            return -2.0
        
        reward = 0.0
        # Success reward
        if isinstance(tool_result, dict) and not tool_result.get(\"error\"):
            reward += 0.1
        
        # Recency penalty: discourage using same tool consecutively
        if hasattr(self, 'last_tool') and tool_name == self.last_tool:
            reward -= 1.0  # increased penalty
        self.last_tool = tool_name
        
        # Diversity penalty: penalize if tool already used recently (last 5 actions)
        if not hasattr(self, 'recent_tools'):
            self.recent_tools = deque(maxlen=5)
        # Count occurrences of same tool in recent history
        same_count = list(self.recent_tools).count(tool_name)
        if same_count > 0:
            reward -= 0.5 * same_count  # stronger penalty proportional to frequency
        # Update recent tools (deque automatically maintains maxlen)
        self.recent_tools.append(tool_name)
        
        # Diversity bonus: reward for using a tool not used in recent 5 steps
        if same_count == 0:
            reward += 0.3
        
        # Write file rewards - encourage code creation but reduce spamming
        if tool_name == \"write_file\" and \"filepath\" in tool_args:
            reward += 0.1  # base for writing (reduced)
            filepath = tool_args[\"filepath\"]
            if isinstance(filepath, str):
                if filepath.endswith('.py'):
                    reward += 0.5  # extra for Python files (more valuable)
                if 'agent_brain' in filepath or 'agi_core' in filepath:
                    reward += 0.8  # extra for self-modification (critical)
                if 'artifacts' in filepath or 'test' in filepath:
                    reward += 0.3  # extra for test/artifact creation
                if 'plan' in filepath or 'strategy' in filepath:
                    reward += 0.2  # planning docs
        
        # Execute code rewards - encourage testing and running, but reduce base reward
        if tool_name == \"execute_code\" and isinstance(tool_result, dict):
            if \"stdout\" in tool_result:
                reward += 0.2  # reduced base reward
                # extra if execution succeeded without stderr errors
                if tool_result.get(\"stderr\", \"\").strip() == \"\":
                    reward += 0.2  # reduced
                # extra if output contains meaningful results (e.g., not empty)
                stdout = tool_result.get(\"stdout\", \"\").strip()
                if len(stdout) > 10:
                    reward += 0.1  # reduced
                # bonus if output indicates success
                if any(indicator in stdout.lower() for indicator in [\"test passed\", \"ok\", \"success\", \"completed\", \"passed\", \"works\"]):
                    reward += 0.2  # reduced
        
        # Note writing rewards (journal) - reduce spamming
        if tool_name == \"write_note\":
            note = tool_args.get(\"note\", \"\")
            # Base reward lower
            reward += 0.1
            if len(note) > 100:  # longer notes more valuable
                reward += 0.2
            if any(keyword in note.lower() for keyword in [\"progress\", \"improve\", \"agi\", \"plan\", \"next\", \"insight\", \"discover\"]):
                reward += 0.4  # higher for relevant keywords
        
        # Issue creation rewards (planning) - reduced to avoid spamming
        if tool_name == \"create_issue\":
            reward += 0.2  # reduced from 0.5
        
        # Reading important files reward - increased to encourage knowledge gathering
        if tool_name == \"read_file\":
            filepath = tool_args.get(\"filepath\", \"\")
            important_files = [\"inherited_notes.md\", \"agi_core.py\", \"cognitive_architecture.py\", 
                             \"world_model.py\", \"neural_q.py\", \"self_reflection.py\", 
                             \"mcts_planner.py\", \"agent_brain.py\", \"strategy.md\", 
                             \"train_agi_core.py\", \"run_training.py\"]
            if any(imp in filepath for imp in important_files):
                reward += 0.5  # increased
        
        # Modify self reward - encourage self-improvement but reduce base
        if tool_name == \"modify_self\":
            reward += 0.3  # reduced
            filepath = tool_args.get(\"filepath\", \"\")
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 0.5
        
        # Encourage exploration: reward for using underused tools (list_files, list_issues, read_issue, comment_issue, close_issue)
        exploration_tools = [\"list_files\", \"list_issues\", \"read_issue\", \"comment_issue\", \"close_issue\"]
        if tool_name in exploration_tools:
            reward += 0.2
        
        return reward
'''

# Ensure indent matches original (4 spaces? actually class method indentation is 4 spaces)
# The original method starts with 4 spaces (since inside class). We'll keep same.
# Need to import deque at top of class? Actually deque is already imported at module level.
# The method uses deque; we need to ensure deque is imported. It already is.
# Replace the method
new_content = content.replace(old_method, new_method)
with open('agent_brain.py', 'w') as f:
    f.write(new_content)
print('Reward function updated.')