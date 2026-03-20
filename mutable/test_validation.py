#!/usr/bin/env python3
"""
Quick test of validation training.
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
import agent_brain
compute_reward = agent_brain.AgentBrain._compute_reward

# Test reward function with dummy self
from collections import deque
class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = deque(maxlen=10)
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.4
    pass

self = DummySelf()

# Test a few actions
print("Testing reward function with updated ratios...")
# Write file .py
reward = compute_reward(self, "write_file", {"filepath": "test.py", "content": "# test"}, {"success": True})
print(f"write_file .py: {reward:.2f}")
# Execute code success
reward = compute_reward(self, "execute_code", {"code": "print('test')", "language": "python"}, {"stdout": "test passed", "stderr": "", "success": True})
print(f"execute_code success: {reward:.2f}")
# Modify self agent_brain
reward = compute_reward(self, "modify_self", {"filepath": "agent_brain.py", "content": "# change"}, {"success": True})
print(f"modify_self agent_brain: {reward:.2f}")
# Read important file
reward = compute_reward(self, "read_file", {"filepath": "agi_core.py"}, {"content": "# AGI Core", "success": True})
print(f"read_file agi_core.py: {reward:.2f}")
# Declare death
reward = compute_reward(self, "declare_death", {"reason": "test"}, {"message": "You have chosen to die."})
print(f"declare_death: {reward:.2f}")
# Issue tool penalty
reward = compute_reward(self, "list_issues", {}, {"issues": []})
print(f"list_issues: {reward:.2f}")

# Test repeated usage penalty
print("\nTesting repeated usage penalty:")
for i in range(3):
    reward = compute_reward(self, "write_file", {"filepath": "test.py", "content": "# test"}, {"success": True})
    print(f"  write_file #{i+1}: {reward:.2f}")
    print(f"    tool_usage_counts[write_file] = {self.tool_usage_counts.get('write_file', 0):.2f}")
    print(f"    recent_tools: {list(self.recent_tools)}")

print("\nTest passed.")