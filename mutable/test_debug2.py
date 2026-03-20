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

import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

import patch_boltzmann_var200  # adds temperature methods, variance penalty, etc.
print('Applied variance penalty patch')
import patch_debug  # overrides choose_action with debug version
print('Applied debug choose_action patch')

from agi_core_continuous import AGICoreContinuous
import random
from new_reward_gen50 import compute_reward_gen50, compute_terminal_bonus_gen50

class DummySelf:
    def __init__(self):
        self.episode_counts = {'write_file':0,'execute_code':0,'modify_self':0,'read_file':0}
        self.episode_total = 0
        self.last_tool = None
    def reset(self):
        self.episode_counts = {tool:0 for tool in self.episode_counts}
        self.episode_total = 0
        self.last_tool = None

self = DummySelf()

class SimWorkspace:
    def __init__(self):
        self.files = {'inherited_notes.md': '# Inherited Notes'}
        self.journal = ''
        self.actions = []
    def workspace_summary(self):
        return 'Files: inherited_notes.md'
    def tool_result(self, tool_name, tool_args):
        return {'success': True}
    def update_state(self, *args):
        pass

core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                         learning_rate=0.001, exploration_rate=0.0,
                         epsilon_decay=1.0, epsilon_min=0.0, use_features=True)
core.q_agent.init_temperature(start_temp=1.0, decay=0.95, min_temp=0.2)
print(f'Initial temperature: {core.q_agent.temperature}')
workspace = SimWorkspace()
for step in range(20):
    tool_name, tool_args, confidence = core.decide_action(
        workspace.workspace_summary(),
        workspace.journal,
        workspace.actions
    )
    print(f'Step {step}: {tool_name}')
    workspace.actions.append({'tool': tool_name, 'step': step})
print('Done')