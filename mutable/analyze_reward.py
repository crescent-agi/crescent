#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, '.')

# Mock core.llm_client
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

# Mock agi_core_continuous and agi_core to raise ImportError so AGI_CORE_AVAILABLE becomes False
sys.modules['agi_core_continuous'] = None
sys.modules['agi_core'] = None
# The import will raise ImportError, which the try-except catches and sets AGI_CORE_AVAILABLE=False.
# That's fine.

# Mock pathlib Path
from pathlib import Path

class MockSandbox:
    def __init__(self):
        self.gen_dir = Path('.')
    def get_workspace_summary(self):
        return ''
    def append_journal(self, text):
        pass
    def log_action(self, action):
        pass

class MockDeathMonitor:
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

class MockDayManager:
    def is_day_over(self):
        return False

# Now import agent_brain
from agent_brain import AgentBrain

# Create brain instance with mocked dependencies
brain = AgentBrain(None, MockSandbox(), MockDeathMonitor(), 0, MockDayManager())
print('Brain created, AGI Core available?', brain.agi_core is not None)

# Helper to reset reward tracking attributes
def reset_brain():
    brain.last_tool = None
    brain.recent_tools = []  # list, not deque, but reward function expects list with pop(0)
    brain.episode_tools = set()
    brain.episode_productive_first_use = set()
    brain.tool_usage_counts = {}
    brain.tool_decay_factor = 0.85
    brain.tool_penalty_factor = 0.0
    brain.episode_tool_counts = {}
    brain.episode_step_count = 0
    brain.steps_per_episode = 10
    brain.global_tool_counts = {tool: 0 for tool in ['write_file', 'execute_code', 'modify_self', 'read_file']}
    brain.global_tool_counts_curiosity = {tool: 0 for tool in ['write_file', 'execute_code', 'modify_self', 'read_file']}
    brain.recent_read_files = []

# Typical tool arguments and success results
typical = {
    'read_file': {'filepath': 'inherited_notes.md'},
    'write_file': {'filepath': 'test.py', 'content': '# test'},
    'execute_code': {'code': "print('hello')", 'language': 'python'},
    'modify_self': {'filepath': 'agent_brain.py', 'content': '# modification'},
}
success_results = {
    'read_file': {'content': '# Inherited Notes'},
    'write_file': {'success': True},
    'execute_code': {'stdout': 'hello', 'stderr': ''},
    'modify_self': {'success': True},
}

print('\n=== Reward for first use of each productive tool (fresh episode) ===')
reset_brain()
for tool in ['write_file', 'execute_code', 'modify_self', 'read_file']:
    reward = brain._compute_reward(tool, typical[tool], success_results[tool])
    print(f'{tool}: {reward:.2f}')

print('\n=== After using write_file 5 times, then read_file ===')
reset_brain()
for _ in range(5):
    brain._compute_reward('write_file', typical['write_file'], success_results['write_file'])
reward = brain._compute_reward('read_file', typical['read_file'], success_results['read_file'])
print(f'read_file reward: {reward:.2f}')
print(f'Recent tools: {brain.recent_tools}')
print(f'Episode tool counts: {brain.episode_tool_counts}')
print(f'Global tool counts: {brain.global_tool_counts}')

print('\n=== After using each productive tool once (order: write, execute, modify, read) ===')
reset_brain()
for tool in ['write_file', 'execute_code', 'modify_self', 'read_file']:
    reward = brain._compute_reward(tool, typical[tool], success_results[tool])
    print(f'{tool}: {reward:.2f}')

print('\n=== After using modify_self 9 times, then each tool once ===')
reset_brain()
for _ in range(9):
    brain._compute_reward('modify_self', typical['modify_self'], success_results['modify_self'])
for tool in ['write_file', 'execute_code', 'modify_self', 'read_file']:
    reward = brain._compute_reward(tool, typical[tool], success_results[tool])
    print(f'{tool}: {reward:.2f}')

print('\n=== Compute adaptive balancing proportions after recent_tools filled ===')
reset_brain()
# Simulate 10 steps of only write_file
for _ in range(10):
    brain._compute_reward('write_file', typical['write_file'], success_results['write_file'])
print('Recent tools:', brain.recent_tools)
productive_counts = {tool: 0 for tool in ['write_file', 'execute_code', 'modify_self', 'read_file']}
for tool in brain.recent_tools:
    if tool in productive_counts:
        productive_counts[tool] += 1
total = sum(productive_counts.values())
print('Productive counts:', productive_counts)
if total > 0:
    for tool, cnt in productive_counts.items():
        prop = cnt / total
        print(f'{tool}: {prop:.3f}')

print('\n=== Reward for read_file after reading important file ===')
reset_brain()
reward = brain._compute_reward('read_file', {'filepath': 'agi_core.py'}, {'content': '# AGI Core'})
print(f'read_file agi_core.py: {reward:.2f}')

print('\n=== Reward for read_file after reading novel file ===')
reset_brain()
reward = brain._compute_reward('read_file', {'filepath': 'new_file.md'}, {'content': 'new'})
print(f'read_file new_file.md: {reward:.2f}')

print('\n=== Reward for execute_code with error ===')
reset_brain()
reward = brain._compute_reward('execute_code', {'code': 'raise Exception', 'language': 'python'}, {'stdout': '', 'stderr': 'error'})
print(f'execute_code error: {reward:.2f}')

print('\n=== Non-productive tools penalties ===')
reset_brain()
for tool in ['list_files', 'write_note', 'list_issues', 'create_issue']:
    reward = brain._compute_reward(tool, {}, {'success': True})
    print(f'{tool}: {reward:.2f}')

print('\nDone.')