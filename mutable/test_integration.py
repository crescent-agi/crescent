#!/usr/bin/env python3
"""
Quick integration test: load the trained AGI Core and ensure it can suggest actions.
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

# Load the trained model
core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.01,
                         exploration_rate=0.5, epsilon_decay=0.995, epsilon_min=0.1,
                         use_features=True)
save_dir = "artifacts/agi_core_continuous_trained"
try:
    core.load(save_dir)
    print(f"Successfully loaded AGI Core from {save_dir}")
except Exception as e:
    print(f"Failed to load AGI Core: {e}")
    sys.exit(1)

# Simulate a simple state
workspace_summary = "Files: inherited_notes.md, agent_brain.py, strategy.md"
journal = ""
actions = []
tool_name, tool_args, confidence = core.decide_action(workspace_summary, journal, actions)
print(f"AGI Core suggestion: {tool_name} with args {tool_args} (confidence {confidence:.3f})")
if confidence > 0:
    print("Integration test passed.")
else:
    print("Warning: confidence zero.")