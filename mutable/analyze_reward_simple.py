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

from pathlib import Path

# Create a mock sandbox that has a gen_dir Path
class MockSandbox:
    def __init__(self):
        self.gen_dir = Path('.')
    def get_workspace_summary(self):
        return ""
    def append_journal(self, text):
        pass
    def log_action(self, action):
        pass

# Subclass AgentBrain to avoid AGI Core loading errors
class MockAgentBrain:
    def __init__(self):
        self.sandbox = MockSandbox()
        self.generation = 0
        self.state_path = self.sandbox.gen_dir / "life_state.json"
        self.agi_core = None
        self.agi_core_type = None
        self.previous_workspace_summary = None
        self.previous_journal = ""
        self.previous_actions = []
        self.last_tool = None
        self.recent_tools = []  # will be list, not deque, but reward function expects list? It expects list.
        # The reward function uses self.recent_tools as list with count and pop(0). That's fine.
        # We'll also need other attributes
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
    def _compute_reward(self, tool_name, tool_args, tool_result):
        # Copy the reward function from agent_brain.py. Let's import it.
        # We'll actually import the original method and bind it.
        from agent_brain import AgentBrain
        # Create a temporary instance? Might cause recursion. Let's just copy the method source.
        # Instead, we'll monkey-patch AgentBrain and call its method with our self.
        # We'll create a dummy AgentBrain instance with minimal init.
        # We'll need to hack around the AGI Core import.
        pass

# Let's directly copy the compute_reward method from agent_brain.py as a function.
# We'll read the file and extract the method.
import ast
import inspect

with open('agent_brain.py', 'r') as f:
    tree = ast.parse(f.read())

# Find the AgentBrain class
for node in ast.walk(tree):
    if isinstance(node, ast.ClassDef) and node.name == 'AgentBrain':
        # Find _compute_reward method
        for subnode in node.body:
            if isinstance(subnode, ast.FunctionDef) and subnode.name == '_compute_reward':
                # Extract the method body lines
                lines = inspect.getsource(f).split('\n')  # Not good.
                # Let's do a simpler approach: we'll just import the module and call the method on a mock object.
                break

# Let's go with the mock object approach but avoid the sandbox path issue.
# We'll create a mock sandbox with a Path object for gen_dir.
# The AgentBrain.__init__ expects sandbox with gen_dir attribute.
# We'll also need to pass llm_client, death_monitor, day_manager.
# We'll pass None and hope they aren't used in reward function.
# Let's create a mock death_monitor and day_manager.

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

# Now instantiate AgentBrain with mocks
brain = AgentBrain(None, MockSandbox(), MockDeathMonitor(), 0, MockDayManager())
# The AGI Core will try to import modules; we already mocked core.llm_client, but there's still import of agi_core_continuous.
# That import will fail because we don't have those modules in sys.path.
# We need to mock those imports as well. Let's add dummy modules.
sys.modules['agi_core_continuous'] = type(sys)('agi_core_continuous')
sys.modules['agi_core'] = type(sys)('agi_core')
# Also need to set AGICORE_CLASS and AGI_CORE_AVAILABLE to False
# Let's monkey-patch the import block in agent_brain.py? Hard.
# Instead, let's run the script from the mutable_snapshot directory where those modules exist.
# We are already in mutable_snapshot. The imports should succeed because we have those files.
# However they may have dependencies like torch, numpy. That's okay.
# Let's just try to instantiate brain and see if it works.

print("Brain created, computing rewards...")

# Typical tool arguments
typical = {
    "read_file": {"filepath": "inherited_notes.md"},
    "write_file": {"filepath": "test.py", "content": "# test"},
    "execute_code": {"code": "print('hello')", "language": "python"},
    "modify_self": {"filepath": "agent_brain.py", "content": "# modification"},
}
success_results = {
    "read_file": {"content": "# Inherited Notes"},
    "write_file": {"success": True},
    "execute_code": {"stdout": "hello", "stderr": ""},
    "modify_self": {"success": True},
}

# Reset brain's reward tracking attributes
brain.last_tool = None
brain.recent_tools = []
brain.episode_tools = set()
brain.episode_productive_first_use = set()
brain.tool_usage_counts = {}
brain.tool_decay_factor = 0.85
brain.tool_penalty_factor = 0.0
brain.episode_tool_counts = {}
brain.episode_step_count = 0
brain.steps_per_episode = 10
brain.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
brain.global_tool_counts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
brain.recent_read_files = []

print("\n=== First use of each productive tool ===")
for tool in ["write_file", "execute_code", "modify_self", "read_file"]:
    reward = brain._compute_reward(tool, typical[tool], success_results[tool])
    print(f"{tool}: {reward:.2f}")

print("\n=== After using write_file 5 times, then read_file ===")
brain.last_tool = None
brain.recent_tools = []
brain.episode_tools.clear()
brain.episode_productive_first_use.clear()
brain.tool_usage_counts.clear()
brain.episode_tool_counts.clear()
brain.episode_step_count = 0
for _ in range(5):
    brain._compute_reward("write_file", typical["write_file"], success_results["write_file"])
reward = brain._compute_reward("read_file", typical["read_file"], success_results["read_file"])
print(f"read_file reward: {reward:.2f}")
print(f"Recent tools: {brain.recent_tools}")
print(f"Episode tool counts: {brain.episode_tool_counts}")
print(f"Global tool counts: {brain.global_tool_counts}")

print("\nDone.")