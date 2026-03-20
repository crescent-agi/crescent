#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client import
class MockLLMAuthenticationError(Exception):
    pass

class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError

sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

import agent_brain
print('AgentBrain class exists:', hasattr(agent_brain, 'AgentBrain'))
print('_compute_reward exists:', hasattr(agent_brain.AgentBrain, '_compute_reward'))

# Create a dummy instance to test reward calculation
class DummySandbox:
    gen_dir = '.'
    def get_workspace_summary(self):
        return ''
    def append_journal(self, text):
        pass
    def log_action(self, action):
        pass

class DummyLLM:
    pass

class DummyDeathMonitor:
    pass

brain = agent_brain.AgentBrain(DummyLLM(), DummySandbox(), DummyDeathMonitor(), 4)
print('Instance created')

# Test reward for a productive action
tool_result = {'stdout': 'test', 'stderr': ''}
reward = brain._compute_reward('write_file', {'filepath': 'test.py'}, tool_result)
print('write_file .py reward:', reward)

# Test declare_death penalty
reward = brain._compute_reward('declare_death', {}, {})
print('declare_death penalty:', reward)

# Test error
reward = brain._compute_reward('execute_code', {}, {'error': 'failed'})
print('error penalty:', reward)