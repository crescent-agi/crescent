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

from agi_core_continuous import AGICoreContinuous
import random, json, os, time
from collections import deque
import agent_brain

# Original reward function
original_compute = agent_brain.AgentBrain._compute_reward

# Wrapper that boosts modify_self reward
def boosted_compute(self, tool_name, tool_args, tool_result):
    reward = original_compute(self, tool_name, tool_args, tool_result)
    if tool_name == "modify_self":
        # Add extra bonus on top of existing rewards
        reward += 3.0
        filepath = tool_args.get("filepath", "")
        if 'agent_brain' in filepath or 'agi_core' in filepath:
            reward += 2.0
    return reward

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = deque(maxlen=10)
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.4

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
    def update_state(self, tool_name, tool_args):
        pass

print("=== Experiment: boosted modify_self reward ===")
core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.01, use_features=True)
workspace = SimWorkspace()

action_counts = {}
for step in range(100):
    tool_name, tool_args, confidence = core.decide_action(
        workspace.workspace_summary(),
        workspace.journal,
        workspace.actions
    )
    tool_result = workspace.tool_result(tool_name, tool_args)
    reward = boosted_compute(self, tool_name, tool_args, tool_result)
    # Learn
    core.learn_from_outcome(reward, workspace.workspace_summary(), workspace.journal, workspace.actions)
    workspace.actions.append({"tool": tool_name, "step": step})
    action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
    if core.q_agent and step % 20 == 0:
        core.q_agent.decay_epsilon()

print("\nAction distribution after 100 steps:")
for tool, count in sorted(action_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  {tool}: {count}")

# Check Q-values
state_vec = [0.0] * 30
if core.q_agent:
    q_vals = core.q_agent.nn.predict(state_vec)
    tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                  "modify_self", "declare_death", "list_issues", "read_issue",
                  "comment_issue", "create_issue", "close_issue"]
    print("\nQ-values (zero state):")
    for i, name in enumerate(tool_names):
        print(f"  {name:20} {q_vals[i]:.3f}")
    sorted_idx = sorted(range(len(q_vals)), key=lambda i: q_vals[i], reverse=True)
    print("\nTop 3 actions:")
    for rank, idx in enumerate(sorted_idx[:3]):
        print(f"  {rank+1}. {tool_names[idx]:20} {q_vals[idx]:.3f}")

print("\nExperiment done.")