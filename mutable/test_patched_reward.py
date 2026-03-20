import sys
sys.path.insert(0, '.')

class MockLLMAuthenticationError(Exception):
    pass

class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError

sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

import importlib
import agent_brain
importlib.reload(agent_brain)
from collections import deque

class MockBrain:
    def __init__(self):
        self.recent_tools = deque(maxlen=5)
        self.last_tool = None
    def _compute_reward(self, tool_name, tool_args, tool_result):
        return agent_brain.AgentBrain._compute_reward(self, tool_name, tool_args, tool_result)

brain = MockBrain()
print('Testing patched reward function:')
tool_name = 'write_file'
tool_args = {'filepath': 'test.py', 'content': 'print(1)'}
tool_result = {'success': True}
reward = brain._compute_reward(tool_name, tool_args, tool_result)
print(f'{tool_name}: {reward}')
# second same tool
brain.last_tool = tool_name
brain.recent_tools.append(tool_name)
reward2 = brain._compute_reward(tool_name, tool_args, tool_result)
print(f'{tool_name} again: {reward2}')
# write_note
tool_name2 = 'write_note'
tool_args2 = {'note': 'test note'}
reward3 = brain._compute_reward(tool_name2, tool_args2, tool_result)
print(f'{tool_name2}: {reward3}')
print('Sequence:')
brain2 = MockBrain()
actions = ['write_file', 'write_note', 'write_file', 'write_file', 'write_file']
for a in actions:
    reward = brain2._compute_reward(a, {}, {'success': True})
    print(f'{a}: {reward}')