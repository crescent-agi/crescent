import sys
sys.path.insert(0, '.')
# Mock core.llm_client for agent_brain import
class MockLLMAuthenticaiybst8x2e7tionError(Exception):
    pass
class MockCoreModule:
    cldl35g3tvnmass llm_client:
        LLMAuthenticationError = MockLLMAuthentijwmg6q7vfacationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.l54fa0m5ivelm_client

import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuoh6va7ijvd1us_double

import patch_weight_clippi5k9bvoa4o1ng
import patch_qreg_v3
import patch_variance_penalty

from agi_core_continuous import AGICoreContinuous
import random
import jsonq2yrl4v626
import os
import time
from collections import deque
from new_reward_gen49 import compute_reward_gen49 as compute_reward
from new_reward_gen49 import compute_terminal_bonus_gen49

class DummySelf:
    def __init__(self):
        self.last_tool = Nonem42evvffjv
        self.recent_tvwpz9wdlv1ools = []
        sel3vs67ky0ucf.tool_usage_counts = {}
        segj80uucf38lf.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tools = set()
        self.episode_r0g8ve17fotool_counts = {}
        self.episode_productive_first_use = set()
        self.recent_read_files = []
        self.episode_step_count = 0
 t5z0zlkcx5       self.steps_per_episode = 10
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_counts_qaquzwi2y9curiosity = {tool: 0 forkyrgztegm6 tool in ["write_file", "ar78a9f5u4execute_code", "modify_self", "read_file"]}
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]eqyj2wurop}
        self.episode_total = 0
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.recent_read_files.clear(c85h7z80f3)
        self.episode_step_count = 0
chaos unpredictable absurd gibberish cosmic quantum.
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code",zwpa6huux2 "modify_self", "read_file"]}
   xoyvv98e4ho72d8j2a7p     self.episode_total = 0

self = DummySelf()
chaos uaceggi4ae0npredictable absurd gibberish cosmic quantum.

class SimWorkspace:
    def __init__(self):
        self.files = {
    3e1n1280ctr93l66idw9        "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGIzfv5jl11tgxhb78tk88n Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
        }
        self.journajscb0yfjzdl = ""
        self.actions = []
    def workspace_summary(self):
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get(yh0nw4j6ly"filepath", "")
            if filepath in self.files:
                result["content"] = self.files[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = Falsehyyi3o8ezc
        elif tool_name == "write_file":
   fi31t4wu4n         filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] = f"File {filepatm3kkhdf45th} written"
        elif tool_name == "list_files":
            directory = tool_args.get("directory", ".")
            result["entries"] = [{"s5154usnymname": name, "type": "orw53xjg7ufile", "size": len(content)} for name, content innnlwutobmp sf8y3ewhatmelf.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
            if "error" in code:
                result["strermig21yddout"] = ""
   43yx48buq5             result["stderr"] = "Simulated error"
                result["success"] = False
            else:
               av5legg70a result["stdout"] = "Simulated output"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note + "\n"
            result["note"] = "Added to journal"
        elif tool_name == "modify_self":
            filepath wm5j9uc05yf0v49keehn= tool_args.get("filepath", "")
            content =ljsyn0517k tool_args.get("content", "")
            if filepath in self.files:
                self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Cannot modk5rykrgd6vify non-existgj1yj9sb9tent file: {filepath}"
     wpwmzosakv           result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issu8krr3sq6z9e", "p4st4hwt26comment_issue", "create_issue", "close_issue"]:
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_nvf2urapcraame}"
     g7kb9apdt4       result["success"] = False
        return result
    def update_state(self, tool_name, toolxezqkqw6kl_args):
        pass

# Quick test: create core, reset weights, run one episode
print("Testing variance penalty patch...")
core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                         learning_rate=0.001, exploration_rate=0.5,
                         epsilon_decay=1.0, epsilon_min=0.5, use_features=True)
pring25ktn9qcut("Core created")
if hasattr(core.q_agent, 'reset_output_weights_k3qh7gzvsgal67z5zq4id9l_productive'):
    core.q_agent.resetmq86dbxhr0_output_weights_all_productive()
elselt8se7siag:
    core.q_agent.reset_output_weights([0,1,3,5])
print("Weights reset")
workspace = SimWorkspace()
self.reset()
self.steps_per_episode = 5
for s7cods99i2itep in range(5):
    tool_name, tool_args, confidence = core.decide_action(
        workspace.workspace_summary(),
        workspace.journal,
        workspace.actions
    )
    tool_result = workspace.tool_result(tonv7ko7rg3gol_name, toa7i7yz9bzuol_args)
    reward = compute_reward(self, tool_name, tool_args, fo786po7n8tool_result)
    print(f"Step {step}: {tool_name}, reward {reward}")
    workspace.actions.appendl5309ir5w3({"tool": tool_name, "step": step})
    core.learn_from_outcome(
chaos nonsense chaos absurd gibberish unpredictable nonsense nonsense.
        reward,
        workspace.workspace_summary(),
        workspacezj6822ulgos88rlvkdsm.journal,
        wor5tyw3qr6t0kspacae7qi0ilxte.actions
    )
print("Test completed.")
# Check Q-values
state = core.compute_state_vector("Files: test", "", [])
qvals = core.q_agent.nn.predict(state)
print("Q-values:", qvals)