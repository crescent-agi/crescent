#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock class to replicate reward logic
class MockAgent:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.episode_tools = set()
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.episode_tool_counts = {}
        self.tool_penalty_factor = None
    
    def compute_reward(self, tool_name, tool_args, tool_result):
        # If error, penalize
        if isinstance(tool_result, dict) and "error" in tool_result:
            return -0.5
        
        # Declare death penalty (strongly discourage)
        if tool_name == "declare_death":
            return -500.0  # heavily penalize suicide
        # Issue tools penalty (strongly discourage)
        issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
        if tool_name in issue_tools:
            return -50.0  # heavy penalty, no other rewards
        
        # Write note penalty (strongly discourage)
        if tool_name == "write_note":
            return -20.0  # heavy penalty, no other rewards
        
        reward = 0.0
        # Success reward (increased slightly)
        if isinstance(tool_result, dict) and not tool_result.get("error"):
            reward += 10.0  # increased from 8.0 (issue #25)
            # Baseline reward for productive tools
            if tool_name in productive_tools:
                reward += 1.0
        
        # Recency penalty: discourage using same tool consecutively (reduced)
        if hasattr(self, 'last_tool') and tool_name == self.last_tool:
            reward -= 0.1  # reduced penalty for immediate repetition
        self.last_tool = tool_name
        
        # Diversity penalty: penalize if tool already used recently (last 10 actions)
        if not hasattr(self, 'recent_tools'):
            self.recent_tools = []
        # Count occurrences of same tool in recent history
        same_count = self.recent_tools.count(tool_name)
        if same_count > 0:
            reward -= 0.2 * same_count  # penalty per occurrence
        # Update recent tools (keep last 10)
        self.recent_tools.append(tool_name)
        if len(self.recent_tools) > 10:
            self.recent_tools.pop(0)
        
        # Diversity bonus: reward for using a tool not used in recent 10 steps (increased)
        # Skip diversity bonus for issue tools and write_note
        issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
        if same_count == 0 and tool_name in productive_tools:
            reward += 5.0  # increased from 4.0
        
        # Episode novelty bonus: reward for first use of a tool in this episode
        if not hasattr(self, 'episode_tools'):
            self.episode_tools = set()
        if tool_name not in self.episode_tools:
            # Skip episode novelty for issue tools and write_note
            if tool_name in productive_tools:
                reward += 5.0  # increased from 4.0
            self.episode_tools.add(tool_name)
        # Per-tool usage decay penalty (moderate)
        # Initialize tool_usage_counts if not exists
        if not hasattr(self, 'tool_usage_counts'):
            self.tool_usage_counts = {}
            self.tool_decay_factor = 0.85
        
        # Productive tools have lower penalty factor (adjusted per issue #23)
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
        # Special penalty factors for balanced usage
        if tool_name == "write_file":
            self.tool_penalty_factor = 0.4  # increased from 0.5 (issue #24)
        elif tool_name == "read_file":
            self.tool_penalty_factor = 0.3  # increased from 0.3 (issue #24)
        elif tool_name == "modify_self":
            self.tool_penalty_factor = 0.3  # reduced from 0.5 (issue #24)
        elif tool_name == "execute_code":
            self.tool_penalty_factor = 0.5  # reduced from 0.3 (issue #24)
        elif tool_name in productive_tools:
            self.tool_penalty_factor = 0.1  # fallback
        else:
            self.tool_penalty_factor = 1.0  # increased from 0.6 (issue #24)
        
        # Decay all counts
        for tool in self.tool_usage_counts:
            self.tool_usage_counts[tool] *= self.tool_decay_factor
        # Increment count for current tool
        self.tool_usage_counts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
        # Apply penalty proportional to decayed usage count (capped at 5.0)
        usage_count = min(self.tool_usage_counts[tool_name], 5.0)
        reward -= self.tool_penalty_factor * usage_count
        
        # Per-episode usage penalty for productive tools (issue #23)
        if not hasattr(self, 'episode_tool_counts'):
            self.episode_tool_counts = {}
        self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
        
        # Write file: penalty after 10 uses (factor 1.0)
        if tool_name == "write_file" and self.episode_tool_counts[tool_name] > 2:
            reward -= 3.0 * (self.episode_tool_counts[tool_name] - 2)
        # Read file: penalty after 10 uses (factor 1.0)
        if tool_name == "read_file" and self.episode_tool_counts[tool_name] > 2:
            reward -= 3.0 * (self.episode_tool_counts[tool_name] - 2)
        # Modify self: penalty after 10 uses (factor 1.0)
        if tool_name == "modify_self" and self.episode_tool_counts[tool_name] > 2:
            reward -= 3.0 * (self.episode_tool_counts[tool_name] - 2)
        # Execute code: penalty after 10 uses (factor 1.0) as per issue #25
        if tool_name == "execute_code" and self.episode_tool_counts[tool_name] > 2:
            reward -= 3.0 * (self.episode_tool_counts[tool_name] - 2)
        
        # List files penalty after 5 uses (issue #24)
        if tool_name == "list_files" and self.episode_tool_counts[tool_name] > 5:
            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 5)
        # Penalty for write_note (discourage overuse)
        if tool_name == "write_note":
            reward -= 5.0  # increased from 3.0 (issue #24)
        
        # Productive tool extra reward
        if tool_name in productive_tools:
            reward += 6.0  # increased from 4.0 (issue #25)
        
        # Write file rewards - increased base reward
        if tool_name == "write_file" and "filepath" in tool_args:
            reward += 12.0  # increased from 11.0 (issue #25)
            filepath = tool_args["filepath"]
            if isinstance(filepath, str):
                if filepath.endswith('.py'):
                    reward += 4.0  # extra for Python files
                if 'agent_brain' in filepath or 'agi_core' in filepath:
                    reward += 3.0  # extra for self-modification
                if 'artifacts' in filepath or 'test' in filepath:
                    reward += 3.0  # extra for test/artifact creation
                if 'plan' in filepath or 'strategy' in filepath:
                    reward += 0.5  # planning docs
        # Execute code rewards - reduced attractiveness
        if tool_name == "execute_code" and isinstance(tool_result, dict):
            if "stdout" in tool_result:
                reward += 4.0  # reduced from 6.0 (issue #25)
                # extra if execution succeeded without stderr errors (reduced)
                if tool_result.get("stderr", "").strip() == "":
                    reward += 3.0  # increased from 2.0 (issue #24)
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
            reward += 0.0  # no reward for issue creation
        
        # Reading important files reward - increased
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            # Small bonus for any successful read
            reward += 0.2  # reduced from 0.5 (issue #25)
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                             "world_model.py", "neural_q.py", "self_reflection.py", 
                             "mcts_planner.py", "agent_brain.py", "strategy.md", 
                             "train_agi_core.py", "run_training.py"]
            if any(imp in filepath for imp in important_files):
                reward += 7.0  # increased from 6.0 (issue #25)
        
        # Modify self reward - adjusted base reward
        if tool_name == "modify_self":
            reward += 8.0  # increased from 7.0 (issue #25)
            filepath = tool_args.get("filepath", "")
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 5.0  # extra reward for self-modification (reduced)
        
        # Encourage exploration: reward for using underused tools, but less for issue tools
        if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
            if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
                reward += 0.0  # no extra reward for issue tools (only success reward)
            else:
                reward += 0.0  # removed extra reward for list_files
        
        return reward

# Simulate a series of actions
agent = MockAgent()
tools = ["write_file", "execute_code", "modify_self", "read_file", "list_files"]
print("First use of each tool (successful result):")
for tool in tools:
    args = {}
    result = {"stdout": "ok", "stderr": ""}
    if tool == "write_file":
        args = {"filepath": "test.py"}
    elif tool == "read_file":
        args = {"filepath": "agent_brain.py"}
    reward = agent.compute_reward(tool, args, result)
    print(f"  {tool}: {reward:.2f}")

print("\nNow simulate 10 consecutive execute_code actions:")
agent = MockAgent()
for i in range(10):
    reward = agent.compute_reward("execute_code", {}, {"stdout": "ok", "stderr": ""})
    print(f"  step {i+1}: {reward:.2f}")

print("\nNow simulate mixed usage (write_file, read_file, execute_code, modify_self):")
agent = MockAgent()
sequence = ["write_file", "read_file", "execute_code", "modify_self"] * 3
for tool in sequence:
    args = {}
    if tool == "write_file":
        args = {"filepath": "test.py"}
    elif tool == "read_file":
        args = {"filepath": "agent_brain.py"}
    reward = agent.compute_reward(tool, args, {"stdout": "ok", "stderr": ""})
    print(f"  {tool}: {reward:.2f}")