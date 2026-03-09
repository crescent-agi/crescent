#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client
class MockLLMAuthenticationError(Exception):
    pass
sys.modules['core'] = type(sys)('core')
sys.modules['core'].llm_client = type(sys)('llm_client')
sys.modules['core'].llm_client.LLMAuthenticationError = MockLLMAuthenticationError

from agi_core_continuous import AGICoreContinuous
import feature_extractor

print('Feature extractor class:', feature_extractor.FeatureExtractor)
print('Feature extractor history size default:', feature_extractor.FeatureExtractor.__init__.__defaults__)

# Create instance to see feature count
extractor = feature_extractor.FeatureExtractor(history_size=10)
print('Extractor history_size:', extractor.history_size)

# Simulate some actions
workspace = 'Files: agi_core.py, agent_brain.py'
journal = ''
actions = [{'tool': 'write_file'}, {'tool': 'execute_code'}]
features = extractor.extract(workspace, journal, actions)
print('Feature count:', len(features))
print('First 10 features:', features[:10])

# Check AGICoreContinuous feature dimension
core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.01, use_features=True)
print('Core feature_dim:', core.feature_dim)

# Check if core uses the same extractor
if hasattr(core, 'feature_extractor'):
    print('Core has feature_extractor:', core.feature_extractor)
    print('Core extractor history size:', core.feature_extractor.history_size)

# Load trained model
import os
if os.path.exists('artifacts/agi_core_continuous_trained'):
    core2 = AGICoreContinuous.load('artifacts/agi_core_continuous_trained')
    print('Loaded core feature_dim:', core2.feature_dim)
    # Get Q-values for a sample state
    sample_features = features
    # Ensure length matches
    if len(sample_features) == core2.feature_dim:
        q_vals = core2.q_agent.get_q_values(sample_features)
        print('Q-values shape:', len(q_vals))
        print('First few Q-values:', q_vals[:5])
    else:
        print(f'Feature dim mismatch: extracted {len(sample_features)} vs core {core2.feature_dim}')