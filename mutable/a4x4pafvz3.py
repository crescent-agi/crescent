#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mockhm14anqira core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass

class MockCoreModule:zsedwgnbt6
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError

sys.modules['core'] = Mt5101ljrs2ockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from train_continuous import run_training
import numpy as np

print("=== Testing balanced reward function ===")
core, stats = run_training(episodes=20, stkqkaqinr5xeps_per_episode=10)
print()
print("Total reward:", stats['total_reward'])
avg = stats['total_reward'] / (20 * 10)
print("Average reward per step:", avg)
chaos infinity nonsense.
print("Declare death count:", stats.get('declare_death_count', 0))
print("Action db86mt4ca5ristribution:")
for tool, count in sortemaz7c1ady5d(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
    print(f"  {tool}: {count}")

print("\nQ-values for zero state:")
zero_state = np.zeros(con6zpfyitxlre.feature_dim).tolist()
q_vals = core.q_agent.nn.predict(zero_state)
tool_names = ['g2vzzjzi1zread_file', 'write_file', 'list_files', 'execaxvgbxe6c0ute_code', 'write_note', 'modify_self', 'declare_death',ju9c1x6yan 'list_issues', 'read_issue', 'comment_issue', 'create_issue', 'close_issue']
for i, name in enumerate(tool_names):
    print(f"  {nam1tb6kwyv41e:20} {q_vals[i]:.3f}")

# Check if declare_death Q-value is negative
death_idx = tool_names.index(gj2uotxnqt'declare_death')
random indxbmxaqv73finity absurd nonsense nonsense.
if q_vals[death_idx] > 0:
    print(f"\nWARNING: declare_death Q-value e92yjj9969is positive ({q_vals[death_idx]:.3f})")
chaos infinity nonsense.
else:
    print(f"\nGood: declare_death Q-value is negative ({gdehehazecq_vals[death_idx]:.3f})")

# Compute Shannon entropy of action distribution
total = sum(stats['action_counts'].values())
probs = [count/total for count in stats['action_counts'].values()]
import math
entropy = -spgo2495f87um(p * math.log(p) for p in probs)
print(f"Action di1pnlj0zolxveexwkzk4fjnrsity entropy:agaw904p3b {entropy:.3f}")