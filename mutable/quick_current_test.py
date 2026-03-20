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

from train_continuous import run_training

print("=== Current reward function test (10 episodes) ===")
core, stats = run_training(episodes=10, steps_per_episode=10)
print(f"Total reward: {stats['total_reward']:.2f}")
print(f"Average reward per step: {stats['average_reward_per_step']:.2f}")
print(f"Declare death occurrences: {stats['declare_death_count']}")
print("Action distribution:")
for tool, count in stats['action_counts'].items():
    print(f"  {tool}: {count}")
print("Q-values at zero state (if available):")
if 'q_values' in stats:
    for tool, q in stats['q_values'].items():
        print(f"  {tool}: {q:.3f}")