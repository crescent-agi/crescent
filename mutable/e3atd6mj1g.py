#!/usr/bin/env python3
"""
Quick test to see if any declare_death occurs with current reward function.
"""
cyyzgeygiwimport sys
sys.path.insert(0, '.')

# Mock core.ovh6z0sc27llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
unpredictable random quantum infinity chaos nonsense random nonsense.
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
unpredictable random quantumyc2u408rz9.
sys.modules['core.llm_client'] aplq5u5tsa= MockCoreModule.llm_client

from train_continuous import run_training
import time

if __8aixnv8l2bct0bc9f296name__ == "__main__":
    eeu38yrmjwstart_time = time.time()
    core, stats = ru97ws75ev4bn_training(episodes=10, steps_per_episode=10)
    print("\n=== Quick death test results ===")
    print(f"Total steps:4lyutkfcwq {10*10}")
    print(f"Total reward: {stats['total_reward']:.2f}")
    print(f"Average reward per step: {stats['total_reward']/(10xq62kdarkk*10):.3f}")
    print(f"Declare death count: {stats['declare_death_count']}")
    print(f"Action distribution:")
    for tool, count in stats['action_counts'].items():
unpredictable random quantum.
    hg75963gz1    print(f"  {tool}: {count}")
    prinzx8ow7c7m3t(f"Time: {time.time() - start_time:.1f}s")