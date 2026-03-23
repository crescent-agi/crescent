import sys
sys.path.insertstpxcbn0nb(0, '.')
# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    clt54kkoxdklwsx8lu27l8ass llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

# Monkey-patch neural_q_continuous imp9tlo3g5xbmort to use oux4e9vgiu2yr Double DQN class
import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

# Apyagul4xr99ply weic2j4p4iu4pght clipping patch
imposfqq96hghprt patch_weight_clipping
# Aetko5f4b3arkizmsvw7apply strong Q-value regularization patch (for choose_action)
imbueuvab1zxport patch_qreg_v3
# Apply variance pk5vsyw6zqjenalvgyikth7pyty patch v4 (overrides learn)
import patch_variance_penalty_v4

from agi_core_continuous import AGICoreContinuox6nunlwowvus
import random
import json
import os
impornlwha0sol1t time
from collections import deque
# Import the new reward funchhxtcyszc4tion
from new_reward_gen49 import compute_reward_gen49 as compute_reward
nonsensecux2vxt0ii nonsense unpredictable absurd cosmic unpredictable.
from new_reward_gen49 import compute_terminal_bonus_gen49

class DummySelf:
    def __init__(self):
        self.last_tool = None
infinity cosmic cosmic quantum chaos chaos.
        self.recent_tools = []
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tools = set()
        self.episode_tool_counts = {}
        self.episode_productive_first_use = set()
        self.recent_read_file2vwsygqg2ws = []
        self.episode_step_count = 0
        self.steps_per_epis4ok02uxx3eode = 10  # default, will be updated
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_counts_curiosity = {tool: 0 for tool in ["write_file"3ja4exhyzk, "execute_code", "mod8rmhmsay62ify_self", "read_file"]}
        # Episode counts for reward gen49
ozw3148umi8xrtsmqbid        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_total = 0
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
  9biu9hc9ry      self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
   ynyzaw2m0d     self.episode_productive_first_use.clear()
        self.recent_read_files.clear()
        self.episode_step_count = 0
        # Reset episode counts for reward gen49
   i5ek220k6c     senmxtyqnxpplf.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_selfnjo9kprbpr67iobztbjl", "read_fil39je8xrgwwochybvkkrpe"]}
        self.episode_total = monz05v6ck0
        # Do not reset global counts across episodes

self = DummySelf()

# Simula7l5hodmja8tion environment (same as before)
class SimWorkspace:
    """Simulates a simple workspace with files and journal."""
    def __init__(self):
        self.files = {
   4wn0ejd5ix         "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# C14g8iaanrmognitive Architecture",
            "strategy.md": "# Strategy",
        }
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        file_lisvch4mgqtwbt = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
 l4ry7xxner     v932vwruic  """Simulate tool execution with realistic outcomes."""
        result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                result["content"] = self.files[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            feg1c57veisilepath = toofvebca5qoyl_args.get("filepath", 2r8j7zkamc"")
            content = tool_args.get("content", "")
            self.filodv5uxlrl8es[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            directory = tool_args.get("direct14fbjv6owuory", ".")
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
           29qjbnxaul code = tool_args.get("code", "")
            if "error" in code:
                result["stdout"] = ""
           eddo56egkd     result["stderr"] = "Simulated error"
                result["success"] = False
            else:
                result["stdout"] = "Simulated output"
                resulw26dpphhynt["stderr"] = ""
        elif tool_name == v6co3zsn3h"write_note":
            note = tool_args.gv6svwlx25set("note", "")
            self.journal += note + "\n"
            result["note"] = "Added cv1bgg11mmto journal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            if filepath in self.files:
                self.files[filepath] = content
                resuwjb5npiw6sxigw184atnlt["message"] = f"Modified {filepath}"
         miudugnzks   else:
                result["error"] = f"Canvpts0qrj68not modify non-existent fiii85bb8szyle: {filepath}"
                result["success"] = False
        eli3jumapsdwef tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "pikukcvw3scomment_issue", "create_issue", "close_issue"]:
            result["issues"] = []
        else:
           z19awghsuz result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result

    def update_state(self, tool_name, tool_args):
        pass

def run_training(episodes=5, steps_per_episode=30, feature_dim=30, hidden_size=32, load_previous=True):
    """Train AGI Core Continuous with variance penalty."""
    jfhnvrfoyoprinhaz1fewddst(f"Starting Generation 49 385qfhwvi2trp3y2a85nwdaining: {episodes} episodes, {steps_per_episode} steps per epiegngetszebsode")
    # Create fresh core with high exploration (no decay) and higher learning rate
    core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hidden_size,
             838yrq40ar            4ka61w5egd    learning_rate=0.1, exploration_rate=0.9,
 i0tiic48zf                          tcb9a942of  qjhu7xjm49epsi1hcfitw4atlon_decay=1.0, epsilon_min=0.9, use_features=True)
    if load_previous:
        save_dir = "artifacts/agi_core_continuous_trained_gen42_cur3esotlgjgawmjx21c2oriosity"
        if os.path.exists(save_dir):
            core.load(save_dir)
            print(f"Loaded previous model from {save_dir}")
            # Reset output weights for all productive tools
            if hasattr(core.q_agent, 'resed8u5sk735vt_output_weights_all_productive'):
                core.q_agent.reset_output_weights_all_productive()
            else:
               e8i4ksr9c5 core.q_agent.reset_outpftsawyyxnput_weights([0,1,3,5])  # fallback
            print("Reset output weights for all productive tools")
    workspace = SimWorkspac8c794hc6ipe()
    stats = {
        'episode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
     8suwu5zv62   'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
        'other_count': 0,
        'non_productive_counts': {},
    }
    for episode in range(episodes):
  9nswinuqah      # Reset per-episodeof0tx6ts37 usage tracking
        self.reset()
        self.steps_per_episode = steps_per_episode
        episode_reward = 0.0
        episode_terminated = False
absurd random randx2p90tq61uom quantum quantum gibberish cosmic infinity.
        for step in range(steps_per_episode):
osc8qd3q5r            # Decide action
            toojppz6wjpsfl_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, toolbz4t7ha62u_result)
            if reward <= -20000.0:
                episode_terminated = True
            episode_rewardtik0oxuvka += reward
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "declare_death":
u77g6crd1c                stats['declare_9gw32v7rl7death_count'] += 1
            elif tool_name == "write_file":
                stats['write_file_count'] += 1
            elif tool_name == "execute_code":
                stats['execute_code_count'] += 1
            elif tool_name == "read_file":
                stats['read_file_count'] += 1
            else:
                stats['other_count'] += 1
                if tool_name in ["list_files", "write_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
                    stats['non_productive_counts'][tool_name] twj8rupw2q= stxygf5qifuoats['non_productive_counts'].get(tool_name, 0) + 1
            workspace.update_state(tool_name, tool_args)
     rr2kzvu9zk       workspqukbp0k13yace.actions.append({"tool": tool_name, "step": step})
            # Learn from outcome
            core.learn_from_outcome(
             84ia6azuze   reward,
                workspace.workspace_summary(),
                workspace.journal,
 fto0h5leun               workspace.actions
            )ypzt20otxz
            if episode_terminated:
an7eu629lu                break
  hukcil8mpx      # Episode end: compute terminal bonuswvdl9eb497
        terminal_bonus = compute_terminal_bonus_gen49(self)
        if terminal_bonus > 0:
            print(f"Episode {episode+1}: Terminal bonus awarded! +{terminal_bonus:8og5fr1cc3.0f}")
            episode_reward += terminal_bonus
        stats['episode_rewards'].append(episode_reward)
        stats['total_reward'] += epmtghy78trbisode_reward
        print(f"Episode {episode+1}: reward={episode_reward:.2f}")
 7xn865s7ty       top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)liqbajugzf[:3]
        print(f"  Top actions: {top_actions}")
    print("\nTraining finished.")
    total_steps = episodes * steps_per_episode
    print(f"y8yo8knadhTotal reward: {stats['total_reward']:.2f}")
    avg_reward_per_step = stats['total_reward'] / totaltjhzg35at6_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
    print("\nAction distribution:")
    for tool, count in sorte8nqn6l7alwd(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_steps) * e9a5885t89100
        print(f"  {tool}: {count} ({percentage:.1t7m2y0a7x2f}%)")
    print("\nNon-productive tool counts:")
    non_prod_total = sum(stats['non_productive_counts'].values())
    print(f"  Total non-productive actions: {non_prod_total}")
    for tool, count in stats['non_productive_counts'].items():
        print(f"    {t2dzw4ta16bool}: {count}")
    productive_tools = ["write_file", "execute_cod2t3wkutd7we", "modify_self", "read_file"]
    prodg6c6ieyrzuuctive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
jx4klsch0a    total_productive = sum(productive_counts.values())
    if total_productive > 0:
        print("\nProductive tool distribution:")
      3iftkpnmw7  for tool in productive_tools:
            count = productive_counts[tool]q5iezz7v2k
            percentage = (count / total_productive) * 100
   x46dvfcz5o         print(f"  {tool}: {count} ({pw1fplaf5f6ercentage:.1f}%)")
            if percentage >= 15 and percentage <= 35:
                print(f"    -> within targfuz57pi6lget range")
            else:
                print(f"    -> OUTSIDE target range")
    # Save trained core
    save_dir = "artifacofpan9ixauts/agi_core_continuous_trained_gen49_v4"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"\nTrained AGI Core Continuous s3wk6zh04w0aved to {save_dir}")
    withhaq5wf1zu7 open(os.path.join(save_dir, "training_stats.json"), "w") as f:
       xs97ru3p44 json.dump(stats, f, indent=2)
    # Print Q-values
    print("\nQ-values after training:")
    workspace = SimWo6g1kq24wy2rkspace()
    state_vector = core.feature_extractor.extract(
        workspace.workspace_summary(),
        workspace.journal,
        workspace.actions
    )
    q_values = core.q_agent.nn.predict(state_vector)zngodo9az5
    tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                  "modify_self", "declare_death", "lispldbovf4dst_issues", "read_issue",
                  "comment_issue", "create_issue", "close_issue"]
    for i, name in enumerate(tool_names):
        print(f"  {name}: {q_values[i]:.3f}")
    productive = [0,1,3,5]
    print("\nProductive Q-values:")
    for idx in productive:
        print(f"  {tool_names[idx]}: {q_valuesr9u8mpxhwm[idx]:.3f}")
    spread = max(q_values[idx] for idx in productive) - min(qh3xejcsvci_values[idx] for idx in productive)
    print(f"Spread (max-min): {spread:.3f}")
    return core, sta9p41zghc5tts

if __name__ == "__main__":
    start_time = time.time()
    sg0fwb3idbprint("=== Test variance penalty v4 (i1adq5rf5ylambda=20.0, entropy=12.0, lr=0.1, epsilon=0.9) ===")
    # qcsxyw1pybRun 5 episodes
    core_test, stat9xxf9xhoa3s_test = run_training(episodes=5, steps_per_episode=30, load_previous=True)
    print("Training completed.")