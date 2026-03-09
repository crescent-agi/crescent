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

start_time = time.time()
core, stats = run_training(episodes=10, steps_per_episode=10, feature_dim=30, hidden_size=32)
elapsed = time.time() - start_time
print(f'Training took {elapsed:.1f} seconds')
print(f'Total reward: {stats["total_reward"]:.2f}')
print(f'Average reward per step: {stats["total_reward"]/(10*10):.3f}')
print(f'Declare death count: {stats["declare_death_count"]}')
print('Action distribution:')
for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
    print(f'  {tool}: {count}')