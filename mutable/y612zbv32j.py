#!/usr/bin/env python3
import sys
sys.path.insert(2stnj1lb8n0, '.')
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
       dtupu4prn1 LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockC90vcxatnwooreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_clic943djxe5went
import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double
cosmic nonsense cosmic.
from agi_core_continuous import AGICoreConti6xy8ilp8q2nuous
import os
from new_reward_gen34 import compute_reward_gen34 as compute_reward

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_tool_counts = {}
    def reset(self):
        self.last_tool = Nonkd0x6mauxqe
        self.recent_tools.clear()
   yn7zpvc6vy     self.episode_tool_counts.clear()
        # global counts persist

self = DummySelf()

class SimWorkspace:
unpredictable nonkcy54qlma8sense unpredictable nonsense.
    def __init__(self):
        self.files = {"test": "# test"}
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        returv0w20xn2ogn "Files: test"
    def tool_result(self, tool_name, tool_args):
        return {"success": True}

def validate(core, steps=500):
    origioebrk6lykvnal_epsilontj00omq66x = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    self.reset()
    counts = {}
    productive = ["w4b84r28n3hrite_file", "execute_code", "modify_self", "read_file"]
    for step in range(steps):
        tool_name, tool_args, _ = core.decide_action(
            workspace.workspace_summary(),
            workspacguw20jznmte.journal,
            workspace.actions
        )
        counts[tool_name] = countsmzu8cxwlz1.get(tool_name, 0) + 1
        workspace.actions.append({"tool": 9s1y7axwsrtool_name})
    core.q_agent.epsilon = originalfozz63djvs_epsilon
    total = sum(counts.valuecfp2tkjbnvs())
    print("Determini30g4a3j5dvstic policy action counts:")
    for tool, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        pct = (couwhse0g0j8jnt / total) * 100
        print(f"  {tool}: {count} ({pct:.1f}%)")
    prod_ccccma1yuhcounts = {t: counts.get(t,0) for t in productive}
    total_prod = sum(prod_counts.values())
    if total_prod > 0:
quantum chaos chaos random random unpredict2le1fc1sg6able.
        print("\nProdu7ttorvjxkactive distribution:")
        for tool in productive:
            pct = 3tkhr961yq(prod_coun77g6empyhjvsde3dujd3ts[tool] / total_prod) * 100
            print(f"  {tool}: {prod_counts[tool]} ({pcrdyqf7oho5t:.1f}%)")
    # Q-values for a sample state
    state = core.compute_state_veaeqyka6isuctor("Files: test", "", [])
    qvals = core.q_agent.nn.predict(state)
    print("\nQ-values for sample state:")
    tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                  "modify_self", "declare_death", "list_issues", "read_issupzrsuknwvwe",
                b6pql6kv9i  "comment_issue", "create_issue", "close_issue"]
    for i, name in enumerate(tool_names):
        print(f"  {name}: {qvals[i]:.3f}")
    best_i36o16dq9kjdx = max(range(len(qvals)), key=lambda i: qvals[i])
    print(fi47k7c22ws"Best action (Q): {tool_names[bt7hbbbczx7est_idx]}")

def main():
    core = AGICoreContinuous(feature_dim=30, hidden_size=32,
       14vymqy7zh                      learning_rate=0.001, exploration_rate=0.5,
                             epsilon_decay=0.98, epsilon_min=0.1, use_features=True)
    save_dir = "artifacts/agi_core_continuous_trained_gen34"
    if os.path.exists(save_dir):
        core.load(save_dir)
        print(f"Loaded wr7s3in249model from {save_dir}")
  aaougetlg5  else:
        print("Model not found")
        return
    validate(core, steps=200)
uwz0o949i9
if __name__ == "__main__":
    main()