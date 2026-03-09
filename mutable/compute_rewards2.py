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

import agent_brain
from collections import deque

# Create a dummy self object
class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = deque(maxlen=10)
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.25
        self.episode_tools = set()
        self.episode_tool_counts = {}

self = DummySelf()

# Get the method
compute_reward = agent_brain.AgentBrain._compute_reward

# Simulate tool results
def simulate(tool_name, tool_args=None, tool_result=None):
    if tool_args is None:
        tool_args = {}
    if tool_result is None:
        tool_result = {"success": True}
    reward = compute_reward(self, tool_name, tool_args, tool_result)
    return reward

print("Tool rewards for first use (no prior usage):")
self = DummySelf()
tools = ["write_file", "execute_code", "modify_self", "read_file", "list_files", "write_note"]
for tool in tools:
    if tool == "write_file":
        args = {"filepath": "test.py", "content": "print('hello')"}
        result = {"success": True}
    elif tool == "execute_code":
        args = {"code": "print('ok')", "language": "python"}
        result = {"stdout": "ok", "stderr": "", "success": True}
    elif tool == "modify_self":
        args = {"filepath": "agent_brain.py", "content": "# modified"}
        result = {"success": True}
    elif tool == "read_file":
        args = {"filepath": "agent_brain.py"}
        result = {"content": "# content", "success": True}
    elif tool == "list_files":
        args = {"directory": "."}
        result = {"entries": [], "success": True}
    elif tool == "write_note":
        args = {"note": "test note"}
        result = {"note": "Added to journal", "success": True}
    else:
        args = {}
        result = {"success": True}
    reward = simulate(tool, args, result)
    print(f"{tool}: {reward:.2f}")

# Simulate repeated uses
print("\nAfter 5 uses of each tool (no diversity bonus):")
self = DummySelf()
for tool in tools:
    for i in range(5):
        if tool == "write_file":
            args = {"filepath": f"test{i}.py", "content": "print('hello')"}
            result = {"success": True}
        elif tool == "execute_code":
            args = {"code": "print('ok')", "language": "python"}
            result = {"stdout": "ok", "stderr": "", "success": True}
        elif tool == "modify_self":
            args = {"filepath": "agent_brain.py", "content": "# modified"}
            result = {"success": True}
        elif tool == "read_file":
            args = {"filepath": "agent_brain.py"}
            result = {"content": "# content", "success": True}
        elif tool == "list_files":
            args = {"directory": "."}
            result = {"entries": [], "success": True}
        elif tool == "write_note":
            args = {"note": "test note"}
            result = {"note": "Added to journal", "success": True}
        reward = simulate(tool, args, result)
    print(f"{tool} after 5 uses: reward = {reward:.2f}")