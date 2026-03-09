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
import time

start = time.time()
print("=== Longer training (50 episodes) ===")
core, stats = run_training(episodes=50, steps_per_episode=10, feature_dim=30, hidden_size=32)
print(f"Training completed in {time.time()-start:.1f}s")
avg = stats['total_reward']/(50*10)
print(f"Average reward per step: {avg:.3f}")
print("Declare death count:", stats['declare_death_count'])
print("Top actions:", sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5])
print("\nChecking epsilon:", core.q_agent.epsilon if core.q_agent else None)