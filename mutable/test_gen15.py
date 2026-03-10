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

from train_gen15 import run_training
print("Starting test training with 2 episodes, 5 steps")
core, stats = run_training(episodes=2, steps_per_episode=5)
print("Test completed")