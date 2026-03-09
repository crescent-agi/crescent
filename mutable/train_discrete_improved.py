#!/usr/bin/env python3
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

from agi_core import AGICore
import random
import json
import os
import time
from collections import deque

# Import the reward function from agent_brain
import agent_brain

class MockBrain:
    def __init__(self):
        self.recent_tools = deque(maxlen=5)
        self.last_tool = None
    def _compute_reward(self, tool_name, tool_args, tool_result):
        return agent_brain.AgentBrain._compute_reward(self, tool_name, tool_args, tool_result)

brain = MockBrain()

# Simulation environment (same as run_training)
class SimWorkspace:
    """Simulates a simple workspace with files and journal."""
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
            "agent_brain.py": "# Agent Brain",
            "world_model.py": "# World Model",
            "neural_q.py": "# Neural Q",
        }
        self.journal = ""
        self.actions = []
    
    def workspace_summary(self):
        """Generate a summary string of workspace."""
        file_list = ", ".join(sorted(self.files.keys()))
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

def run_training(core, total_episodes=150, steps_per_episode=20, use_planner=False, planner_iterations=30, planner_depth=5):
    """Train core with or without planner."""
    workspace = SimWorkspace()
    stats = {
        'episode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
    }
    # Configure planner
    if use_planner and core.world_model and core.q_agent:
        from mcts_planner import MCTSPlanner
        core.planner = MCTSPlanner(core.world_model, core.q_agent, core.action_size, core.state_size,
                                   max_iterations=planner_iterations, max_depth=planner_depth)
        print(f"Planner enabled (iterations={planner_iterations}, depth={planner_depth})")
    else:
        core.planner = None
        print("Planner disabled")
    
    # Epsilon decay
    initial_epsilon = core.q_agent.epsilon if core.q_agent else 0.1
    for episode in range(total_episodes):
        episode_reward = 0.0
        # Decay epsilon linearly
        if core.q_agent:
            progress = episode / total_episodes
            core.q_agent.epsilon = initial_epsilon * (1 - progress) + 0.01
        for step in range(steps_per_episode):
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = brain._compute_reward(tool_name, tool_args, tool_result)
            episode_reward += reward
            # Update stats
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            # Learn
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            workspace.actions.append({"tool": tool_name, "step": step})
        stats['episode_rewards'].append(episode_reward)
        stats['total_reward'] += episode_reward
        if (episode + 1) % 25 == 0:
            avg_reward = sum(stats['episode_rewards'][-25:]) / 25
            eps = core.q_agent.epsilon if core.q_agent else None
            print(f"Episode {episode+1}: avg reward last 25={avg_reward:.2f}, epsilon={eps}")
            top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
    return stats

def evaluate(core, eval_episodes=10, steps_per_episode=20):
    """Run evaluation without learning."""
    workspace = SimWorkspace()
    action_counts = {}
    total_reward = 0.0
    # Disable exploration for evaluation
    original_epsilon = None
    if core.q_agent:
        original_epsilon = core.q_agent.epsilon
        core.q_agent.epsilon = 0.0
    for episode in range(eval_episodes):
        episode_reward = 0.0
        for step in range(steps_per_episode):
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = brain._compute_reward(tool_name, tool_args, tool_result)
            episode_reward += reward
            action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
            workspace.actions.append({"tool": tool_name, "step": step})
        total_reward += episode_reward
        print(f"Eval episode {episode+1}: reward {episode_reward:.2f}")
    avg_reward = total_reward / eval_episodes
    print(f"Average reward per episode: {avg_reward:.2f}")
    print("Action distribution:")
    for tool, count in sorted(action_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {tool}: {count}")
    # Restore epsilon
    if core.q_agent and original_epsilon is not None:
        core.q_agent.epsilon = original_epsilon
    return avg_reward, action_counts

def main():
    start_time = time.time()
    # Create AGI Core
    core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
    print(f"AGI Core created with state_size={core.state_size}, action_size={core.action_size}")
    
    # Phase 1: Train without planner
    print("\n=== Phase 1: Training without planner (100 episodes) ===")
    stats1 = run_training(core, total_episodes=100, steps_per_episode=20, use_planner=False)
    
    # Save intermediate model
    os.makedirs("artifacts/agi_core_phase1_v2", exist_ok=True)
    core.save("artifacts/agi_core_phase1_v2")
    print("Saved phase1 model.")
    
    # Phase 2: Train with planner (reduced iterations)
    print("\n=== Phase 2: Training with planner (50 episodes) ===")
    stats2 = run_training(core, total_episodes=50, steps_per_episode=20, use_planner=True, planner_iterations=20, planner_depth=4)
    
    # Evaluation
    print("\n=== Evaluation (10 episodes) ===")
    eval_avg, eval_counts = evaluate(core, eval_episodes=10, steps_per_episode=20)
    
    # Save final trained core
    save_dir = "artifacts/agi_core_trained_v2"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"\nTrained AGI Core saved to {save_dir}")
    
    # Save combined stats
    stats = {
        "phase1": stats1,
        "phase2": stats2,
        "evaluation": {"avg_reward": eval_avg, "action_counts": eval_counts},
        "total_training_steps": 100*20 + 50*20,
        "total_training_reward": stats1['total_reward'] + stats2['total_reward'],
    }
    with open(os.path.join(save_dir, "training_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    
    elapsed = time.time() - start_time
    print(f"\nTotal training time: {elapsed:.1f} seconds")
    print("Exhaustive training complete.")

if __name__ == "__main__":
    main()