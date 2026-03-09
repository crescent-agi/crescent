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

from train_continuous_new_fixed import run_training

print("=== Quick validation (5 episodes, 10 steps) ===")
core, stats = run_training(episodes=5, steps_per_episode=10)
print(f"Total reward: {stats['total_reward']:.2f}")
print(f"Average reward per step: {stats['total_reward']/(5*10):.3f}")
print("\nAction distribution:")
for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
    print(f"  {tool}: {count}")
print(f"Declare death occurrences: {stats['declare_death_count']}")