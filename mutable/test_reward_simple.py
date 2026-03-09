#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client import
class MockLLMAuthenticationError(Exception):
    pass
sys.modules['core'] = type(sys)('core')
sys.modules['core'].llm_client = type(sys)('llm_client')
sys.modules['core'].llm_client.LLMAuthenticationError = MockLLMAuthenticationError

import agent_brain

# Create a minimal mock instance
class DummyBrain:
    pass

brain = DummyBrain()
brain.last_tool = None
brain.recent_tools = []
brain.tool_usage_counts = {}
brain.tool_decay_factor = 0.85
brain.tool_penalty_factor = 0.3

# Bind the method
brain._compute_reward = agent_brain.AgentBrain._compute_reward.__get__(brain, agent_brain.AgentBrain)

# Test basic rewards
print('Testing reward function:')
# Success reward
result = {'stdout': ''}
reward = brain._compute_reward('write_file', {'filepath': 'test.py'}, result)
print(f'write_file .py (first): {reward}')
# Same tool again (recency penalty)
brain.last_tool = 'write_file'
reward2 = brain._compute_reward('write_file', {'filepath': 'test.py'}, result)
print(f'write_file .py (second): {reward2}')
print(f'Difference due to recency penalty: {reward - reward2}')

# Declare death penalty
reward = brain._compute_reward('declare_death', {}, {})
print(f'declare_death penalty: {reward}')

# Error penalty
reward = brain._compute_reward('execute_code', {}, {'error': 'failed'})
print(f'error penalty: {reward}')

# Test per-tool usage decay
print('\nPer-tool usage decay test:')
brain.tool_usage_counts = {}
for i in range(3):
    reward = brain._compute_reward('execute_code', {}, result)
    print(f'  use {i+1}: reward {reward}, usage count {brain.tool_usage_counts.get(\"execute_code\", 0)}')

# Test diversity bonus
brain.recent_tools = []
reward = brain._compute_reward('list_files', {}, result)
print(f'\nlist_files first use (diversity bonus): {reward}')
brain.recent_tools = ['list_files'] * 5
reward = brain._compute_reward('list_files', {}, result)
print(f'list_files repeated (penalty): {reward}')