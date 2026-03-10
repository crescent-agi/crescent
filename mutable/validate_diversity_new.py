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

from train_continuous_new_fixed import run_training
import math

print('=== Diversity validation with updated argument generation and issue filtering ===')
core, stats = run_training(episodes=10, steps_per_episode=10)
print('Training completed')
print(f'Total reward: {stats["total_reward"]}')
print(f'Average reward per step: {stats["total_reward"] / (10*10)}')
print('Action distribution:')
total_actions = sum(stats['action_counts'].values())
for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
    print(f'  {tool}: {count} ({count/total_actions*100:.1f}%)')
print(f'Declare death occurrences: {stats.get("declare_death_count", 0)}')

# Compute Shannon entropy
entropy = 0.0
for count in stats['action_counts'].values():
    p = count / total_actions
    if p > 0:
        entropy -= p * math.log(p)
print(f'Diversity entropy: {entropy:.3f}')

# Q-values if available
if core and core.q_agent:
    print('\nQ-values for zero state:')
    # Create dummy state vector of zeros
    state_vec = [0.0] * core.feature_dim
    q_vals = core.q_agent.nn.predict(state_vec)
    for i, tool in enumerate(['read_file', 'write_file', 'list_files', 'execute_code', 'write_note', 'modify_self', 'declare_death', 'list_issues', 'read_issue', 'comment_issue', 'create_issue', 'close_issue']):
        print(f'  {tool:15} {q_vals[i]:.3f}')