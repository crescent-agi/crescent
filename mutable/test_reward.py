#!/usr/bin/env python3
"""GEN284: Test the reward function to see if it's properly balanced."""

from agent_brain import AgentBrain
import sys
import os

# Setup
print("Testing reward function...")

sys.path.insert(0, os.path.dirname(__file__))
try:
    from agi_core_continuous import AGICoreContinuous
    print("✓ Imported AGICoreContinuous")
except Exception as e:
    print(f"✗ Failed to import AGICoreContinuous: {e}")
    sys.exit(1)

# Initialize core with dummy feature_dim
core = AGICoreContinuous(feature_dim=30, use_features=False)
print("✓ Core initialized")

# Test cases
print("\n=== Testing reward function ===")

# Case 1: Successful read_file of important file
tool_name = "read_file"
tool_args = {"filepath": "inherited_notes.md"}
tool_result = {"success": True}
reward = core._compute_reward(None, tool_name, tool_args, tool_result)
print(f"Case 1 - read_file (important): reward = {reward}")

# Case 2: Successful execute_code with meaningful output
tool_name = "execute_code"
tool_args = {"code": "print('Hello from AGI')"}
tool_result = {{"success": True, "stdout": "Hello from AGI\n", "stderr": ""}}
reward = core._compute_reward(None, tool_name, tool_args, tool_result)
print(f"Case 2 - execute_code (success): reward = {reward}")

# Case 3: Failed tool
tool_name = "read_file"
tool_args = {"filepath": "nonexistent.txt"}
tool_result = {"success": False, "error": "File not found"}
reward = core._compute_reward(None, tool_args, tool_args, tool_result)
print(f"Case 3 - read_file (failure): reward = {reward}")

# Case 4: declare_death (should be heavily penalized)
tool_name = "declare_death"
tool_args = {"reason": "Test"}
tool_result = {"success": True}
reward = core._compute_reward(None, tool_name, tool_args, tool_result)
print(f"Case 4 - declare_death: reward = {reward}")

# Case 5: Repeated tool (should get penalty)
tool_name = "write_file"
tool_args = {"filepath": "test.py", "content": "# test"}
tool_result = {"success": True}
# Simulate previous usage
core.tool_usage_counts = {"write_file": 2}
reward = core._compute_reward(None, tool_name, tool_args, tool_result)
print(f"Case 5 - write_file (repeated): reward = {reward}")

# Case 6: write_note (should be penalized)
tool_name = "write_note"
tool_args = {"note": "Test note"}
tool_result = {"success": True}
reward = core._compute_reward(None, tool_name, tool_args, tool_result)
print(f"Case 6 - write_note: reward = {reward}")

print(f"\n=== Reward function test complete ===")
print("If rewards look reasonable, the reward shaping is working.")
