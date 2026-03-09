#!/usr/bin/env python3
"""
Test the improved reward function.
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

# Import AgentBrain after mocking
from agent_brain import AgentBrain

# Create a mock instance without full init
class MockLLMClient:
    pass

class MockSandbox:
    gen_dir = '/tmp'

class MockDeathMonitor:
    pass

brain = AgentBrain(MockLLMClient(), MockSandbox(), MockDeathMonitor(), generation=6)

# Test cases
print("Testing reward function...")
# Test 1: successful write file
reward = brain._compute_reward('write_file', {'filepath': 'test.py'}, {'success': True})
print(f"write_file .py: {reward}")
assert reward > 0.5, f"Expected >0.5, got {reward}"

# Test 2: write non-py file
reward = brain._compute_reward('write_file', {'filepath': 'test.txt'}, {'success': True})
print(f"write_file .txt: {reward}")

# Test 3: write agent_brain.py
reward = brain._compute_reward('write_file', {'filepath': 'agent_brain.py'}, {'success': True})
print(f"write_file agent_brain.py: {reward}")

# Test 4: execute code with stdout
reward = brain._compute_reward('execute_code', {'code': 'print(1)'}, {'stdout': '1'})
print(f"execute_code stdout: {reward}")

# Test 5: execute code with stderr error
reward = brain._compute_reward('execute_code', {'code': 'print(1)'}, {'stdout': '', 'stderr': 'error'})
print(f"execute_code stderr: {reward}")

# Test 6: write_note short
reward = brain._compute_reward('write_note', {'note': 'test'}, {'success': True})
print(f"write_note short: {reward}")

# Test 7: write_note with keyword
reward = brain._compute_reward('write_note', {'note': 'Progress: improved AGI core'}, {'success': True})
print(f"write_note progress: {reward}")

# Test 8: create_issue
reward = brain._compute_reward('create_issue', {'title': 'test'}, {'success': True})
print(f"create_issue: {reward}")

# Test 9: read_file important
reward = brain._compute_reward('read_file', {'filepath': 'agi_core.py'}, {'content': ''})
print(f"read_file important: {reward}")

# Test 10: declare_death penalty
reward = brain._compute_reward('declare_death', {'reason': 'test'}, {'success': True})
print(f"declare_death: {reward}")
assert reward < 0, f"Expected negative reward, got {reward}"

# Test 11: error penalty
reward = brain._compute_reward('write_file', {'filepath': 'test.py'}, {'error': 'failed'})
print(f"error: {reward}")
assert reward < 0, f"Expected negative reward, got {reward}"

print("All reward tests passed.")