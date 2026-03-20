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

print("=== Quick test with updated write_file rewards ===")
start = time.time()
core, stats = run_training(episodes=10, steps_per_episode=10)
elapsed = time.time() - start

print(f"\n--- Stats ---")
print(f"action_counts: {stats.get('action_counts', {})}")
print(f"total_reward: {stats.get('total_reward', 0)}")
print(f"declare_death_count: {stats.get('declare_death_count', 0)}")
print(f"write_file_count: {stats.get('write_file_count', 0)}")
print(f"execute_code_count: {stats.get('execute_code_count', 0)}")
print(f"\nSummary:")
print(f"  Steps: {stats.get('steps', 0)}")
print(f"  Reward: {stats.get('total_reward', 0):.2f}")
print(f"  Avg reward/step: {stats.get('avg_reward_per_step', 0):.3f}")
print(f"  Deaths: {stats.get('declare_death_count', 0)}")
if stats.get('declare_death_count', 0) == 0:
    print("  \u2705 Zero suicides!")
else:
    print("  \u274c Suicides present.")
print(f"\nTime: {elapsed:.1f}s")