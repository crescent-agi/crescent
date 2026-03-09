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
import agent_brain
from collections import deque

class MockBrain:
    def __init__(self):
        self.recent_tools = deque(maxlen=5)
        self.last_tool = None
    def _compute_reward(self, tool_name, tool_args, tool_result):
        # Call the original method with self
        return agent_brain.AgentBrain._compute_reward(self, tool_name, tool_args, tool_result)

brain = MockBrain()
compute_reward = brain._compute_reward

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
            reward = compute_reward(tool_name, tool_args, tool_result)
            episode_reward += reward
            action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
            workspace.actions.append({"tool": tool_name, "step": step})
            print(f'  step {step}: {tool_name} -> {reward:.2f}')
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
    core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
    core.load("artifacts/agi_core_trained")
    print("Loaded trained AGI Core")
    avg, counts = evaluate(core, eval_episodes=2, steps_per_episode=5)
    print(f"\nAverage reward: {avg:.2f}")
    # Compare with previous baseline
    baseline = 3.43
    print(f"Previous baseline: {baseline}")
    print(f"Difference: {avg - baseline:.2f}")
    return avg

if __name__ == "__main__":
    main()