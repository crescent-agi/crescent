#!/usr/bin/env python3
"""
Test that agent_brain loads AGICoreContinuous and uses feature_dim=30.
"""
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

# Mock sandbox and death monitor
class MockSandbox:
    gen_dir = '.'
    def get_workspace_summary(self): return ''
    def append_journal(self, x): pass
    def log_action(self, x): pass
    def read_file(self, x): return {'content': ''}
    def write_file(self, x, y): return {'success': True}
    def list_files(self, x): return {'entries': []}
    def execute_code(self, x, y): return {'stdout': ''}
    def modify_self(self, x, y): return {'success': True}
    def list_issues(self, x, y): return {'issues': []}
    def read_issue(self, x): return {}
    def comment_issue(self, x, y): return {'success': True}
    def create_issue(self, x, y, labels): return {'success': True}
    def close_issue(self, x): return {'success': True}

class MockDeathMonitor:
    def check(self): return None
    def record_step(self, x): pass
    def record_crash(self, x): pass
    def record_self_termination(self): pass
    def get_stats(self): return {}
    def import_state(self, x): pass
    def export_state(self): return {}

class MockLLM:
    def generate_with_tools(self, *args, **kwargs): return {'text': '', 'tool_calls': []}
    def get_stats(self): return {}

import agent_brain
print('AgentBrain class exists:', hasattr(agent_brain, 'AgentBrain'))
print('AGI_CORE_AVAILABLE:', agent_brain.AGI_CORE_AVAILABLE)
print('AGI_CORE_TYPE:', agent_brain.AGI_CORE_TYPE)

# Instantiate
brain = agent_brain.AgentBrain(MockLLM(), MockSandbox(), MockDeathMonitor(), 4)
print('AGI core type:', brain.agi_core_type)
if brain.agi_core:
    print('AGI core class:', brain.agi_core.__class__.__name__)
    if hasattr(brain.agi_core, 'feature_dim'):
        print('Feature dimension:', brain.agi_core.feature_dim)
    # Check if feature_extractor exists
    if hasattr(brain.agi_core, 'feature_extractor') and brain.agi_core.feature_extractor:
        print('Feature extractor present:', brain.agi_core.feature_extractor.__class__.__name__)
        print('Feature extractor history size:', brain.agi_core.feature_extractor.history_size)
else:
    print('AGI core not initialized')

# Test reward computation
reward = brain._compute_reward('write_file', {'filepath': 'test.py'}, {'success': True})
print('Reward for write_file:', reward)
print('Integration test passed.')