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
from agent_brain import AgentBrain
import random

# Create core
core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
print("AGI Core created")

# Load trained model (optional)
try:
    core.load("artifacts/agi_core_trained")
    print("Loaded trained model")
except Exception as e:
    print(f"Could not load model: {e}")

# Simulate workspace
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
        # Simple mock
        return {"success": True}

workspace = SimWorkspace()
print("Workspace summary:", workspace.workspace_summary())

# Test decide_action
tool, args, conf = core.decide_action(workspace.workspace_summary(), workspace.journal, workspace.actions)
print(f"Decision: {tool} with args {args} (confidence {conf})")

# Test reward computation
brain = AgentBrain(None, None, None, 0)
# Monkey-patch sandbox
brain.sandbox = type('MockSandbox', (), {'gen_dir': '.'})()
reward = brain._compute_reward(tool, args, {"success": True})
print(f"Reward for that action: {reward}")

# Run a few steps
print("\nRunning 5 steps...")
for i in range(5):
    tool, args, conf = core.decide_action(workspace.workspace_summary(), workspace.journal, workspace.actions)
    print(f"Step {i}: {tool} {args}")
    result = workspace.tool_result(tool, args)
    reward = brain._compute_reward(tool, args, result)
    print(f"  reward {reward}")
    core.learn_from_outcome(reward, workspace.workspace_summary(), workspace.journal, workspace.actions)
    workspace.actions.append({"tool": tool, "step": i})

print("Test complete.")