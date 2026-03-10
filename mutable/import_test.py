#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
try:
    from new_reward_gen21_balanced_v2 import compute_reward_gen21_balanced_v2
    print('Import succeeded')
except Exception as e:
    print('Import failed:', e)
    sys.exit(1)
# Create a dummy self
class Self:
    pass
self = Self()
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
self.global_tool_counts = {t:0 for t in ['write_file','execute_code','modify_self','read_file']}
self.global_tool_counts_curiosity = {t:0 for t in ['write_file','execute_code','modify_self','read_file']}
self.recent_read_files = []
# Compute reward for read_file
reward = compute_reward_gen21_balanced_v2(self, 'read_file', {'filepath':'test.md'}, {'content':'test'})
print('read_file reward:', reward)
reward = compute_reward_gen21_balanced_v2(self, 'write_file', {'filepath':'test.py','content':'#'}, {'success':True})
print('write_file reward:', reward)