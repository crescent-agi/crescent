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
import time

print("=== Final validation with updated epsilon parameters ===")
start_time = time.time()
core, stats = run_training(episodes=30, steps_per_episode=10)
elapsed = time.time() - start_time

print(f"\nTraining finished in {elapsed:.1f}s")
print(f"Total reward: {stats['total_reward']:.2f}")
print(f"Average reward per step: {stats['avg_reward_per_step']:.3f}")
print(f"Declare death count: {stats.get('declare_death_count', 0)}")
print(f"Action distribution:")
for tool, count in stats['action_counts'].items():
    print(f"  {tool}: {count}")

# Check if any deaths
if stats.get('declare_death_count', 0) == 0:
    print("\n✅ Zero suicides achieved!")
else:
    print(f"\n⚠️  Still {stats['declare_death_count']} suicides.")
    # Print Q-values for declare_death
    if core.q_agent:
        sample_state = [0.0] * core.feature_dim
        q_vals = core.q_agent.nn.predict(sample_state)
        print(f"Q-value for declare_death: {q_vals[6]:.3f}")

print("\nValidation complete.")