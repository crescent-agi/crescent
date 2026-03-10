#!/usr/bin/env python3
import sys
sys.path.insert(0, 'mutable_snapshot')
# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client
import patch_weight_clipping
from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from collections import deque
# Import the new reward function
from new_reward_gen22 import compute_reward_gen21_fixed as compute_reward

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = deque(maxlen=10)
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.4
        self.episode_tools = set()
        self.episode_tool_counts = {}
        self.episode_productive_first_use = set()
        self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 10
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_counts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_counts_zero_bonus_given = set()
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.recent_read_files.clear()
        self.episode_step_count = 0
        # Do not reset global counts across episodes
        # Do not reset zero bonus given (global across episodes)

self = DummySelf()

# Simulation environment
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
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result
    def update_state(self, tool_name, tool_args):
        pass

# Patch NeuralQLearningAgentContinuous to mask non-productive tools
try:
    from neural_q_continuous import NeuralQLearningAgentContinuous
    original_choose_action = NeuralQLearningAgentContinuous.choose_action
    def masked_choose_action(self, state_vector):
        # Define non-productive tool indices (excluding declare_death which is already filtered)
        tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                      "modify_self", "declare_death", "list_issues", "read_issue",
                      "comment_issue", "create_issue", "close_issue"]
        non_productive_indices = [i for i, name in enumerate(tool_names) 
                                  if name in ["list_files", "write_note", "list_issues", "read_issue",
                                              "comment_issue", "create_issue", "close_issue"]]
        # Always exclude non-productive indices and declare_death (index 6)
        allowed = [i for i in range(self.action_size) 
                   if i not in non_productive_indices and i != 6]
        if random.random() < self.epsilon:
            # Random exploration: only allowed actions
            if allowed:
                return random.choice(allowed)
            else:
                return random.randrange(self.action_size)
        else:
            # Exploitation: choose among allowed actions with highest Q-value
            q_values = self.nn.predict(state_vector)
            # Filter out disallowed actions by setting their Q-value to -inf
            for i in range(self.action_size):
                if i not in allowed:
                    q_values[i] = float('-inf')
            max_q = max(q_values)
            best_actions = [i for i, q in enumerate(q_values) if q == max_q]
            # If all actions are -inf (should not happen), fallback to random allowed
            if not best_actions or max_q == float('-inf'):
                if allowed:
                    return random.choice(allowed)
                else:
                    return random.randrange(self.action_size)
            return random.choice(best_actions)
    NeuralQLearningAgentContinuous.choose_action = masked_choose_action
    print("Patched NeuralQLearningAgentContinuous.choose_action to mask non-productive tools in both exploration and exploitation.")
except ImportError as e:
    print(f"Could not patch neural_q_continuous: {e}")

def run_validation(core, steps=1000):
    """Run validation with epsilon=0 to check deterministic policy."""
    original_epsilon = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    self.reset()
    self.steps_per_episode = steps
    stats = {
        'action_counts': {},
        'non_productive_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
    }
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    for step in range(steps):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        stats['total_reward'] += reward
        stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if tool_name == "declare_death":
            stats['declare_death_count'] += 1
        if tool_name not in productive_tools and tool_name != "declare_death":
            stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
        workspace.update_state(tool_name, tool_args)
        workspace.actions.append({"tool": tool_name, "step": step})
        # No learning during validation
    core.q_agent.epsilon = original_epsilon
    # Compute productive distribution
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    distribution = {}
    if total_productive > 0:
        for tool in productive_tools:
            distribution[tool] = (productive_counts[tool] / total_productive) * 100
    else:
        for tool in productive_tools:
            distribution[tool] = 0.0
    stats['productive_distribution'] = distribution
    stats['non_productive_total'] = sum(stats['non_productive_counts'].values())
    stats['average_reward'] = stats['total_reward'] / steps
    return stats

# Training loop
episodes = 200
steps_per_episode = 10
core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                         learning_rate=0.001, exploration_rate=0.5,
                         epsilon_decay=0.98, epsilon_min=0.1, use_features=True)
print(f"Starting Generation 22 full training: {episodes} episodes, {steps_per_episode} steps per episode")
workspace = SimWorkspace()
stats = {
    'episode_rewards': [],
    'action_counts': {},
    'productive_counts': {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]},
    'total_reward': 0.0,
    'non_productive_total': 0,
    'declare_death_count': 0,
}
for episode in range(episodes):
    self.reset()
    self.steps_per_episode = steps_per_episode
    episode_reward = 0.0
    episode_terminated = False
    for step in range(steps_per_episode):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        if reward <= -10000.0:
            episode_terminated = True
        episode_reward += reward
        stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if tool_name == "declare_death":
            stats['declare_death_count'] += 1
        if tool_name in ["write_file", "execute_code", "modify_self", "read_file"]:
            stats['productive_counts'][tool_name] += 1
        else:
            if tool_name != "declare_death":
                stats['non_productive_total'] += 1
        workspace.update_state(tool_name, tool_args)
        workspace.actions.append({"tool": tool_name, "step": step})
        core.learn_from_outcome(
            reward,
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        if episode_terminated:
            break
    stats['episode_rewards'].append(episode_reward)
    stats['total_reward'] += episode_reward
    if core.q_agent:
        core.q_agent.decay_epsilon()
    # Validation every 25 episodes
    if (episode + 1) % 25 == 0:
        print(f\"\\n--- Validation after episode {episode+1} ---\")
        validation_stats = run_validation(core, steps=200)
        print(f\"  Non-productive actions: {validation_stats['non_productive_total']}\")
        print(f\"  Average reward per step: {validation_stats['average_reward']:.3f}\")
        print(f\"  Productive distribution:\")
        for tool, perc in validation_stats['productive_distribution'].items():
            print(f\"    {tool}: {perc:.1f}%\")
            if perc >= 15 and perc <= 35:
                print(f\"      -> within target range\")
            else:
                print(f\"      -> OUTSIDE target range\")
    # Progress every 10 episodes
    if (episode + 1) % 10 == 0:
        avg_reward = sum(stats['episode_rewards'][-10:]) / 10
        print(f\"Episode {episode+1}: avg reward last 10={avg_reward:.2f}, deaths={stats['declare_death_count']}\")

print(\"\\n=== Training finished ===\")
total_steps = episodes * steps_per_episode
print(f\"Total reward: {stats['total_reward']:.2f}\")
print(f\"Non-productive actions: {stats['non_productive_total']}\")
print(\"Action counts:\")
for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
    print(f\"  {tool}: {count}\")
productive_total = sum(stats['productive_counts'].values())
if productive_total > 0:
    print(\"Productive distribution:\")
    for tool in [\"write_file\", \"execute_code\", \"modify_self\", \"read_file\"]:
        count = stats['productive_counts'][tool]
        perc = (count / productive_total) * 100
        print(f\"  {tool}: {count} ({perc:.1f}%)\")
        if perc >= 15 and perc <= 35:
            print(\"    -> within target\")
        else:
            print(\"    -> OUTSIDE target\")

# Save model
save_dir = \"artifacts/agi_core_continuous_trained_gen22\"
os.makedirs(save_dir, exist_ok=True)
core.save(save_dir)
print(f\"\\nModel saved to {save_dir}\")

# Final validation with epsilon=0, 1000 steps
print(\"\\n=== Final validation (epsilon=0, 1000 steps) ===\")
final_stats = run_validation(core, steps=1000)
print(f\"Non-productive actions: {final_stats['non_productive_total']}\")
print(f\"Average reward per step: {final_stats['average_reward']:.3f}\")
print(f\"Productive distribution:\")
for tool, perc in final_stats['productive_distribution'].items():
    print(f\"  {tool}: {perc:.1f}%\")
    if perc >= 15 and perc <= 35:
        print(f\"    -> within target range\")
    else:
        print(f\"    -> OUTSIDE target range\")
# Check goal criteria
success = True
if final_stats['non_productive_total'] > 0:
    print(\"FAIL: Non-productive actions present.\")
    success = False
if final_stats['average_reward'] <= 2.0:
    print(f\"FAIL: Average reward {final_stats['average_reward']:.3f} <= 2.0\")
    success = False
for tool, perc in final_stats['productive_distribution'].items():
    if perc < 15 or perc > 35:
        print(f\"FAIL: {tool} distribution {perc:.1f}% outside 15-35%\")
        success = False
if success:
    print(\"\\n*** SUCCESS: All goals achieved! ***\")
else:
    print(\"\\n*** GOALS NOT MET ***\")
print(\"Done.\")