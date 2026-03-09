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
print('Testing new reward function:')
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
# third same tool
reward3 = brain._compute_reward(tool_name, tool_args, tool_result)
print(f'{tool_name} third: {reward3}')
# write_note
tool_name2 = 'write_note'
tool_args2 = {'note': 'test note'}
reward4 = brain._compute_reward(tool_name2, tool_args2, tool_result)
print(f'{tool_name2}: {reward4}')
# read_file important
tool_name3 = 'read_file'
tool_args3 = {'filepath': 'agi_core.py'}
reward5 = brain._compute_reward(tool_name3, tool_args3, tool_result)
print(f'{tool_name3} important: {reward5}')
# execute_code
tool_name4 = 'execute_code'
tool_args4 = {'code': 'print(1)', 'language': 'python'}
tool_result4 = {'success': True, 'stdout': '1\\n', 'stderr': ''}
reward6 = brain._compute_reward(tool_name4, tool_args4, tool_result4)
print(f'{tool_name4}: {reward6}')
# list_files
tool_name5 = 'list_files'
tool_args5 = {'directory': '.'}
reward7 = brain._compute_reward(tool_name5, tool_args5, tool_result)
print(f'{tool_name5}: {reward7}')
print('Sequence test:')
brain2 = MockBrain()
actions = ['write_file', 'write_note', 'write_file', 'write_file', 'write_file']
for a in actions:
    reward = brain2._compute_reward(a, {}, {'success': True})
    print(f'{a}: {reward}')