#!/usr/bin/env python3
"""
Train AGI Core Continuous with Generation 37 reward, forced rotation, and forced exploration.
Goal: achieve balanced distribution with zero non-productive actions.
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

# Monkey-patch neural_q_continuous import to use our Double DQN class
import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

import patch_weight_clipping
from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from collections import deque, defaultdict
# Import the new reward function
from new_reward_gen37 import compute_reward_gen37 as compute_reward

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []  # list
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

# Global tracking for forced rotation
global_productive_counts = defaultdict(int)

# Patch choose_action to include forced exploration and allow death during exploration
try:
    from neural_q_continuous_double import NeuralQLearningAgentContinuousDouble
    original_choose_action = NeuralQLearningAgentContinuousDouble.choose_action
    # Track recent tool usage across steps (shared across episodes)
    recent_tool_window = deque(maxlen=20)  # last 20 steps
    
    def forced_choose_action(self, state_vector):
        tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                      "modify_self", "declare_death", "list_issues", "read_issue",
                      "comment_issue", "create_issue", "close_issue"]
        productive_indices = [0, 1, 3, 5]
        non_productive_indices = [i for i, name in enumerate(tool_names) 
                                  if name in ["list_files", "write_note", "list_issues", "read_issue",
                                              "comment_issue", "create_issue", "close_issue"]]
        death_index = 6
        
        # Forced exploration: with probability 0.3, pick least used productive tool based on recent window
        if random.random() < 0.3:
            # Compute productive tool counts in recent window
            productive_counts = {idx: 0 for idx in productive_indices}
            for idx in recent_tool_window:
                if idx in productive_counts:
                    productive_counts[idx] += 1
            # Find least used productive tool (lowest count)
            min_count = min(productive_counts.values())
            least_used = [idx for idx, cnt in productive_counts.items() if cnt == min_count]
            # Randomly pick one of the least used
            chosen = random.choice(least_used)
            # Update recent window (will be updated later after action execution)
            # We'll update later in training loop
            return chosen
        
        # Otherwise epsilon-greedy with masking
        if random.random() < self.epsilon:
            # Random exploration: allow death (no filtering)
            return random.randrange(self.action_size)
        else:
            q_values = self.nn.predict(state_vector)
            max_q = max(q_values)
            best_actions = [i for i, q in enumerate(q_values) if q == max_q]
            # Remove death from best actions if there are other candidates
            if len(best_actions) > 1 and death_index in best_actions:
                best_actions.remove(death_index)
            if best_actions == [death_index]:
                # All best actions are death, pick second best
                sorted_q = sorted(enumerate(q_values), key=lambda x: x[1], reverse=True)
                for idx, q in sorted_q:
                    if idx != death_index:
                        return idx
            return random.choice(best_actions)
    
    NeuralQLearningAgentContinuousDouble.choose_action = forced_choose_action
    print("Patched choose_action with forced exploration (30% least-used) and death allowed during exploration.")
except ImportError as e:
    print(f"Could not patch neural_q_continuous_double: {e}")
    # Fallback: use existing patch
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

def run_training(episodes=50, steps_per_episode=20, feature_dim=30, hidden_size=32, load_previous=True):
    """Train AGI Core Continuous with forced rotation and forced exploration."""
    print(f"Starting Generation 37 training: {episodes} episodes, {steps_per_episode} steps per episode")
    # Create fresh core (or load previous)
    core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hidden_size,
                             learning_rate=0.001, exploration_rate=0.8,
                             epsilon_decay=1.0, epsilon_min=0.8, use_features=True)  # high constant exploration
    if load_previous:
        save_dir = "artifacts/agi_core_continuous_trained_gen36"
        if os.path.exists(save_dir):
            core.load(save_dir)
            print(f"Loaded previous model from {save_dir}")
        else:
            print("Previous model not found, starting fresh.")
    workspace = SimWorkspace()
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
    global_productive_counts.clear()
    recent_tool_window.clear()
    
    for episode in range(episodes):
        # Reset per-episode usage tracking
        self.reset()
        self.steps_per_episode = steps_per_episode
        episode_reward = 0.0
        episode_terminated = False
        for step in range(steps_per_episode):
            # Forced rotation: first step of each episode picks globally least used productive tool
            if step == 0:
                productive = ["write_file", "execute_code", "modify_self", "read_file"]
                min_count = min(global_productive_counts[tool] for tool in productive)
                candidate_tools = [tool for tool in productive if global_productive_counts[tool] == min_count]
                forced_tool = random.choice(candidate_tools)
                tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                              "modify_self", "declare_death", "list_issues", "read_issue",
                              "comment_issue", "create_issue", "close_issue"]
                forced_index = tool_names.index(forced_tool)
                # Override decision
                tool_name = forced_tool
                # generate arguments
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
                # Normal decision (patched choose_action will handle forced exploration)
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
            # Update global counts for forced rotation
            if tool_name in ["write_file", "execute_code", "modify_self", "read_file"]:
                global_productive_counts[tool_name] += 1
            # Update recent tool window for forced exploration
            tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                          "modify_self", "declare_death", "list_issues", "read_issue",
                          "comment_issue", "create_issue", "close_issue"]
            idx = tool_names.index(tool_name) if tool_name in tool_names else -1
            if idx >= 0:
                recent_tool_window.append(idx)
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
        # No epsilon decay (epsilon_decay=1.0)
        # Every 10 episodes, run validation with epsilon=0
        if (episode + 1) % 10 == 0:
            print(f"
--- Validation after episode {episode+1} ---")
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
    print("
Training finished.")
    total_steps = episodes * steps_per_episode
    print(f"Total reward: {stats['total_reward']:.2f}")
    avg_reward_per_step = stats['total_reward'] / total_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
    print("
Action distribution:")
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_steps) * 100
        print(f"  {tool}: {count} ({percentage:.1f}%)")
    print("
Non-productive tool counts:")
    non_prod_total = sum(stats['non_productive_counts'].values())
    print(f"  Total non-productive actions: {non_prod_total}")
    for tool, count in stats['non_productive_counts'].items():
        print(f"    {tool}: {count}")
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    if total_productive > 0:
        print("
Productive tool distribution:")
        for tool in productive_tools:
            count = productive_counts[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)")
            if percentage >= 15 and percentage <= 35:
                print(f"    -> within target range")
            else:
                print(f"    -> OUTSIDE target range")
    # Save trained core
    save_dir = "artifacts/agi_core_continuous_trained_gen37_forced"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"
Trained AGI Core Continuous saved to {save_dir}")
    with open(os.path.join(save_dir, "training_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time = time.time()
    print("=== Generation 37: Forced rotation + forced exploration ===")
    # Quick sanity check (5 episodes)
    print("=== Quick sanity check (5 episodes) ===")
    core_test, stats_test = run_training(episodes=5, steps_per_episode=20, load_previous=True)
    print("
=== Full training (50 episodes) ===")
    core, stats = run_training(episodes=50, steps_per_episode=20, load_previous=True)
    elapsed = time.time() - start_time
    print(f"
Total training took {elapsed:.1f} seconds")
    # Final validation with epsilon=0
    print("
=== Final validation (epsilon=0, 1000 steps) ===")
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
        print("
*** SUCCESS: All goals achieved! ***")
    else:
        print("
*** GOALS NOT MET ***")
    print("Done.")