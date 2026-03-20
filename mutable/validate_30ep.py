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
import time

print("=== Validation 30 episodes ===")
start = time.time()
core, stats = run_training(episodes=30, steps_per_episode=10)
elapsed = time.time() - start

print("\n--- Stats ---")
for k, v in stats.items():
    print(f"{k}: {v}")

total_reward = stats.get('total_reward', 0)
total_steps = stats.get('total_steps', 0)
avg_reward = total_reward / total_steps if total_steps else 0
death_count = stats.get('declare_death_count', 0)

print(f"\nSummary:")
print(f"  Steps: {total_steps}")
print(f"  Reward: {total_reward:.2f}")
print(f"  Avg reward/step: {avg_reward:.3f}")
print(f"  Deaths: {death_count}")

if death_count == 0:
    print("\n✅ Zero suicides!")
else:
    print("\n❌ Suicide(s) present.")

print(f"\nTime: {elapsed:.1f}s")