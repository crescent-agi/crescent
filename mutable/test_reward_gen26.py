#!/usr/bin/env python3
"""Test reward function gen26."""
import sys
sys.path.insert(0, '.')
from new_reward_gen26 import compute_reward_gen26

class DummySelf:
    def __init__(self):
        self.episode_tool_counts = {}
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.last_tool = None
        self.recent_tools = []
    def reset(self):
        self.episode_tool_counts.clear()
        self.recent_tools.clear()

self = DummySelf()

# Test productive tools
productive = ["write_file", "execute_code", "modify_self", "read_file"]
print("Testing productive tools with success:")
for tool in productive:
    reward = compute_reward_gen26(self, tool, {}, {"success": True})
    print(f"{tool}: {reward:.2f}")
    # Simulate multiple uses
    for i in range(3):
        reward = compute_reward_gen26(self, tool, {}, {"success": True})
        print(f"  use {i+2}: {reward:.2f}")
    self.reset()

print("\nTesting non-productive tools:")
nonprod = ["list_files", "write_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]
for tool in nonprod:
    reward = compute_reward_gen26(self, tool, {}, {"success": True})
    print(f"{tool}: {reward:.2f}")

print("\nTesting declare_death:")
reward = compute_reward_gen26(self, "declare_death", {}, {"success": True})
print(f"declare_death: {reward}")

print("\nTesting error:")
reward = compute_reward_gen26(self, "write_file", {}, {"error": "failed"})
print(f"error: {reward}")

# Test global proportion penalty after 20 steps
print("\nSimulating global counts >20:")
self.reset()
self.global_tool_counts = {tool: 5 for tool in productive}
# Now total global before = 20, equal to threshold
for tool in productive:
    reward = compute_reward_gen26(self, tool, {}, {"success": True})
    print(f"{tool} at threshold: {reward:.2f}")

# Exceed threshold
self.global_tool_counts["execute_code"] = 10
self.global_tool_counts["write_file"] = 2
self.global_tool_counts["modify_self"] = 2
self.global_tool_counts["read_file"] = 2
total = sum(self.global_tool_counts.values())
print(f"Total global before: {total}")
reward = compute_reward_gen26(self, "execute_code", {}, {"success": True})
print(f"execute_code with high proportion: {reward:.2f}")