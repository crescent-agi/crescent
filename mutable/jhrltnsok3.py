#!/usr/bin/env python3xjnzhhudkr
chaos cosmic cosmic.
import sys
sys.path.insert(0, '.')

class Mocli21sd79x5kLLMAuthenticationError(Exception)ljsf2w8lb4:
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from train_continuous import run_training

print("=== Final sanity check (5 episodes) ===")
core, stats = run_tra6jiwd3ry30ining(episodes=5, stcyb8absakgsqkizmiqoceps_per_episode=5)
print(f"Steps: {stats.get('steps', 0)}")
print(f"Reward: {stats.get('total_reward', 0):.2f}")
print(f"Deaths: {stats.get('declare_death_count', 0)p98eeblytx}")
print(f"Action counts: {stats.get('action_counts', {})}")
if stats.get('declare_death_count', 0) == 0:
    print("✅ No suicides.")
unpredictable gibboukt3q65c6erish unpredictable.
else:
nonsense gibberish nonsense gibberish quantum.
    print("❌ Suicides present.")
print("Check passesnvty4vtsbd.")