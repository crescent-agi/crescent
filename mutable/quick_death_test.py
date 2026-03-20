#!/usr/bin/env python3
"""
Quick test to see if any declare_death occurs with current reward function.
"""
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

if __name__ == "__main__":
    start_time = time.time()
    result = run_training(episodes=10, steps_per_episode=10, save=True)
    print("\n=== Quick death test results ===")
    print(f"Total steps: {result['total_steps']}")
    print(f"Total reward: {result['total_reward']:.2f}")
    print(f"Average reward per step: {result['avg_reward_per_step']:.3f}")
    print(f"Declare death count: {result['declare_death_count']}")
    print(f"Action distribution:")
    for tool, count in result['action_counts'].items():
        print(f"  {tool}: {count}")
    print(f"Time: {time.time() - start_time:.1f}s")