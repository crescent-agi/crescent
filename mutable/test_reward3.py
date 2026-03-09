#!/usr/bin/env python3
"""
Test the improved reward function without full AgentBrain init.
"""
import sys
import os
sys.path.insert(0, '.')

# Mock core.llm_client
class MockLLMAuthenticationError(Exception):
    pass

class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError

sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

# Import the module and extract the reward function
import agent_brain
# Get the unbound method
compute_reward = agent_brain.AgentBrain._compute_reward

# Create a dummy self (any object)
class DummySelf:
    pass

self = DummySelf()

print("Testing reward function...")
# Test error case
reward = compute_reward(self, 'write_file', {'filepath': 'test.py'}, {'error': 'failed'})
print(f"error case: {reward}")
assert reward == -0.5, f"Expected -0.5, got {reward}"

# Test declare_death case
reward = compute_reward(self, 'declare_death', {'reason': 'test'}, {'success': True})
print(f"declare_death: {reward}")
assert reward == -2.0, f"Expected -2.0, got {reward}"

# Test success with write .py
reward = compute_reward(self, 'write_file', {'filepath': 'test.py'}, {'success': True})
print(f"write .py success: {reward}")
assert reward > 0.5

# Test read important file
reward = compute_reward(self, 'read_file', {'filepath': 'agi_core.py'}, {'content': ''})
print(f"read important: {reward}")
assert reward > 0.2

print("All basic tests passed.")