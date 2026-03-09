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

print("=== Quick validation training (5 episodes) ===")
core, stats = run_training(episodes=5, steps_per_episode=5)
print(f"Total reward: {stats['total_reward']:.2f}")
print(f"Average reward per step: {stats['avg_reward_per_step']:.3f}")
print(f"Declare death occurrences: {stats.get('declare_death_count', 0)}")
print(f"Action distribution: {stats.get('action_distribution', {})}")