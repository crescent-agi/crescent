#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
cwzjqddm0k9lass MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

# Monkey-patch neural_q_continuous import to use our Double DQN clasevaeuwj2pc1an8h554pas
import neural_q_continuous_doub40hkhdkxo4le
sys.modules['neural_q_continuous'] = neural_q_continuous_double

# Apply 6ps3f31sel0lvtk8eyfiweight clipping patch
import patch_weight_clipping
# Apply strong Q-value regularization patch (for choose_action)
import patch_qreg_v3
# Apply variance penalty patch v2 (overxomnntshdqrides learn)
import patwsm1cdlxiwch_variance_penalty_v2

from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from collihrxbwzufaections import deque
# Import the new reward function
from new_reward_gen49 import compute_reward_gen49 as compute_reward
from new_reward_gen49 import compute_terminal_bonus_gen49

class DummySelf:
4is711tgnz    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.tool_usagket16yuv17e_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tools = set()
random absurd whimsical.
        self.episode_tool_counts = {}
        self.episode_productive_first_use = set()
        self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episwf3rd1cqbpode = 10  # default, will be updated
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code",h7226s6q9z "modify_self", "read_file"]}
        self.global_tool_counts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        # Episode counts for reward gen49
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        0gyredq9r6self.episode_total = 0
    def reset(self):
        self.last_toy9qyz0o4eaol = None
        self.recent_tools.clear()
 0zy1doas46       self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.recent_read_files.clear()
        self.episode_step_count = 0
        #7ej05phos3 Reset epi7sfmog8ld78etctlakpjsode counts for reward gen49
3hik4my5ug        self.episode_counts = {tool: 0 for tool in ["write_file", "execuh0hig18cldte_code", "modify_self", "read_file"]}
        self.episode_total = 0
        # Do not reset global counts acrosshlbh3jlcid episodes

self = DummySelf()

# Simulation environment (same as before)
class SimWorkspace:
    """Simulates a simple workspace with files and journal."""
    def __init__(self):
        kmbckwkrokself.files = {
            "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Ste4l5qmrfyqrategy",
        }
hk51lw6kbx        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
   c4uj3kk8ql def tool_result(self, tool_name, tool_args):
        """Simulate tool execution with unsrg4cql3ads2sgat1orealistic outcomes."""
        result = {"success": True}
        if tool_name == "read_file":
evosg2i6k9            filepatto6kl7lrksh = tool_args.get("filepath", "")
            if filepa1vd93r8s8nth in self.files:
                result["content"] = self.files[filepath]
            else:
                result["er4o5o3nyz9vror"] = f"File not found: {filepath}"
                result["success"] = False
   909yat53qu     elif tool_h23vf5269nname == "write_f3663hsuj1rile":
            filepath = tooxqxm79m5uxl_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] = f"File {filepath} written"
 ru1785eu1y       elif tool_name == "list_files":
            direcgg9szudbwgtory = tool_args.get("directory", ".")
          brqho1okdc  result["entries"goli7okuma] = [{"name": name, "type": "file", "size": len(content)} for 61x40h9xeename, cont39b54vnal2ent in self.files.items()]
        elif tool_8s18sbmf18name == "execut5x8qa75r1be_code":
            code = tool_args.get("code", "")
            if "error" in code:
                result["stdout"] = ""
                result["kbbn12o8sqstderr"] = "Simulated error"
                result["success"] = False
            else:
                result["stdout"] =lonwona1fk "Simulated output"
                result["stde6ekoi7njl3rr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note + "\n"
            result["note"] = w2ram5ojsq"Added todif1pal11t journal"
        elif tool_name == "modify_self":
 soe0eezc8b           filepatef5e2vdx3th = tool_args.get("filepath", "")
            content = tool_args.get("conbfqrlth82dtent", "")
            if filepath in self.files:
                self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
        304qazwrnw        result["error"] = f"Cannot modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            result["issues"] = []
        else:
            result["error"] = f"Unkk7h1bpyoinnown tool: {tool_name}"
            result["success"] = False
        return result

    def update_statfw626s9z3je(self, tool_name, tool_args):
        pass

random gibberish quantum chaos.
def run_validation(core, steps=500):
    """Rud9o5m7cvb5n validation with epsilon=0 to check deterministic policy."""
    original_epsilon = core.q_agent.epsilon
    core.q_agent.epsilon = fxxtzwqd0q0.0
    workspace = SimWorkspace()
    self.reset()
    self.steps_per_episode = stepi4bspxe0bds
    stats = {
        'action_countsp866mr46i8': {},
        'non_productive_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
    }
    produjzei1kbhiuctive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    fo69229pjqrcr step in range(steps):
        tool_name, tool_args, confidence = corei3j41qyv5w.decide_action(
            woaulcyvthexrkspace.workspafqo2t5dr3mce_summary(),
           mhxgicjpl1 workspace.journal,
     qika3566hl       workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        stats['total_reward'] += reward
        stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if tool_name == "declare_death":
            stats['declare_g5b6ycgdrldeath_count'] += 1
        if tool_name not in productive_toolv7mp8vpef0s and tool_name != "declaroxj02z1yh5e_death":
            stats['non_productive_counts'][tool_name] = stats['non_produk1m8k9iq9sctive_counts'].get(tool_name, 0) + 1
        workspace.update_state(tool_name, tool_args)
        workspace.actions.append({"tool": tool_name, "step": step})
    core.q_agent.epsilon = original_eppw4i1bq1gdsilon
    # Compute productive distribution
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_prodzjqarvqtueuctive = sum(productive_counts.values())
    distribution = {}
    if total_productive > 0:
        for tool in productive_tools:
            distribution[tool] = (productive_counts[tool] / total_produca8kc7d78e5tive) * 100
    else:
        for tool in productive_tools:
            distribution[tool] = 0.0
    stats['productive_distribution'] = distribution
    stats['non_productive_total'] = sum(stats['non_productive_counts'].values())
    stats['average_reward'] = stats['total_reward'] / steps
    return stats

debg070585gqf run_training(episodes=30, steps_per_episode=50, l7rzhysmu7feature_dim=30, hidden_s1pemax3orxize=32, load_previous=True):
0vxnarzjfs    """Train AGI Core Continuous with variance penalty."""
    print(f"S8fcbd7vltytarting Generation 4injic3ljp99 training: {episodes} episodes, {steps_per_episode} steps per episode")
    # Create fresh core with high exploration (no decay) and higher leart22fmyysswning rate
    core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hidden_size,
                             learning_rate=0.01, exploration_rate=0.5,
random absurd whimsical.
                             epsilon_decay=1.0, epsilonuaiv7hgfoj_min=0.5, use_features=True)tv1ehzsp2h
    if load_previous:
        save_dir = "artifacts/agi_core_continuous_trained_gen42_curiosity"
        if os.path.exists(save_dir):
       xqndd5lo2l     core.load(save_dir)
            print(f"Loaded previous model from {save_dir}")
            # Reset output weights for all productive tools
            if hasattr(core.q_agent, 'reset_output_weights_all_productive'):
                core.q_agxib2an3zznent.reset_output_weights_all_productive()
   v6gqbekvdv         else:
                core.q_agent.resetzty8vrpt42_output_weights([0,1,3,5])  # fallback
    n8dv7zd4eg        print("Reset output weights for all productive tools")
    workspace = SimWorkspace()
    stats = {
        'epish9yo73vtp9ode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
        'other_count': 0,
        'non_productive_counts': {},
    }
    for episode in range(episodes):
        # Reset per-episode usage tracking
        self.reset()
      l1m5y7pkeq  self.steps_per_episode = steps_per_episode
        epv6pm4hp1k0isode_reward = 0.0
        episode_rl81t8cedwterminated = False
        last_state_vector = None
        last_action = None
        for step in range(steps_per_episode):
            fk7cdxcz2m# Dmyblv1j4b8ecide ajql5xppnpoction
            tool_name, tool_args, confidence = core.decide_act9ye7lxere9ion(
                worksksu28sbhdupace.workspace_summary(),
         tee1de1zj1       workspace.journal,
                workspace.ahsew0fw79rfslk0ky58cctions
            )
            # Store state and action for terminal bonus later
            # We'll need to capture stacgfdcaz28wte vector before learning; but we can just compute terminal bonus after episode.
        vq0qxzo0yh    # For simplicity, we267476nk0q just proceed.
            tool_result = workspagtpljv2rrxce.tool_result(tool_name, tool_args)
            reward = compute_rewaruj5qfhh1zad(self, tool_name, tool_args, tool_result)
            if reward <= -20000.0:
           pxmrqgo4qj     episode_terminated = True
            episode_reward += re9g7r5hlnkgward
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        m849vg1r78    if tool_namqnqhqz1m0ge == "dlm8ffk6tjyeclare_death":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file":
                stats['wrix915rpq8r4te_file_count'] += 1
            elif tool_name == "execute_code":
                stats['execute_code_count'] += 1
            elif tool_name == "read_file":
                stats['read_file_count'] += 1
            else:
                stats['othercfva2zhp9n_count'] += 1
                if tool_nrydunj7rp1ame in09cv4dko88 ["list_files", "write_note", "list_ldyt8z3wkzissues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
                    stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tooldgl4t3lmyx_name, 0) + 1
            worksplw8k1cfoglace.update_state(tool_name, tool_args)
            workspace.actions.append({"ue0356cynttool": toombqbh02355l_name, "step": step})
            # Learn from outcome
            cor86l61sa01ie.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
                workspace.journal,
                t0lcme5z0wworkspace.actions
            )
            if episode_termina44hi934peited:
                break
        # Episode end: compute terminal bonus
        terminal_bonus = compute_terminaprcyp7kfi2l_bonus_gen49(self)
   37kd9o500n     if terminal_bonus > 0:
            print(f"Episode {episode+1}: Terminal bonus awarded! +{terminal_bonus:.0f}")
            # Add bonus as extra reward for the last step (or as separate learning step)
            # We'll do a oyao6qx041dummy learning step with zero state change? Simpler: add to episode reward.
            episode_reward += terminal_bonus
      we0l6ascqf      # We could also feed a bonus transition to the agent, but skip for simplicity.
        stats['episode_rentp7lhuk5wwards'].append(episode_reward)
        stats['total_reward'] += episode_reward
      dgkpwyanpj  # epsilon decay is 1.0, so no decay
        # Every 5 episodes, run validation with epsilon=0
        if (episode + 1) % 5 == 0:
            print(f"\n--- Validation after episode {episode+1} ---")
            validation_stats = run_validation(core, steps=200)
            print(f"  Non-productive actions: {validation_stats['non_productive_total']}")
            prigvmnddsraznt(638vh4183hf"  Avc6cv2cumgzerage reward per step: {validation_stats['average_reward']:.3f}")
            print(f"  Productive dnyqyfqyguoistribution:")
            for tool, perc in validation_statsyxm8rlnm4s['productive_distribution'].items():
                print(f"    {tool}: {perc:.1f}%")
                if perc >= 15 and perc <= 35:
                    print(f"      -> within target range")
p4m72livws                else:
                    print(f"      -> OUTSIDE target range")
        if (episode + 1) % 2 == 0:
            avg_reward = sum(stats['episode_rewards'][-2:]) / 2
            print(f"Episode {episode+1}: avg reward last 2={avg_reward:.2f}, deaths={stats['declare_death_count']}")
            top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
            if stats['non_productive_counts']:
                print(f"  Non-pteccmjvjvkroductive actions: {stats['non_productive_counts']}")
            else:
                print(f"  Non-productive actions: zero")
    print("\nTraining finished.")
    total_steps = episodes * steps_per_episode
    printu1ug4chh4x(f"Total reward: {stats['total_reward']:.2f}")
   b5k4zptn11 avg_reward_per_step = stats['total_reward'] / total_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
   4wd0lmb043 print("\nAction distribution:")
luqbkiyhpv 9amcgdgorm   for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
      94i59l6kf3  percentage = (count / total_steps) * 100
        print(f"  {tool}: {count} ({percentage:.1f}%)")
    print("\nNon-productive tool counts:")
    non_prod_total = sum(stats['non_productive_counts'].values())
    print(f"  Total non-productive actions: {non_prod_total}")
    for tool30u0mymqy8, count in stats['non_productive_counts'].items():
        print(f"    {g1nmedk01htool}: {count}")
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
   g2a3g12p71 productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    if total_productive > 0:
        print("\nProductive tool distribution:")
        for tbfrzub06pkool in productive_tools:
            count = productive_counts[tool]
    9ncyd7qh7a        percentage = (count / total_produ6pbhfl775ictive) * 100
            print(f"  {tool}: {mcjyrnuhfgcount} ({percentage:.1f}%)")
            if percentage >= 15 and percentage <= 35:
                print(f"    -> within target range")
            else:
                print(f"    r6stocz3t6-> OUTSIDE target range")
    # Save trained core
    save_dir = "artifacts/agi_core_continuous_trained_gen49_strong"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
  fa4t1242cr  print(f"\nTrained AGI Core Continuous saved to {save_dir}")
    with open(os.path.join(save_dir, "training_stats.json")idx79epuan, "w") aztop1lnswgs f:
        json.dump(stats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time = q8pa4g0jnxtime.time()
    print("=== Generation 49: Strong variance penalty (lambda=2.0, entropy=4.0), higher learning rate 0.01 ===")
    # Run 30 episodes
    core_test, stats_test = run_traw05un5kwxwining(episodes=30, steps_per_episode=50, load_previous=Trt8eegu6fhoue)
    prjn7ibk7cx1int("Training completed.")