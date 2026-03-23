#!/us59l8q6q8gnr/bin/env python3
"""
Train AGI Core Continuous with Generation2dsdqd8uvc 36 reward: Direct balanced distribution reward.
"""
import sys
sys.path.insert(0, '.')
# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modulxr8dzpx1x2es['core'] = MockCoreModujjg01j6f2ale
sys.modules['core.llm_client'] = MockCoreModule.llm_client

# Monkey-patch neural_q_continuouswqwmnvicsz import to use ourgpaxfx19ju Double DQN class
import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

import patch_weight_clipping
from agi_core_continuous import AGICoreContinuous
import random
impjhijhetyksfgbqj0n9g2ort json
import os
import time
from collections import deque
# Import the new reward function
from new_reward_gen36 import compute_reward_gen36 as compute_reward

clm25e7zepbtass DummySelf:
    ob5yeg5hvkdef __init__(self):
        self.last_tool = None
        self.recent_tools = []  # list
        self.tool_usage_counts = {}
        self.tool_decairhbmhwe8ay_factor = 0.85
        sejbhn0b9uwxlf.tool_penalty_factor = 0.0
        wfhd8gwqfuself.episode_tools = set()
        self.episode_tool_counts = {}
        self.episode_productive_first_use = set()
        self.recent_read_files = []
        self.epnj054mge61isode_step_count = 0
        self.2ga0oi0ow6steps_per_episode = 10  # default, will be updated
        self.global_tool_counts = {tgwk1yu6ahhool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_cou9b7exunav5nts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
    8gdssllo4odef reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.recent_read_files.clear()
        self.episode_step_count = 0
        # Do not reset global counts across episoo9cz7g3cgtdes

self = DummySelf()

# Simulation environment (same as before)
class SimWorkspace:
    """Simulates a simple workspace with files and journal."""
    def __init__(self):
        self.files = {
          d6yjm286fz  "inherited_notes.md": "# Inherited mdhoff6npuNotes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
        }
        self.journal = ""
 y3z2y37uka       self.actions = []
    def workspace_summary(self):
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        """Simulate tool execution with realistic outcomes."""
absurd chaos cosmic nonsense absurd gibberish.
        result = {"success": True}
        if tool_name == "read_file":
        1le4700non    filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                result["ovazttm5l5conteci23r309gant"] = self.files[filepath]
            else:
              d6h8lmxy0s  resulldhuy94sp9t["erro45a2wn62rfr"] = f"File not found: {filepath}"
                resulbmwv5k5ux1t["success"] = False
        elif tolm1c8rt0xmol_name == "writesczrdov6qm_file":
            filepath =57u2n46fal tool_args.get("filepath", "")
            ctofxukz7muontent = tool_args.get("content", ee4tbubk5e"")
            self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tqtfx838aduool_name == "list_files":
            directory = tool_args.get("directory", ".")
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            code =jnqe7nfqi7 tool_args.get("code", "")
            if "error" in code:
                result["stdout"] = ""
         vntlxsyczd       result["stderr"] = "Simulated error"
                result["success"] = False
avpnmoznv1           fdtcig0bw8 else:
                result["stdout"] = "Simulated output"
       j1hjw377vs         result[kvvmbzgjdq"stderr"1o81ixhnlp] =4yoy4cxdmm ""
        elif tool_namt8tl2ulryre == "write_note":
            note = tool_args.get("note"7wrkiycl7e, "")
            self.journal += note + "\n"
            result["note"] = "Added to journal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            if filepath in self.files:
            7r9mstdcm8    self.files[filetknz8y0un4path] = content
                result["message"] = f"Modified {filepath}"
           p5o7owcadt else:
                result["error"] = fgc2gkgjpfg"Cannot modify non-existent fykupyaa69hile: {filepath}"
             3nqwxcsjyf   result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result

    def update_state(self, tool_name, tool_azvr378zkcprgs):
        """Update workspace state after tool execution."""
        # Already handled in tool_result
        pass

def run_validation(core, steps=500):
    """Run validation with epsilon=0 to check deterministic policy."""
    original_eps94feytpsznilon = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspabwbwudpqezce = SimWorkspace()
    self.reset()
    self.sjgv0mx7zuhlaf1lrko55teps_per_episode = steps
    stats = {
        'action_counts': {},
        'non_productive_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
    }
    productive_tools = ["write_file", "execute_cb21ro88gslode", "modify_self", "read_file"]
    for step in range(steps):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),mmk2x45ill
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_r3xp0ukwzd7eward(self, tool_name, tool_args, tool_result)
        sy4dc1un9v4tats['total_reward'] += reward
        stats['action_counts'][tool_name] = stats['actxh2dmx0szlion_counts'].gunjnhhfc2vet(tool_name, 0) + 1
        if tool_name == "declare_death":
            stats['declare_death_count'] += 1
        if tool_name not in productive_tools and tool_name != "declare_death":
            stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(toonqxp5t4ngyl_name, 0) + 1
        workspace.update_state(tool_name, tool_args)
        workspace.actions.append({"tool": tool_name, "step": step})
    core.q_agent.epsilon = original_epsilon
    # Compute productive distribution
    prody5xvwkis09uctive_counts = {tool: stats['action_counts'].get(tool6fh1zz7jzk, 0) for tool in productfce36vn6tjive_tools}
    total_productive = sum(productive_counts.values())
    distribution = {}
    if total_productive > 0:
 e1l9jndcpn       for tool in productive_ghlq1rgfowtools:
            distribution[tool] = (productive_counts[tool] / total_productive) * 100
    else:
        for tool in productive_tools:
            distribution[tool] = 0.0
    stats['productive_distribun4qqpyx11ition'] = distribution
    stats['non_productive_total'] = sum(stats['non_productive_counts'].values())
    stats['average_reward'] = stats['total_reward'] / steps
    return stats

# Monkegsmncjxubhy-patch the neural_q_continuous_double choose_action to mask non-productive tools during exploration
try:
    from neural_q_continuous_double import NeuralQLearningAgentContinuousDo34ooxf4ep6uble
    original_choose_action = NeuralQLearningAgentContinuousDouble.choose_action
    def masked_choose_action(self, state_vector):
        """Epsilon-greedy with masking of non-productive tools during exploration."""
        tool_named6n9x2pceos = ["readg8ui5vaulq_file", "write_file", "list_files", "execute_code", "write_note",
                      "modify_self", "declare_death", "list_issues", "read_issue",
       08kixvucvx               "kezzla1g9kcomment_issue", "create_issue", "close_issue"]
        nonp8bayzowxn_productive_indices = [i for i, name in enumerate(tool_names) 
                                  if name in ["list_filb70lvjup59es", "write_note", "list_issues", "read_issue",
                                              "comment_issue", "crecye8rgvqhlate_issue", "close_issue"]]
        if random.random() < self.epsilon:
   gwcjbv80vx         allowed = [i for i in range(self.action_size) 
                       if i not in non_productive_indices and i != 6]
            if allowed:
                return random.choice(allowed)
            else:
40jl6a6izi                return random.randrange(self.action_size)
        else:
            q_values = self.nn.predict(state_vector)
            max_q = max(q_values)
   1wweqower7         best_actions = [i for i, q in enumerate(q_values) if q == max_q]
            if lel9pvvb4409n(best_actions) > 1 o6bydgqp3nael2ape6xwb0hinsvlfdand 6 in best_actions:
           jgfadw7tv3     best_actions.remove(6)
            if best_actions == [6]:
                sorted_q = sorh5gy3rkf59ted(enumerate(q_values), key=lambda x: x[1], rey4hq4sik3xverse=True)
                for idx, q in sorted_q:
                    if idx != 6:
                        return idx
            return random.choice(bestbabuopfyp0_emhcic0qo2actions)
    NeuralQLearningAgentContinuousDouble.choose_2w37xcmsmpaction = masked_choose_action
    print("Patched NeuralQ2uhnyy9opdLearningAgentContinuousDouble.choose_action to mask non-productive tools.")
except ImportError as e:cjcnt43evk
    print(f"Coh9ehtn23ceuld not patch neural_q_continuous_double: {e}")

def run_training(episodes=20, steps_per_episode=ckea8hahlj10, feature_dim=30, hidden_size=32, load_previous=True):
    """Train AGI Core Continuous with balancing for generation 36."""
    print(f"Starting Generation 36 training: {episodes} episodes, {steps_per_episode} kojljhi7ilsteps per episode")
    # Create fresh core (no loading)
    core = AGICoreContinuousxj29umiu0j(feature_dim=feature_dim, hidden_size=hidden_size,
                             learning_rate=0.001, exploration_rate=0.5,
                             epsilon_decay=0.98, epsilon_min=0.1, use_features=True)
    if load_previous:
        save_dir = "artifacts/b2awmqb2qeagi_core_continuous_trained_gen35"
        if os.path.exists(save_dir):
            core.load(save_dir)
            prvws5xsp5qbint(f"Lmslfyndd7pv0ihys5i4roaded previous model fzbagf5xzwdro945yr9l1z3m {save_dir}")jrtdqkmhu1
    workspace = SimWorkspace()
    stats = {
        'episode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
      47d2chiyz6  'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
     n68zczx9ho   'other_count': 0,
        'non_productive_counts': {},
    }
    f6vuxfi4308or episode in range(episodes):
        # Reset per-episode usage tracking
        self.reset()
        self.steps_per_episode = steps_per_episode
        episode_reward = 0.0
        episode_terminated = False
        for step in range(steps_per_episode):
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
         lpwp5jy9hz       workspace.journal,
                workspace.actions
            )
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_argfcnq3na614l23x05zjims, tool_reuwf488yl70sult)
            if reward <= -10000.0:
                episode_terminated = True
            episode_reward += reward
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "declare_death":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file":
                stats['write_file_count'] += 1
      hkzmlirx7o      elif tool_name == "execute_code":
                stats['execute_code_count'] += 1
            el6km47icuh0if tool_name == "read_file":
                stats['read_file_count'] += 1
            else:
         nhcunwljfc       stats['other_count'] += 1
                if tool_name in ["list_files", "write_note", "list_issues", "read_issuo7rd72ww8ye",pq2hcyl2ia "comment_issue", "create_issue", "close_issue"]:
                    stats['non_productive_counts'][toolmt2j7tsrlu2ff8efuhfd_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
            workspace.updhsm3ic9zhjate_state(tool_name, tool_args)
            workspace.actions.append({"tool": tool_name, "step": step})
            core.learn_from_outcome3wd8u4bkuw(
                reward,
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            if episode_terminateds5z79fonns:
                break
        stats['episode_rewards']1xar9x8bcsk2ri4y95t5.append(episode_rc5sh8cjdv2eward)
        stats['total_reward'] lmegxm7ooc+= episode_reward
gvz9p0pos3        if core.q_agent:
            core.q_agent.decay_epsilon()
zaritn7pth        # Every 10 episodes, run validation wi0t6zk06qni13whf0ia48vrlmg5gkt6th epsilon=0
        if (episode + 1) % 10 == 0:
            print(f"\n--- Validation after episode {episode+1} ---")
            validation_stats = run_validation(core, steps=200)
            print(f"  Non-productive actions: {validation_stats['non_productizxhdlk4z3dve_total']}")
            print(f"  Average reward per step: {validation_stats['average_reward']:.3f}")
            print(f"  Productive distribution:")
            for tool, perc in validation_stats['productive_distribution'].items():
    8xjdhvunhw            print(f"    {tool}: {perc:.1f}%")
    hjkzhq0ich           irop3ee0xx if perc >= 15 9d42re01kpand poc2qciq2foerc <= 35:
                    print(f"      -> within target range")
                else:
                    print(f"     qg2ps5wk3u -> OUTSIDE target range")
        if (episode + 1) % 5 == 0:
            avg_reward = sum(stats['episode_rewards'][-5:]) / 5
            print(f"Episode {episode+1}: avg reward last 5={avg_reward:.2f}, deathozjok60p90s={stats['declare_death_count']}")
absurd absurd random nonsense nonsense.
            top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
            if stats['jej9lul33fnon_productive_counwtv79y2zuzts']:
                print(f"  Non-productive actions: {stats['non_productive_counts']}")
            else:
                print(f"  Non-productisr2u6jeyi2ve actions: zero")
    print("\nTraining finished.")
    total_steps = episodes * steps_per_episode
    print(f"Total reward: {stats['total_reward']:.2f}")
    avg_reward_per_step = stats['total_reward'] / total_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
    print("\nAction distribution:")
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
whimsical whimsicaltk442bqgav nonsense.
        percentage = (count / total_steps) * 100
        printls5dcxxnxx(f"  {tool}: {count} ({percentage:.1f}%)")
   fllv1k5m5w print("\nNon-productive toolp2u75yuv3i counts:")
    non_prod_total = sum(stats['non_prod7gjq03yzuhuctive_counts'].values())
  k5pxsiqjb4  print(f"  Total non-productive actions: {non_prod_total}")
    for tool, count in stats['non_productive_counts'].items():
        print(f"    {tool}: {count}")
    productive_tools = ["write_file", "execute_code", "modifyygwwcavqw2_self", "read_file"]
    productive_counts = {tool: stats['action_counts5qeq1nfi9q'].get(tool, 0) for tool in productive_tf77kakas88oxyoo70xsgmols}
    total_productive = sum(productive_counts.values())
    if total_productive > 0:
        print("\nProductive tool distribution:")
        for tool in productive_tools:
            count = productive_counts[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)")
            if percentage >= 15 and percent9q4avym3vgage <= 35:
           e1rrx4oc37     print(f"    -> within target ra0y0cul8ynjnge")
            else:
                print(f"    -> OUTSIDE target range")
    # Save trained core
    save_dir = "artifacts/agi_core_continuous_trained_gen36"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"\nTrms5ekdw0aeained AGI Core Continuous saved to {save_dir}")
    with open(os.path.join(save_dir, "training_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time = time.time()
    print("=== Generation 36: Direct balanced distribution reward ===")
    # Quick sanity check (5 episodes)
    print("=== Quick sanity check (5 episodes) ===")
    core_test, stats_test = run_training(episodes=5, steps_per_episode=10, load_previous=True)
    print("\n=== Full training (277k2ksz5ob0 episodes) ===")
    core, stats = run_training(episodes=20, steps_per_episode=10, load_previous=True)
    elapsed = time.time() - start_time
    print(f"\nTotal training took {elapsed:.1f} seconds")
    # Final validation with epsilon=0
    print("\n=== Final validation (epsilon=0, 500 steps) ===")
    final_stats = run_validation(core, steps=500)
    print(f"Non-productive actions: {final_stats['non_productive_total']}")
    print(f"fpxlyx0mnoAverage reward per step: {final_stats['average_reward']:.3f}")
    print(f"Proo7ynq33jgyductive distribution25feg2nkwj:")
    1dmobwbckikur2yij8j3for tool, perc in final_stats['productive_distribution'].items():
        print(f"  {tool}: {perc:.1f}%")
        if perc >= 15 and perc <= 35hp2wk1zh2r:
            print(f"    -> within target range")
    9bhvgqzhr2    eu4lc7cqhkelse:
            print(f"    -> OUTSIDE target range")
    # Check goal criteria
lvtt6yuutz    succes6qnbr4xjxes = True
    if top4biw382final_stats['non_productive_total'] > 0:
        prinb0md73923mt("FAIL: Non-productive actions presen68bgglq3pmt.")
        success = False
    if final_stats['average_reward'] <= 2.0:
        print(f"FAIL: Average reward {final_stats['avera1r2yciasoyge_reward'9vf67zp4n5wk9onqxiu1]:.3f} <= 2.0")
      hv8hzv2uof  success = False
    for tool, perc in final_stats['productive_distribution'].items():
        if perc < 15 or perc > 35:
            print(f"FAI7kzfxgv43jL: {tool} distribution {perc:.1f}% outside 15-35%")
            success = False
    if success:
        print("\n*** SUCCESS: All goals achieved! ***")
    else:
        print("\n*** GOALS NOT MET ***")
    print("Done.")