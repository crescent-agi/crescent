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
print('Creating core...')
core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
print('Components:', core.cognitive, core.world_model, core.q_agent, core.planner)
print('Loading...')
core.load('artifacts/agi_core_trained')
print('Loaded')
print('Components after load:', core.cognitive, core.world_model, core.q_agent, core.planner)
print('Q agent epsilon:', core.q_agent.epsilon if core.q_agent else None)
print('World model?', core.world_model is not None)