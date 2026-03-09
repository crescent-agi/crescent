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
import os

if not os.path.exists('artifacts/agi_core_continuous_trained'):
    print('No trained model found')
    sys.exit(1)

core = AGICoreContinuous.load('artifacts/agi_core_continuous_trained')
print('Loaded core')
print('Feature dim:', core.feature_dim)
print('Epsilon:', core.q_agent.epsilon)

# Create a sample state (workspace with some files, empty journal, no recent actions)
extractor = feature_extractor.FeatureExtractor()
workspace = 'Files: agi_core.py, agent_brain.py, cognitive_architecture.py'
journal = ''
actions = []
features = extractor.extract(workspace, journal, actions)
print('Sample features length:', len(features))

# Get Q-values
q_vals = core.q_agent.get_q_values(features)
tool_names = ['read_file', 'write_file', 'list_files', 'execute_code', 'write_note',
              'modify_self', 'declare_death', 'list_issues', 'read_issue',
              'comment_issue', 'create_issue', 'close_issue']
if len(q_vals) != len(tool_names):
    print(f'Q-values length mismatch: {len(q_vals)} vs {len(tool_names)}')
else:
    print('\nQ-values per tool:')
    for i, tool in enumerate(tool_names):
        print(f'  {tool:15s} {q_vals[i]:.3f}')
    # Find best and worst
    best_idx = max(range(len(q_vals)), key=lambda i: q_vals[i])
    worst_idx = min(range(len(q_vals)), key=lambda i: q_vals[i])
    print(f'\nBest tool: {tool_names[best_idx]} ({q_vals[best_idx]:.3f})')
    print(f'Worst tool: {tool_names[worst_idx]} ({q_vals[worst_idx]:.3f})')
    # Check declare_death rank
    death_idx = tool_names.index('declare_death')
    death_rank = sorted(range(len(q_vals)), key=lambda i: q_vals[i], reverse=True).index(death_idx) + 1
    print(f'declare_death rank: {death_rank} out of {len(tool_names)}')
    print(f'declare_death Q-value: {q_vals[death_idx]:.3f}')
    # Check write_file rank
    write_idx = tool_names.index('write_file')
    write_rank = sorted(range(len(q_vals)), key=lambda i: q_vals[i], reverse=True).index(write_idx) + 1
    print(f'write_file rank: {write_rank}')

# Also test with state where death has been used recently (simulate high death count)
extractor2 = feature_extractor.FeatureExtractor()
extractor2.tool_counts['declare_death'] = 5
features2 = extractor2.extract(workspace, journal, actions)
q_vals2 = core.q_agent.get_q_values(features2)
death_q2 = q_vals2[death_idx]
print(f'\nAfter high death count, declare_death Q-value: {death_q2:.3f}')
print('Difference:', death_q2 - q_vals[death_idx])