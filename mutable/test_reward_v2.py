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
    pass

self = DummySelf()
self.last_tool = None
self.recent_tools = deque(maxlen=10)
self.tool_usage_counts = {}
self.tool_decay_factor = 0.85
self.tool_penalty_factor = 0.15

compute_reward = agent_brain.AgentBrain._compute_reward

# Sample tool results (success)
success_result = {"success": True, "stdout": "test output", "stderr": ""}
error_result = {"error": "file not found"}

def test(tool, args, result):
    reward = compute_reward(self, tool, args, result)
    print(f"{tool} {args} -> {reward:.2f}")
    return reward

print("Testing new reward function:")
print("1. Productive actions (first use):")
test("write_file", {"filepath": "test.py", "content": "print('hello')"}, success_result)
test("execute_code", {"code": "print('test')", "language": "python"}, success_result)
test("modify_self", {"filepath": "agent_brain.py", "content": "# change"}, success_result)
test("read_file", {"filepath": "agi_core.py"}, success_result)
test("create_issue", {"title": "test", "body": "test"}, success_result)
test("write_note", {"note": "Made progress on AGI core."}, success_result)
print("\n2. Issue tools (first use):")
test("list_issues", {}, success_result)
test("read_issue", {"number": "1"}, success_result)
test("comment_issue", {"number": "1", "body": "comment"}, success_result)
test("close_issue", {"number": "1"}, success_result)
print("\n3. Error penalty:")
test("read_file", {"filepath": "nonexistent"}, error_result)
print("\n4. Declare death:")
test("declare_death", {"reason": "test"}, {"message": "You died"})
print("\n5. Repeated same tool penalty (simulate second use):")
self.last_tool = "write_file"
self.recent_tools.append("write_file")
self.tool_usage_counts["write_file"] = 1.0
test("write_file", {"filepath": "test2.py", "content": "print('hello')"}, success_result)