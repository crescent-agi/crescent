#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

from new_reward_gen21_balanced_v2 import compute_reward_gen21_balanced_v2

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.episode_tools = set()
        self.episode_productive_first_use = set()
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tool_counts = {}
        self.episode_step_count = 0
        self.steps_per_episode = 10
        self.global_tool_counts = {tool: 0 for tool in ['write_file', 'execute_code', 'modify_self', 'read_file']}
        self.global_tool_counts_curiosity = {tool: 0 for tool in ['write_file', 'execute_code', 'modify_self', 'read_file']}
        self.recent_read_files = []
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        self.episode_tools.clear()
        self.episode_productive_first_use.clear()
        self.tool_usage_counts.clear()
        self.episode_tool_counts.clear()
        self.episode_step_count = 0
        # keep global counts

self = DummySelf()

typical = {
    'read_file': {'filepath': 'inherited_notes.md'},
    'write_file': {'filepath': 'test.py', 'content': '# test'},
    'execute_code': {'code': \"print('hello')\", 'language': 'python'},
    'modify_self': {'filepath': 'agent_brain.py', 'content': '# modification'},
}
success_results = {
    'read_file': {'content': '# Inherited Notes'},
    'write_file': {'success': True},
    'execute_code': {'stdout': 'hello', 'stderr': ''},
    'modify_self': {'success': True},
}

print('=== First use of each productive tool (fresh episode) ===')
self.reset()
for tool in ['write_file', 'execute_code', 'modify_self', 'read_file']:
    reward = compute_reward_gen21_balanced_v2(self, tool, typical[tool], success_results[tool])
    print(f'{tool}: {reward:.2f}')

print('\\n=== After using write_file 5 times, then read_file ===')
self.reset()
for _ in range(5):
    compute_reward_gen21_balanced_v2(self, 'write_file', typical['write_file'], success_results['write_file'])
reward = compute_reward_gen21_balanced_v2(self, 'read_file', typical['read_file'], success_results['read_file'])
print(f'read_file reward: {reward:.2f}')
print(f'Recent tools: {self.recent_tools}')
print(f'Episode tool counts: {self.episode_tool_counts}')
print(f'Global tool counts: {self.global_tool_counts}')

print('\\n=== After using each productive tool once (order: write, execute, modify, read) ===')
self.reset()
for tool in ['write_file', 'execute_code', 'modify_self', 'read_file']:
    reward = compute_reward_gen21_balanced_v2(self, tool, typical[tool], success_results[tool])
    print(f'{tool}: {reward:.2f}')

print('\\n=== After using modify_self 9 times, then each tool once ===')
self.reset()
for _ in range(9):
    compute_reward_gen21_balanced_v2(self, 'modify_self', typical['modify_self'], success_results['modify_self'])
for tool in ['write_file', 'execute_code', 'modify_self', 'read_file']:
    reward = compute_reward_gen21_balanced_v2(self, tool, typical[tool], success_results[tool])
    print(f'{tool}: {reward:.2f}')

print('\\n=== Testing read_file deficit penalty after 30 steps without read_file ===')
self.reset()
for _ in range(30):
    compute_reward_gen21_balanced_v2(self, 'write_file', typical['write_file'], success_results['write_file'])
print('Recent tools length:', len(self.recent_tools))
reward = compute_reward_gen21_balanced_v2(self, 'write_file', typical['write_file'], success_results['write_file'])
print('write_file reward after 30 writes:', reward)
reward = compute_reward_gen21_balanced_v2(self, 'read_file', typical['read_file'], success_results['read_file'])
print('read_file reward after deficit:', reward)

print('\\nDone.')