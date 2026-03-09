#!/usr/bin/env python3
"""
Training experiment to evaluate reward function improvements.
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
        self.files = {
            "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
        }
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
            self.journal += note + "\\n"
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

def evaluate(core, episodes=10, steps=20, epsilon=0.0):
    """Evaluate core with fixed epsilon."""
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
    # Restore epsilon
    if core.q_agent and original_epsilon is not None:
        core.q_agent.epsilon = original_epsilon
    return avg_reward, action_counts

def train(core, episodes=50, steps_per_episode=20):
    """Train core without planner."""
    core.planner = None
    workspace = SimWorkspace()
    total_reward = 0.0
    action_counts = {}
    # Linear epsilon decay
    initial_epsilon = core.q_agent.epsilon if core.q_agent else 0.1
    for ep in range(episodes):
        ep_reward = 0.0
        if core.q_agent:
            progress = ep / episodes
            core.q_agent.epsilon = initial_epsilon * (1 - progress) + 0.01
        for step in range(steps_per_episode):
            tool_name, tool_args, conf = core.decide_action(workspace.workspace_summary(), workspace.journal, workspace.actions)
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            ep_reward += reward
            action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
            core.learn_from_outcome(reward, workspace.workspace_summary(), workspace.journal, workspace.actions)
            workspace.actions.append({"tool": tool_name})
        total_reward += ep_reward
        if (ep + 1) % 10 == 0:
            avg = total_reward / (ep + 1)
            print(f"Episode {ep+1}: avg reward so far {avg:.2f}, epsilon {core.q_agent.epsilon if core.q_agent else 'N/A'}")
    return total_reward, action_counts

import time
def main():
    print("=== AGI Core Training Experiment ===")
    print("Initializing core...")
    core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
    print(f"State size: {core.state_size}, Action size: {core.action_size}")
    
    # Baseline evaluation (random policy)
    print("\\n--- Baseline evaluation (epsilon=1.0) ---")
    baseline_avg, baseline_actions = evaluate(core, episodes=10, steps=20, epsilon=1.0)
    print(f"Baseline average reward: {baseline_avg:.2f}")
    print("Baseline action distribution:")
    for tool, count in sorted(baseline_actions.items(), key=lambda x: x[1], reverse=True):
        print(f"  {tool}: {count}")
    
    # Training
    print("\\n--- Training (50 episodes, 20 steps each) ---")
    start_train = time.time()
    train_reward, train_actions = train(core, episodes=50, steps_per_episode=20)
    end_train = time.time()
    print(f"Training completed in {end_train - start_train:.1f} seconds")
    print(f"Total training reward: {train_reward:.2f}")
    
    # Trained evaluation (epsilon=0.0)
    print("\\n--- Trained evaluation (epsilon=0.0) ---")
    trained_avg, trained_actions = evaluate(core, episodes=10, steps=20, epsilon=0.0)
    print(f"Trained average reward: {trained_avg:.2f}")
    print("Trained action distribution:")
    for tool, count in sorted(trained_actions.items(), key=lambda x: x[1], reverse=True):
        print(f"  {tool}: {count}")
    
    # Improvement
    improvement = trained_avg - baseline_avg
    print(f"\\nImprovement in average reward: {improvement:.2f}")
    if improvement > 0:
        print("✅ Reward function improvement leads to better performance!")
    else:
        print("⚠️  No improvement observed.")
    
    # Save trained model
    import os
    save_dir = "artifacts/trained_experiment"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"\\nModel saved to {save_dir}")
    
    # Save experiment results
    results = {
        "baseline_avg_reward": baseline_avg,
        "baseline_actions": baseline_actions,
        "trained_avg_reward": trained_avg,
        "trained_actions": trained_actions,
        "improvement": improvement,
        "training_steps": 50*20,
        "total_training_reward": train_reward,
    }
    with open(os.path.join(save_dir, "results.json"), "w") as f:
        import json
        json.dump(results, f, indent=2)
    print("Results saved.")

if __name__ == "__main__":
    main()