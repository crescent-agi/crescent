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

class MockSelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = deque(maxlen=10)
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.3

self = MockSelf()
compute = agent_brain.AgentBrain._compute_reward

# Helper to compute reward
def compute_reward(tool_name, tool_args=None, tool_result=None):
    if tool_args is None:
        tool_args = {}
    if tool_result is None:
        tool_result = {}
    # Reset per-call attributes
    self.last_tool = None
    self.recent_tools.clear()
    self.tool_usage_counts.clear()
    return compute(self, tool_name, tool_args, tool_result)

print('Testing reward tweaks:')
print('1. Issue tools penalty:')
for tool in ['list_issues', 'read_issue', 'comment_issue', 'close_issue']:
    reward = compute_reward(tool, {}, {'success': True})
    print(f'  {tool}: {reward:.2f}')

print('\\n2. Read important file:')
reward = compute_reward('read_file', {'filepath': 'agi_core.py'}, {'success': True})
print(f'  read_file agi_core.py: {reward:.2f}')

print('\\n3. Modify self:')
reward = compute_reward('modify_self', {'filepath': 'agent_brain.py', 'content': '...'}, {'success': True})
print(f'  modify_self agent_brain.py: {reward:.2f}')

print('\\n4. Write file .py:')
reward = compute_reward('write_file', {'filepath': 'test.py', 'content': 'print()'}, {'success': True})
print(f'  write_file test.py: {reward:.2f}')

print('\\n5. Execute code success:')
reward = compute_reward('execute_code', {'code': 'print(1)', 'language': 'python'}, {'stdout': '1', 'stderr': ''})
print(f'  execute_code success: {reward:.2f}')

print('\\n6. Repeated usage penalty:')
self.last_tool = 'write_file'
self.recent_tools.append('write_file')
self.recent_tools.append('write_file')
self.tool_usage_counts['write_file'] = 3.0
reward = compute(self, 'write_file', {'filepath': 'test.py', 'content': '...'}, {'success': True})
print(f'  write_file after 3 uses: {reward:.2f}')

print('\\nDone.')