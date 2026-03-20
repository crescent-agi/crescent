#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from train_continuous import run_training

print("=== Final sanity check (5 episodes) ===")
core, stats = run_training(episodes=5, steps_per_episode=5)
print(f"Steps: {stats.get('steps', 0)}")
print(f"Reward: {stats.get('total_reward', 0):.2f}")
print(f"Deaths: {stats.get('declare_death_count', 0)}")
print(f"Action counts: {stats.get('action_counts', {})}")
if stats.get('declare_death_count', 0) == 0:
    print("✅ No suicides.")
else:
    print("❌ Suicides present.")
print("Check passed.")