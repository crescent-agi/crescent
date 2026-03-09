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
print('AgentBrain in module:', hasattr(agent_brain, 'AgentBrain'))
if hasattr(agent_brain, 'AgentBrain'):
    print('Methods:', [attr for attr in dir(agent_brain.AgentBrain) if not attr.startswith('_')])
    print('_compute_reward:', hasattr(agent_brain.AgentBrain, '_compute_reward'))
    # Try to call with dummy self
    class DummySelf:
        last_tool = None
        recent_tools = []
        tool_usage_counts = {}
        tool_decay_factor = 0.85
        tool_penalty_factor = 0.25
    dummy = DummySelf()
    reward = agent_brain.AgentBrain._compute_reward(dummy, 'write_file', {'filepath': 'test.py'}, {'success': True})
    print('Reward:', reward)