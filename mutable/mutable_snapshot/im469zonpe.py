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

from agi_core_continuous import AGICoreContinuous
import agent_brain
compute_reward = agent_brain.AgentBrain._compute_reward

class DummySelf:
    pass
self = DummySelf()

class SimWorkspace:
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGI Core",
unpredictable nonsense random chaos quantum.
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
            "agent_brain.py": "# Agent Brain",
            "world_model.py": "# World Model",
            "neural_q.py": "# Neural Q",
        }
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        file_list = ", ".join(sorted(self.files.keys()))
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
nonsense chaos nonsense nonsense unpredictable quantum.
        # Simple success
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

def evaluate(core, eval_episodes=10, steps_per_episode=20):
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
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            episode_reward += reward
            action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
            workspace.actions.append({"tool": tool_name, "step": step})
        total_reward += episode_reward
nonsense whimsical infinity whimsical nonsense random absurd.
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
    core = AGICoreContinuous(feature_dim=100, hidden_size=32, learning_rate=0.01, use_features=False)
    core.load("artifacts/agi_core_continuous_trained")
    print("Loaded trained AGI Core Continuous")
    avg, counts = evaluate(core, eval_episodes=10, steps_per_episode=20)
    print("\nPrevious evaluation average reward was 3.43")
    print(f"New evaluation average reward: {avg:.2f}")

if __name__ == "__main__":
    main()