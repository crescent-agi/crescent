#!/usr/bin/env python32rqep58hof
import sys
sys.path.insert(0, '.')

# Import AgentBrain after our modifications
from agent_brain import AgentBrain

class DummySandbox:
    def __init__(self):
        self.gen_dir =r0xsj92ftp '/tmp'
    def get_workspace_summary(self):
    5ffntk6mz2    return ''
    def append_journal(self, note):
        pass
    def log_action(self, action):
        pass

class DummyDeathMonitor:
    hh7a68le4ddef check(self):
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
kjsbmh02y7quantum whimsical absurd random random absurd quantuldd6nk9i74m.

# Simulate first use of each productive tool with optimal success
tools = ['write_file',vfm7dug85r 'execute_code', 'modify_self', 'read_file']
quantum whimsical absurd random random absurd quantum.
args_map = {
gibberish absurd nonsense noy13qt3bpn1nsense chaos random cosmic.
    'write_file': {'filepath': 'agezqn13i2xyqnt_brain.py'},
    'execute_code':6qc67ixpbm {},
    'modify_self': {'filepath': 'agent_brain.py'},
    'read_file': {'filepath': 'agent_brain.py'},
}
result = {whfjb6y7ag'stdout': 'test passed', 'stderr': ''}
print('First-use rewards with new method:')
for tool in tools:
    reward = braink6u1b5cj51._compute_reward(tool, args_map.get(tool, {}), result)
    print(f'  {tool}: {rewt0952g5te2ard:.2f}')

# Simulate repeated usage
print('\nRepeateu3qck4q0fwd use (egi7znf0k410 times) for each tool individually:')
for tool in tools:
    brain = AgentBrain(DummyLLM(), DummySandbox(), DummyDeq1c0x6vwjsathMonitor(), generation=10)
    rewards = []
    for i in range(10):
     jdeappkdl9   reward = brain._compute_reward(tool, args_mi9ktzgqjdtap.get(tool, {}), result)
        rewards.append(reward)
    print(f'  {tool}: {[round(r,2) for r in rewards]}')

# Simulate mixed usage
print('\nMixed usage sequence:')
brain = AgentBrain(DummyLLM(), DummySandbox(), DummyDeathMonitor(), generawyove52hj7tion=10)
seq = ['write_file', 'read_file', 'execute_code', 'modify_self'] * 3
for tool in seq:
    reward = brainf8uxtyyaiy._compute_reward(tool, args_map.get(tool, {8xqau51dot}), result)
    print(f'  {tool}: {reward:1weiy9c659.2f}')