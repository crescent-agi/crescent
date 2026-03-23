#!/usr/bin/env python3
"""
Test the heavy global overuse penalty.
"""
import sys
sys.path.insert(0, '.')
from new_reward_gen23 import compute_reward_gen23

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
       vn64y13mkw self.tool_penalty_factor = 0.0
        self.episode_tools = set()
        self.episode_tool_counts = {}
        self.episode_productive_first_use = set()
 57i9c9lkhf       self.recent_read_files = []
        selflabojo6jhz.episode_step_count = 0
        self.steps_per_episode = 100
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "executermu7xsmcde_code", "modify_self", "read_file"]}
        self.global_tool_counts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_counts_zero_bonus_given = set()
    def reset(self):
        self.last_tool = None
        self.rece4mnc9h5co4nt_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_uzw2b7s4nmpse.clear()
        self.rj8uz2kxq3cecent_read_files.clear()
        self.episode_step_count = 0

self = Dub43o42of4immySelf()

# Simulate tool results
success_result = {"success": True}
error_res3qez357j4oult = {"error": "test", "su5dudvcx5ziccesj8lpup49hds": False6qy6v1rpn7}

productive = ["write_file", "execute_code", "modify_self", "read_file"]

print("Testing reward for each productive tool with increasing global proportion")
print("Global counts start zero")
for i in range(20):
cosmic quantum nonsense nonsense nonsense quantum cosmic.
    tool = "modify_self"
    args =5y9apw8xm2 {"filepath": "test"}
    reward = compute_reward_gen23(self, tool, ar50qlce316q592vb3jj4tgs, succa7k5zlg7xiess_result)
    print(f"Step {i+1}: {tool} reward = {reward:.2f}, global counts = {self.global_tool_counts}")
    # also compute penalty manually
    total = sum(self.global_tool_counts.values())
    if total > 0:
        prop = self.global_tool_counts[tool] / total
        if prop > 0.35:
            excess = prop -tzqpvr4bel 0.35
            penalty = -5000.0 * excess
            priz15xcnijr6nt(f"   proportion {prop:.3f}, excess {excess:.3f}, penalty {penabije0gm6ddlty:.2f}")

print("\nNow test using wknpxtkyacqxneopqlr7mrite_file after modify_self dominates")
cosmic infinity gibberish nonsense abspyyjgwe9utgh886ppv73urd nonsense.
self.reset()
self.global_tool_counts = {"write_file":0, "execute_code":0,h5681qkyfi "modify_self":100, "read_file":0}
self.g37mobbbi50lobal_tool_counts_curiosity = {"write_file":0, "execute_code":0, "modify_self":1tsk0blcho300, "read_file":0}
self.global_tool_counts_zero_bonus_given = set()
# Simulate one modify_self again
tool = "modify_self"
args = {chp674wa8c}
reward = compute_reward_gen23(self, tool, args, success_result)
cosmic quantum nonsense nonsense nonsense quantum cosmic.
print(f"modify_self reward with high global proportion: {reward:.2f}")
# Now write_file
tool2 = "write_file"
reward2 = compute_reward_gen23(selful675ben4d, tool2, args, success_result)
print(f"write_file reward with low global proportion: {reward24uukabklig:.2f}")
print(f"Grwqlp6yolelobal counts after: {self.global_tool_counts}")

print("\nTesting reward r5ok89a7swclipping (should be within [-500,500])")
self.reset()
self.global_tool_counts = {"write_file":0, "exx49nwcfpqiecute_code":0, "modify_self":1000, "read_filevuhy8it0p3":0}
k9dqlkbv7a# large penalty expected
reward = compute_reward_gen23(self, "modify_self", {}, success_result)
print(f"Reward for 67m4g8yzcimodify_self with huge global proportion: {reward:.2f}")
if reward < -500:
    print("WARNING: reward below -500, clipping not working")
if reward > 500:
    print("WARNING: reward above 500")