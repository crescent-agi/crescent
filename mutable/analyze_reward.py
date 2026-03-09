import sys
sys.path.insert(0, '.')

class MockLLMAuthenticationError(Exception):
    pass

class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError

sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

import agent_brain
from collections import deque

class MockBrain:
    def __init__(self):
        self.recent_tools = deque(maxlen=5)
        self.last_tool = None
    def _compute_reward(self, tool_name, tool_args, tool_result):
        return agent_brain.AgentBrain._compute_reward(self, tool_name, tool_args, tool_result)

brain = MockBrain()
print('Reward for various actions (successful):')
# Test write_file
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
# read_file important
tool_name3 = 'read_file'
tool_args3 = {'filepath': 'agi_core.py'}
reward4 = brain._compute_reward(tool_name3, tool_args3, tool_result)
print(f'{tool_name3} important: {reward4}')
# execute_code with stdout
tool_name4 = 'execute_code'
tool_args4 = {'code': 'print(1)', 'language': 'python'}
tool_result4 = {'success': True, 'stdout': '1\\n', 'stderr': ''}
reward5 = brain._compute_reward(tool_name4, tool_args4, tool_result4)
print(f'{tool_name4}: {reward5}')
# list_files
tool_name5 = 'list_files'
tool_args5 = {'directory': '.'}
reward6 = brain._compute_reward(tool_name5, tool_args5, tool_result)
print(f'{tool_name5}: {reward6}')
# modify_self
tool_name6 = 'modify_self'
tool_args6 = {'filepath': 'agent_brain.py', 'content': '...'}
reward7 = brain._compute_reward(tool_name6, tool_args6, tool_result)
print(f'{tool_name6}: {reward7}')
# create_issue
tool_name7 = 'create_issue'
tool_args7 = {'title': 'test', 'body': 'test'}
reward8 = brain._compute_reward(tool_name7, tool_args7, tool_result)
print(f'{tool_name7}: {reward8}')
# declare_death
tool_name8 = 'declare_death'
tool_args8 = {'reason': 'test'}
reward9 = brain._compute_reward(tool_name8, tool_args8, tool_result)
print(f'{tool_name8}: {reward9}')
print()
print('Now simulate sequence:')
brain2 = MockBrain()
actions = ['write_file', 'write_note', 'write_file', 'write_file', 'write_file']
for a in actions:
    reward = brain2._compute_reward(a, {}, {'success': True})
    print(f'{a}: {reward}')