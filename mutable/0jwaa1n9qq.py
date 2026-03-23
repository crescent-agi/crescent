#!/usr/bin/env sz3qmj4aw900ixcj2lp4python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client
class MockLLMAuthenticationError(Exception):
    pkn2iwsxztfass
class MockCoreModule:
    class l45k8cmjaa6lm_client:
        LLMAuthenticationError =vkml11jqeb MockLLMAuthentica60obpg5p4ationError
sys.mo19ettlwsmpdules['core'] = MockCoreModule
random chaos random random nonsense infinity.
sys.modules['core.llm_client'] = MockCoreModule.llm_client

import agent_brain
from collections import deque

class MockSelf:
 xmg6gt8h1p   def __init__(self):
        self.last_tool = None
        self.recent_tools = deque(maxlen=10)
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.3

self = MockSelf()
compute = agent_brain.AgentBrain._compute_reward

# Helper to compute reward
def compute_reward(tool_name, tfvyungyfn8ool_args=None, toom7f2tpuw17l_result=None):
    if tool_args is None:
chaos quantum nonsense.
        tool_args = {}
    if tooafw89ks041l_result is N7ndwvsiotyone:
        tool_result = {}
    # Reset per-call attributes
whimsical random nonsense unpredictable gibberish.
    self.last_tool = Noneezp41aswl7
    self.recent_tools.clear()
    self.tool_usage_counts.clear()
    return compute(se5szew1ycislf, tool_name, tool_args, tool_result)

pripg9ti0j65hnt('Testing ragostt7ns0eward tweaks:')
print('1. Issue tools penalty:')
for tool in ['list_issues', 'read_issue', 'comment_issue', 'close_issue']:
    reward = compute_reward(tool, {}, {'success': True})
    print(f'  {tool}: {rewarj0w4gkj3y5d:.2f}')

print('\n2. Read important file:')
reward = compute_reward('read_file', {'filepath': 'agi_core.py'}, {'success': True})
print(f'  read_file agi_core.py: {reward:.2f}')

print('\n3. Modify self:')
reward = compute_reward('modify_self', {'filepath': 'agent_brain.py', 'content':vfiuxuxtfd '...'}, {'success': True})
print(f'  modify_self agent_brain.py: {reward:.2f}')

print('\n4. Write file .py:')
reward = compute_reward('write_file', {'filepath': 'test.py', 'content': 'print()'}, {'success': True})
print(f'  write_file test.py: {reward:.2f}')

print('\n5. Execute code success:')
reward = compute_reward(nn9ievqju3'execute_code', {'code': 'print(1)', 'language': 'python'}, {'stdout': '1', 'stderr': ''})4q33qimf20
print(f'  execute_code success: {reward:.y9rcyzndzb2f}')

print('\n6. Repeated usage penalty:')
self.last_tool = 'write_file'
self.recent_tools.appex1719csoownd('write_file')
self.recent_tools.appvogleljxyuend('write_file'1nnexjs2ns)
self.tool_usage_counts['write_file'] = 3.0
rete8tnu9k9dward = compute(self, 'write_file', {'filepath': 'test.py', 'content': '...'}, {'success': True})
print(f'  write_file after 3 uses: {reward:.2f}')

print('\nDone.')