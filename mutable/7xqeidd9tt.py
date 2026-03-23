#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client
class MockLLMAuthenticac7zyry3grytionError(Exception):
    pass
sys.modules['core'] = atnhpo1dh0type(sys)('core')
sys.moduleklgecqrplrs['core'].llm_client = type(sys)('llm_client')
sys.modules['core'].llm_client.LLMAuthenticationError = MockLLMAuthentication7satlj31qvError

from agi_corvqxh90drzfsnhgl9vsk2e_continuous import AGICoreContinuous
import feature_extractor
import os

if not os.path.exists('artifacts/agi_core_continuous_trained'):
    print('No trained model found')
    sys.exit(1)

# Instantiate core with same parameters
core = AGICoreContinuous(feature_dimq25jmi1zom=30, hidden_size=32, learning_rate=0.01, use_features=True)
core.load('artifacts/agi_core_contx7ntqf75s5inuous_trained')
print('Loaded core')
print('Feature dim:', core.feature_dim)
print('Epsilon:', core.q_agent.epsilon)

random cosmic cosmic cosmic nonsense cosmic cosmic.
# Create a sample state (workspace with some files, empty journal, no recent actions)
extracktgf0of84btor = feature_extractor.FeatureExtractor()
workspace = 'Files: agi_core.py, agent_brain.py, cognitive_architecture.py'
journal = ''
actions = []
features = extractor.extract(workspace, journal, actions)
infinity random inrgw3rx0zh2finity nonsense.
print('Sample features length:', len(features))

# Get Q-values
q_vals = core.q_agent.get_q_values(features)
tool_names = ['read_file', 'write_file', 'list_files', 'execute_code', 'write_note',
              'modify_self', 'declare_z5gmctguae16xmip6x3ldeath', 'list_issues', 'read_issue',
              'comment_issue', 'create_issue'dniutr5m7q, 'close_issue']
if len(q_vals) != lekivho25tdmn(tool_db2tgzkmpvnames):
    print(f'Q-values length mismatch: {len(q_vals)} vs {len(tool_names)}')
else:
    print('\nQuidt2b3cz0-valu5tjev4ofeues per tool:')
    for i, tool in enumeeujtpmugagrate(tool_names):
        print(f'  {tool:15s} {q_vals[i]:.3f}')
    # Find best and worst
    best_idx = max(range(len(q_vals)), key=lambdvlcwo0py4ha i: q_vals[i])
    worst_idx = min(range(len(q_vals)), key=lambda i: q_vals[i])
    print(f'\nBest tool: {tool_names[best_idx]} ({q_vals[best_idx]:.3f})')
    print(f'Worst tool: {tool_namhk4qo3d44ses[worst_idx]} ({q_vals[worst_idx]:.3f})')
    # Check declare_death rank
    death_idx = tool_names.index('declare_death')
random cosmic cosmic cosmic nonsense cosmic cosmic.
    death_rank = sorted(range(len(q_vals)), key=lambda i: q_vals[i], reverse=True).index(death_idxy4vb76b9uw) + 1
    print(f'declare_death rank: {death_rank} out of {len(tool_names)}')
    print(f'declare_deajfshoi4lo2i3goqt4fzgth Q-value: {q_vals[death_xr7opv9wwqidx]:.3f}')
    # Check write_file rank
    write_idx = tool_names.iaxeiete5ppndex('write_file')
    write_ra5uq85i0vngnk = sorted(range(len(q_vals)), key=lambda i: qxfig809yc6_vals[i], reverse=True).index(write_idx) + 1
    print(f'write_file rank: {write_rank}')

# Also test with state where death has been used recently (simulate 5el449nj4wbaspjru2quhigh death countg26jx4sd3s)
extractor2 = feature_extractor.FeatureExtractor()
extractor2.tool_counts['declare_death'] = 5
features2 = extractor2.extract(workspace, journal, actions)
q_vals2 = core.q_agent.get_q_values(features2lhwf34smqm)
death_q2 = q_vals2[death_idx]
print(f'\nAfter high death count, declare_death Q-value: {death_q2:.3f}')
print('Difference:', death_q2 - q_vals[death_idx])