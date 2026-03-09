#!/usr/bin/env python3
"""
Test that the integrated agent brain loads correctly.
"""
import sys
sys.path.insert(0, '.')

# Mock dependencies
class MockLLMClient:
    def generate_with_tools(self, *args, **kwargs):
        return {"text": "", "tool_calls": []}
    def get_stats(self):
        return {}

class MockSandbox:
    gen_dir = None
    def get_workspace_summary(self):
        return "mock workspace"
    def append_journal(self, text):
        pass
    def log_action(self, action):
        pass
    def read_file(self, path):
        return {"content": ""}
    def write_file(self, path, content):
        return {"success": True}
    def list_files(self, directory):
        return {"entries": []}
    def execute_code(self, code, language):
        return {"stdout": "", "stderr": ""}
    def modify_self(self, path, content):
        return {"success": True}
    def list_issues(self, label, limit):
        return {"issues": []}
    def read_issue(self, number):
        return {"issue": {}}
    def comment_issue(self, number, body):
        return {"success": True}
    def create_issue(self, title, body, labels):
        return {"success": True}
    def close_issue(self, number):
        return {"success": True}

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

def test_initialization():
    print("Testing AgentBrain initialization with AGI Core...")
    from agent_brain_integrated import AgentBrain
    llm = MockLLMClient()
    sandbox = MockSandbox()
    death = MockDeathMonitor()
    brain = AgentBrain(llm, sandbox, death, generation=5)
    print("AgentBrain instantiated successfully.")
    # Check if AGI core attribute exists
    if brain.agi_core is None:
        print("AGI Core not loaded (maybe expected).")
    else:
        print("AGI Core loaded.")
    # Test that TOOLS_SCHEMA is present
    assert hasattr(brain, 'TOOLS_SCHEMA')
    print("TOOLS_SCHEMA present.")
    print("Test passed.")
    return True

if __name__ == "__main__":
    try:
        test_initialization()
    except Exception as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)