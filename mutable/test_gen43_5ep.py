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
import os
from collections import deque
from new_reward_gen43 import compute_reward_gen43 as compute_reward
from new_reward_gen43 import compute_terminal_bonus_gen43

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

print("Starting 5 episodes test with gen43 reward")
core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                         learning_rate=0.001, exploration_rate=0.5,
                         epsilon_decay=0.995, epsilon_min=0.5, use_features=True)
save_dir = "artifacts/agi_core_continuous_trained_gen30"
if os.path.exists(save_dir):
    core.load(save_dir)
    print(f"Loaded previous model from {save_dir}")

# Monkey-patch masking (same as before)
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
    print("Patched masking")
except ImportError as e:
    print(f"Could not patch: {e}")

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
        return "Files: " + ", ".join(self.files.keys())
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
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            result["stdout"] = "Simulated output"
            result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note + "\\n"
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
        else:
            result["issues"] = []
        return result
    def update_state(self, tool_name, tool_args):
        pass

for episode in range(5):
    self.reset()
    workspace = SimWorkspace()
    for step in range(20):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
        workspace.actions.append({"tool": tool_name, "step": step})
        core.learn_from_outcome(
            reward,
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        if step == 19:
            terminal_bonus = compute_terminal_bonus_gen43(self, sum(self.episode_tool_counts.values()))
            if terminal_bonus > 0:
                print(f"Episode {episode+1} terminal bonus {terminal_bonus}")
    if core.q_agent:
        core.q_agent.decay_epsilon()
    print(f"Episode {episode+1} done, episode tool counts: {self.episode_tool_counts}")
print("Test completed.")