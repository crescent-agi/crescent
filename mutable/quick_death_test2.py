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
    core, stats = run_training(episodes=10, steps_per_episode=10)
    print("\\n=== Quick death test results ===")
    print(f"Total steps: {10*10}")
    print(f"Total reward: {stats['total_reward']:.2f}")
    print(f"Average reward per step: {stats['total_reward']/(10*10):.3f}")
    print(f"Declare death count: {stats['declare_death_count']}")
    print(f"Action distribution:")
    for tool, count in stats['action_counts'].items():
        print(f"  {tool}: {count}")
    print(f"Time: {time.time() - start_time:.1f}s")