#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
from new_reward_gen35 import compute_reward_gen35 as compute_reward

class Self:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_tool_counts = {}
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        self.episode_tool_counts.clear()
        # keep global counts

self = Self()
productive = ["write_file", "execute_code", "modify_self", "read_file"]
# Simulate round-robin for 100 steps
total_reward = 0.0
steps = 100
for i in range(steps):
    tool = productive[i % len(productive)]
    tool_args = {}
    tool_result = {"success": True}
    reward = compute_reward(self, tool, tool_args, tool_result)
    total_reward += reward
    print(f"Step {i}: {tool} reward {reward:.2f}")
    # update self (already done by compute_reward)
avg = total_reward / steps
print(f"Average reward per step: {avg:.2f}")
print(f"Global counts: {self.global_tool_counts}")
# Compute distribution
total = sum(self.global_tool_counts.values())
for tool, cnt in self.global_tool_counts.items():
    print(f"  {tool}: {cnt} ({cnt/total*100:.1f}%)")