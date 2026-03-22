#!/usr/bin/env python3
"""
Train with Generation 48 reward plus forced rotation: each episode, first step picks the least used productive tool globally.
Goal: break symmetry and encourage balanced distribution.
"""
import sys
sys.path.insert(0, '.')
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client
import neural_q_continuous
sys.modules['neural_q_continuous'] = neural_q_continuous
import patch_weight_clipping
from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from collections import deque, defaultdict
from new_reward_gen48 import compute_reward_gen48 as compute_reward
from new_reward_gen48 import compute_terminal_bonus_gen48

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = deque(maxlen=10)
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tools = set()
        self.episode_tool_counts = {}
        self.episode_productive_first_use = set()
        self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 10
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_counts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_total = 0
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.recent_read_files.clear()
        self.episode_step_count = 0

self = DummySelf()

class SimWorkspace:
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
        }
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                result["content"] = self.files[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            directory = tool_args.get("directory", ".")
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
            if "error" in code:
                result["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["success"] = False
            else:
                result["stdout"] = "Simulated output"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note + "\n"
            result["note"] = "Added to journal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            if filepath in self.files:
                self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Cannot modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result
    def update_state(self, tool_name, tool_args):
        pass

# Patch choose_action
try:
    from neural_q_continuous import NeuralQLearningAgentContinuous
    original_choose_action = NeuralQLearningAgentContinuous.choose_action
    def masked_choose_action(self, state_vector):
        tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                      "modify_self", "declare_death", "list_issues", "read_issue",
                      "comment_issue", "create_issue", "close_issue"]
        non_productive_indices = [i for i, name in enumerate(tool_names) 
                                  if name in ["list_files", "write_note", "list_issues", "read_issue",
                                              "comment_issue", "create_issue", "close_issue"]]
        productive_indices = [0, 1, 3, 5]
        death_index = 6
        if random.random() < self.epsilon:
            allowed = [i for i in range(self.action_size) 
                       if i not in non_productive_indices]
            if allowed:
                return random.choice(allowed)
            else:
                return random.randrange(self.action_size)
        else:
            q_values = self.nn.predict(state_vector)
            best_q = max(q_values[i] for i in productive_indices)
            best_actions = [i for i in productive_indices if q_values[i] == best_q]
            return random.choice(best_actions)
    NeuralQLearningAgentContinuous.choose_action = masked_choose_action
    print("Patched choose_action")
except ImportError as e:
    print(f"Could not patch: {e}")

# Patch entropy coefficient
try:
    from neural_q_continuous import NeuralQLearningAgentContinuous
    original_learn = NeuralQLearningAgentContinuous.learn
    def learn_with_entropy2(self, state_vector, action, reward, next_state_vector, done, entropy_coeff=2.0):
        return original_learn(self, state_vector, action, reward, next_state_vector, done, entropy_coeff=entropy_coeff)
    NeuralQLearningAgentContinuous.learn = learn_with_entropy2
    print("Patched entropy coeff=2.0")
except ImportError as e:
    print(f"Could not patch entropy: {e}")

# Load model
core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                         learning_rate=0.001, exploration_rate=0.5,
                         epsilon_decay=1.0, epsilon_min=0.5, use_features=True)
save_dir = "artifacts/agi_core_continuous_trained_gen32"
if os.path.exists(save_dir):
    core.load(save_dir)
    print(f"Loaded model from {save_dir}")
else:
    print("Model not found")
    sys.exit(1)

# Global tool counts across episodes for forced rotation
global_productive_counts = defaultdict(int)

# Run training with forced rotation
episodes = 0
steps_per_episode = 20
print(f"Running {episodes} episodes with forced rotation...")
for episode in range(episodes):
    self.reset()
    workspace = SimWorkspace()
    episode_reward = 0.0
    for step in range(steps_per_episode):
        # For first step of each episode, pick the least used productive tool globally
        if step == 0:
            # Determine which productive tool has smallest global count
            productive = ["write_file", "execute_code", "modify_self", "read_file"]
            min_count = min(global_productive_counts[tool] for tool in productive)
            candidate_tools = [tool for tool in productive if global_productive_counts[tool] == min_count]
            forced_tool = random.choice(candidate_tools)
            # Map tool name to index
            tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                          "modify_self", "declare_death", "list_issues", "read_issue",
                          "comment_issue", "create_issue", "close_issue"]
            forced_index = tool_names.index(forced_tool)
            # Override decision: manually set tool_name and generate args
            tool_name = forced_tool
            # generate arguments using core's method (or simple)
            files = core.extract_files(workspace.workspace_summary())
            if tool_name == "read_file":
                important = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py"]
                for imp in important:
                    if imp in files:
                        tool_args = {"filepath": imp}
                        break
                else:
                    tool_args = {"filepath": files[0] if files else "inherited_notes.md"}
            elif tool_name == "write_file":
                tool_args = {"filepath": "artifacts/forced.txt", "content": "Forced rotation"}
            elif tool_name == "execute_code":
                tool_args = {"code": "print('forced')", "language": "python"}
            elif tool_name == "modify_self":
                tool_args = {"filepath": "strategy.md", "content": "# Forced"}
            else:
                tool_args = {}
            confidence = 0.9
            print(f"Episode {episode+1} step 1: forced tool {forced_tool}")
        else:
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        # terminal bonus at last step
        if step == steps_per_episode - 1:
            terminal_bonus = compute_terminal_bonus_gen48(self, sum(self.episode_tool_counts.values()))
            reward += terminal_bonus
            if terminal_bonus > 0:
                print(f"Episode {episode+1} terminal bonus {terminal_bonus}")
        episode_reward += reward
        # Update global counts
        if tool_name in ["write_file", "execute_code", "modify_self", "read_file"]:
            global_productive_counts[tool_name] += 1
        workspace.actions.append({"tool": tool_name})
        core.learn_from_outcome(
            reward,
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
    print(f"Episode {episode+1} reward: {episode_reward:.2f}")
    print(f"  Episode tool counts: {self.episode_tool_counts}")
    print(f"  Global productive counts: {dict(global_productive_counts)}")

# Validation with epsilon=0
original_epsilon = core.q_agent.epsilon
core.q_agent.epsilon = 0.0
workspace = SimWorkspace()
self.reset()
counts = {}
productive = ["write_file", "execute_code", "modify_self", "read_file"]
steps = 200
for step in range(steps):
    tool_name, tool_args, _ = core.decide_action(
        workspace.workspace_summary(),
        workspace.journal,
        workspace.actions
    )
    counts[tool_name] = counts.get(tool_name, 0) + 1
    workspace.actions.append({"tool": tool_name})
core.q_agent.epsilon = original_epsilon
total = sum(counts.values())
print("\n=== Validation after forced rotation training ===")
print("Deterministic policy action counts:")
for tool, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    pct = (count / total) * 100
    print(f"  {tool}: {count} ({pct:.1f}%)")
prod_counts = {t: counts.get(t,0) for t in productive}
total_prod = sum(prod_counts.values())
if total_prod > 0:
    print("\nProductive distribution:")
    for tool in productive:
        pct = (prod_counts[tool] / total_prod) * 100
        print(f"  {tool}: {prod_counts[tool]} ({pct:.1f}%)")
        if pct >= 15 and pct <= 35:
            print(f"    -> within target range")
        else:
            print(f"    -> OUTSIDE target range")
# Q-values
state = core.compute_state_vector("Files: test", "", [])
qvals = core.q_agent.nn.predict(state)
print("\nQ-values for sample state:")
tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
              "modify_self", "declare_death", "list_issues", "read_issue",
              "comment_issue", "create_issue", "close_issue"]
for i, name in enumerate(tool_names):
    print(f"  {name}: {qvals[i]:.3f}")
best_idx = max(range(len(qvals)), key=lambda i: qvals[i])
print(f"Best action (Q): {tool_names[best_idx]}")

# Save model
save_dir = "artifacts/agi_core_continuous_trained_gen34_forced"
os.makedirs(save_dir, exist_ok=True)
core.save(save_dir)
print(f"\nModel saved to {save_dir}")