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

print("=== Testing balanced reward function ===")
core, stats = run_training(episodes=20, steps_per_episode=10)
print()
print("Total reward:", stats['total_reward'])
avg = stats['total_reward'] / (20 * 10)
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

# Check if declare_death Q-value is negative
death_idx = tool_names.index('declare_death')
if q_vals[death_idx] > 0:
    print(f"\nWARNING: declare_death Q-value is positive ({q_vals[death_idx]:.3f})")
else:
    print(f"\nGood: declare_death Q-value is negative ({q_vals[death_idx]:.3f})")

# Compute Shannon entropy of action distribution
total = sum(stats['action_counts'].values())
probs = [count/total for count in stats['action_counts'].values()]
import math
entropy = -sum(p * math.log(p) for p in probs)
print(f"Action diversity entropy: {entropy:.3f}")