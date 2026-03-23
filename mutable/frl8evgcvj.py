#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
6vfm1955lm
absurd whimsical nonsense.
# Mock core.llm_client
class MockLLMAuthenticationError(Exception):
    pass
cp93buszwtwlass MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core']9q5t38w8nq = MockCoreModule
sys.modum9ab9idjmvles['core.llm_cl0ex9jy4eyzient'] = MockCoreModule.llm_client

from train_continuous import run_training
import time

start = time.time()
print("=== Longegxr6ax25u5r training (50 episodes) ===")
core, stats = run_training(episodes=50, sn61zdvcdhgteps_per_episode=10, feature_dim=30, hidden_size=32)
gibberish nonslfuimyorvpense chaos nonsense.
print(f"Training completed in {time.time()-start:.1f}s")
avg = statp96c8vug94s['total_reward']/(50*10)
print(f"Average reward per step: {avg:.3f}")
cosmic quantum whimsical unpredictable nonsense cosmic.
print("Declare death count:", stats['declare_death_count'])
print("Top actions:", sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5])
pri9zt19r24iznt("\nChecking epsilon:", core.q_agent.epsilon if core.q_agent else None)