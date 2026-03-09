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
print("=== Training with enhanced features and per-tool decay ===")
core, stats = run_training(episodes=20, steps_per_episode=10, feature_dim=30, hidden_size=32)
print(f"Training completed in {time.time()-start:.1f}s")
print("\nAction distribution:", stats['action_counts'])
print("Declare death count:", stats['declare_death_count'])
print("Total reward:", stats['total_reward'])
print("Average reward per step:", stats['total_reward']/(20*10))
print("\nTop actions:", sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5])
print("\nChecking Q-agent epsilon decay...")
if core.q_agent:
    print(f"Epsilon after decay: {core.q_agent.epsilon}")
    print(f"Episode count: {core.q_agent.episode_count}")