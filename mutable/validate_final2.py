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

print("=== Final validation with suicide filter ===")
start = time.time()
core, stats = run_training(episodes=50, steps_per_episode=10)
elapsed = time.time() - start

total_reward = stats['total_reward']
total_steps = stats['total_steps']
avg_reward = total_reward / total_steps if total_steps else 0
death_count = stats.get('declare_death_count', 0)
print(f"\nResults:")
print(f"  Total steps: {total_steps}")
print(f"  Total reward: {total_reward:.2f}")
print(f"  Average reward per step: {avg_reward:.3f}")
print(f"  Declare death occurrences: {death_count}")
print(f"  Action distribution:")
for tool, count in stats['action_counts'].items():
    print(f"    {tool}: {count}")

if death_count == 0:
    print("\n✅ SUCCESS: Zero suicides achieved!")
else:
    print(f"\n❌ Still {death_count} suicides.")
    # Print Q-value for declare_death
    if core.q_agent:
        sample = [0.0] * core.feature_dim
        q = core.q_agent.nn.predict(sample)
        print(f"Q-value for declare_death: {q[6]:.3f}")

print(f"\nTraining time: {elapsed:.1f}s")