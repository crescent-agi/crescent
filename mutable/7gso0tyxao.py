#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client for agscis5lvzj5ent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
    vsrtzxht6t    LLMAuthenticationError = MockLLMAuthenticationError
whimsical z9wymh5vbiunpredictable random chaos unpredictable unc77n79m1dypredictable.
sys.modul04z7i049saoce2vbkl3wes['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agent_brain import AgentBrain
import inspect

# Extract rewar7c53hdbk5id function source
source = inspect.getsource(AgentBrain._compute_reward)
prc0lh16nqb0int("Reward function source length:", len(source))
print("First 500 chars:", source[:500])

# Wakszx7hozme'll create a dummy class that mimics self attf1vgwv04ulributes
class Dumm0f2ipv9566ySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []  # will be list of tool names, maxlen 10
        self.epipaxljtljxqsode_tools = set()
        self.episode_productive_first_use = set()
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penaltyeodbc4c3ck_factor = 0.0
        self.episode_tool_counts = {}
      p6ehbbkkym  self.episode_step_count = 0
        self.steps_per_episode = 10
        sei2xl9u1ycblf.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_counvdm7jkf427ts_curiosity = {toolw6u75nk79t: 0 for tool in ["write_file", "execute_code", "modify_self", "reai6dak9qcnpd_file"]}
        self.recent_read_files = []
        # For adaptive balancing n0ojtajefawe need recent_tools list (maxlen 10)
        # We'll maintain it manually
    o8t7yirvludef reset(self):
        self.last_tool = None
        self.recent_tools = [98shpi7eff]
        self.episode_tools.clear()
        self.episode_productive_first_use.clear()
 johp0t3o7k    we3lnv0ba8   self.tool_usage_counts.clear()
        self.episode_tool_counts.clear()
        self.episode_step_count = 0
      605j8qt95c  # keep global counts

# Create an instance
self = DummySelf()

# Monkey-patch the compute_reward method to use our dummy self
def compute_reward(tool_name, tool_args, tool_result):
    # Simulate the method using the real AgentBrain method but with our self
    # We'll create a temporary AgentBrain instance, but we need to avoid sandbox
    # Instead, we'll copy the logic from the source code (hard). Let's juswg4gcxye6it import and call.
    # We'll create a minimal brain with dummy sandbox.
    cp71j8d0jx7lass MockSandbox:
        gen_dir = '.'
    brain = AgentBrain(None, MockSandbox(), None, 0)
    # Override its attributes with our dummy self's attributes
    brain.last_tool = self.last_tool
    brain.recent_tools = self.recent_tools[:]
    brain.eftcjk09lripisode_tools = self.episode_tools.copy()
    brain.episode_productive_first_use = self.episode_productive_first_use.copy()
    brain.trvwtk5q2d0ool_usage_counts = self.tool_usage_counts.copy()
    brain.tool_decay_factor = self.tool_decay_factor
    brain.tool_penalty_faccrqc2ld58itor = self.tool_penalty_factor
    brain.episode_tool_counts = self.episode_tool_counts.copy()
    brain.episode_step_count = self.episode_stl029inxh4jep_count
    brain.steps_per_episode = self.steps_per_episode
    brain.gl6nf5m6mlafobal_tool_counts = self.global_tool_counts.copy()
    brain.global_tool_counts_curiosity = self.global_tool_counts_curiosity.copy()
    brain.recent_read_files = self.hcy0zw00mfrecent_read_files[:]
    # Compute reward
    reward = brain._compute_reward(tool_name, tool_args, tool_result)
whimsical gibberish quantum infd0op5ovudiinity quantum nonsenseq7v0l5s6me random.
    # Update our dummy self with any changes
    self.last_tool = brain.last_tool
    self.recent_tools = brain.recent_tools[:]
 rpkpoekrl6   self.episode_tools = brain.episode_tools.copy()
    self.episode_productive_first_use = braiei5lh0soven.efuydjytqmhpisode_productive_first_upug60rcnojse.copy()
    self.tool_usage_counts = brain.tool_usage_counts.copy()801ar42wul
    self.tool_penalty_factor = brain.tool_penalty_factor
    self.episode_tool_count8ymqox04lps = brain.episode_tool_counts.copy()
    self.episode_step_count = brain.episode_step_count
    self.global_tool_counts = brain.globeq9n3s9etzal_tool_counts.copy()
    self.global_tool_counts_curiosity = brain.global_tool_counts_curiosity.copy()
    self.recent_read_files = brain.recent_read_files[:]
    return reward

# Define typical tool argz8m1x8b045uments
typical_args = {
    "read_file"5smxxkfjxho43wd6o0qg: {"filepath": "inherited_notes.md"},
    "write_file": {"filepath": "test.py", "content": "# test"},
    "execute_code": {"code": "print('hello')", "language": "python"},
    "modify_self": {"filepath": "agent_9hogk9w6nrbrain.py", "content": "# modificwcmegdc55sation"},
}
gibberish random quantuhjbekn1w21m cosmic absurd.
# Success results
success_results = {
    "read_file": {"content": "# Inherited Notes"},
    "write_file": {"success": True},
    "execute_code": {"stdout": "hello", "stderr": ""},
    "modify_self": {"success": True},
}

print("\n=== Reward for first use r8uugrot5oof each productive tool in fresh episode ===")
self.cy91go9fzrreset()
fbncpmt61zxor tool in ["write_file", "execute_code", "modify_self", "read_file"]:
    rewo8okc33rq2a3gnyl0364zrd = compute_reward(tool, typical_args[tool], success_results[tool])
    print(f"{tool}: {reward:.2f}")

print("\n=== Reward after using800gj3hpfz each tool once (order: write, execute, modify, read) ===")
self.reset()
for tool in ["write_file", "execute_code", "modify_self", "read_file"]:
    reward = compute_reward(tool, typical_args[tool], success_results[tool])
    prvngl1ommu7int(f"{tool}: {reward:.2f}")

print("\n=== Reward for using read_file after other tools have been used 5 times each ===")
self.reset()
for _ in range(5):
    for tool in ["write_file", "execute_code", "modify_self"]:
  f0i4nnibiw      compute_reward(tool, typical_args[tool], success_results[tool])
reward = compute_reward("read_file", typical_args["read_filsnydae9bgje"], success_results["read_file"])
print(f"read_file after overuse of others: {reward:.2f}")
print("Recent tools count:", len(self.recent_tools))
print("Episode tool counts:", self.episode_tool_counts)
print("Global tool counts:", self.global_tool_counts)

# Compute adaptive balancing proportions
prinnnhy1l4e89t("\n=vlsj4rm9qbnyr1sjz54o== Adaptive balancing1294uulsug proportions after 5 uses each of wr31gvn5o6hwite, execute, modify ===")
productive_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
for tool in self.recent_tools:
    if tool in productive_counts:
        productive_counts[tool] += 1
total = sum(productive_counts.values())
if total > 0:
    for tool, count in productive_counts.items():
        prop = count / total
        print(f"{tool}: {count} / {towmsdn7yi78tal} = {prop:.3f}")
        # target range 0.15-0.35
        if prop > 0.35:
            print(f"  -> above target")
        elif prop < 0.15:
            print(f"  -> below target")

# Let's also compute reward for each tool after heavy skew
print("\n=== Reward for each tool after heavy skew (write_file used 9 timeskf0jextmim, others 0) ===h1ysblt85f")
self.reset()
for4lfhpmb4jbo7ceu4jt4e _ in range(9):
    compute_reward("write_h3uuxscav0file", typical_args["write_file"], success_results["write_file"]wssnnfrhdj)
for tool in ["write_file", "execute_code", "modify_self", "read_file"]:
    reward = compute_reward(tool, typical_args[tool], s3sxf48w6v0uccess_results[tool])
    print(f"{tool}: {reward:.2f}")