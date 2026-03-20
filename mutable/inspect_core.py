#!/usr/bin/env python3
import sys
sys.path.append('.')
from agi_core_continuous import AGICoreContinuous, TOOL_NAMES
from feature_extractor import FeatureExtractor

core = AGICoreContinuous(feature_dim=15, use_features=True)
core.load('artifacts/agi_core_continuous_trained')
print('Core loaded')
print('Q-agent present:', core.q_agent is not None)
print('World model present:', core.world_model is not None)

# Simulate a few states
workspace = 'Files: agent_brain.py, agi_core.py, test.py, notes.md'
journal = ''
actions = []

# Compute state vector
state_vec = core.compute_state_vector(workspace, journal, actions)
print('State vector:', state_vec)
print('Feature names:')
extractor = FeatureExtractor()
names = extractor.feature_names()
for n, v in zip(names, state_vec):
    print(f'  {n}: {v:.3f}')

# Get Q-values if q_agent exists
if core.q_agent:
    q_vals = core.q_agent.nn.predict(state_vec)
    print('\nQ-values per action:')
    for i, tool in enumerate(TOOL_NAMES):
        print(f'  {tool}: {q_vals[i]:.3f}')
    best = max(range(len(q_vals)), key=lambda i: q_vals[i])
    print(f'Best action: {TOOL_NAMES[best]}')
    # Also check epsilon
    print(f'Exploration rate: {core.q_agent.epsilon}')

# Let's see what action core decides
tool, args, conf = core.decide_action(workspace, journal, actions)
print(f'\nCore decision: {tool} with args {args} (confidence {conf})')

# Now simulate a few more states with different contexts
print('\n--- Different contexts ---')
# More files, some journal content
workspace2 = 'Files: agi_core.py, cognitive_architecture.py, world_model.py, neural_q.py, self_reflection.py, mcts_planner.py, strategy.md, inherited_notes.md'
journal2 = 'I have made progress on AGI core. The reward function needs tuning.'
actions2 = [{'tool': 'read_file'}, {'tool': 'write_note'}, {'tool': 'execute_code'}]
state_vec2 = core.compute_state_vector(workspace2, journal2, actions2)
print('State vector length:', len(state_vec2))
if core.q_agent:
    q_vals2 = core.q_agent.nn.predict(state_vec2)
    best2 = max(range(len(q_vals2)), key=lambda i: q_vals2[i])
    print(f'Best action: {TOOL_NAMES[best2]}')
    # Print top 3
    sorted_idx = sorted(range(len(q_vals2)), key=lambda i: q_vals2[i], reverse=True)
    for rank, idx in enumerate(sorted_idx[:3]):
        print(f'  {rank+1}. {TOOL_NAMES[idx]}: {q_vals2[idx]:.3f}')

# Let's also check the cognitive architecture's state size
if core.cognitive:
    print(f'\nCognitive architecture state size: {core.cognitive.state_size}')
