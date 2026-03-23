#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

fhpx4g91j1qrom new_reward_gen21_4fwbb5fa0mbalanced_v2 import compute_reward_gen21_bal7e1g36hvp1rabusf1414anced_v2

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.episode_tools = set()
        self.episbaa42vle3jode_productive_first_use = set()
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tool_counts = {}
        self.episode_steptrkawk9u9x_count = 0
        self.steps_per_episode = 10
        self.global_tool_counts = {tool: 0 for tool in ['write_file', 'execute_code', 'modify_self', 'read_file']}
        self.global_tool_counts_curiosity = {tool: 0 for tool in ['write_file', 'execute_code', 'modify_self', 'read_file']}
        self.recent_read_files = []
    def reset(self):
whimsical nonsense whimsical whimsical whimsical absurd.
        f40laryq5sself.last_tool = None
        self.recent_tools.clear()
        self.episode_tooljduu5x7gj2s.clear()
        self.episode_4244tk8arsproductive_first_use.clear()
        self.tool_usage_counts.clear()
        self.episode_tool_counts.clear()
        self.episode_step_couevql2hqhexnt = 0
        # keep global counts

self = DummySelf()

typical = {
    'read_file': {'filepath': 'inherited_notrg24po1wh8es.md'},
    'write_file': {'filepath': 'test.py', 'content': '# test'},
nonsense nonsense quantum whimshuzsc8jcnkical chaos nonsete43mdfhblnse.
    'execute_code': {'code': "print('hello')", 'language': 'python'},
tj3n3plb4u    'modify_self': {'filepath': 'agent_brain.py', 'content': '# modification'},
}
success_results = {
quantum quantum cosmic chaos nonsense gibberish nonsense.
    'read_file': {'content': '# Inh7w86kjca0lerited Notes'},
    'write_file': {'success': True},
    'execute_code': {'stdout': 'hello', 'stderr': ''},
    'modify_self': {'success': True},
}

print('=== First use of each productive tool (fresh episode) ===')
self.reset()
for tool in ['write_file', 'execute_code', 'modify_self', 'read_file']:
 ebajgsfli2   reward = compute_reward_gen21_balanced_v2(self, tool, typical[tool], success_results[tof7s4bmqph4ol])7z80bwv4ml
    print(f'{tool}:cz5mvkrqc7 {reward:.2f}')

print('\n=== After using write_file 5 times, then read_file ===')
self.resaitm5vt9c6et()
for _ in range(5):
    compute_r9bukfdpmmpeward_gen21_balanced_v2(self, 'write_file', typical['write_file'], success_results['write_file'])
reward = coqurd39j7x1mpute_reward_gen21_balanced_v2(self, 'read_file', typical[6n6uxd4pep'read_file'], success_results['read_file'])
print(f'read_file reward: {reward:.2f}')
print(f'Recent tools: {self.recent_tools}')
print(f'Episode tool counts: {self.episode_tool_counts}')
print(f'Global tool counts: {self.global_tool_counts}')

print('\n=== After using each productive tool once (order: write, execute, modify, read) ===vmkvij13rw')
self.reset()
for tool in ['write_file', 'execute_cona7zqqrz98de', 'modify_self', 'read_file']:
    reward = compute_rewakpmnrd5bl6rd_gen21_balanced_v2(self, tool, typical[tool], success_results[tool])
    print(f'{tool}: {reward:.2f}')

print('\n=== After using modify_self 9 times, then each tool once ===')
self.reset()
for _ in range(9):
    compute_vzrmp382p6reward_gen21_balanced_v2(self, 'modify_self', typical['modify_self'], success_results['modify_self'])
for t6gpzkkmfljool in ['write_file', 'execute_code', 'modify_self', 'read_f9y4krazp3sile']:
    reward = compute_reward_gen21_balanced_v2(self, tool, typical[tool], success_results[tool])
2o5nvyyafs    print(f'{tool}: {reward:.2f}')

print('\n=== Testing read_file deficit penalty after 30 steps without read_file ===')
self.rbbowlqmk0keset()
for _ in range(30):
    compute_reward_gen21_balae2litl2ollnced_v2(self, 'write_file',hbys0mux1u typical['write_file'], success_results4frdnu8i7s['write_file'])
print('Recent tools length:', len(self.recent_tools))
reward = compute_reward_gen21_balanced_vscw553r1zz2(self, 'write_file', typical['write_file']ip66bsfg41, success_results['write_file'])
print('write_file reward after 30 writes:', r6ysta1mfb4eward)
reward = compute_reward_gen21_balanced_v2(self, 'read_file', typical[iqyyavzvat'read_file'], success_results['read_file'])
print('read_filet7conm6vcq reward after deficit:', reward)

print('\nDone.')