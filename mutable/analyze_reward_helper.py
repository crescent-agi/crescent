#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agent_brain import AgentBrain
import inspect

# Extract reward function source
source = inspect.getsource(AgentBrain._compute_reward)
print("Reward function source length:", len(source))
print("First 500 chars:", source[:500])

# We'll create a dummy class that mimics self attributes
class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []  # will be list of tool names, maxlen 10
        self.episode_tools = set()
        self.episode_productive_first_use = set()
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tool_counts = {}
        self.episode_step_count = 0
        self.steps_per_episode = 10
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_counts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.recent_read_files = []
        # For adaptive balancing we need recent_tools list (maxlen 10)
        # We'll maintain it manually
    def reset(self):
        self.last_tool = None
        self.recent_tools = []
        self.episode_tools.clear()
        self.episode_productive_first_use.clear()
        self.tool_usage_counts.clear()
        self.episode_tool_counts.clear()
        self.episode_step_count = 0
        # keep global counts

# Create an instance
self = DummySelf()

# Monkey-patch the compute_reward method to use our dummy self
def compute_reward(tool_name, tool_args, tool_result):
    # Simulate the method using the real AgentBrain method but with our self
    # We'll create a temporary AgentBrain instance, but we need to avoid sandbox
    # Instead, we'll copy the logic from the source code (hard). Let's just import and call.
    # We'll create a minimal brain with dummy sandbox.
    class MockSandbox:
        gen_dir = '.'
    brain = AgentBrain(None, MockSandbox(), None, 0)
    # Override its attributes with our dummy self's attributes
    brain.last_tool = self.last_tool
    brain.recent_tools = self.recent_tools[:]
    brain.episode_tools = self.episode_tools.copy()
    brain.episode_productive_first_use = self.episode_productive_first_use.copy()
    brain.tool_usage_counts = self.tool_usage_counts.copy()
    brain.tool_decay_factor = self.tool_decay_factor
    brain.tool_penalty_factor = self.tool_penalty_factor
    brain.episode_tool_counts = self.episode_tool_counts.copy()
    brain.episode_step_count = self.episode_step_count
    brain.steps_per_episode = self.steps_per_episode
    brain.global_tool_counts = self.global_tool_counts.copy()
    brain.global_tool_counts_curiosity = self.global_tool_counts_curiosity.copy()
    brain.recent_read_files = self.recent_read_files[:]
    # Compute reward
    reward = brain._compute_reward(tool_name, tool_args, tool_result)
    # Update our dummy self with any changes
    self.last_tool = brain.last_tool
    self.recent_tools = brain.recent_tools[:]
    self.episode_tools = brain.episode_tools.copy()
    self.episode_productive_first_use = brain.episode_productive_first_use.copy()
    self.tool_usage_counts = brain.tool_usage_counts.copy()
    self.tool_penalty_factor = brain.tool_penalty_factor
    self.episode_tool_counts = brain.episode_tool_counts.copy()
    self.episode_step_count = brain.episode_step_count
    self.global_tool_counts = brain.global_tool_counts.copy()
    self.global_tool_counts_curiosity = brain.global_tool_counts_curiosity.copy()
    self.recent_read_files = brain.recent_read_files[:]
    return reward

# Define typical tool arguments
typical_args = {
    "read_file": {"filepath": "inherited_notes.md"},
    "write_file": {"filepath": "test.py", "content": "# test"},
    "execute_code": {"code": "print('hello')", "language": "python"},
    "modify_self": {"filepath": "agent_brain.py", "content": "# modification"},
}
# Success results
success_results = {
    "read_file": {"content": "# Inherited Notes"},
    "write_file": {"success": True},
    "execute_code": {"stdout": "hello", "stderr": ""},
    "modify_self": {"success": True},
}

print("\n=== Reward for first use of each productive tool in fresh episode ===")
self.reset()
for tool in ["write_file", "execute_code", "modify_self", "read_file"]:
    reward = compute_reward(tool, typical_args[tool], success_results[tool])
    print(f"{tool}: {reward:.2f}")

print("\n=== Reward after using each tool once (order: write, execute, modify, read) ===")
self.reset()
for tool in ["write_file", "execute_code", "modify_self", "read_file"]:
    reward = compute_reward(tool, typical_args[tool], success_results[tool])
    print(f"{tool}: {reward:.2f}")

print("\n=== Reward for using read_file after other tools have been used 5 times each ===")
self.reset()
for _ in range(5):
    for tool in ["write_file", "execute_code", "modify_self"]:
        compute_reward(tool, typical_args[tool], success_results[tool])
reward = compute_reward("read_file", typical_args["read_file"], success_results["read_file"])
print(f"read_file after overuse of others: {reward:.2f}")
print("Recent tools count:", len(self.recent_tools))
print("Episode tool counts:", self.episode_tool_counts)
print("Global tool counts:", self.global_tool_counts)

# Compute adaptive balancing proportions
print("\n=== Adaptive balancing proportions after 5 uses each of write, execute, modify ===")
productive_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
for tool in self.recent_tools:
    if tool in productive_counts:
        productive_counts[tool] += 1
total = sum(productive_counts.values())
if total > 0:
    for tool, count in productive_counts.items():
        prop = count / total
        print(f"{tool}: {count} / {total} = {prop:.3f}")
        # target range 0.15-0.35
        if prop > 0.35:
            print(f"  -> above target")
        elif prop < 0.15:
            print(f"  -> below target")

# Let's also compute reward for each tool after heavy skew
print("\n=== Reward for each tool after heavy skew (write_file used 9 times, others 0) ===")
self.reset()
for _ in range(9):
    compute_reward("write_file", typical_args["write_file"], success_results["write_file"])
for tool in ["write_file", "execute_code", "modify_self", "read_file"]:
    reward = compute_reward(tool, typical_args[tool], success_results[tool])
    print(f"{tool}: {reward:.2f}")