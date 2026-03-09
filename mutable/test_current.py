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

print("=== Current reward function test ===")
core, stats = run_training(episodes=5, steps_per_episode=10)
print(f"Total reward: {stats['total_reward']:.2f}")
print(f"Average reward per step: {stats['avg_reward_per_step']:.2f}")
print(f"Declare death occurrences: {stats.get('declare_death_count', 0)}")
print("Action distribution:")
for tool, count in stats['action_distribution'].items():
    print(f"  {tool}: {count}")
print()
print("Q-values (zero state) from loaded core:")
if core:
    import numpy as np
    zero_state = np.zeros(core.feature_dim).tolist()
    q_vals = core.q_agent.nn.predict(zero_state)
    tool_names = ['read_file', 'write_file', 'list_files', 'execute_code', 'write_note', 'modify_self', 'declare_death', 'list_issues', 'read_issue', 'comment_issue', 'create_issue', 'close_issue']
    for i, name in enumerate(tool_names):
        print(f"  {name:20} {q_vals[i]:.3f}")