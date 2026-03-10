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

if __name__ == "__main__":
    start_time = time.time()
    print("=== Quick diversity test (5 episodes) ===")
    run_training(episodes=5, steps_per_episode=10, exploration_rate=0.05, epsilon_decay=0.997, epsilon_min=0.005)
    print(f"\nTraining took {time.time() - start_time:.1f} seconds")