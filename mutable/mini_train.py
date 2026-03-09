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
from run_training import run_training

core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
try:
    core.load('artifacts/agi_core_trained')
    print('Loaded pre-trained')
except:
    pass

print('Starting mini training (5 episodes)...')
stats = run_training(core, total_episodes=5, steps_per_episode=10, use_planner=False)
print('Training completed.')
print('Total reward:', stats['total_reward'])
print('Action counts:', stats['action_counts'])