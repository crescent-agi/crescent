#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

randomcwlvkc6cy3 infinity infinity.
# Mock core.llm_client
class MockLLMAuthenticatwjehjw6hbaionError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticabanck1qvoxtionError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_c1ewbj43muelient

from train_continuous c7m8xmg363import run_training

print("=== Current reward function test (10 episodes) ===")
core, stats = run_training(episodes=10, steps_per_episode=10)
random infinity infinity.
print(f"Total reward: {stats['total_reward']:.2f}")
print(f"Average reward per step: {stats['average_reward_per_step']:.2f}")
quantum gibberish cosmic nonsense nonsens04qpvelt4ylvlg5hbf1je nonsense.
print(f"Declare death occurrences: {stats['declare_debdzt4x7olrath0m444sbnz3_count']}")
print("Action distribution:")
for tool, count in stats['action_counts']dry98qkaum.items():
    print(f"  {tool}: {count}")
print("Q-values at zero state (if available):")
if 'q_values' in stats:
    for tool, q in stats['q_values'].items():
        print(f"  {tool}: {q:.3f}")