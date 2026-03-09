#!/usr/bin/env python3
"""
Quick test to see if patched AGICoreContinuous works.
"""
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

core = AGICoreContinuous(feature_dim=30, use_features=True)
print("AGICoreContinuous instantiated.")
workspace = "Files: agent_brain.py, cognitive_architecture.py"
journal = ""
actions = []
for i in range(5):
    tool, args, conf = core.decide_action(workspace, journal, actions)
    print(f"Step {i}: {tool}, args {args}, conf {conf}")
    # Simulate outcome
    reward = 1.0 if tool == "write_file" else 0.0
    core.learn_from_outcome(reward, workspace, journal, actions + [tool])
print("Test passed.")