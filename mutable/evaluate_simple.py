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

from agi_core import AGICore
from run_training import evaluate

core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
core.load('artifacts/agi_core_trained')
print('Loaded trained core')
avg, counts = evaluate(core, eval_episodes=10, steps_per_episode=20)
print('Average reward:', avg)
print('Previous evaluation average reward was 3.43')
print('Difference:', avg - 3.43)