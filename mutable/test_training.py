#!/usr/bin/env python3
"""
Quick test of training pipeline.
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

print("Initializing AGI Core...")
core = AGICore(state_size=50, hidden_size=16, learning_rate=0.01)
core.planner = None
workspace = SimWorkspace()
print("Starting quick training (2 episodes, 3 steps)...")
for episode in range(2):
    episode_reward = 0
    for step in range(3):
        tool_name, tool_args, conf = core.decide_action(workspace.workspace_summary(), workspace.journal, workspace.actions)
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        episode_reward += reward
        core.learn_from_outcome(reward, workspace.workspace_summary(), workspace.journal, workspace.actions)
        workspace.actions.append({"tool": tool_name})
    print(f"Episode {episode+1}: reward {episode_reward:.2f}")
print("Training test completed.")