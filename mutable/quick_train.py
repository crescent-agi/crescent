#!/usr/bin/env python3
"""
Quick training run (50 episodes total).
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

from agi_core import AGICore
import agent_brain
compute_reward = agent_brain.AgentBrain._compute_reward

class DummySelf: pass
self = DummySelf()

# Sim workspace (simplified)
class SimWorkspace:
    def __init__(self):
        self.files = {"inherited_notes.md": "# Inherited Notes"}
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        return f"Files: {', '.join(self.files.keys())}"
    def tool_result(self, tool_name, tool_args):
        result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                result["content"] = self.files[filepath]
            else:
                result["error"] = "File not found"
                result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            result["entries"] = [{"name": name, "type": "file"} for name in self.files]
        elif tool_name == "execute_code":
            result["stdout"] = "output"
            result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note + "\n"
            result["note"] = "Added to journal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                self.files[filepath] = tool_args.get("content", "")
                result["message"] = f"Modified {filepath}"
            else:
                result["error"] = "File not found"
                result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You died"
        else:
            result["success"] = True
        return result

def train_phase(core, episodes, steps, use_planner=False):
    workspace = SimWorkspace()
    action_counts = {}
    total_reward = 0
    if use_planner and core.world_model and core.q_agent:
        from mcts_planner import MCTSPlanner
        core.planner = MCTSPlanner(core.world_model, core.q_agent, core.action_size, core.state_size,
                                   max_iterations=10, max_depth=3)
        print(f"Planner enabled (iterations=10)")
    else:
        core.planner = None
    for ep in range(episodes):
        ep_reward = 0
        for step in range(steps):
            tool_name, tool_args, conf = core.decide_action(workspace.workspace_summary(), workspace.journal, workspace.actions)
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            ep_reward += reward
            action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
            core.learn_from_outcome(reward, workspace.workspace_summary(), workspace.journal, workspace.actions)
            workspace.actions.append({"tool": tool_name})
        total_reward += ep_reward
        if (ep+1) % 10 == 0:
            print(f"Episode {ep+1}: reward {ep_reward:.2f}")
    avg_reward = total_reward / episodes
    print(f"Phase done: avg reward per episode {avg_reward:.2f}, top actions: {sorted(action_counts.items(), key=lambda x: x[1], reverse=True)[:5]}")
    return total_reward, action_counts

def evaluate(core, episodes=5, steps=10):
    workspace = SimWorkspace()
    action_counts = {}
    total_reward = 0
    original_epsilon = core.q_agent.epsilon if core.q_agent else None
    if core.q_agent:
        core.q_agent.epsilon = 0.0
    for ep in range(episodes):
        ep_reward = 0
        for step in range(steps):
            tool_name, tool_args, conf = core.decide_action(workspace.workspace_summary(), workspace.journal, workspace.actions)
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            ep_reward += reward
            action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
            workspace.actions.append({"tool": tool_name})
        total_reward += ep_reward
    avg = total_reward / episodes
    print(f"Evaluation: avg reward {avg:.2f}, action dist: {action_counts}")
    if core.q_agent and original_epsilon is not None:
        core.q_agent.epsilon = original_epsilon
    return avg, action_counts

import time
start = time.time()
core = AGICore(state_size=50, hidden_size=16, learning_rate=0.01)
print("Starting quick training (30 episodes without planner)...")
train_phase(core, episodes=30, steps=15, use_planner=False)
print("\nContinuing training with planner (20 episodes)...")
train_phase(core, episodes=20, steps=15, use_planner=True)
print("\nEvaluating...")
eval_avg, eval_counts = evaluate(core, episodes=5, steps=15)
# Save model
import os, json
os.makedirs('artifacts/quick_trained', exist_ok=True)
core.save('artifacts/quick_trained')
print("Model saved to artifacts/quick_trained")
end = time.time()
print(f"Total time: {end-start:.1f}s")