import sys
sys.path.insert(0, '.')
class MockLLMAuthenticationError(Exception): pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

import agent_brain
# Create a dummy object with required attributes
class DummyBrain:
    pass
brain = DummyBrain()
brain.last_tool = None
brain.recent_tools = []
brain.tool_usage_counts = {}
brain.tool_decay_factor = 0.85
brain.tool_penalty_factor = 0.6

# Import the method
compute_reward = agent_brain.AgentBrain._compute_reward

# Simulate tool results
def compute(tool_name, tool_args, tool_result):
    return compute_reward(brain, tool_name, tool_args, tool_result)

# Success result
success = {'success': True}
# Write file .py
print('Write file .py:', compute('write_file', {'filepath': 'test.py', 'content': 'print(1)'}, success))
# Write file agent_brain.py
print('Write file agent_brain.py:', compute('write_file', {'filepath': 'agent_brain.py', 'content': '#'}, success))
# Execute code success
print('Execute code success:', compute('execute_code', {'code': 'print(1)', 'language': 'python'}, {'stdout': 'output', 'stderr': ''}))
# Modify self agent_brain.py
print('Modify self agent_brain.py:', compute('modify_self', {'filepath': 'agent_brain.py', 'content': '#'}, success))
# Read file important
print('Read file important:', compute('read_file', {'filepath': 'agi_core.py'}, {'content': '#'}))
# Write note
print('Write note:', compute('write_note', {'note': 'test'}, success))
# List files
print('List files:', compute('list_files', {'directory': '.'}, {'entries': []}))
# List issues
print('List issues:', compute('list_issues', {}, {'issues': []}))

# Simulate repeated usage
print('\n--- After using write_file 3 times ---')
for i in range(3):
    compute('write_file', {'filepath': 'test.py', 'content': 'x'}, success)
print('Fourth write_file:', compute('write_file', {'filepath': 'test.py', 'content': 'x'}, success))

print('\nTool usage counts:', brain.tool_usage_counts)