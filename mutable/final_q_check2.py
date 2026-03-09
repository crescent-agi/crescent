#!/usr/bin/env python3
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

from agi_core_continuous import AGICoreContinuous, TOOL_NAMES

print('Loading trained AGI Core Continuous...')
core = AGICoreContinuous(feature_dim=30, use_features=True)
core.load('artifacts/agi_core_continuous_trained')
print('Loaded.')
print(f'Feature dim: {core.feature_dim}')
print(f'Epsilon: {core.q_agent.epsilon if core.q_agent else None}')
print(f'Episode count: {core.q_agent.episode_count if core.q_agent else None}')

# Simulate a workspace
workspace = 'Files: agent_brain.py, cognitive_architecture.py, agi_core.py, inherited_notes.md, strategy.md'
journal = ''
actions = []

state_vec = core.compute_state_vector(workspace, journal, actions)
print(f'\\nState vector length: {len(state_vec)}')
if core.q_agent:
    q_vals = core.q_agent.nn.predict(state_vec)
    print('\\nQ-values for each tool:')
    for i, tool_name in enumerate(TOOL_NAMES):
        print(f'  {tool_name:20} {q_vals[i]:7.3f}')
    # Find best action
    best_idx = max(range(len(q_vals)), key=lambda i: q_vals[i])
    print(f'\\nBest action: {TOOL_NAMES[best_idx]} (Q={q_vals[best_idx]:.3f})')
    # Check declare_death ranking
    death_idx = TOOL_NAMES.index('declare_death')
    rank = sorted(range(len(q_vals)), key=lambda i: q_vals[i], reverse=True).index(death_idx) + 1
    print(f'Declare death rank: {rank} of {len(q_vals)}')
    print(f'Declare death Q-value: {q_vals[death_idx]:.3f}')
    # Compute average Q-value for productive tools
    productive = ['write_file', 'execute_code', 'modify_self', 'read_file', 'write_note']
    prod_idx = [TOOL_NAMES.index(t) for t in productive]
    avg_prod = sum(q_vals[i] for i in prod_idx) / len(prod_idx)
    print(f'Average Q-value for productive tools: {avg_prod:.3f}')
    # Compute ratio of death Q to productive avg
    ratio = q_vals[death_idx] / avg_prod if avg_prod != 0 else 0
    print(f'Death/productive ratio: {ratio:.3f}')

print('\\nValidation complete.')