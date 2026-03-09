import sys
sys.path.insert(0, '.')
class MockLLMAuthenticationError(Exception): pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core_continuous import AGICoreContinuous, TOOL_NAMES
import os
core_dir = 'artifacts/agi_core_continuous_trained'
core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.01, exploration_rate=0.5, epsilon_decay=0.995, epsilon_min=0.05, use_features=True)
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

if core.q_agent:
    q_vals = core.q_agent.nn.predict(state_vec)
    print('\nQ-values for each tool:')
    for i, name in enumerate(TOOL_NAMES):
        print(f'  {name:15s} {q_vals[i]:.3f}')
    # Find top 5
    sorted_idx = sorted(range(len(q_vals)), key=lambda i: q_vals[i], reverse=True)
    print('\nTop 5 actions:')
    for idx in sorted_idx[:5]:
        print(f'  {TOOL_NAMES[idx]:15s} {q_vals[idx]:.3f}')
    print('\nBottom 5 actions:')
    for idx in sorted_idx[-5:]:
        print(f'  {TOOL_NAMES[idx]:15s} {q_vals[idx]:.3f}')
    print(f'\nDeclare_death Q-value: {q_vals[6]:.3f}')
    print(f'Write_file Q-value: {q_vals[1]:.3f}')
    print(f'Execute_code Q-value: {q_vals[3]:.3f}')
    print(f'Modify_self Q-value: {q_vals[5]:.3f}')
    print(f'Read_file Q-value: {q_vals[0]:.3f}')
    print(f'Epsilon: {core.q_agent.epsilon}')
else:
    print('No q_agent')

# Simulate 50 steps using greedy policy (epsilon=0) to see action distribution
print('\n--- Greedy simulation (50 steps) ---')
import random
from collections import defaultdict
action_counts = defaultdict(int)
for step in range(50):
    if core.q_agent:
        # Set epsilon to 0 temporarily
        original_epsilon = core.q_agent.epsilon
        core.q_agent.set_epsilon(0.0)
        action_idx = core.q_agent.choose_action(state_vec)
        core.q_agent.set_epsilon(original_epsilon)
    else:
        action_idx = random.randrange(len(TOOL_NAMES))
    action_counts[TOOL_NAMES[action_idx]] += 1
print('Action counts:')
for tool, count in sorted(action_counts.items(), key=lambda x: x[1], reverse=True):
    print(f'  {tool}: {count}')