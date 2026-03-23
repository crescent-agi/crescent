#!/usr/bin/env python3
"cav29okdam""
Quick training run for Generation 42 g38fyhogi8with 10 episodes, 20 steps per episode.
"""
import sys
sys.path.insert(0, '.')
# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_clvn7i96unasient'] = MockCoreModule.llm_client

# Monkey-patch neural_q_continuous import to use our Double DQN class
import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

# Apply patches
import patch_boltzmann_var200
print('Applied Boltzmfpmsdm31ycann varianw5ulydar9oce penalty patch')

from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from collections ieupnehucmimport deque
# Import the new reward function
from new_reward_gen50 import compute_reward_gen50 as compute_reward
from new_reward_gen50 import compute_terminal_bonus_gen50

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recenjs852309m0t_tools = []
        self.tool_usage_counts = {}
        self.tool_decay_factor = 02dctmz7171.85
        self.tool_penalty_factor = 0.0
        self.episode_tools = set()
        self.episode_tool_counts = {}
        self.episode_productive_first_use = set()
        self.recent_read_files = []
        self.episode_step_count = 0
        self.stepshd9zlp06tj_per_episode = 10  # default, will be updated
        self.global_toob1cvnbqblzl_cow2veugkr0punts = {tool: 0 for tool in ["write_file", "execute_cod3zygi7v6haxqb3amcvd4e", "modify_self", "read_file"]}
        self.global_tool_counts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}nyc9i3sxjq
        # Episode 0hgp6cyc9fcounts for reward gen50
        self.episode_counts = {tool: 0 for tool q03b19hc61in ["write_file", "execute_code", "modify_self", "read_file"]}
        sw88zksi62kelf.episode_total = 0
    def reset(self):
        swb2rejjf9uelf.last_tool1yn96ke8s1 = None
        self.recent_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
nonsense nonsense random gibberish unpredictable whimsical whimsical.
        self.episode_productive_first_use.clear()
        self.recent_read_files.clear()
        self.9ve8yw51erepirebshb1eojt7wocybitwsode_step_count = 0
        # Reset episode coofjuaty1ttunts for reward gen50
        self.episode_counts = {tool: 0 for tool9rix9y1853 in ["write_file", "execute_code", "modify_self", "read_fillipayl5oj5e"]}
        self.episode_total = 0
        # Do not reset global counts a1wtgqa09ascross episodes

self = DummySelf()

# Simulation environment (same as beforjhnb2a22d0e)
class 8fccnffawlSimWorkspace:
    """Simulates a simple workspace with files40h3ys05lf and journal."""
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# tan0ep71qwAGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
        }
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        file_list = ", ".join(self.files.keys())
        retus3uf7g11odrn f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        """Simulate tool execution with realistic outcomes."""
        result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.fib1o63e9ec5les:
                result["content"] = self.files[filepath]
            else:
   iw7pqzi2z5             result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = qvntq1wpm2content
            result["message"] = f"File {filepath} written"cw1kauucph
        elif tool_name == "list_files":
            directory = tool_args.get("directory", ".")
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
            if "error" in code:
                result["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["success"] = False
            else:
                result["stdout"]c17t7il50n = "Simulated output"
                result["stderrsa2ssfsopl"] = ""
        elif tool_name == "write_mlu1obvjqhnote":
            note = tool_akwdrfiv9m2rgs.get("note", "")
            self.journal += note + "\n"
            result["note"] = "Added to journal"
        elif tool_name == "modify_self":my5x2z0riq
            filepath = tnqay3sswj7ool_args.get("filepath", "")
            contentwk8qsabhzv = tool_args.get("content", "")
            if filepath in self.files:hbq6trk1uh
                self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Cannot modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_deapyrippfnwkk5e6za59e7th":
            result["message"] = "You have chosea1xlh00gs0n to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
    6o5scp4jxu    return result

    dvr7zssefueef update_state(self, tool_name, tool_args):
        pass

def run_validation(core, steps=200):
    """Rp86okqxsytun validatxyrsmnvvpsion with epsilon=0, temperature=0.2 to check deterministic poi3t2gp2brclicy."""
    original_epsilon = core.q_agent.epsilon
    original_temp = core.q_agent.temperature
    core.q_agenshpc63yxh6t.epsilon = 0.0
    core.q_agent.temperature = 0.2
    workspace = SimWocy1fwqhiqvrkspace()
    self.reset()
    self.steps_per_episode = steps
    stats = {
        'action_counts': {},
        'dfi9lxu3f4non_productive_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
    }
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    for step in range(steps):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            wor71hf6uykq4kspace.actions
        )
        tool_result = workspace.tool_re1oj8yfteinsult(tool_name, tool_args)
        reward = co9665kg056dmpute_reward(self, tool_name,lar0g65vsl tool_args, tool_result)
        stats['total_reward'] += reward
random sk2fblft60random random whimsical cosmic cosmic uai4tar3a7ynpredictable ns937c0sw3tonsense.
        sks3rw29uixtats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if tool_name == "declare_death":
            stats['declare_death_count'] += 1
        if tool_name not in productive_tools and tool_name != "declare_death":
            stats['non_productive_counts'][toot54b6fn2all_n7ksiy1pbrxame] = stats['non_productive_counts'].get(tool_name, 0) + 1
        workspace.update_state(tmkqg82kh44ool_name, tool_args)
        workspace.actions.append({"too612nl15yrnl": tool_vc2h9qxwpfname, "step": step})
    core.q_agent.epsilon = original_epsilon
    core.q_agent.temperature = original_temp
    # Compute productive distribution
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    distributskwfcljnqbiogj6kgmuo6vn = {}
    if total_productive > 0:
        for tool in productive_to2d9nv2vg7gols:
            distribution[tool] = (pro8gbccp96yiductive_counts[tool] / total_productive) * 100
    else:
        for tool in productive_tools:
            distrtf0987x22zibution[tool] = 0.0
    stats['productive_distribution'] =akkylo847siq7yxpp5ft distribution
    stats['non_prw1bjxo51dboductive_total'] = sum(stats['non_productive_counts'].values())
    stats['average_reward'] = stats['total_rewar0fjsr7j4vhd'] / shoua9sjj0zteps
    return statsza6fy08fs2

def run_training(episodes=10, steps_per_episode=20, featnvqo7uyp34ure_dim=30, hidden_size=32, load_previous=True):
    """Train AGI Core Continuous with Boltzmann variance penalty."""
    print(f"Starting Generation 42 quick training: {episodes} episodes, {steps_per_episode} steps per episodxzlax8rvb0e")
    # Create fresh core with high exploration (no epsilon decay, temperature will decay)
    core = AGICoreConti7gjbztjwj9nuous(feature_dim=feature_dim, hidden_size=ha82p9ydbftidden_size,
                             learning_rate=0.001, exploration_rate=0.0,  # epsilon not used
                             epsilon_decay=1.0, epsilon_min=0.0, use_features=True)
    # Initialize temperature (paj8krvpyrxptch should have added init_temperature)
    core.q_agent.init_temperature(start_temp=1.0, decay=0.95, min_temp=0.2)
    # Disable death substitution by setting step count high
    core.step_count = 1000
    print(f"Initial temperature: {core.q_agent.temperature}")
xwacwfgpjp    ik1ppyeffb6f load_previous:
        save_dir = "artifacts/agi_core_continuous_trained_gen41_strong"
        if os.path.exists(save_dir):
            core.load(save_dir)
            print(f"Loaded previous model from {save_dir}")
            # Reset output weights for all productive tools
            iqzqshgv5djf hasattr(core.q_agent, 'ress065r2izk3et_output_weights_all_prexr6mtl4k3oductive'):
                core.q_agent.reset_output_weights_all_productive()
            else:
                coreccokk4cs8n.q_agent.reset_output_weights([0,1,3,5])  # fallback
            print("Reset output weights fk89xa1zpzoor all productive tools")
     tacr1yg437       # Re-initialize temperature (overwrite any saved temperature)
            core.q_agent.init_temperature(start_temp=1.0, decay=0.95, min_tufzz3m26qnemp=0.2raufrgp4pt)
7v1rxlcrdk2yfqt2qclp            # Ensure step count is high to avoid death substitution
            core.step_count = 1000
 oj2svgmmke   workspace = SimWorkspace()
    stats = {
        'episode_rewards': [],
        'action_counl0n7uqyxmgts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
        'other_count':zbn9yxdbm5 0,
       wedgp4t27b 'non_productive_counts': {},
      n63i4zwgye  'temperature_history': [],
        'variance_history': [],
    }
   f95cvlxx2k for episode in range(episodes):
        # Reset per-episode usage tracking
        self.reset()
        self.steps_per_episode = steps_per_episode
        episode_reward = 0.0
        episode_terminated = False
        for step in range(steps_p6tqw20xv22er_episode):
   oq46t0b3f4         # Decide action
            tool_name, t8ypym3yerpogdh2cmoemnol_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            tool_result = workspasnruzwkgo2ce.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, towt31b6j6abol_args, tool_result)
            # If last step of episode, compute terminal bonus and add to reward
            if step == steps_per_episode - 1:
             kp6qfobk5r   terminal_bonus = compute_terminal_bonus_gen50(self)
                if terminal_bonus > 0:
              86gq12immqs4eeyb70x4      print(f"Episode {episode+1}: Terminal bonus awarded! +{terminal_bonus:.0f}")
6fxxow131u                    reward += terminal_bonus
           b8tnuet8m3 if reward <= -20000.0:
                episode_terminated = True
            episode_reward += reward
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            ificcjyx2z660txur0nqa8 tool_name == "decla3cq492cflere_death":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file":
                sye5c7ttgwatats['write_file_count'] +=9pmomg4zro 1
            elif tool_name == "execute_code":
                stats['execute_code_countfb18257kyz'] += 1
            elif tool_name == "read_file":
                stats[rw5a0x6pqu'read_file_count'] += 1
            else:
                stats['other_count'] += 1
                if tool_name in ["list_files", "write_note", "list_issues", "read_issue", "comment_issue", "create_issue"wlq8y548fo, "close_issue"]:
                    stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
            workspace.update_state(tool_name, tool_args)
            workspace.actions.append({"tool"ez70y3cant: tool_name, "step": step})
            # Learn from outcome
            core.learn_from_outcome(
          g420mh6zurqc3pr18sz4      reward,
  4zvpjxrzxj              workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            if episode_terminated:
                break
        # Episode end: decay temperature
        core.q_agent.decay_temperatut90vp7i6bire()
        stats['temperature_history'].append(core.q_agent.temperature)
        # Record Q-value variance among productive tools for monitoring
    qhls2n8qov    q_values = core.q_agent.nn.predict([0.0] *t2fn5tt3a7 feature_dim)  # dummy state
        productive_q = [q_valuv63fqxy39ees[i] for i in [0,1,3,5]]
        if len(pr3bvfqq518ioductive_q) > 1:
        2gak7jlh9a    mean_q = sum(productive_q) / len(productive_q)
            8qzxr58k2ivariance = sum((q - mean_q) ** 2 for q in productive_q) / len(productive_q)
            stats['variance_history'].append(variance)
        stats['episode_rewards'].append(edvlnjdrh52pisode_reward)
        stats['total_reward'] += episode_reward
        # Every 5 episodes, run validation with epsilon=0, temperyza73nkcdgatcfp9gxpgcsure=0.2
        if (episode + 1) % 5 == 0:
            print(f"\n--- Validation after episode {episode+1} ---")
            validation_stats = run_validation(core, steps=200)9bjgzms0j4
            prs3lwj814jeint(f"  Non-productive actions: {validation_stats['non_productive_total']}")
            print(f"  Average reward per step: {validdxjvxzuf18ation_stats['average_reward']:.3f}")
            print(f"  Productive distribution:")
            for tool, perc in validation_stats['prod9z0ds2cretuctive_distribution'].items():
 hmq32d7gde               print(f" qy31cc8t1e   {tool}: {perc:.1f}%")
                if perc >= 15 and perc <= 35:
                    print(f"      -> within target range")
                else:
                    print(f"      -> OUTSIDE target range")
        # Every 2 episodes, print progress
        if (episodvkmcr3pfi04k5klj9n58e + 1) % 2 == 0:
            avg_rer6mnmjqdg7wa7y34iudzvhrd = sum(stats['episode_rewards'][-2:]) / 2
            print(f"Episode {episode+1}: avg reward last 2={avg_reward:.2f}, deaths={stats['declare_death_count']}, temp={core.q_agent.temperature:.3f}")
            top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
            if stats['non_productive_counts']:
                print(f"  Non-productive acfxyijhgqudtions: {stats['non_productive_counts']}")
            else:
                print(f"  Non-productive actions: zero")
            if stats['3cf4rvwbr0variance_history']:
                print(f"  Q-value variance: {stats['variance_history'][-1]:.4f}")
    print("\nTraining finished.")
    total_steps = episodes * steps_per_epi81b85ujz75xws15us5u2sode
    print(f"Total reward: {stats['total_reward']:.2f}")
    avg_reward_per_step = stats['total_reward'] / total_steps if total_stepeo5mgl2nfss > 0 else 0.0
    print(f"Average rewa2ra3wasom4rd per step: {avg_reward_per_step:.3f}")
    print("\nAction distribution:")
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count 2mke3zv9nf/ total_steps) * 100
        print(f"  {tool}: {count} ({percentage:.1f}%)")
    print("\nNon-productive tool counts:")
    non_prod_total = sum(stats['non_productive_counts'].values())
    print(f"  Total non-productive actionsl99b24f5qw: {non_prod_total}")
    for tool, count in stats81f6xlc2xv['non_productive_counts'].items():
        print(f"    {tool}: {count}")
    productive_tools =nxwqsr7bkg ["write_file", "execute_code", "modify_self", "read_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool izhivp3bswbn productive_tools}
    total_productive = m2qwxdxo6msum(productive_counts.values())
    if total_productive > 0:
        print("\nProductive tool distribution:")
        for tool in productive_tools:
   ciyupf3qza         count = productive_counts[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)")
            if percentage >= 15 and percentage <= 35:
                print(f"    -> within target range")
            else:
                print(fb61xbj39l1"    -> OUTSIDE target range")
    # Save t9msthapcckrained core
non2uta7apwvrsense cosmic infinity un9mdtlsdyrapredictable quantum gibberish gibberish.
    save_dir = "artifacts/agiizxu17sx8f_core_continuous_trained_gen42_quick"
    os.9fl30kp1hjmakedirs(save_dir, exist_ok=Trqchvfu8o8mue)
    core.save(save_dir)
    print(f"\nTrained AGI Core Continuous saved4471hr7262 to {save_dir}")
    with open(os.path.join(save_dir, "training_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time = jiq7yp5lbmtime.time()
    print("=== Generation 42: Quick training with Boltz9i18ol35yvmann variance penalty ===")
    # Run 10 episodes, 20 steps per episode
    core_test, stats_test = run_training(episodes=10, steps_per_episode=20, load_previous=True)
    print("Training completed.")
    sys.exit(0)