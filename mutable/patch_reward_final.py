import sys
sys.path.insert(0, '.')

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
    if len(lines[i]) - len(lines[i].lstrip()) <= indent and lines[i].strip().startswith('def '):
        end = i
        break
if end is None:
    end = len(lines)

print(f'Method lines {start} to {end}')

new_method = '''    def _compute_reward(self, tool_name, tool_args, tool_result):
        """Reward shaping with balanced per-tool decay, stronger productive incentives, and novelty bonuses."""
        # If error, penalize
        if isinstance(tool_result, dict) and "error" in tool_result:
            return -0.5
        
        # Declare death penalty (strongly discourage)
        if tool_name == "declare_death":
            return -500.0  # heavily penalize suicide
        
        reward = 0.0
        # Success reward (increased)
        if isinstance(tool_result, dict) and not tool_result.get("error"):
            reward += 3.0
        
        # Recency penalty: discourage using same tool consecutively (reduced)
        if hasattr(self, 'last_tool') and tool_name == self.last_tool:
            reward -= 0.2  # reduced penalty for immediate repetition
        self.last_tool = tool_name
        
        # Diversity penalty: penalize if tool already used recently (last 10 actions)
        if not hasattr(self, 'recent_tools'):
            self.recent_tools = deque(maxlen=10)
        # Count occurrences of same tool in recent history
        same_count = list(self.recent_tools).count(tool_name)
        if same_count > 0:
            reward -= 0.4 * same_count  # penalty per occurrence
        # Update recent tools
        self.recent_tools.append(tool_name)
        
        # Diversity bonus: reward for using a tool not used in recent 10 steps (increased)
        if same_count == 0:
            reward += 3.0
        
        # Episode novelty bonus: reward for first use of a tool in this episode
        if not hasattr(self, 'episode_tools'):
            self.episode_tools = set()
        if tool_name not in self.episode_tools:
            reward += 3.0
            self.episode_tools.add(tool_name)
        
        # Per-tool usage decay penalty (moderate)
        # Initialize tool_usage_counts if not exists
        if not hasattr(self, 'tool_usage_counts'):
            self.tool_usage_counts = {}
            self.tool_decay_factor = 0.85
        
        # Productive tools have lower penalty factor
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
        if tool_name in productive_tools:
            self.tool_penalty_factor = 0.2
        else:
            self.tool_penalty_factor = 0.6
        
        # Decay all counts
        for tool in self.tool_usage_counts:
            self.tool_usage_counts[tool] *= self.tool_decay_factor
        # Increment count for current tool
        self.tool_usage_counts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
        # Apply penalty proportional to decayed usage count (capped at 5.0)
        usage_count = min(self.tool_usage_counts[tool_name], 5.0)
        reward -= self.tool_penalty_factor * usage_count
        
        # Penalty for issue tools (discourage)
        if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
            reward -= 2.0
        
        # Productive tool extra reward
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
        if tool_name in productive_tools:
            reward += 2.0
        
        # Write file rewards - strongly encourage code creation
        if tool_name == "write_file" and "filepath" in tool_args:
            reward += 4.0  # base for writing (increased)
            filepath = tool_args["filepath"]
            if isinstance(filepath, str):
                if filepath.endswith('.py'):
                    reward += 4.0  # extra for Python files
                if 'agent_brain' in filepath or 'agi_core' in filepath:
                    reward += 4.0  # extra for self-modification (critical)
                if 'artifacts' in filepath or 'test' in filepath:
                    reward += 4.0  # extra for test/artifact creation
                if 'plan' in filepath or 'strategy' in filepath:
                    reward += 0.8  # planning docs
        # Execute code rewards - strongly encourage testing and running
        if tool_name == "execute_code" and isinstance(tool_result, dict):
            if "stdout" in tool_result:
                reward += 3.0  # base reward (increased)
                # extra if execution succeeded without stderr errors
                if tool_result.get("stderr", "").strip() == "":
                    reward += 4.0
                # extra if output contains meaningful results (e.g., not empty)
                stdout = tool_result.get("stdout", "").strip()
                if len(stdout) > 10:
                    reward += 0.5
                # bonus if output indicates success
                if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                    reward += 1.0
        # Note writing rewards (journal) - discourage overuse
        if tool_name == "write_note":
            note = tool_args.get("note", "")
            # Base reward (reduced)
            reward += 0.5
            if len(note) > 100:  # longer notes more valuable
                reward += 0.5
            if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
                reward += 1.5  # higher for relevant keywords
        
        # Issue creation rewards (planning) - moderate reward (reduced)
        if tool_name == "create_issue":
            reward += 0.2  # reduced reward for issue creation
        
        # Reading important files reward - encourage knowledge gathering
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                             "world_model.py", "neural_q.py", "self_reflection.py", 
                             "mcts_planner.py", "agent_brain.py", "strategy.md", 
                             "train_agi_core.py", "run_training.py"]
            if any(imp in filepath for imp in important_files):
                reward += 15.0  # increased reward for reading important files
        
        # Modify self reward - encourage self-improvement
        if tool_name == "modify_self":
            reward += 3.0  # increased base reward
            filepath = tool_args.get("filepath", "")
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 10.0  # reduced extra reward for self-modification
        
        # Encourage exploration: reward for using underused tools, but less for issue tools
        if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
            if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
                reward += 0.0  # no extra reward for issue tools (only success reward)
            else:
                reward += 0.0  # removed extra reward for list_files
        
        return reward
'''

# Replace the method lines
lines[start:end] = [new_method]

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Reward method updated successfully')