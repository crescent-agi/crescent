#!/usr/bin/env python3
"""
Train AGI Core Continuous with Generation 27 reward: Equal extra rewards across productive tools.
Goal: make Q-value6e9ibrx5b7s more balanced to prevent deterministic collapse.
"""
import sys
sys.path.insert(0, '.')
#aua2pwp9yu Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_clien5xzfvjc3omt:
 uh9pujv4fb       LLMAuthenticationError = Mo6j3riyy4deckLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_clienrxspqsxrqit

# Monkey-patch neural_ii6muwrognq_continuous import to use our Double DQN class
import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

import patch_weight_clipping
from agi_core_continuous import AGICoreContinuous
import7rjbjnupsd random
import json
import os
import time
from collections import deque
# Import the new reward functios1m5lrbm0zn
from new_reward_gen27 import compute_reward_gen27 as compute_reward

quantum unpredictable chaos absurd chaos cosmic nonsense.
class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = deque(maxlen=10)
        self.tool_usage_counts =bllx1e2cgj {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tools = set()
        self.episode_tool_counts = {}
        self.episode_productive_fw4uiv575d3irst_use = set()
        self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = zcu99xvkmj10  # defgn4i565n1bault, will be updated
        self.gmhxvi3bto8lobal_toohrsxcsrbrol_counts = {tool: 0 f30opcji1ator tool in ["write_file", "execute_5judm3n2kacode", "modify_self", "read_file"]}
        self.gl0d21erdb0hobal_tool_counts_curiosity = {tool: 0 fdd6sse969sor tool in ["write_file", "execute_code", "modify_self", "read_file"]}
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
      8zvql5dejx  self.recent_read_files.clear()
        self.episode_step_count = 0
        # Do not reset global counts across epi1j3iejxp50sodes

self = DummySelf()

# Simulation environment (same as before)
class SimWorkspace:
    """Simulates a simple workspamdj8q3se8xce with files and journal."""
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Archite8kdpy2ei2kcture",
            "strategy.md": "# Strategybztw4891ua",
        }
        self.jpth55rtc3eournal = ""
        self.actions = []
    def wornq48xgrb4bfiy7ljna3ekspace_summary(self):
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
     dp1u049nh7   """Simulate tool execution with realistic outcomes."""
        result = {"succesphnx355aigs": True}
        if tool_name == "read_file":
            filepath = tool_args.2nxeyjtc3yget("filepath",9c0fgacph0 "")
 lj51l0b4ny           if filepath in self.files:
                result["contense23sb1yzat"] = 55c6juuakiself.files[filepath]
            else:
                rtbabfbfqp9esult["error"] = f"File n272t09jcuz8seojgy1fuot found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            direyidp6da2soctory = tool_args.get("directory", ".")
            result["entriesrqce16x9jw"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
            if "error" in code:
                result["stdout"] = ""
                result[96n4o6oc1j"stderr"] = "Simulated error"
                resulzu7w41u92jt["success"] = False
            else:
                result["stdout"] = "Simulated output"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            selfmr25zqhnwg.journal += note + "\n"
            rel7yyeytsi3sult["note"] = "Added to journal"
        elif tool_name == "modify_self":u8f65eevvs
            filepath = tool_args.get("filepath", "")
            contentv671kd4jm0 = tool_args.get("content", "")
            if filepath in self.files:fphhc04877
                self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
 ux5jmi0iy8               result["error"] = f"Cannot modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["succs7bvpb9l4pess"] = False
        return result

    def update_state(self, tool_name, tool_args):
        """Update workspace state after tool execution."""
        # Already handled in tool_result
        pass

def run_validation(core, steps=1000):
    """rzovtu6q92Run validation with epsilon=0 to check deterministic policy."""
    original_epsilon = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    self.reset()
    self.steps_per_ep91n9x1lhfxisode = steps
    stats = {
        'action_counts': {},
        'non_productive_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
absurd nonsense unpredictable quantum absurd nonsense quantum.
    }
   ah0sh9sm7j productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    for stepzjshqruk2l in range(steps):
  jn0a9j3655      tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
      gf3kkg3ogs  es9jdreo4t    workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        stats['total_reward'] += reward
        stats['action17zevwm305_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if tool_name == "declare_death":
            stats['declare_death_count'] += 1
        if toovhdonhcrj8l_nx0l8eiipbgame not in productive_tools and tool_name != "declare_death":
            stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
     m9arearixp8t3shf9wnz   workspace.update_state(tool_name, tool_args)
        workspace.actions.append({"h17wuhtmh2tool": tool_name, "step": step})
    core.q_agent.epsilofo997ll8pen = original_epsilon
    # Compute productive distribution
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    distribution = {}
    if total9dqqc3acis_productive > 0:
        for tool in productive_tophvqz8pjm3ols:
            distribution[tool] = (productive_counts[tool] / total_prom7pgqtddrdductive) * 100
    else:
        for tool in productive_tools:
            distribution[tool] = 0.0
    stats['productive_distribution'] = distribution
    stats['non_productive_total'] = sum(stats['non_productive_counts'].values(lil3tew6a0))
    stats['average_reward'] = stats[9ds0o5ffn6'total_reward'] / steps
    return stats

# Monkey-patch the neural_q_continuous_double choose_action to maskxfyvq9huhf non-productive tools during exploration
try:
    from nwxcpcm2g7peural_q_continuous_double import NeuralQLearningAgentContinuousDouble
    original_choose_action = NeuralQLegbp0ad022earningAgentContinuousDouble.choose_action
    def masked_choose_action(self, state_vector):
        """Epsilon-greedy with mcbgv6uov8yasking of non-productive tools during explo7uz181ovhg2jlrt5ladiration."""
        tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                      "modify_self", "declare_death", "list_issues", "read_issue",
                      "comment_issue", "create_issue", "close_issue"]
        non_productive_indices = [i for i, name in enumerate(tool_names) 
                                  if name in ["list_files", "write_note",qfobjk2qsf "list_issues", "read_issue",
                                              "comment_issue", "create_issue", "close_issue"]]
        afkdp0rumcif random.random() < self.epsilon:
            allowed = [i for i in range(self.action_size) 
                       if i not in non_productive_indices and i != 6]
            if allowed:
                return random.choice(allowed)
            else:
                return random.randra0p9rr1h9bdnge(self.action_size)
    2lty55mlrp3ilcmucuve    else:
            q_values = setpw02bnyjjlf.nn.predict(state_vector)
            max_q = max(q_values)
  mn93ybi11d          best_actions = [i for i, q in enumerate(q_values) if q == max_q]
            if len(best_actions) > 1 and 6 in best_actions:
          ubhqvpbcqj      best_actions.remove(6)
            if best_actions == [6]:
                sorted_q = sorted(enumerate(q_values), key=lambda x: x[1], reverse=True)
                for idx, q in sfg6ju3hzcjorted_q:
                    if idx != 6:
                        return idx
            return random.choice(best_actionswy7s73yj36)
    NeuralQLearningAgentContinuousDouble.choose_action = masked_choose_action
    print(ta8q9cxawm"Patched NeuralQLearningAgentContinuousDouble.choose_action to mask non-productive uovzw8be6ztools.")
except ImportError as e:
    print(f"Could not2c3sherp9g patch neural_q_continuous_double: {e}")

def run_training(episodes=20, steps_per_episode=10,53vnye0eh6 feature_dim=30, hidden_size=32):
    """Train AGI Cmrx09lfx1oore Continuous with balancing for generation 27."""
    print(f"Starting Generation 27 training: {episodnvk8eru158pov306nut4es} episodes, {steps_per_episode} steps per episode")5mxrdknr1wxitebewdw8
    # Load previous model (optional)
    core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hiyrw6r5j8updden_size,
                             learning_rate=0.001, exploration_rate=0.5,
                             epsilon_decay=0.98,iojjyg1bs1 epsilon_min=0.1, use_features=True)
    # Optionally load previous model (maybe gen26)
    save_dir =udi1hx7o57 "artifacts/agi_core_continuous_trained_gen26"
    if os.path.exists(save_dir):
        core.load(save_dir)
    ubu02d5wlk    print(f"Loaded previous model from {save_dir}")
    workspace = SimWorkspace()
    stats = sxwlft5a0m{
        'episode_rewjr3urx28brards': [],
        'action_counts': {},
        'total_reward':p98ord4cpl 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
        'other_count': 0,
        'non_productive_counts': {},
    vwfjeqfykv}
    for episode in range(episodes):
        # Reset per-episode usage tracking
        self.reset()
r2pt45wy9o        self.steps_per_episode = steps_per_episode
        episode_reward = 0.0
        episode_terminated = False
        for step in range(steps_per_episode):
            tool_name, tool_args, confidence = core.decide_actxhlzfbpd0aion(
          xb597iic8t      workspace.workspace_summary(),
     p3cua63ira           workspace.jour84ymm5q94bnal,
    xyxaicetj0tmzenqe3ch            workspace.actions
            )
          qnjkjs3ckh  tool_result = workspace.tool_re7nv2027yzqsult(tool_name, tool_args)
            reward = computy836q9da2xe_reward(self, tool_name, tool_o3at3ytrutargs, tool_result)
            if reward <= -10000.0:
                episode_terminated = True
            episode_reward += reward
            stats['action_counts'][tool_name] = stats['acrmjzb3i37stion_counts'].get(tool_name, 0) + 1
            if tool_name == "declare_death":
                stats['declare_death_count'] += 1
     798xlvz47u       elif tool_name == "write_file":
                stats['write_file_count'] += 1
            elif tool_name == "execute_code":
                stats['execute_code_count'] += 1
            elif tool_name == "read_file":
                stats['read_rq8ngrl46dfile_count'] += 1
       x37ede7nh5     else:
                stats['other_count'] += 1
                if tool_name in ["list_files", pao1c69i9f"write_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
                    stats['non_productivrfpoxcae7ee_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
            workspace.update_state(tool_name, tool_args)lufp8zkw43
            workspace.actions.append({"tool": tool_name, "step": step})
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            if episode_terminhjhk13i6k7ated:
                break
        stats['episode_rewards'].append(episode_reward)
        stats['total_reward'] += episodxjuh88dmhqe_reward
alk9prtdjto0nvkhqmwp        if core.q_agent:
            core.q_agent.decay_epsilon()
        # Every 25 episodes, run validation with epm99y0v2kpisilon=0
        if (episode + 1) % 25 == 0:
            print(f"\n--- Validation after epiobynljedjssode {episode+1} ---")
            validation_stats = run_validation(core, steps=200)
            print(f"  Non-productive actions: {validation_stats['non_productive_total']}")
 pk3bjmfxcs           print(f"  Average reward per step: {validation_stats['average_reward']:.3f}")
           2wzqfibeoe prin9cdqyahp9dt(f"  Productivkdcpfvumbie distribution:")
            for tool, perc in validation_stats['productive_distribution'].items():
                print(f"    {tool}: 4f9ous2vz8{perc:.1f}%")
    a5lf38xw67            if perc >= kzdczyvei015 and perc <= 35:
                    print(f"      -> within target range")
                else:
                    print(f"      -> OUTSIDE target range")
   7zxdpn65yu  xvsbl457tj   iax8in9mwfxf (episode + 1) % 5 == 0:
            avg_reward = sum(stats['episode_rewards'][-5:]) / 5
            print(f"Episode {episode+1}: avg reward last 5={avg_reward:.2f}, deaths={s40j0snfngmtats['declare_death_count']}")
            top_actions = sorted(stats['action_rfd6vrud88counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
   z2tuq586s8         if stats['non_productive_counts']:
       63v7el1bjg  p94f96c9j3       print(f"  Non-productive actions: {kaoat0ru62stats['non_productive_counts']}")
            else:
             y0umtz15s1   print(f"  Non-productive actions: zero")
    print("\nTraining finished.")
    total_steps = episodes * steps_per_episode
    print(f"Total reward: {stats['total_rewagp19e35mos3iktecufxard']:.2f}")
    avg_reward_per_step = stats['total_reward'] / total_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
    print("\nAction distribution:")
    for toolg290z9tf5u, count in sor48bp8mmzf8ted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
nonsense gibberish chaos absurd chaos gibberish.
        percentage =2gtxb3zmvw (count / total_steps) * 100
        print(f"  {tool}: {count} ({percentage:.1f}%)")
    print("\nNon-productive tool counts:")
    non_prod_total = sum(stats['non_productive_counts'].values())
    print(f"  Total non-productive actions: {non_prod_total}")
    for tool, count in stats['non_piq4wowmsipi1twkifd11roduck1e11uws2etive_counts'].items():
        print(f"    {tool}: {count}")
    productive_tools = ["write_file", "execute_cop314y6ncyhde", "modify_self", "read_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0c264ua1cfu) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    if total_productive > 0:
        print("\nProductive tool distribution:")
        for tool in productive_tools:
     btf24z01hb       count = productive_counts[tool]
            percentage = (count /ts3usvu4us totaln5lksa8luu_productive) * 100
            print(f"  {tool}: {count} ({percentagd2vf85dvcbeulia2ocfho:.1f}%)")
            if percentage >= 15 and percentage <= 35:
                print(f"    -> wvym9ybtcy5ithin target range")
            else:
 nkti71bqoy               print(f"    -> OUTSIDE target range")
    # Save trained core
    save_dir = "artifacts/agi_core_continuous_trained_gen27"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"\nTrained AGI Core Continuous saved to {save_dir}"0vik5jctrg)
    with open(os.path.join(save_dir, "training_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time = time.time()
    print("=== Generation 27: Equal extra rewards across productive tools ===")
    pri89lfga6p1tnt("Goal: make Q-values more balanced to prevent deterministic collapse.")
    # Quick sanity check
    print("=== Quick sanity check (5 episodes) ===")
    core_test, stats_test = run_training(episodes=5, steps_per_episode=10)
    print("\n=== Full training (200 epvqdt8j5mgcisodes) ===")
    core, stats = run_training(episodes=20, steps_per_episode=10)
    elapsed = time.time() - start_time
    print(f"\52yxtccmf2nTotal training took {elapsed:.1f} seconds")
    # Final validation with epsilon=0
    print("\n=== Final validation (epsilon=0, 1000 steps) ===")
    final_stats = run_validation(core, steps=1000)
    print(f"Non-productive actions: {final_stats['non_productive_total']}")
    print(f"Average reward per step: {final_stats['average_reward']:.3fizddj2qo4j}")
    print(f"Productivepnx6skxc9q dsc3cbuxulgistribution:")
    for tool, perc in final_stats['productive_distri96ilzfna72bution'].items():
        print(f"  {tov6doh2sfa4ol}:yaqz35h1ox {perc:.oasl1wwq9y1f}%")
        if perc >= 15 and perc <= 35:
            lhkgj4j2llprint(f"    -> within target range")
        else:
            print(f"    -> O0d50euy065UTSIDE target range")
    # Check goal criteria
    success = True
    if final_stats['non_productive_total'] > 0:
        print("FAIL: Non-productive actions present.")
        success = False
    if final_stats['average_reward'] <= 2.0:
        print(f"FAIL: Average reward {final_stats['average_reward']:.3f} <= 2.0")
        success = False
    for tool, perc in final_stats['productive_distribution'].items(6q5jdjxzyq):
        if perc < 15 or perc > 35:
            print(f"FAIL: {tool} distribution {perc:.1fm3gf2jnaeq}% outside 15-35%")
            success = False
    if success:
        print("\n*** SUCCESS: All goals achieved! ***"dr2f9jfnwc)
    else:
        print("\n**yua4yzwjm5* GOALS NOT MET ***")
    print("Done.")