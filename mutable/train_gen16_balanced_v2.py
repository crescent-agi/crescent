#!/usr/bin/env python3
"""
Train AGI Core Continuous with Generation 15 balancing v2 reward function.
Load previously balanced model and fine-tune with higher scaling factor.
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
from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from collections import deque
# Import the balancing reward function v2
from new_reward_gen16_balanced_v2 import compute_reward_gen16_balanced as compute_reward

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
        self.steps_per_episode = 10  # default, will be updated
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
        """Generate a summary string of workspace."""
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        """Simulate tool execution with realistic outcomes."""
        # Default success
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
            # Simulate execution: if code contains "error", produce stderr
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
            # Only allow modifying existing files
            if filepath in self.files:
                self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Cannot modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            # Simulate GitHub issue operations
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result
    def update_state(self, tool_name, tool_args):
        """Update workspace state after tool execution."""
        # Already handled in tool_result
        pass

def run_training(episodes=100, steps_per_episode=10, feature_dim=30, hidden_size=32):
    """Train AGI Core Continuous with balancing v2."""
    print(f"Starting balancing v2 training: {episodes} episodes, {steps_per_episode} steps per episode")
    # Load previously balanced model
    core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hidden_size, learning_rate=0.01, exploration_rate=0.3, epsilon_decay=0.95, epsilon_min=0.01, use_features=True)
    save_dir = "artifacts/agi_core_continuous_trained_gen15_balanced"
    if os.path.exists(save_dir):
        core.load(save_dir)
        print(f"Loaded previously balanced model from {save_dir}")
    else:
        print("WARNING: No previously balanced model found, starting fresh")
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
    for episode in range(episodes):
        # Reset per-episode usage tracking
        self.reset()
        self.steps_per_episode = steps_per_episode
        episode_reward = 0.0
        for step in range(steps_per_episode):
            # AGI Core decides action
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            # Simulate tool result
            tool_result = workspace.tool_result(tool_name, tool_args)
            # Compute reward using agent_brain's reward function
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            episode_reward += reward
            # Update stats
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
                # Track non-productive tools
                if tool_name in ["list_files", "write_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
                    stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
            # Update workspace state (already done in tool_result)
            workspace.update_state(tool_name, tool_args)
            workspace.actions.append({"tool": tool_name, "step": step})
            # Learn from outcome
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
        stats['episode_rewards'].append(episode_reward)
        stats['total_reward'] += episode_reward
        if core.q_agent:
            core.q_agent.decay_epsilon()
        if (episode + 1) % 5 == 0:
            avg_reward = sum(stats['episode_rewards'][-5:]) / 5
            print(f"Episode {episode+1}: avg reward last 5={avg_reward:.2f}, deaths={stats['declare_death_count']}")
            # Print top actions
            top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
            # Print non-productive counts
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
    # Compute productive tool distribution (excluding non-productive and death)
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    if total_productive > 0:
        print("\nProductive tool distribution:")
        for tool in productive_tools:
            count = productive_counts[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)")
            # Check if within 15-35%
            if percentage >= 15 and percentage <= 35:
                print(f"    -> within target range")
            else:
                print(f"    -> OUTSIDE target range")
    # Save trained core
    save_dir = "artifacts/agi_core_continuous_trained_gen16_balanced_v2"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"\nTrained AGI Core Continuous saved to {save_dir}")
    # Save training stats
    with open(os.path.join(save_dir, "training_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time = time.time()
    core, stats = run_training(episodes=30, steps_per_episode=10)
    elapsed = time.time() - start_time
    print(f"Training took {elapsed:.1f} seconds")
    print("Done.")