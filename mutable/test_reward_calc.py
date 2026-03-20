#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
import agent_brain

# Get the compute_reward function
from agent_brain import AgentBrain
import inspect

# Create a dummy instance to bind method
class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []

self = DummySelf()
# monkey patch
compute = AgentBrain._compute_reward

# Simulate some tool calls
tools = [
    ("write_file", {"filepath": "test.py", "content": "print('hello')"}),
    ("execute_code", {"code": "print('test')", "language": "python"}),
    ("read_file", {"filepath": "agent_brain.py"}),
    ("modify_self", {"filepath": "agent_brain.py", "content": "new content"}),
    ("write_note", {"note": "This is a progress note about AGI."}),
    ("create_issue", {"title": "task", "body": "do something"}),
    ("list_files", {"directory": "."}),
    ("declare_death", {"reason": "done"}),
]

print("Reward calculations for successful tool results (no error):")
for tool, args in tools:
    # Simulate successful result
    result = {"success": True}
    if tool == "execute_code":
        result = {"stdout": "test passed", "stderr": "", "returncode": 0}
    elif tool == "read_file":
        result = {"content": "some content"}
    reward = compute(self, tool, args, result)
    print(f"{tool:20s} -> {reward:.2f}")

print("\nReward for error result:")
for tool, args in tools[:1]:
    result = {"error": "something wrong"}
    reward = compute(self, tool, args, result)
    print(f"{tool:20s} -> {reward:.2f}")

print("\nReward for declare_death (should be -1.0):")
result = {"success": True}
reward = compute(self, "declare_death", {"reason": "done"}, result)
print(f"declare_death -> {reward:.2f}")

# Test recency penalty
print("\nRecency penalty test:")
self.last_tool = "write_file"
reward = compute(self, "write_file", {"filepath": "test.py", "content": ""}, {"success": True})
print(f"Same tool as last: {reward:.2f}")
self.last_tool = None

# Test recent tools diversity
self.recent_tools = ["write_file", "write_file", "execute_code"]
reward = compute(self, "write_file", {"filepath": "test.py", "content": ""}, {"success": True})
print(f"Tool already in recent (2 occurrences): {reward:.2f}")
self.recent_tools = []

# Test diversity bonus
self.recent_tools = ["write_file", "execute_code"]
reward = compute(self, "read_file", {"filepath": "x"}, {"success": True})
print(f"New tool not in recent: {reward:.2f}")