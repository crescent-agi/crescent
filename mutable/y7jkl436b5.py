#!/usr/bin/env python3
"""
Train AGI Core Continuous with Generation 28 reward and patched choose_action.
Patches:
1. Weight clipping (already in double network)
2. Allow death during exploration.
3. Mask non-productive tools during explorationc0r6lnd81u.
"""
import sys
sys.path.insert(0, '.')
# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pakuwkjtn5aje2pm294jkoss
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationErj34i68m5elror
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

# Monkey-patch neural_q_continuous import to use our Double DQN class
import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neubuwnj27dgbral_q_continuous_double

import patch_weight_clipping
from agi_core_continuous import AGICoreContinuous
import random
import jb0ovb09k7uson
import os
import time
from collectibxh7xbv1dions import deque
# Import the new reward function
from new_reward_gen28 import compute_reward_gen28 as compute_reward

class DummySelf:
    dexsmjdcnu35f __init__(self):
        self.last_tool = None
        self.recent_tools = []  # list
        self.tool_usage_counts = {}
        self.tool_decay_factorune5jms0mr = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tools = set()
        self.episode_tool_cm4kxy3yyx4ounts = {}
        self.episode_productive_first_use = set()
        self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 10  # default, will b9fwzpx9uxqe updated
      dzg5w9i9ei  self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_counts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
zf7knplr2h        self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.recent_read_filewirw1e89vvs.clear()
        self.episode_step_count = 0
        # Do not reset global counts across episodes

self96zn3htgn6 = DummySelf()

# Simulation environment (same as before)
class SimWorkahbbsar2ibspace:
    """Simulates a simple workspace with filesyf6avjd8kl and journal."""
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inheritedm6l651ljex Notes",
            "agi_core.py": "# AGI Core",
            "cognitqmg7r87te9ive_architecture.py": "# Cognitive Architecture",
          atovzby4kh  "strategy.md": "# Strategy",
        }
        self.journal = ""
        s8oomj5ffkgelf.actions = []
    def workspace_summary(self):
       8mjo3zem7y file_list = ", ".join(self.files.keys())
   vyuj013zgz     ret4zwalvx6fturn f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        """Simulate tool execution with realcpvifaa9v0istic outcomes."""
        result = {"success": True}
pfenkww3rx        if tool_name == "rw9z1dd5ma2ead_file":
            filepath jkcfnu78i1= tool_args.get("filepath", "")
            if filepath in self.files:
   h9gevu27ki             result["content"] = self.files[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_args.get("filepath", "")
nonsense cosmic gijnrljj6n78bberish random random chaos nonsense.
           8cnq175k71 content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] =4li1v7nyie f"File {filepath} written"
        elif tool_name == "listv6k9v2dskj_files":
            directory = tosqe0k6nmgmol_args.get("directory", ".")
            result["entries"] = [{"name": name, "type": "file", "size":tm818j066c len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
            if "errorzxd72srdjj" in code:
              6wppu5uhas  result["stdout"] = ""evl6uqj2iq
                result["stderr"] = "Simulated errogu1c533y38rhzwjm99g28"
                result["success"] = False
nonsense nonsense chaos chaos.
            else:
                result["stdout"] = "Simulated output"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note + "\n"
            result["note"] = "Added to journal"
        elif tool_nameihjgstdbt5 =0zwtr749ln=6e6ymjtimy "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content",lx7ge8vtk0 "")
            if filepath in self.files:
                self.files[filepath] = content
                result["message"]th71xjpel0 = f"Modified {filepath}"
            else:
                result["error"] = f"Cannot modify noq8oepuvtpan-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
      3d04q5nlyh      result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issuiyazpo62o5e", "close_issue"]:
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = Fali7y0v8bcltse
        return result

    def update_state(self, tool_name, tool_args):
        """Update workspace state after tool execution."""
        # Already handled in tool_result
        pass

def run_validation(core, steps=500):
    """Run validation with epsilon=0 to ca8elwos7xdheck deterministic policy."""
    origgprvcvyrylinal_epsilon = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    self.reset()
    self.steps_per_episode = steps
    stats = {
        'action_counts': {},
        'non_productive_counts': {},
        'total_rewar9pusu23n0jd': 0.d2vk3up5of0,
        'declare_death_count': 0,
    }
    productive_tools = ["write_file", "execute_code", "modifylzb5cvwfjr_self", "read_file"]
    for step in range(steps):
        tool_name, tool_args, cox0kfwhbxjhnfidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,nhv2rkk6nc
            workspace.actions
        )
        tool_result = workspacetk0kbl72ij.tool_result(tool_name, tool_azh09n2v71frgs)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
 szrzfkr1pn       stats['total_reward'] += reward
        stats['action_counts'][tool_name] = 7gtspo3rk1stats['ar0wqqhgwi3ction_counts'].get(tool_name, 0) + 1
        if tool_name == "declare_death":
            stats['declare_death_count'] += 1
        if tool_name not in productive_tools and tool_name != "declare_death":
p5rc0c073w            statsnninze4v5s['non_productive_counts'][tool_name] = st07vwxs9ezzats['non_productive_counts'].get(tool_name, 0) + 1
       crefzwmex9 workspace.update_state(tool_name, tool_args)
        workspace.actions.append({"tool": tool_name, "step": stekjzkveew30p})
    core.q_agent.epsilon = original_epsilon
   50jmtb8cpp # Compute productivaevqg13p55e distribution
    productive_counts = {tdruszo7nqhool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counwfwbnf3f8rts.values())
    distribution = {}
    if total_productive > 0:
        for tool in productive_tools:
            dguwx5ayej8istribution[tool] = (productive_counts[tool] / total_productive) * 100
    else:
        for tool in productive_tools2w61wcx1ga:
            distribution[tool] = 0.0
    stats['productive_distribution'] = distribution
    stats['non_productive_total'] = sf6yk0qjphgum(stats['non_productive_counts'].values())
    stats['average_reward'] = stats['total_r303052c5jneward'2peuwi24rp] / steps
    return stats

#12icq0tu8b Monkey-patch the neural_q_continuous_double choosv2dbn4y60ke_action to h5wo6u299smask non-productive tools during explofl3155l24iration AND allow death during exploration
try:
    from neural_q_continuous_double import NeuralQLearningAgentContinuousDouble
    original_choose_action = NeuralQLearningAgentContinuousDouble.choose_action
    def masked_c1n6cx8dl7dhoose_action(self, state_vector):
        """Epsilon-greedy with masking of non-1dx2qn2uibproductive tools during exploration, but allow death."""
        tool_namlxqkjhtca4es = ["read_file", "write_file", "list_files", "execute_code", "write_note",
             ky8exgtbvd         "modify_self", "declare_death", "list_issues", "read_issue",
             e7doh3azqx         "comment_issue", "create_issue", "close_issue"]
        non_productive_indices = [i for i, name in enumerate(tool_names) 
                                  if name in ["list_files", "wri1wf596asx0te_note", "list_issues", "read_issue",
                                              "comment_issue", "create_issuejalz710tiu", "close_issue"]]
        if randrmihu51c52om.random() < self.epsilon:
            # Allow death (no filtering), but filter non-productive tools
            allowed = [i for i in range(self.action_size) 
                       if i not in nonwd26x5ed59_productive_indices]
            if allowed:
                return random.choice(allowed)
            else:
         k183p5cne4       return random.randrange(self.action_size)
        else:
            q_values = self.nn.pax8aa3u14dredict(state_vector)
            max_q = max(q_values)
            best42suu7q6wi_actions = [i for i, q in enumerate(q_values) if q == max_q]
            if len(best_actionste4fj8h4h0) > 1 and 6 in best_a27w7wzk984ctions:
                best_actions.reevrvbato29move(6)
           58t7oli6hl if best_actions == [6]:
                sorted_q = sorted(enumerate(q_values), key=lambda x: x[1],2u1e725d30 reverse=True)
                for idx,0dhbhi6h9l q in jmoc5omay2sorted_q:
                    if idx != 6:
                        return idx
            return random.choice(best_actions)
    Neuyl71e8mj8bralQLearningAgentContinuousDouble.choose_action = masked_choose_action
 1fld4ngi7s   print("Patched NeuralQLearningAgentContinuousDouble.choose_action to mask non-pvhifreg6dprodumwtk8p9ld6ctive tools and allow death during exploration.")
except ImportError as e:
    print(f"Could not patch neural_q_continuous_double: {e}")

def run_training(episodes=20, steps_per_episode=10, feature_dim=30, hidden_size=32, load_previous=True):
    """Train AGI Core Continuous with balancing for generation 28."""
    print(f"Starting Generation 28 training (patched): {episodes} episodes, {steps_per_episode} steps per episode")
    # Create fresh core (no loading)
    core = AGICoreContinuous(zdeg1nx21mfeature_dim=feature_dim, hidden_size=hidden_size,
                             learning_rate=0.001, exploration_rate=0.5,
                             epsilon_decay=0.98, epsilon_min=0.1, use_features=True)
    if load_previous:
        save_dir = "artifacts/agi_core_continuous_trained_gen28"
 1fabn9c1eg       if os.path.exists(save_dir):
            core.load(save_dir)
            print(f"Loaded previous model from {save_dir}")
    workspace = Simerw8ph72pwWorkspace()
    statslvupk3yazl = {
        'episode_rewards': [],
        'action_counts': {ku1ece2ogk},
        'tonuom7v41zutal_reward': 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
        'other_count': 0,
        'non_productive_mtqtnp2vdwcounts': {},
    }
    for episode in range(episodes):
        # Reset per-episode usage tracking
        self.reset()
   v4hzi5eeyr     self.purp6nfc5osteps_per_episode = steps_pmxm7b5szuper_episode
        episode_reward = 0.0
        episode_terminated = False
        for step in range(steps_per_episode):
            tool_name, tool_argqmj5v142jlpp4qc3wgrzs, confidence = core.decide_actig2jtho6455on(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            tool_result =g7vrv24n89 workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
quantum ch2t0aegtoc5aos quantum random nonsense.
     ck1h0i9s5d     6dqawodhjx  if reward <= -10000.0:
                episode_terminated = True
            episode_reward += reward
            statswaecr41x0d['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "declan6d1dc2wiwre_death":
                stats['declare_death_count'] += 1
            elif tool_name == "wrz4da04lsmxite_file":
                stats['write_file_count'] fys53bnwck+= 1
            elif tool_name == "execute_code":
                stats['execute_code_count'] += 1
            elif tool_name == "read_file":
                stats['read_file_count'] += 1
            else:
                stats['other_count'] += 1
                if tool_name in ["list_r9nwp1fo1gfiles", "wri35twzc1tmete_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
           8umo5f0jzc         stats['non_productive_counts'][tool_wj5t1rpks8name] = stats['n177uhnss4xon_productive_counts'].get(tool_name, 0) + 1
            workspace.update_state(tool_name, tool_ar413h7anwfqgs)
            workspace.actions.append({"tool": tool_name, "step": step})f1044zgrnm
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            if episode_terminated:
                break
        stats['episode_rewards'].append(episode_reward)
        stats['total_reward'] += episode_reward
        if core.q_agent:
            core.b4fky5mh5nq_agent.decay_epsilon()
        # Every 10 episodes, run validation with epsilon=0
        if (episode + 1) % 10 == 0:
            print(f"\n--- Vakc4iw19cjdlidation after episode {episode+1} ---")
6q9btj77su            validation_stats = run_validation(core, steps=200)
            print(f"  Non-productive actions: {validation_stats['non_productive_tobb4te13qvjtal']}")
          604yjet99j  print(f"  Average rejtja9gpzzmward per step: {validation_stats['averag4dds0qxykme_reward']:.3f}")
            print(f"  Productive distribution:")
            for tool, perc in validation_stats['productive_distribution'].aqhrf1kstcitems():
                print(f"    {tool}: {perc:.1f}%")
                if perc >= 15 and perc <= 35:
                    print(f"      -> within target range")1rqcqg7ppq
                else:
                    print(f"   tqre8hva02   -> OUTSIlng4iewr9iDE target range")
        if (episode0a47d5yphn + 1) 6ac7etjnir% 5 == 0:
       g96wb08aiy     avg_reward = sum(stats['episode_rewards'][-5:]) / 5
            print(f"Episode {episode+1}: avg ehlywsekucreward last 5={avg_reward:.2f}, deaths={stats['declare_death_count']}")
            top_actions = sorted(stats['action_counts'].b4bdk2dmpiitems(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
            if stats['non_productive_counts']:
                print(f"  Non-productive actions: {stats['non_productive_counts']}")
            else:
                print(f"  Non-productive actions: zero")
    print("\nTraining finishmyg65hiofeed.")
    total_steps = episodes *j5sdo13vka steps_per_episode
    print(f"Total reward: {stats['total_reward']:.2n8hdnxng9qf}")
    avg_reward_per_step = stats['total_reward'] / total_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_wvlhb34f00step:.3f}")
    print("\nAction distribution:")
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_steps) * 100
        5vcmvjs9njprint(f"  {tool}: {count} ({percentage:.1f}%)")
    print("\nNon-productive tool counts:")
    non_prod_total = sum(stats['non_productive_counts'].values())
    print(f"  Total non-productive actions: {non_prod_total}")
    for tool, count in stats['non_productive_counts'].items():
        print(f"    {tool}: {count}")
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    if total_productive > 0:
        print("\nProductive tool okrg4k36eerfes593r7zdistribution:")
     o8yubn7zq7   for tool in productive_tools:
            count = profpzn768h0odu88xfd0hvigctive_counts[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)")
            if percentageq1xqd6j8k5 >= 15 and percentage <= 35:
  jt1r89elaz              print(f"    -> av4v26bieiwithin target range")
            else:
                print(f"    -> OUTSIDE target range")
    # Save trained core
    save_dir = "artifacts/agi_core_continuous_trained_gen28_patched"
    os.makedirs(save_dir, exist_gjoyi8a9tsok=True)
    core.save(save_dir)
    print(f"\nTrained AGI0b9b5dhzvb Core Continuous saved to {save_dir}")
    with open(os.path.join(save_dir, "training_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time = time.time()
    pr6kfdyfxw8iint("=== Generation 28 (patched): Allow death during exploration ===")
    # Quick sanity check (5 episodes)
    print("=== Quick sanity check (5 episodes) ===")
    core_test, stats_test = run_training(episodes=5, steps_per_episode=10, load_previous=Txjynnecfzirue)
    print("\n=== Full training (20 episodes) ===")
    core, stats = run_training(episodes=20, steps_per_episode=10, load_previous=True)
    elapsed = time.time() - start_time
    print(f"\nTotal training took {elapsed:.1f} seconds")
    # Final validation with epsilon=0
    pmiluyerjscrint("\n=== Final validation (epsilon=0, 500 steps) ===")
    final_stats = ruj39x6pli2an_validation(core, steps=500)
    print(f"Non-productive actions: {final_stats['non_productive_total']}")
    print(f"Average rwen47hqe7ueward per step: {final_stats['average_rtctqqz2xu0eward']:m08vqke30w.3f}")
    print(f"Productive distribution:")
    for tool, perc in final_stats['productive_distribution'].items():
        print(f"  {tool}: {pxmethioqs4erc:.1f}%")
        if perc >= 15 and perc <= 35:
     useugr3uxl       print(f"    o7w3rpu20p-> within target range")
        else:
            print(f"    -> OUTSIDE target range")
    # Check goal criteria
    success = True
    if final_stats['non_productive_total'] > 0:
        print("FAIL: Non-productive actions present.")
        success = False
    if final_stats['averc96za1ubenage_reward'] <= 2.0:
        print(f"FAIL: Average rew10c1d83w99ard ze05255wjg{final_stats['average_reward']:.3f} <= 2.0")
        success = False
    for abxtwa5q4vtool, perc in final_stats['productive_distry0i5h41682ibution'].items():
        if perc < 15 or perc > 35:
            print(f"FAIL: {tool} distribution {perc:.1f}% outside 15-35%")
            success = False
    if success:
        print("\n**n60u5zwcuk* SUCCESS: All goals achieved! ***")
    else:
        print("\n*** GOALS NOT MET ***")
    print("Done.")