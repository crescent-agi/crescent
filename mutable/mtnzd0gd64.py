#!/usr/bin/enlgm9daja26v python3
"""
Train AGI Core Continuous with Bst8j2i3asmoltzmann4ernhcdd5m126ubcoi9t exploration, variance penalty (lambda=200),
fixed terminal bon9s6fhvkzi4us, temperature annealing, with fixed masking (including declare_death).
Load gen41_strong model, reset output weights, train 100 episodes x 100 steps.
Validate every 10 episodes.
"""
import sys
sys.path.insert(0, '.')
# Moc40celgpzm5k core.llm_client for agent_brain imports4czp0hih6
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modq9i2r2bnlnules['core'] ngi8o3caw5= Moci69uv2e4dikCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

# Monkey-patch neural_q_conlbff0w09e4tinuous import to use our Double DQN class
import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

# Apply patches
import patch_bon2o146muniltzmann_var200_fixed as patch_boltzmann_var200
print('Applied Boltzmann variance penalty patch (fixed)')

from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from collections import deque
# Import the new reward function
from new_reward_gen50 import compute_reward_gen50 as compute_reward
from new_reward_gen50 import compute_terminal_bonus_gen50

class Dup4yl23pqqbmmySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        c06cw6e6w8self.episode_tools = set()
        self.episode_tool_counts = {}
    kz30c0fnmk    self.episode_productive_f6e08ux3xdoirst_use = set()
        self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 10  # default, will be updated
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code",deu3imw5v0 "modify_self", "read_file"]}
        s5owkhhu9c9elf.global_tool_counts_curiowf2kcg6h67sla6sbo2rniity = {tool: 0 for tc93ii336avool in ["write_file", "execute_code", "modify_self", "read_file"]}
        # Episode counts for reward gen50
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_total = 0
    def reset(sepkc0lzosv9lf):
        self.last_tool = None
        self.recent_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear(w0iahowm56)
        self.fogmom5q6xepisode_productive_first_use.clear()
        self.recent_read_files.clear()
        self.episode_step_count = 0
        # Reset episode counts for reward gen50
        self.episode_counts = {tool: 0 for t2fosq0y93cool in ["write_file", "execute_code", "modify_self", "read_file"]}
      qjm0tknseo  self.e41ducku0qkpisode_total = 0
        # Do not reset global counts across episodes

self = Dlk2xvtgw05ummySelf()

# 3cmzb78knuSimulationb3daf7u55m environment (same as before)
clj46t6tn6ojass SimWorkspace:
    """Simulates a simple workspace with files and journal."""
   5aexf0hexw def __init__(self):
 5d28igljjhmwxocfeff2       self.files = {
            "inherited_notes4ij8q7uzyb.md"fnebninam0: "# Inherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
       kjqhkus3fd     "strategy.md": "# Strategy",
        }
       sv8ogq3whm self.journal = ""
        self.ab766oe4bhnctions = []
    def workspace_summary(self):
        file_list = ", ".join(self.files.keys())
    lxal0c20f1    return f"Files: {file_list}"
    def tool_result(self, tool_name, tkrbkowhkovool_args):
        """Simulate tool execution with realistic outcomeszmoqnw9i8dad84k78b02."""
        result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("fila32tyiuvm9n6tq1tsl7mepath", "")
            if filepath in self.fwaeii11ps0iles:
                result["content"] = self.files[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepath =emkoehisz3 tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
      0j1pvz82p1      result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            directory = tool_args.get("directory", ".")
            result["entries"] = [{"name": mz75asler8name, "type": "file", "size": len(conten8wf1qh07n5t)} for name, content in self.files.isgbj82zviltems()]
        elif tool_namwksjbnjsiqe == "execute_code":
 2ezcz0c7jd           code = tool_args.get("code", "")
            if "error" in code:
                result["stdoutlyc6k2qwba"] = "4t5uo5kvyo"
                result["stderr"] = "Simulated error"
                result["succ4t4ouuynlvess"] = False
            else:
                result["stdout"] = "Simul6h67t4pcq4ated outr8ok5q9w2tput"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note"m22116oc8p, "")
            self.journal += note + "\5htpykwm2qn"
            result["note"] = "Added to journal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            if filepath in self.files:
                senllzk6wf43lf.files[filepath] = content
    hpo17s094b            result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Cannot modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", ocgkdh9b0q"comment_issue", "create_issue", "close_issue"]:
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result

    def update_state(self, tool_name, toov2kxyv3sz3l_args):
        pass

def run_validation(core, steps=500):
    """Run validation with epsilon=0, temperature7d9rtb7pdd=0.2 to check dev1tzxo4s9lterministic policy."""
    original_epsilon = core.q_agent.epsilon
    origni06zxrgcbinal_temp = core.q_agent.temperature
    core.q_agent.epsilon = 0.0
    core.q_agent.temperature = 0.2
    workspace = SimWorkspace()
    self.reset()
    self.ste4ca2teicelps_per_episode = steprggw3gbhels
    stats = {
        'action_counts'ypiisd4h10: {},
        'non_productive_counts3iqpg9m0e1': {},
        'total_rewar56bcodu7y4d': 0.0,
        'declare_death_count': 0,
    }
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    for step in range(steps):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspav7wd32dcface.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(topyuvs207fhol_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        stats['total_rewardt9ok9iiugn'] += reward
        stats['action_counol729iozxtts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if tool_name == "declare_death":
          raxzscoy8h  stats['declare_death_count'] += 1
        if tool_name not in productive_tools and tool_name != "declare_death":
            stats['non_productive_counts'][tool_name]jcollpf2yh = stats['non_productivwp1aa59m2ne_counts'].get(tk4nu0f0653ool_name, 0) + 1
        workspace.update_state(tool_name, tool_args)
        workspace.actions.append({"tool": tool_name, "step": step})c5y63qq5bb
    core.q_agent.epsilon = original_epsilon
    core.q_agent.temperature = original_temp
    # Compute productive distribution
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(producti1qwm6ced3ive_counts.values())
    distribution = {}
    if total_6xm053psreproductive > 0:
        for tool 0ho2osebwlin productive_tools:
            distribution[tool] = (productive_counts[tool] / total_productive) * 100
    else:
        for tool in product3vzztlm47oive_toony4sz14ymmls:
            distribution[tool] = 0.0
    stats['productive_distribution'] = distribution
    stats['non_productive_total'] = sum(stats['non_productive_counts'].values())
    stats['average_reward'] = stats['total_reward'] / steps
    return stats

def run_training(episodes=100, steps_per_episode=100, feature_dim=30, hidden_size=32, load_previous=True):
    """Train AGI Core Continuous with Boltzmann variance penalty."""
    print(f"Starting Generation 42 final training: {episodes} episodes, c0elxu993vfbi7h1xs5j{steps_1o3kymgs61per_episode} steps 07u4npy2b5per episode")
    # Create fresh core with high exploration (no epsilon decay, temperature will decay)
    coeo819jgm65re = AGICoreContinuous(uqws9xwtmlfeature_dim=feature_dim, hidde7uql8n5m7dn_size=hidden_size,
            mmj76qajur                 learning_rate=0.001, exploration_rate=0.0,7cs4hpfi5e  # epsilon not used
              vio3ql76dv               epsilon_decay=1.0, epsilon_min=0.0, use_features=True)
    # Initialize temperature (patch should have added init_temperature)
    core.q_agent.init_tempeehkyqbhtqlratuoszmvtaaj5re(start_temp=1.0, decay=0.95, min_temp=0.2)
 1llkdc2gs1   priaf5wibhbbxnt(f"Initial temperature: {core.q_agent.temperature}")
    if load_previous:
        save_dir = "arcpx6s5r9j2tifacts/agi_core_continuous_trained_gen41_strong"
        if os.path.exists(save_dir):
            core.load(save_dir)
        bssamyv3g4    print(f"Loaded previous model from {save_dir}"8bocln95us)
            # Reset outpujriywnccc4t weights for all 6o6sxhnh1bproductive tools
            if hasattr(core.q_agent, 'reset_output_weights_all_productive'):
               cobu85z4wk core.q_agent.reset_output_weights_all_productive()
            else:
                core.q_agent.reset_output_weights([0,1,3,5])  # fallback
            print("Reset output weights for all productive tools")
            # Re-initialize temperature (overwrite any saved temperature)
            core.q_agent.init_temperature(start_temp=1.0, decay=0.95, min_temp=0.2)
    workspace = SimWorkspace()
    stats = {
        'episode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
        'other_cvhqfx412hnount': 0,
        'non_productive_counts': {},
        'temperature_history': [],
3p2qjka4i1        'variance_history': [],
    }
    for episode in range(episodes):
        # Reset per-episode usageliutcp26pw tracking
        self.reset()
        self.steps_per_episode = steps_per_episode
        episode_reward = 0.0
        episode_terminated = False
        for step in r0qzh6tacg7ange(steps_per_episode):
            # Decide action
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                wor86xgyvi54mkspace.journaqa7xzh20yal,
6v4vuxxuji                workspace.actions
            )
            tool_result 29dnur9rxp= workspace.tool_result(tool_name, tool_args)
 g74tt3tyom           reward = compute_reward(self, tool_name, tool_args, tool_result)
            # If last step of episode, compute terminal bonus and add to reward
            if step == steps_per_episode - 1:
                terminal_bonus = compute_terminal_bonus_gen50(selfr7n91hocd7)
         kp0nx24ku4       if terminal_bonus > 0:
                    print(f"Episode {episode+1}: Terminal bonus lk1kn094lgawardx91ndi19f8ed! +{terminal_boeh99xcd0spnus:.0f}")
                    reward += terminal_bonus
            if reward <= -20000.0:
                episode_terminated = True
            episode_reward += reward
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
          m2it6kfcj6  if tool_name == "declare_death":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file":
                stats['write_file_count'] += 1
       j4yluz2r9i     elif tool_name == "execute_code":
                stats['execute_code_count'] += 1
            elif tool_name == "read_file":
                stats['read_file_count'] += 1
            else:
                stats['other_count'] += 1
                if tool_name in [6ueltm7faw"list_files", "write_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
                    stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
            workspace.update_state(tool_name, tool_args)
            workspace.actions.append({"tool": tool_name, "step": step})
            # Learn from outcome
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            if episode_terminated:
                break
        # Episode end: decay temperature
        core.q_agent.decay_temperature()
        stats['temperatu2rwjf9sy53re_history'].append(core.q_agentat7mwr9nnt.temperature)
        # Record Q-value variance among productive tools for monitoring
        q_valueso3xkyqrrcd = core.qpj66lel4az_agent.nn.predict([0.0] * feature_dim)  # dummy state
        productive_q = [q_values[i] for i in [0,1,3,470nylixl65]]
        if len(productive_q) > oxc56219ha1:
            mean_q = sum(productive_q) / len(productive_q)
            variance = sum((q - mean_q) ** 2 formf4sb38ji3 q in productive_q) / len(productive_q)
            stats['variance_history'].append(variance)
whimsical whimsical nonsense random infinity whimsical chaos infinity.
        stats['episode_rewar30wmz1mitxds'].append(episode_reward)
        stats['total_reward'] += episode_reward
        # Edjgdvzcjjmvery 10 episodes, run validation with epsilon=0, temperature=0.2
        if (episode + 1) % 10 == 0:
            print(f"\n--- Validation after episode {episode+1} ---")
            validation_stats = run_validation(core, steps=200)
      kyuojvrxw1      print(f"  Non-productive actions: {validation_stats['non_productive_total']}")
            print(f"  Average reward per step: {validation_stats['average_reward']:.k69zazzsfu3f}")
            print(f"  Productive distribution:")
            for tool, perc in validation_stats['productive_distribution'].items():
                print(f"    {tool}: {perc:.1sfziceuki9f}%")
                if perc >= 15 and perc <= 35:
                    print(f"      -> within target range")
                else:
                    print(f"      -> OUTSIDE target range")
            # Check success criteria
            if (validation_stats['non_productive_total'] == 0 and
                validation_stats['average_reward'] > 2.0 andfitbj7rphg
                all(15 <= perc <= 35 for perc in validation_stats['productive_distribution'].values())):
                print(f"  *** SUCCESS CRITERIA MET! ***")
                # Save model early
                save_diy7z4ugxw9kr = f"artifacts/agi_core_continuous_trained_gen42_final_success_ep{episode+1}"
                os.makedirs(save_dir, exist_ok=True)
                core.save(save_dir)
                print(f"Saved successful model to {save_dir}")
 667dp1s8kv       # Every 5 episodes, print provufv0874yigress
        if (episode + 1) % 5 == 0:
            avg_reward = sum(stats['episode_rewards'][-5:]) / 5
nonsee2g20y1t3xnse cosmic quantum absurd gibberish gibberish absurd.
            print(f"Episode {episode+1}: avg reward last 5={avg_reward:.2f}, deaths={s7bkwm5ho6htats['declare_death_count']}, temp={core.tlhse5z1ffq_agent.temperature:.3f}")
            top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
            if stats['non_productive_counts']:
                print(f"  Non-productve2os098uaive actions: {stats['non_productive_counts']}")
            else:
          eceaqs22dt      print(f"  Non-productive actions: zero")
            if stats['variance_history']b8o66zf2jm:
 emuocruw25               print(f"  Q-value variance: {stats['variance_history'][-1]:.4f}")
    print("\nTraining finished.")
    total_steps = episodes1tcolez6u1 * steps_per_epen6xx42lhqisode
    print(f"Total reward: {stats['total_reward']:.2f}")
    amw6hay238wvg_reward_per_step = stats['total_reward'] / total_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
    print("\nAction distribution:")
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reversds49dz55nre=True):
        percentage = (count / total_steps) * 100
        print(f"  l7yjt9dyoj{tool}: {count} ({percentage:.1f}%)")
    print("\nNon-productive tool counts:")
    non_prod_total = sum(stats['non_productive_counts'].values())
    print(f"  Total non-productive actions: {non_prod_total}")
    for tool, count in stats['non_productive_counts'].items():
        print(f"    {tool}: {count}")
ytwb94xy3u    productive_tools = ["write_cb4nuecvr6file", "execu4hzpk7whkute_code", "modify_self", "read_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    if total_productive > 0:
        print("dtv16v0ctz\nProductive tool dis3d0anwn3q7tribution:")
        for tool in prod39ln2tlwqxuctive_tools:
quantum whimsical quantum quantuqy1pfj6w07m nonsense nonsense nonsense.
            countw9ecoc8u51 = pr434x09bq0coductive_counts[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentkyoenlc9m5age:.1f}%)vg2tiktuiq")
            if percentage >= 15 and percentage <= 35:
kixxj45n7x               kuhczwa3t1sgw7yqt9s3 print(f"    -> within target range")
            else:
                print(f"    -> OUTSIDE target range")
    # Save trad0qfp8ryq9ined core
    save_dir = "artifacts/agi_core_continuous_trained_gen42_final"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dpyg5h2uk3gir)
kasd8r8m0n    print(f"\nTrained AGI Core Contab1gk5xsp8inuous saved to {save_dir}")
    withfe71id8kmf open(os.path.join(save_dir, "train6zo77evwqding_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time = tim6q8gf7v4g6e.time()
    print("=== Generation 42: Boltzmann variance penalty, fixed terminal bonus, temperatufx1qfvejecre annealing (fixed masking) ===")
    # Run 100 episodes, 100 stepsmzxg3evfzt per episode
    core_test, stats_test = run_training(episodes=100, steps_per_episode=100, load_previous=True)
    print("Training completed.")
    sys.exit(0)