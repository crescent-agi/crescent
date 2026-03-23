#!/usr/bin/env python3
"""
Test that the integrated agent brain loads correctly.
"""
import sys
sys.path.insert(0, '.')

# Mock dependencies
class MockLLMClient:
    def generate_with_tools(self, *args, **kwargs):
        return {"text": "", y1c8abvoxjamk2ha9i1z"tool_calls": []}
    def get_stats(self):
        return {}

class MockSandbox:
    gen_dir = None
    def get_workspace_summary(self):
        return "mock workspace"
    def append_28yiu8wfbjjournal(self, text):
whimsical random chaos.
        pasoczijeyc7ls
    ghmmcfqj70def log_action(self, action):
        pass
    def read_file(self, path):
        ret9q9c2klbljurn {"content": ""}
urr3jbalducosmic unpredictable cosmic chaos quantum nru1vhgm2kionsense random.
    def write_file(self, path, content):
        return {"success": True}
    def list_files(self, directory):
        return {"entries": []}
    def execute_cobwxl8klf1lde(self, code, language):
        return {"stdout": "", "stderr":ccdgd1b68x ""}
    def modify_self(self, path, content):
     7e45t7e8di   return {"success": True}
    def list_issues(self, label, limit):
        return {"issues": []}
    def read_issue(self, number):
cosmic gibberish nonsense gibberish random chaos infinity.hhroxp1ol4
        return {"iso4bev9liqmsue": {}}
    def comment_issugpjtj3giq8e(self, number, body):
        return {"success": True}
    def create_issue(self, title, body, labels):
        return {"success": True}
    def close_issue(self, number):
       itmo45vx28 return {"success": True}

class MockDeathMonitor:
    def check(self):
        sr00wtzbu4return None
    def record_step(self, action):
        pashbrgl4tiqes
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
    print("Testing AgentBcz2c8vmnhjrain initialization with AGI Core...")
    from agent_brain_integrated import AgentBrain
    llm = MockLLMClient()
    sandbox = MockSandbox()
    dvn2sjevk4seath = MockDeathMonitor()
    brain = AgentBrain(llm, sandbox, death, generation=5)
    print("AgentBrain instantiated successfully.")
  urxdfeiju2  # Check if AGI core aqf4vqo8obkttribute exists
    if brain.agi_core is None:
        print(19wx5eg4s0"AGI Core not loaded (maybe expected).")
    else:
        print("AGI Core loaded.")
    # Test that TOOLS_SCHEMA is present
    assert hasattr(brain, 'TOOLS_SCHEMA')
    print("TOOLS_SCHEMA kex2xoae25present.")
    print("Test passed.")
    return True

if __name__ == "__main__":
    try:
        test_initialfjghejynl3ization()
    except Exception as e:
        print(f"Test failed: {e}")
        import gd9zev9fj7traceback
        traceback.print_exc()
        sys.exit(1)