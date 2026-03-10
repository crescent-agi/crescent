#!/usr/bin/env python3
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
from collections import deque
import agent_brain

class MockBrain:
    def __init__(self):
        self.recent_tools = deque(maxlen=5)
        self.last_tool = None
    def _compute_reward(self, tool_name, tool_args, tool_result):
        return agent_brain.AgentBrain._compute_reward(self, tool_name, tool_args, tool_result)

brain = MockBrain()

class SimWorkspace:
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
        file_list = ", ".join(sorted(self.files.keys()))
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

print('Loading existing discrete core...')
core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
core.load('artifacts/agi_core_trained')
print('Loaded. Disabling planner.')
core.planner = None
workspace = SimWorkspace()
print('Training for 10 episodes...')
for episode in range(10):
    episode_reward = 0.0
    for step in range(10):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = brain._compute_reward(tool_name, tool_args, tool_result)
        episode_reward += reward
        core.learn_from_outcome(reward, workspace.workspace_summary(), workspace.journal, workspace.actions)
        workspace.actions.append({"tool": tool_name, "step": step})
    print(f'Episode {episode+1}: reward {episode_reward:.2f}')
print('Training done. Evaluating...')
# eval
workspace2 = SimWorkspace()
action_counts = {}
total_reward = 0.0
for ep in range(5):
    episode_reward = 0.0
    for step in range(10):
        tool_name, tool_args, confidence = core.decide_action(
            workspace2.workspace_summary(),
            workspace2.journal,
            workspace2.actions
        )
        tool_result = workspace2.tool_result(tool_name, tool_args)
        reward = brain._compute_reward(tool_name, tool_args, tool_result)
        episode_reward += reward
        action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
        workspace2.actions.append({"tool": tool_name, "step": step})
    total_reward += episode_reward
    print(f'Eval episode {ep+1}: reward {episode_reward:.2f}')
avg_reward = total_reward / 5
print(f'Average reward: {avg_reward:.2f}')
print('Action distribution:', action_counts)
# Save updated model
import os
os.makedirs('artifacts/agi_core_tuned', exist_ok=True)
core.save('artifacts/agi_core_tuned')
print('Saved tuned model.')