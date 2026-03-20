#!/usr/bin/env python3
"""
Train AGI Core Continuous with Generation 48 reward: Increased least-used bonus (10000), increased most-used penalty (500),
added global deficit bonus for tools below 15% proportion, larger terminal bonus (20000).
Goal: achieve balanced productive tool distribution with positive average reward.
Fixes: reset workspace.actions each episode, add terminal bonus, adjust epsilon_min, entropy coefficient 2.0.
"""
import sys
sys.path.insert(0, '.')
# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

# Use the updated neural_q_continuous (with death exploration allowed)
import neural_q_continuous
sys.modules['neural_q_continuous'] = neural_q_continuous

import patch_weight_clipping
from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from collections import deque
# Import the new reward function
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
        self.steps_per_episode = 10  # default, will be updated
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
        # Do not reset global counts across episodes

self = DummySelf()

# Simulation environment (same as before)
class SimWorkspace:
    """Simulates a simple workspace with files and journal."""
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
        """Simulate tool execution with realistic outcomes."""
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
        """Update workspace state after tool execution."""
        # Already handled in tool_result
        pass

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

# Monkey-patch the neural_q_continuous choose_action to mask non-productive tools during both exploration and exploitation
try:
    from neural_q_continuous import NeuralQLearningAgentContinuous
    original_choose_action = NeuralQLearningAgentContinuous.choose_action
    def masked_choose_action(self, state_vector):
        """Epsilon-greedy with masking of non-productive tools during exploration and exploitation."""
        tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                      "modify_self", "declare_death", "list_issues", "read_issue",
                      "comment_issue", "create_issue", "close_issue"]
        non_productive_indices = [i for i, name in enumerate(tool_names) 
                                  if name in ["list_files", "write_note", "list_issues", "read_issue",
                                              "comment_issue", "create_issue", "close_issue"]]
        productive_indices = [0, 1, 3, 5]  # read_file, write_file, execute_code, modify_self
        death_index = 6
        allowed_indices = productive_indices + [death_index]  # allow death for exploration
        if random.random() < self.epsilon:
            # Random exploration: allow death but mask non-productive tools
            allowed = [i for i in range(self.action_size) 
                       if i not in non_productive_indices]
            if allowed:
                return random.choice(allowed)
            else:
                return random.randrange(self.action_size)
        else:
            # Exploitation: only choose among productive tools (exclude death and non-productive)
            q_values = self.nn.predict(state_vector)
            # Find best among productive indices
            best_q = max(q_values[i] for i in productive_indices)
            best_actions = [i for i in productive_indices if q_values[i] == best_q]
            return random.choice(best_actions)
    NeuralQLearningAgentContinuous.choose_action = masked_choose_action
    print("Patched NeuralQLearningAgentContinuous.choose_action to mask non-productive tools and exclude death from exploitation.")
except ImportError as e:
    print(f"Could not patch neural_q_continuous: {e}")

# Monkey-patch entropy coefficient to 2.0
try:
    from neural_q_continuous import NeuralQLearningAgentContinuous
    original_learn = NeuralQLearningAgentContinuous.learn
    def learn_with_entropy2(self, state_vector, action, reward, next_state_vector, done, entropy_coeff=2.0):
        """Override default entropy_coeff to 2.0."""
        return original_learn(self, state_vector, action, reward, next_state_vector, done, entropy_coeff=entropy_coeff)
    NeuralQLearningAgentContinuous.learn = learn_with_entropy2
    print("Patched NeuralQLearningAgentContinuous.learn to set entropy_coeff=2.0")
except ImportError as e:
    print(f"Could not patch entropy coefficient: {e}")

def run_training(episodes=45, steps_per_episode=20, feature_dim=30, hidden_size=32):
    """Train AGI Core Continuous with balancing for generation 48."""
    print(f"Starting Generation 48 training: {episodes} episodes, {steps_per_episode} steps per episode")
    # Load previous model (gen32)
    core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hidden_size,
                             learning_rate=0.001, exploration_rate=0.5,
                             epsilon_decay=1.0, epsilon_min=0.5, use_features=True)  # epsilon_decay=1.0 to keep exploration constant
    save_dir = "artifacts/agi_core_continuous_trained_gen32"
    if os.path.exists(save_dir):
        core.load(save_dir)
        print(f"Loaded previous model from {save_dir}")
    else:
        print(f"Warning: {save_dir} not found, starting fresh")
    
    stats = {
        'episode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
        'other_count': 0,
        'non_productive_counts': {},
    }
    for episode in range(episodes):
        # Reset per-episode usage tracking
        self.reset()
        self.steps_per_episode = steps_per_episode
        # Create fresh workspace each episode to avoid actions list growth
        workspace = SimWorkspace()
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
            # Track episode tool counts for terminal bonus
            self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
            # If this is the last step of episode (or terminated), add terminal bonus
            is_last_step = (step == steps_per_episode - 1) or episode_terminated
            if is_last_step:
                terminal_bonus = compute_terminal_bonus_gen48(self, sum(self.episode_tool_counts.values()))
                reward += terminal_bonus
                if terminal_bonus > 0:
                    print(f"Episode {episode+1} step {step+1}: added terminal bonus {terminal_bonus}")
            if reward <= -10000.0:
                episode_terminated = True
            episode_reward += reward
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "declare_death":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file":
                stats['write_file_count'] += 1
            elif tool_name == "execute_code":
                stats['execute_code_count'] += 1
            elif tool_name == "read_file":
                stats['read_file_count'] += 1
            else:
                stats['other_count'] += 1
                if tool_name in ["list_files", "write_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
                    stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
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
        # No epsilon decay because epsilon_decay=1.0
        # Every 25 episodes, run validation with epsilon=0
        if (episode + 1) % 25 == 0:
            print(f"\n--- Validation after episode {episode+1} ---")
            validation_stats = run_validation(core, steps=200)
            print(f"  Non-productive actions: {validation_stats['non_productive_total']}")
            print(f"  Average reward per step: {validation_stats['average_reward']:.3f}")
            print(f"  Productive distribution:")
            for tool, perc in validation_stats['productive_distribution'].items():
                print(f"    {tool}: {perc:.1f}%")
                if perc >= 15 and perc <= 35:
                    print(f"      -> within target range")
                else:
                    print(f"      -> OUTSIDE target range")
        if (episode + 1) % 5 == 0:
            avg_reward = sum(stats['episode_rewards'][-5:]) / 5
            print(f"Episode {episode+1}: avg reward last 5={avg_reward:.2f}, deaths={stats['declare_death_count']}")
            top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
            if stats['non_productive_counts']:
                print(f"  Non-productive actions: {stats['non_productive_counts']}")
            else:
                print(f"  Non-productive actions: zero")
    print("\nTraining finished.")
    total_steps = episodes * steps_per_episode
    print(f"Total reward: {stats['total_reward']:.2f}")
    avg_reward_per_step = stats['total_reward'] / total_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
    print("\nAction distribution:")
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_steps) * 100
        print(f"  {tool}: {count} ({percentage:.1f}%)")
    print("\nNon-productive tool counts:")
    non_prod_total = sum(stats['non_productive_counts'].values())
    print(f"  Total non-productive actions: {non_prod_total}")
    for tool, count in stats['non_productive_counts'].items():
        print(f"    {tool}: {count}")
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    if total_productive > 0:
        print("\nProductive tool distribution:")
        for tool in productive_tools:
            count = productive_counts[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)")
            if percentage >= 15 and percentage <= 35:
                print(f"    -> within target range")
            else:
                print(f"    -> OUTSIDE target range")
    # Save trained core
    save_dir = "artifacts/agi_core_continuous_trained_gen34_v3"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"\nTrained AGI Core Continuous saved to {save_dir}")
    with open(os.path.join(save_dir, "training_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time = time.time()
    print("=== Generation 48: Increased least-used bonus (10000), increased most-used penalty (500), global deficit bonus ===")
    print("Goal: balance productive tool Q-values under deterministic policy.")
    # Run full training (45 episodes)
    core, stats = run_training(episodes=45, steps_per_episode=20)
    elapsed = time.time() - start_time
    print(f"\nTotal training took {elapsed:.1f} seconds")
    # Final validation with epsilon=0
    print("\n=== Final validation (epsilon=0, 1000 steps) ===")
    final_stats = run_validation(core, steps=1000)
    print(f"Non-productive actions: {final_stats['non_productive_total']}")
    print(f"Average reward per step: {final_stats['average_reward']:.3f}")
    print(f"Productive distribution:")
    for tool, perc in final_stats['productive_distribution'].items():
        print(f"  {tool}: {perc:.1f}%")
        if perc >= 15 and perc <= 35:
            print(f"    -> within target range")
        else:
            print(f"    -> OUTSIDE target range")
    # Check goal criteria
    success = True
    if final_stats['non_productive_total'] > 0:
        print("FAIL: Non-productive actions present.")
        success = False
    if final_stats['average_reward'] <= 2.0:
        print(f"FAIL: Average reward {final_stats['average_reward']:.3f} <= 2.0")
        success = False
    for tool, perc in final_stats['productive_distribution'].items():
        if perc < 15 or perc > 35:
            print(f"FAIL: {tool} distribution {perc:.1f}% outside 15-35%")
            success = False
    if success:
        print("\n*** SUCCESS: All goals achieved! ***")
    else:
        print("\n*** GOALS NOT MET ***")
    print("Done.")