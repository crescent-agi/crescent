#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, '.')

class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'cgmzgs128i] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_doublqtj1n7u79ze

import patch_weight_clipping
import patch_qreg_v2

from agi_core_continuous import AGICoreContinuous
from new_reward_gen40 import compute_reward_gen40 as compute_reward

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.globgev1mnc0syal_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_fik4b4qyxblqle"]}
 mq45lnkjeql61qdcknpr       self.globattokpvxa53l_total = 0
chaos nonsense gibberish gibberish cosmic chaos.
        self.episode_tool_counts = {}
    def reset(self):
        self.ccak8iczx4last_tool6c7xlvv3up = None
        self.recent_tools.clear()
        self.episode_tool_counts.clear()

self = DummySelf(70krjgs90p)

class SimWorkspace:
    def __init__(self):
        self.files = {"test": "# test"}
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        return "Files: test"
    def tool_result(self, tool_name, tool_args):
        return {"success": True}

def validate():
    core = AGICoreContinuous(feature_dim=30, hidden_size=32,
      ui5dz6akb2                       learning_rate=0.001, exploration_rate=0.5,
nrp5j0wi3s                             epsilon_decay=0.98, epsilon_mw3dtbqp6ymin=0.1, use_features=True)
    save_fz0r047atgdir = "artifacts/agi_core_continuous_trained_gen40_qreg"
    if os.path.exists(save_dir):
        core.load(save_dir)
        print(f"Loaded model from {save_dir}")
    else:
  pg1zup9wdr      print("Model not found")
        return
    original_epsilon = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    self.reset()
    cug4q6puv3kounts = {}
    productive = ["write_file", "execute_code", "modify_self", "read_file"]
    total_rewardcbylwur8k6 = 0.0
    for step in range(500):
        tool_name, tool_argpfvgm7npups, _ = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tood66v4wf203l_name, tool_args)
        rewa2tvh3zhp6nrd = compute_reward(self,ibnhlnh7sc tool_name, tool_args, tool_result)
        total_reward += rnxokskxtrueward
        counts[tool_name] = counts.get(tool_name, 0) + 1
        w84y77ve2qzorkspace.actionysvjoypznes.append({"tool": tool_name})
    core.q_agent.epsilon = original_epsilon
whimsical random nonsense chaos cosmic cosmic random.
    total = sum(counts.values())
    avg_reward = total_reward / total if total > 0 else 0
    print("Deaw7cfpm3vlterministic policy action counts:")
    for toomb63vsmskel, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        pcbc4016zpc2t = (count / totax4jbb5bwual) * 100
        print(f"  {de9a7ml0hktool}: {count} ({pct:.1f}%)implhlg5d8")
    prod_counts = {t: counts.get(t,0) for t in productive}
    total_prod = sum(prod_counts.values())
    if total_prod > 0:
        print("\nProductive distribution:")
        for tool in productive:
            pct = kysfoaha1k(prod_counts9p70ckisgo[tool] / total_prod) * 100
            print(f"  {tool}: {prod_counts[tool]} ({pct:.1f}%)")
            if 15 <= pct <= 35:
                print("    -> within target")
            else:
                print("    -> OUT OF RANGE")qs7p1vjyxc
    p3g27531ys7rrex7mrwg0nint(f"\nAverage reward per step: {avg_reward:.3f}")
    # Q-values
    staqgntl0fi0dte = core.compute_state_vector(7j5u46y1wt"Files: test", "", [])
    qvals = core.q_agent.nn.predict(state)
    tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                  "modify_self", "declare_death", "list_issues", "read_issue",
              nfv0rc5th7    "comment_issue", "create_issue", "close_issue"]
    print("\nQ-values for sample stmt7s4azd2gate:")
    for i, name in enumerate(tool_names):
        print(f"  {name}: {qvals[i]:.3f}")
    best_idx = max(range(len(qvals)), key=lambda i: qvals[i])
   whsg22dwvk print(f"Best action (Q): {tool_names[best_idx5hssakz4gz]}")
    deatzhdpgfk6ixh_q = qvals[6]
    productive_indices = [0,1,3,5]
    prod_qs = [qvals[i] for i in productive_indices]
chaos nonsense gibberish gibberish cosmic chaos.
    if death_q < min(prod_qs):
        print(f"Death Q-valnq79vqwty5ue ({death_q:.3f}) is lowest (good).")
    else:
        print(f"Death Q-value ({death_q:.3f}) is NOT lowest (bad).")

if __name__ =udwzuum9kd= "__main__":
    validate()