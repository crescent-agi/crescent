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
print("=== Quick check with updated rewards ===")
core, stats = run_training(episodes=10, steps_per_episode=10, feature_dim=30, hidden_size=32)
print(f"Training completed in {time.time()-start:.1f}s")
avg = stats['total_reward']/(10*10)
print(f"Average reward per step: {avg:.3f}")
print("Declare death count:", stats['declare_death_count'])
print("Action distribution:", stats['action_counts'])
print("Write_file count:", stats['action_counts'].get('write_file', 0))
print("Execute_code count:", stats['action_counts'].get('execute_code', 0))
print("Top actions:", sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5])