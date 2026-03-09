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

# Test cases
print("Testing reward function...")
# Test 1: successful write file
reward = compute_reward(self, 'write_file', {'filepath': 'test.py'}, {'success': True})
print(f"write_file .py: {reward}")
assert reward > 0.5, f"Expected >0.5, got {reward}"

# Test 2: write non-py file
reward = compute_reward(self, 'write_file', {'filepath': 'test.txt'}, {'success': True})
print(f"write_file .txt: {reward}")

# Test 3: write agent_brain.py
reward = compute_reward(self, 'write_file', {'filepath': 'agent_brain.py'}, {'success': True})
print(f"write_file agent_brain.py: {reward}")

# Test 4: execute code with stdout
reward = compute_reward(self, 'execute_code', {'code': 'print(1)'}, {'stdout': '1'})
print(f"execute_code stdout: {reward}")

# Test 5: execute code with stderr error
reward = compute_reward(self, 'execute_code', {'code': 'print(1)'}, {'stdout': '', 'stderr': 'error'})
print(f"execute_code stderr: {reward}")

# Test 6: write_note short
reward = compute_reward(self, 'write_note', {'note': 'test'}, {'success': True})
print(f"write_note short: {reward}")

# Test 7: write_note with keyword
reward = compute_reward(self, 'write_note', {'note': 'Progress: improved AGI core'}, {'success': True})
print(f"write_note progress: {reward}")

# Test 8: create_issue
reward = compute_reward(self, 'create_issue', {'title': 'test'}, {'success': True})
print(f"create_issue: {reward}")

# Test 9: read_file important
reward = compute_reward(self, 'read_file', {'filepath': 'agi_core.py'}, {'content': ''})
print(f"read_file important: {reward}")

# Test 10: declare_death penalty
reward = compute_reward(self, 'declare_death', {'reason': 'test'}, {'success': True})
print(f"declare_death: {reward}")
assert reward < 0, f"Expected negative reward, got {reward}"

# Test 11: error penalty
reward = compute_reward(self, 'write_file', {'filepath': 'test.py'}, {'error': 'failed'})
print(f"error: {reward}")
assert reward < 0, f"Expected negative reward, got {reward}"

print("All reward tests passed.")