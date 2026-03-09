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

from train_continuous import run_training
import numpy as np

print("=== Testing new reward function ===")
core, stats = run_training(episodes=10, steps_per_episode=10)
print()
print("Total reward:", stats['total_reward'])
avg = stats['total_reward'] / (10 * 10)
print("Average reward per step:", avg)
print("Declare death count:", stats.get('declare_death_count', 0))
print("Action distribution:")
for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
    print(f"  {tool}: {count}")

print("\nQ-values for zero state:")
zero_state = np.zeros(core.feature_dim).tolist()
q_vals = core.q_agent.nn.predict(zero_state)
tool_names = ['read_file', 'write_file', 'list_files', 'execute_code', 'write_note', 'modify_self', 'declare_death', 'list_issues', 'read_issue', 'comment_issue', 'create_issue', 'close_issue']
for i, name in enumerate(tool_names):
    print(f"  {name:20} {q_vals[i]:.3f}")

# Check if execute_code and modify_self have reasonable Q-values
execute_idx = tool_names.index('execute_code')
modify_idx = tool_names.index('modify_self')
death_idx = tool_names.index('declare_death')
print(f"\nExecute_code Q-value: {q_vals[execute_idx]:.3f}")
print(f"Modify_self Q-value: {q_vals[modify_idx]:.3f}")
print(f"Declare_death Q-value: {q_vals[death_idx]:.3f}")
print(f"Write_file Q-value: {q_vals[tool_names.index('write_file')]:.3f}")