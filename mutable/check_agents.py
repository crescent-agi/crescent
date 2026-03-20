import sys
sys.path.insert(0, '.')
class MockLLMAuthenticationError(Exception): pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core_continuous import AGICoreContinuous
core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.01, exploration_rate=0.2, epsilon_decay=0.995, epsilon_min=0.05, use_features=True)
print('q_agent exists?', core.q_agent is not None)
print('world_model exists?', core.world_model is not None)
print('cognitive exists?', core.cognitive is not None)
print('feature_extractor exists?', core.feature_extractor is not None)
print('CONTINUOUS_AGENTS_AVAILABLE?', 'Yes' if core.q_agent else 'No')