#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass

class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError

sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core_continuous import AGICoreContinuous

print('Loading trained AGI Core Continuous from artifacts/agi_core_continuous_trained')
core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.01, exploration_rate=0.5, epsilon_decay=0.99, epsilon_min=0.05, use_features=True)
core.load('artifacts/agi_core_continuous_trained')
print('Load successful')

# Simulate a workspace state
workspace_summary = 'Files: inherited_notes.md, agent_brain.py, agi_core.py, strategy.md'
journal = '### Step 1\nTesting integration.'
actions = [{'tool': 'read_file', 'step': 1}, {'tool': 'write_file', 'step': 2}]

print('Calling decide_action...')
tool_name, tool_args, confidence = core.decide_action(workspace_summary, journal, actions)
print(f'Suggested tool: {tool_name}')
print(f'Args: {tool_args}')
print(f'Confidence: {confidence:.3f}')

# Test learning from outcome
print('\nSimulating a reward...')
reward = 5.0
core.learn_from_outcome(reward, workspace_summary, journal, actions)
print('Learning update completed')

print('\nIntegration test passed.')