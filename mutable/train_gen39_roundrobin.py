#!/usr/bin/env python3
"""
Train with round-robin forced selection of productive tools.
Goal: force equal usage and hope Q-values equalize.
"""
import sys
sys.path.insert(0, '.')
# Mock core.llm_client
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from new_reward_gen38 import compute_reward_gen38 as compute_reward

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_total = 0
        self.episode_tool_counts = {}
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        self.episode_tool_counts.clear()

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

def run_validation(core, steps=500):
    original_epsilon = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    self.reset()
    counts = {}
    total_reward = 0.0
    productive = ["write_file", "execute_code", "modify_self", "read_file"]
    for step in range(steps):
        tool_name, tool_args, _ = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        total_reward += reward
        counts[tool_name] = counts.get(tool_name, 0) + 1
        workspace.actions.append({"tool": tool_name})
    core.q_agent.epsilon = original_epsilon
    total = sum(counts.values())
    prod_counts = {t: counts.get(t,0) for t in productive}
    total_prod = sum(prod_counts.values())
    distribution = {}
    if total_prod > 0:
        for tool in productive:
            distribution[tool] = (prod_counts[tool] / total_prod) * 100
    else:
        for tool in productive:
            distribution[tool] = 0.0
    non_prod_total = sum(counts.get(t,0) for t in counts if t not in productive and t != "declare_death")
    avg_reward = total_reward / steps
    return {
        'action_counts': counts,
        'productive_distribution': distribution,
        'non_productive_total': non_prod_total,
        'average_reward': avg_reward
    }

def run_training(episodes=30, steps_per_episode=20, load_previous=True):
    print(f"Starting round-robin training: {episodes} episodes, {steps_per_episode} steps per episode")
    core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                             learning_rate=0.001, exploration_rate=0.8,
                             epsilon_decay=1.0, epsilon_min=0.8, use_features=True)
    if load_previous:
        save_dir = "artifacts/agi_core_continuous_trained_gen36"
        if os.path.exists(save_dir):
            core.load(save_dir)
            print(f"Loaded previous model from {save_dir}")
        else:
            print("Previous model not found, starting fresh.")
    workspace = SimWorkspace()
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    tool_cycle = productive_tools * (steps_per_episode // 4 + 1)
    
    for episode in range(episodes):
        self.reset()
        episode_reward = 0.0
        for step in range(steps_per_episode):
            # Round-robin forced selection
            forced_tool = tool_cycle[step]
            tool_name = forced_tool
            # generate simple arguments
            if tool_name == "read_file":
                tool_args = {"filepath": "inherited_notes.md"}
            elif tool_name == "write_file":
                tool_args = {"filepath": "artifacts/roundrobin.txt", "content": "Round robin"}
            elif tool_name == "execute_code":
                tool_args = {"code": "print('round robin')", "language": "python"}
            elif tool_name == "modify_self":
                tool_args = {"filepath": "strategy.md", "content": "# Round robin"}
            else:
                tool_args = {}
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            episode_reward += reward
            workspace.actions.append({"tool": tool_name})
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
        # No epsilon decay
        if (episode + 1) % 5 == 0:
            print(f"Episode {episode+1}: reward {episode_reward:.2f}")
            # Quick validation
            val = run_validation(core, steps=100)
            print(f"  Validation: non-prod {val['non_productive_total']}, avg reward {val['average_reward']:.3f}")
            print(f"  Distribution: {val['productive_distribution']}")
    # Save model
    save_dir = "artifacts/agi_core_continuous_trained_gen39_roundrobin"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"Saved model to {save_dir}")
    return core

if __name__ == "__main__":
    start_time = time.time()
    print("=== Generation 39: Round-robin forced selection ===")
    core = run_training(episodes=30, steps_per_episode=20, load_previous=True)
    elapsed = time.time() - start_time
    print(f"Training took {elapsed:.1f} seconds")
    # Final validation
    print("\n=== Final validation (epsilon=0, 500 steps) ===")
    final_stats = run_validation(core, steps=500)
    print(f"Non-productive actions: {final_stats['non_productive_total']}")
    print(f"Average reward per step: {final_stats['average_reward']:.3f}")
    print("Productive distribution:")
    for tool, perc in final_stats['productive_distribution'].items():
        print(f"  {tool}: {perc:.1f}%")
        if perc >= 15 and perc <= 35:
            print("    -> within target range")
        else:
            print("    -> OUTSIDE target range")
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