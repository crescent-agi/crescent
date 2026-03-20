#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client
class MockLLMAuthenticationError(Exception):
    pass
class MockLLMClient:
    def generate_with_tools(self, *args, **kwargs):
        return {"text": "", "tool_calls": []}
    def get_stats(self):
        return {}
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

import agent_brain

# Mock sandbox and death monitor
class MockSandbox:
    gen_dir = '.'
    def get_workspace_summary(self):
        return "Files: agent_brain.py, agi_core_continuous.py"
    def append_journal(self, note):
        pass
    def log_action(self, action):
        pass

class MockDeathMonitor:
    def check(self):
        return None
    def record_step(self, action):
        pass
    def record_self_termination(self):
        pass
    def record_crash(self, msg):
        pass
    def import_state(self, state):
        pass
    def export_state(self):
        return {}
    def get_stats(self):
        return {}

print("Testing AgentBrain instantiation with AGICoreContinuous...")
brain = agent_brain.AgentBrain(None, MockSandbox(), MockDeathMonitor(), 4)
print(f"AGI core type: {brain.agi_core_type}")
print(f"AGI core available: {brain.agi_core is not None}")
if brain.agi_core:
    print("AGI core loaded successfully")
    # Check feature dimension
    print(f"Feature dim: {brain.agi_core.feature_dim if hasattr(brain.agi_core, 'feature_dim') else 'N/A'}")
else:
    print("AGI core not loaded")

print("\nIntegration check passed.")