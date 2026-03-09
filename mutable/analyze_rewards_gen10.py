#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

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
        
        if tool_name == "declare_death":
            return -500.0
        issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
        if tool_name in issue_tools:
            return -50.0
        
        if tool_name == "write_note":
            return -20.0
        
        reward = 0.0
        if isinstance(tool_result, dict) and not tool_result.get("error"):
            reward += 10.0
            if tool_name in productive_tools:
                reward += 1.0
        
        if hasattr(self, 'last_tool') and tool_name == self.last_tool:
            reward -= 0.1
        self.last_tool = tool_name
        
        if not hasattr(self, 'recent_tools'):
            self.recent_tools = []
        same_count = self.recent_tools.count(tool_name)
        if same_count > 0:
            reward -= 0.2 * same_count
        self.recent_tools.append(tool_name)
        if len(self.recent_tools) > 10:
            self.recent_tools.pop(0)
        
        if same_count == 0 and tool_name in productive_tools:
            reward += 5.0
        
        if not hasattr(self, 'episode_tools'):
            self.episode_tools = set()
        if tool_name not in self.episode_tools:
            if tool_name in productive_tools:
                reward += 5.0
            self.episode_tools.add(tool_name)
        
        if not hasattr(self, 'tool_usage_counts'):
            self.tool_usage_counts = {}
            self.tool_decay_factor = 0.85
        
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
        if tool_name == "write_file":
            self.tool_penalty_factor = 0.4
        elif tool_name == "read_file":
            self.tool_penalty_factor = 0.3
        elif tool_name == "modify_self":
            self.tool_penalty_factor = 0.3
        elif tool_name == "execute_code":
            self.tool_penalty_factor = 0.5
        elif tool_name in productive_tools:
            self.tool_penalty_factor = 0.1
        else:
            self.tool_penalty_factor = 1.0
        
        for tool in self.tool_usage_counts:
            self.tool_usage_counts[tool] *= self.tool_decay_factor
        self.tool_usage_counts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
        usage_count = min(self.tool_usage_counts[tool_name], 5.0)
        reward -= self.tool_penalty_factor * usage_count
        
        if not hasattr(self, 'episode_tool_counts'):
            self.episode_tool_counts = {}
        self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
        
        if tool_name == "write_file" and self.episode_tool_counts[tool_name] > 2:
            reward -= 3.0 * (self.episode_tool_counts[tool_name] - 2)
        if tool_name == "read_file" and self.episode_tool_counts[tool_name] > 2:
            reward -= 3.0 * (self.episode_tool_counts[tool_name] - 2)
        if tool_name == "modify_self" and self.episode_tool_counts[tool_name] > 2:
            reward -= 3.0 * (self.episode_tool_counts[tool_name] - 2)
        if tool_name == "execute_code" and self.episode_tool_counts[tool_name] > 2:
            reward -= 3.0 * (self.episode_tool_counts[tool_name] - 2)
        
        if tool_name == "list_files" and self.episode_tool_counts[tool_name] > 5:
            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 5)
        if tool_name == "write_note":
            reward -= 5.0
        
        if tool_name in productive_tools:
            reward += 6.0
        
        if tool_name == "write_file" and "filepath" in tool_args:
            reward += 12.0
            filepath = tool_args["filepath"]
            if isinstance(filepath, str):
                if filepath.endswith('.py'):
                    reward += 4.0
                if 'agent_brain' in filepath or 'agi_core' in filepath:
                    reward += 3.0
                if 'artifacts' in filepath or 'test' in filepath:
                    reward += 3.0
                if 'plan' in filepath or 'strategy' in filepath:
                    reward += 0.5
        if tool_name == "execute_code" and isinstance(tool_result, dict):
            if "stdout" in tool_result:
                reward += 4.0
                if tool_result.get("stderr", "").strip() == "":
                    reward += 3.0
                stdout = tool_result.get("stdout", "").strip()
                if len(stdout) > 10:
                    reward += 0.5
                if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                    reward += 1.0
        if tool_name == "write_note":
            note = tool_args.get("note", "")
            reward += 0.5
            if len(note) > 100:
                reward += 0.5
            if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
                reward += 1.5
        
        if tool_name == "create_issue":
            reward += 0.0
        
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            reward += 0.2
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                             "world_model.py", "neural_q.py", "self_reflection.py", 
                             "mcts_planner.py", "agent_brain.py", "strategy.md", 
                             "train_agi_core.py", "run_training.py"]
            if any(imp in filepath for imp in important_files):
                reward += 7.0
        
        if tool_name == "modify_self":
            reward += 8.0
            filepath = tool_args.get("filepath", "")
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 5.0
        
        if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
            if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
                reward += 0.0
            else:
                reward += 0.0
        
        return reward

# Compute first-use rewards with optimal conditions
agent = MockAgent()
tools = ["write_file", "execute_code", "modify_self", "read_file"]
args_map = {
    "write_file": {"filepath": "agent_brain.py"},
    "execute_code": {},
    "modify_self": {"filepath": "agent_brain.py"},
    "read_file": {"filepath": "agent_brain.py"},
}
result = {"stdout": "test passed", "stderr": ""}
print("First-use rewards (optimal):")
for tool in tools:
    reward = agent.compute_reward(tool, args_map.get(tool, {}), result)
    print(f"  {tool}: {reward:.2f}")

# Compute rewards after 5 uses each (simulate)
print("\nAfter 5 uses each (no recent repeats):")
agent = MockAgent()
for i in range(5):
    for tool in tools:
        agent.compute_reward(tool, args_map.get(tool, {}), result)
# now compute 6th use
print("6th use rewards:")
for tool in tools:
    reward = agent.compute_reward(tool, args_map.get(tool, {}), result)
    print(f"  {tool}: {reward:.2f}")

# Compute rewards for execute_code with varying results
print("\nExecute_code reward variations:")
agent = MockAgent()
# perfect success
reward = agent.compute_reward("execute_code", {}, {"stdout": "test passed", "stderr": ""})
print(f"  perfect success: {reward:.2f}")
# success with stderr
reward = agent.compute_reward("execute_code", {}, {"stdout": "ok", "stderr": "warning"})
print(f"  success with stderr: {reward:.2f}")
# success empty stdout
reward = agent.compute_reward("execute_code", {}, {"stdout": "", "stderr": ""})
print(f"  success empty stdout: {reward:.2f}")
# error
reward = agent.compute_reward("execute_code", {}, {"error": "failed"})
print(f"  error: {reward:.2f}")