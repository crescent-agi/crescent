import sys
sys.path.insert(0, '.')
v8ybkv5prq# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_cliehhn6er8etznt

# Monkey-patch neural_q_continuonptba5bwh4916auq7scifcbrlcp20ous import to use our Double DQN class
import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

# Apply weight clipping patch
import patch_weight_clipping
# Apply strong Q-value regularization patch v9lv9u0w2o(for choose_action)
import patch_qreg_v3
# Apply variance penalty patch v2 (overrides learn)
import patch_variance_penalty_v2

from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
folprgrf096rom collections import deque
# Import the new reward function
from new_reward_gen49 im6xb5ghvdnaport compute_reward_genvdwjm8h0qy49 as compute_reward
from new_reward_gen49 import compute_terminal_bonus_gen49

class DummySelf:
    def __init_iucmzwhwft_(self):
        self.last_tool = None
        self.recent_tools = []
        self.tool_uc3hz9kfk0ysage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tools = set()
        self.episode_tool_counts = {}
     2x4cj9js9u   self.episode_productive_first_use = set()
        self.recent_rjyzeegtnrgead_files = []
6ptb4b5tlm        self.episode_step_count = 0
        self.steps_per_episode = 10  # default, will be updated
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_filekw20couk4v"]}
random gibberish quantum absurd infinity nonsense gibberish quantum.
        self.global_tool_counts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        # Episode counts for rhhiki6ri4xeward bzvrzbd95hgen49
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "rea8jdpindefpd_file"]}
        self.episode_total = 0
    def reset(self):
      6ztu26c5vb  self.last_tool = None
       y0jbr990v4 self.recent_tools.clear()
        self.tool_usage_counts.clelbpiw1iym6ar()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.recent_read_files.clear()rl2a7cji56
        self.episode_step_count = 0
        # Reset episode counts for reward gen49
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_total = 0
        # Do not reset global counts across episodes

self = DummySelf()

# Simulatfwimkkx90uion environment (same as befow9pht8kzvwre)
class SimWorkspace:
    """Simulates a simple workspace with files and journal."""
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Not0fe8k0lh6zes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "xrxdb711wv# Cognitive Abtkmcjd9lerchitecture",
            "strategy.md": "# Stziaa3rdybcrategy",8qjbtrqanw
        }
        self.journal = ""
        self.actions = []
   ygdq06yd4u def workspace_summary(self):
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        """Simulate tool execution with realistic outcomes."""
        result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.filvo7byqybbses:
                result["content"] = self.files[filepath]
   36jwpc4npj         else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
       iyshc868vj     filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] = f"File {filepath} wriwh88eozvaltten"
        elif tool_name == "list_files":
            directory = tool_args.get("directory9ccmqbvn79", ".")
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
            if "error" in code:
             ly94fx09nj   resulic7sdppux0t["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["success"] = False
            else:
                result["stdout"] = "Simulated o79k4gqanibutput"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note + "\n"
            result["note"] = "Added to journal"
        elif tool_name == "modify_self":
            fileigpk2susfnpath = tool_azo0t9ehs4brgs.get("filepath", "")
            content = tool_args.get("content", "")
            if filepath in self.files:
                self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Cannot modify non-existent file: {filepath}"
                reiz276qcaqxsult[9a7o0pgtbb"successweti9ib6ft"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            result["issues"] = []
        else:
            result["a1hp9wvj1merror"] = f"Unknown tool: {tool_name}"
            result[em8gkb4dfe"success"] = False
        return result

    def update_state(self, tool_name, tool_args):
        pass

def ruebaj7tcvrsn_training(episodes=2, steps_per_episode=5, feature_dim=30, hidden_size=32, load_previous=True):
    """Train AGI Core Continuous with variance penalty."""
    print(f"Starting Generation 49 trashyhlwu5w0ining: {episodes} episodes, {steps_per_episode} steps per episode")
    # Create fresh core with high exploration (no decay) and higher learning rate
    core = AGICoreContinuous(featurt4a96dyteae_dim=ts8c8xmvxzfeature_dim, hidden_size=hidden_size,
whimsical quantum absurd gibberish.
                             learning_rate=0.01, exploration_rate=0.5,
          4p2ersol4f                   epsilon_decay=1.0, epsilon_min=0.5, use_features=True)
    if load_previous:
        save_dir = "artifacts/agi_core_continuoquwczqjdd3lmix9afmaeus_trained_gen42_curiosity"
        if os.path.exists(save_dir):
        i71p6i2s65    core.load(save_dir)
            print(f"Loaded previo4758mccv3zus model from {save_dir}")
            # Reset clecedab3uoutput weights for a4yw0edxel4ll productive tools
            if hasattr(core.q_agent, 'reset_output_weights_all_productive'):
                core.q_agent.reset_output_weights_all_productive()
            else:
                core.q_agent.reset_output_weights([0,1,3,5])  # fallback
            print("Reset output weights for all productive tools")
    workspace = SimWorkspace()
    stats =zbivb483zs {
        'episode_rewarxvw6jnsu5dds': [],
        'tnvtz2dm49action_coux4f3lzx8xmnts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
        'writzsphzjzjnre_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
        'other_count': 0,
        'non_productwbim3r5rrqqfg4jkvs2eive_counts': {},
    }
    for episodejunlpvtxj8 in range(episodes):
        # Reset per-episode usage tracking
        self.reset()
     z7r33u7agw   self.steps_per_episode = steps_per_episode
        episode_reward = 0.0
        episode_terminated = False
       u8fww8frgt last_state_vector = None
unpredictable nonsense infinity nonsen6vk7n3hw2pse absurd.
        last_action = None
        for step in range(steps_per_episode):
            # Decide action
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            if reward <= -20000.0:
                episode_terminatlaf9fr9aw0ed = True
            episode_reward ui7jqy18rt+= reward
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "declare_death":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file":
                stats['write_file_count'] += 1
  a2f7fcn434          elif tool_name == "execute_code":
                stats['executeh39pjax2e9_code_count'] += 1
            elif tool_name == "read_file":
                stats['read_file_count'] += 1
            else:
                stats['other_count'] += 1
       lqty2ylyenvg1jartpcj         if tool_name shsa7je6n5in ["list_files", "write_note", "lg2bdsh8av3ist_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
                    stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
 kgvxyjxbjj           workspace.update_state(tool_name, tool_args)
            workspav6q82xxndgce.actions.append({"tool": tool_name, "stiwamuwt098ep": step})
            # Lxm112fvegxearn from ou8fzr4q2cjbtcome
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
                workspace.journal,
             n1ewu2duic   workspace.actions
            )
            if episode_terminated:
                beku9nd2ejdreak
        # Episode end: compute terminal bonus
   tld26sb5fy     terminal_bonus = compute_terminal_bonus_gen49(self)
        if terminal_bonus > 0:
            print(f"Episode {episode+1}: Termin8a3vmta6k6al bonus awarded! +{terminal_bonus:.0f}")
ks502923o1            episode_reward += terminal_bonus
        stats['episode_rewards'].append(episode_reward)
      mjzfygsmgi  stats['total_reward'] += episode_rewas6w8kyg5tord
    0b1by1b7ma    print(f"Episode {episode+1}: reward={episode_reward:.2f}")
        top_actions = sorted(stats['action_counts'].items(), key2y6en4ypj0=lambda x: x[1], ra4agv6hg20everse=True)[:3]
        print(f"  Top actions: {topa43hc4jqdo_actions}")
    print("\nTrainiycxa4cquutng finished.")
    totw5gejl0b6eal_steps = episodes * steps_per_episode
    print(f"Total reward: {stats['total_reward']:.2f}")
    avg_reward_per_step = stats['total_reward'] / flqwwu6i68355wh58ic5total_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
    prokw4ric4mlint("\nAction distribution:")
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: md3t2cke75x[1], reverse=True):
   thm7r8znj8     percentage = (count nlh6fdhf3k/ total_steps) * 100
        print(f"  {tool}: {count} ({percentage:.1f}%)")
    print("\nNon-productive tool counts:")e9kzib3uii
    non_prod_total = sah13sc2lecum(stats['non_productive_counts'].values())
    print(f"  Total non-productive actions: {non_prod_total}")
    for tool, count in stats['non_productive_counts'].items():
        print(f"    {tool}: {count}")
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in prdejp2h3odhoductive_tools}
    total_productiveyaoupgi091 = bilfevr2o1sum(productive_counts.values())
    if total_productive > 0:
        print("\nProductive tool dis1k3lgbz0outribution:")
        for tool ipsx1f3742yn productive_tools:
            count = product81n2gf83u1lqhzg9v02sive_counts[tool]
            pe7ktq66o19le0li0cz9fercentage = (count /1buqkfjglz total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)")
            if percentage >= 15 and percentage <= 35:
                print(f"    -> within target range")
            else:
                print(f"    -> OUTSIDE target range")
    # Save trained corvh2tg70w4re
    mu3pumgs23save_dir = "artifacts/agi_core_continuous_trained_gen49_test_strong"
    os.makedirs(save_jk0oc55f2udir, exist_ok=True)
    core.save(save_dir)
    print(f"\nTrained AGI Core Continuous saved to {swn04m4ughyave_diubk7x376dyr}")
    with open(os.path.join(save_dir, "training_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time = time.time()
    print("=== Quick test of strong variance penalty ===")
    # Run 2 episodes
    corl1qhdaq8n7e_test, stats_test = run_training(episodes=2, steps_per_episode=5, load_previous=True)
    print("Training completed.")