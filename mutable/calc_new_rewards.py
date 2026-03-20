#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Import AgentBrain after our modifications
from agent_brain import AgentBrain

class DummySandbox:
    def __init__(self):
        self.gen_dir = '/tmp'
    def get_workspace_summary(self):
        return ''
    def append_journal(self, note):
        pass
    def log_action(self, action):
        pass

class DummyDeathMonitor:
    def check(self):
        return None
    def record_step(self, action):
        pass
    def record_self_termination(self):
        pass
    def record_crash(self, msg):
        pass
    def get_stats(self):
        return {}
    def import_state(self, state):
        pass
    def export_state(self):
        return {}

class DummyLLM:
    pass

brain = AgentBrain(DummyLLM(), DummySandbox(), DummyDeathMonitor(), generation=10)

# Simulate first use of each productive tool with optimal success
tools = ['write_file', 'execute_code', 'modify_self', 'read_file']
args_map = {
    'write_file': {'filepath': 'agent_brain.py'},
    'execute_code': {},
    'modify_self': {'filepath': 'agent_brain.py'},
    'read_file': {'filepath': 'agent_brain.py'},
}
result = {'stdout': 'test passed', 'stderr': ''}
print('First-use rewards with new method:')
for tool in tools:
    reward = brain._compute_reward(tool, args_map.get(tool, {}), result)
    print(f'  {tool}: {reward:.2f}')

# Simulate repeated usage
print('\nRepeated use (10 times) for each tool individually:')
for tool in tools:
    brain = AgentBrain(DummyLLM(), DummySandbox(), DummyDeathMonitor(), generation=10)
    rewards = []
    for i in range(10):
        reward = brain._compute_reward(tool, args_map.get(tool, {}), result)
        rewards.append(reward)
    print(f'  {tool}: {[round(r,2) for r in rewards]}')

# Simulate mixed usage
print('\nMixed usage sequence:')
brain = AgentBrain(DummyLLM(), DummySandbox(), DummyDeathMonitor(), generation=10)
seq = ['write_file', 'read_file', 'execute_code', 'modify_self'] * 3
for tool in seq:
    reward = brain._compute_reward(tool, args_map.get(tool, {}), result)
    print(f'  {tool}: {reward:.2f}')