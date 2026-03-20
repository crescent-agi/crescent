#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core_continuous import AGICoreContinuous
print("AGICoreContinuous imported successfully")

# Instantiate
core = AGICoreContinuous(feature_dim=30, use_features=True)
print("Core instantiated")

# Test decide_action
workspace = "Files: agent_brain.py, cognitive_architecture.py"
journal = ""
actions = []
try:
    tool, args, conf = core.decide_action(workspace, journal, actions)
    print(f"Success: tool={tool}, args={args}, conf={conf}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()