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

import agent_brain
from collections import deque

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = deque(maxlen=10)
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.25

self = DummySelf()
compute_reward = agent_brain.AgentBrain._compute_reward

# Success result
success_result = {"success": True, "stdout": "Simulated output with more than ten characters.", "stderr": ""}
# Write file args (non-python)
write_file_args = {"filepath": "artifacts/note.txt", "content": "some content"}
# Write file .py args
write_file_py_args = {"filepath": "test.py", "content": "print('hello')"}
# Write file agent_brain.py args
write_file_self_args = {"filepath": "agent_brain.py", "content": "# modification"}
# Execute code args
execute_args = {"code": "print('test')", "language": "python"}
# Read file important
read_file_args = {"filepath": "agi_core.py"}
# Modify self args
modify_self_args = {"filepath": "agent_brain.py", "content": "# change"}
# Create issue args
create_issue_args = {"title": "test", "body": "test"}
# Write note args
write_note_args = {"note": "Made progress on AGI core. Next step: improve planning."}

tools = [
    ("write_file", write_file_args),
    ("write_file .py", write_file_py_args),
    ("write_file self", write_file_self_args),
    ("execute_code", execute_args),
    ("read_file important", read_file_args),
    ("modify_self", modify_self_args),
    ("create_issue", create_issue_args),
    ("write_note", write_note_args),
]

print("=== First use rewards ===")
for name, args in tools:
    reward = compute_reward(self, name.split()[0], args, success_result)
    print(f"{name:30} -> {reward:.2f}")
    # reset recent tools and usage counts for next tool
    self.recent_tools.clear()
    self.tool_usage_counts.clear()
    self.last_tool = None

print("\n=== Repeated use penalty (same tool 5 times) ===")
tool_name = "execute_code"
self.recent_tools.clear()
self.tool_usage_counts.clear()
self.last_tool = None
for i in range(5):
    reward = compute_reward(self, tool_name, execute_args, success_result)
    print(f"  {tool_name} #{i+1}: reward {reward:.2f}")
    print(f"    tool_usage_counts[{tool_name}] = {self.tool_usage_counts.get(tool_name, 0):.2f}")
    print(f"    recent_tools count: {list(self.recent_tools).count(tool_name)}")

print("\n=== Diversity bonus (different tools) ===")
self.recent_tools.clear()
self.tool_usage_counts.clear()
self.last_tool = None
for tool in ["write_file", "execute_code", "read_file", "modify_self"]:
    reward = compute_reward(self, tool, {"filepath": "test.py"}, success_result)
    print(f"{tool:20} -> {reward:.2f}")

print("\n=== Declare death penalty ===")
reward = compute_reward(self, "declare_death", {"reason": "test"}, {"message": "died"})
print(f"declare_death -> {reward:.2f}")