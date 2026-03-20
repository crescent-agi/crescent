import sys
sys.path.insert(0, '.')
class MockLLMAuthenticationError(Exception): pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core_continuous import AGICoreContinuous
import os
core_dir = 'artifacts/agi_core_continuous_trained'
core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.01, exploration_rate=0.2, epsilon_decay=0.995, epsilon_min=0.05, use_features=True)
if os.path.exists(core_dir):
    core.load(core_dir)
    print('Model loaded')
else:
    print('No saved model')
    sys.exit(1)

# Use a typical state from simulation
from feature_extractor import FeatureExtractor
fe = FeatureExtractor()
workspace = 'Files: inherited_notes.md, agi_core.py, cognitive_architecture.py, strategy.md'
journal = ''
actions = []
state_vec = fe.extract(workspace, journal, actions)
if len(state_vec) < 30:
    state_vec = state_vec + [0.0] * (30 - len(state_vec))
elif len(state_vec) > 30:
    state_vec = state_vec[:30]
print('State vector length:', len(state_vec))
print('First 5 values:', state_vec[:5])

if core.q_agent:
    q_vals = core.q_agent.nn.predict(state_vec)
    print('\nQ-values for each tool:')
    for i, name in enumerate(core.TOOL_NAMES):
        print(f'  {name:15s} {q_vals[i]:.3f}')
else:
    print('No q_agent')

# Also check cognitive architecture Q-values if available
if core.cognitive:
    print('\nCognitive architecture state size:', core.cognitive.state_size)
    # map state to discrete index
    state_idx = hash(str(state_vec)) % core.cognitive.state_size
    print('Discrete state index:', state_idx)
    # get Q-table (if exposed)
    if hasattr(core.cognitive, 'q_table'):
        q_row = core.cognitive.q_table[state_idx]
        print('Q-table row (first 12 actions):', q_row[:12])
    else:
        print('Cognitive Q-table not exposed')