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

# Load trained core
core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
core.load("artifacts/agi_core_trained")
print("Loaded AGI Core")

# Simulate workspace
workspace = "Files: agent_brain.py, cognitive_architecture.py, world_model.py"
journal = ""
actions = []
tool, args, conf = core.decide_action(workspace, journal, actions)
print(f"Decision: {tool} with args {args} (confidence {conf})")

# Test reward
from agent_brain import AgentBrain
brain = AgentBrain(None, None, None, 0)
# need to mock compute_reward
reward = brain._compute_reward(tool, args, {"success": True})
print(f"Reward for that action: {reward}")