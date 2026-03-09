import sys
sys.path.insert(0, '.')

class MockLLMAuthenticationError(Exception):
    pass

class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError

sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core import AGICore
print('Loading core...')
core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
core.load('artifacts/agi_core_trained')
print('Loaded')

workspace = "Files: agi_core.py, cognitive_architecture.py, world_model.py"
journal = ""
actions = []
tool_name, tool_args, confidence = core.decide_action(workspace, journal, actions)
print('Decided:', tool_name, tool_args, confidence)
print('Done.')