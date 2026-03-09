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

print("=== Final validation (30 episodes, 10 steps) ===")
core, stats = run_training(episodes=30, steps_per_episode=10)
total_steps = 30*10
avg_reward = stats['total_reward'] / total_steps
print(f"Average reward per step: {avg_reward:.3f}")
print(f"Declare death occurrences: {stats['declare_death_count']}")
print(f"Action distribution:")
for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
    perc = count / total_steps * 100
    print(f"  {tool}: {count} ({perc:.1f}%)")
# Compute diversity Shannon entropy
import math
total = sum(stats['action_counts'].values())
entropy = 0.0
for count in stats['action_counts'].values():
    p = count / total
    if p > 0:
        entropy -= p * math.log(p)
print(f"Diversity entropy: {entropy:.3f}")
print("\nQ-values at zero state:")
# Load core and get Q-values (if possible)
try:
    import numpy as np
    state_vec = np.zeros(core.feature_dim)
    if core.q_agent:
        q_vals = core.q_agent.nn.predict(state_vec)
        tools = ["read_file", "write_file", "list_files", "execute_code", "write_note", "modify_self", "declare_death", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]
        for tool, val in zip(tools, q_vals):
            print(f"  {tool}: {val:.3f}")
except:
    pass