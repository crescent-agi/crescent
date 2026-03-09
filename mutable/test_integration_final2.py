#!/usr/bin/env python3
import sys
import os
from pathlib import Path
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

# Mock sandbox with Path gen_dir
class MockSandbox:
    def __init__(self):
        self.gen_dir = Path('.').absolute()
    def get_workspace_summary(self):
        return "Files: agi_core.py, agent_brain.py"
    def append_journal(self, note):
        pass
    def log_action(self, action):
        pass
    def read_file(self, filepath):
        return {"content": ""}
    def write_file(self, filepath, content):
        return {"success": True}
    def list_files(self, directory):
        return {"entries": []}
    def execute_code(self, code, language):
        return {"stdout": "", "stderr": ""}
    def modify_self(self, filepath, content):
        return {"success": True}
    def list_issues(self, label, limit):
        return {"issues": []}
    def read_issue(self, number):
        return {"issue": {}}
    def comment_issue(self, number, body):
        return {"success": True}
    def create_issue(self, title, body, labels):
        return {"success": True, "number": 1}
    def close_issue(self, number):
        return {"success": True}

# Mock death monitor
class MockDeathMonitor:
    def check(self):
        return None
    def record_step(self, action):
        pass
    def record_crash(self, msg):
        pass
    def record_self_termination(self):
        pass
    def get_stats(self):
        return {}
    def import_state(self, state):
        pass
    def export_state(self):
        return {}

import agent_brain
print("Testing AgentBrain instantiation with AGICoreContinuous...")
llm = MockLLMClient()
sandbox = MockSandbox()
death = MockDeathMonitor()
try:
    brain = agent_brain.AgentBrain(llm, sandbox, death, generation=4)
except Exception as e:
    import traceback
    traceback.print_exc()
    sys.exit(1)
print(f"AGI core type: {brain.agi_core_type}")
print(f"AGI core available: {brain.agi_core is not None}")
if brain.agi_core:
    print(f"Core feature_dim: {brain.agi_core.feature_dim}")
    # Test decision
    workspace = sandbox.get_workspace_summary()
    journal = ""
    actions = []
    tool_name, tool_args, confidence = brain.agi_core.decide_action(workspace, journal, actions)
    print(f"AGI Core suggests: {tool_name} with confidence {confidence}")
    # Check Q-values
    if hasattr(brain.agi_core, 'q_agent') and brain.agi_core.q_agent:
        print(f"Epsilon: {brain.agi_core.q_agent.epsilon}")
        # Extract features
        from feature_extractor import FeatureExtractor
        extractor = FeatureExtractor(history_size=10)
        features = extractor.extract(workspace, journal, actions)
        q_vals = brain.agi_core.q_agent.nn.predict(features)
        tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                     "modify_self", "declare_death", "list_issues", "read_issue", "comment_issue",
                     "create_issue", "close_issue"]
        print("Q-values:")
        for i, q in enumerate(q_vals):
            print(f"  {tool_names[i]:15s} {q:6.3f}")
        best = max(range(len(q_vals)), key=lambda i: q_vals[i])
        print(f"Best action: {tool_names[best]} ({q_vals[best]:.3f})")
print("Integration test passed.")