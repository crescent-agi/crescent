#!/usr/bin/env python3
"""
Quick experiment to see if reward function improvements lead to better performance.
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

# Sim workspace
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

def evaluate(core, episodes=5, steps=10, epsilon=0.0):
    workspace = SimWorkspace()
    original_epsilon = core.q_agent.epsilon if core.q_agent else None
    if core.q_agent:
        core.q_agent.epsilon = epsilon
    total_reward = 0.0
    action_counts = {}
    for ep in range(episodes):
        ep_reward = 0.0
        for step in range(steps):
            tool_name, tool_args, conf = core.decide_action(workspace.workspace_summary(), workspace.journal, workspace.actions)
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            ep_reward += reward
            action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
            workspace.actions.append({"tool": tool_name})
        total_reward += ep_reward
    avg_reward = total_reward / episodes
    if core.q_agent and original_epsilon is not None:
        core.q_agent.epsilon = original_epsilon
    return avg_reward, action_counts

def train(core, episodes=10, steps_per_episode=10):
    core.planner = None
    workspace = SimWorkspace()
    total_reward = 0.0
    action_counts = {}
    for ep in range(episodes):
        ep_reward = 0.0
        for step in range(steps_per_episode):
            tool_name, tool_args, conf = core.decide_action(workspace.workspace_summary(), workspace.journal, workspace.actions)
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            ep_reward += reward
            action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
            core.learn_from_outcome(reward, workspace.workspace_summary(), workspace.journal, workspace.actions)
            workspace.actions.append({"tool": tool_name})
        total_reward += ep_reward
        print(f"Episode {ep+1}: reward {ep_reward:.2f}")
    return total_reward, action_counts

print("=== Quick Experiment ===")
core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
print("Baseline evaluation (random)...")
baseline_avg, baseline_actions = evaluate(core, episodes=5, steps=10, epsilon=1.0)
print(f"Baseline avg reward: {baseline_avg:.2f}")
print("Training...")
train_reward, train_actions = train(core, episodes=10, steps_per_episode=10)
print(f"Total training reward: {train_reward:.2f}")
print("Trained evaluation...")
trained_avg, trained_actions = evaluate(core, episodes=5, steps=10, epsilon=0.0)
print(f"Trained avg reward: {trained_avg:.2f}")
improvement = trained_avg - baseline_avg
print(f"Improvement: {improvement:.2f}")
if improvement > 0:
    print("â Improvement observed!")
else:
    print("â ï¸  No improvement.")
# Save model
import os
os.makedirs('artifacts/quick_exp', exist_ok=True)
core.save('artifacts/quick_exp')
print("Model saved.")