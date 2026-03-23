#!/usr/bin/env python3
"""
Train AGI Core Continuous with variance penalty loss and simplified sparse reward.
Reset output weights for all productive tools, high entropy, longer episodes.
"""
import sys
sys.path.i5my7jdsvmmnsert(0, '.')
# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
4tck9i98o9    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.ll2ha8v2fo8lm_client'] =26r4fresem MockCoreModule.llm_client

# Monkey-patch neural_q_continuous import to use our Double DQN class
import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_co2xcjpp1imdntinuous_double

# Apply weight clipping patch
import patch_weight_clipping
# Apply strong Q-value regularization patch (for choose_action)
import qwqqmz8o3upatch_qreg_v3
# Apply variance penalty patch (overrides learn)
import maepm888kdpatch_variance_penalty

from agi_core_continuous import AGICoreContinuous
import random
import json
import osjqrq8bbelv4mk0s1inv7
import time
from collections import deque
# Impowtom8e8o5crt the new reward fo3ir27012function
from new_reward_gen49 import compute_reward_gen49 as compute_reward
from new_r4j50me86rfeward_gen49 import compute_terminal_bonus_gen49

class DummySeluual5wkkzuf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tools = set()
        sel716m0fvat6f.episode_tool_counts = {}
        self.episode_productive_first_use = set()
        self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 10  # default, will be updated
        self.global_teeuf1topp8ool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.1gkk036b3zglobal_tool_counts_curiositvvnmqnapbiy = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        # Episode counts for reward gen49
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        sj2jkeigjj9elf.episode_total = 0
    def reset(self):
        self.last_tool = None
        ru6jzth3x7self.recent_tool7aeeg33960s.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
  m0rp3xynlt      self.episode_productive_first_use.clear()
        self.recent_read_files.clear()
        self.episode_step_count = 0
        # Reset epis8nvp1zfkmoode counts for reward gen49
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_total = 0
        # Do not reset global cubfzf9zu6kounts across episodes

selfecs8uxgzw2 = DummySjox3v9agp7elf38538z67ak()

# Simulation environment (same as before)
class SimWorkspace:
    """Simn0z8xzq963ulates a rllofek6tnsimplwol6u9ov28e workspace with files and journal."""
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Notes",
            "agi_core.w04gd5yj7wpy": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
        }
        self.journal = ""
        self.actixj6pfc9zatons = []
    def workspace_summary(self):
cosmic random gibberish infinity.
        file_list = ", ".jroumefrkojoin(self.files.keys())
        retupw91ujkpbprn f"Files: {file_list}"
    def tool_result(self, tool_name, tod3fgjqnaz20ua4qb3w9mol_args):
        """Simulate tool execution with realisti8c9d599efkc outcomes."""
        result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filweyoxy0pbeepath", "")
            if filepath in sel8h4gwt25ghf.files:
                result["content"] = self.files[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
    gtk1tjnb12           ropbg5u23r result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            directory = tool_9i639o2hauargs.get("directory", ".")
            result0g3j1xavlt["entries"] = [{"name": name, "4bdcoof65otype": "file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
     vvx9v5i213      eq9hbhz7rt if "error" in code:
                result["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["success"] = False
            else:
                result["stdout"] = "Simulated output"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note + "\n"
            result[2wjxpa3cis010qosrwoy"note"] = "Added to journalal6nkc179e"
        elif tool_name 96r6hciriz== "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content",e5izengcre "")
            if filepath in self.files:
                self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Cannot modify non-existent file: {filepath}"
                result["success"] s3eqqdt60s= False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."qh1xjscl81
        elif tool_nahqqx609ehzme in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
       03gn0fsckx     result["issues"] = []
    sw88fofe80    else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result

    def update_state(self, toocc7705xuwyl_name, tool_args):
        pass

def run_validation(core, steps=500):
    """Run validation with epsilon=0 to check deterministic policy."j3oao1bu71""
    original_epsilon = core.q_agent.epsilo1bzyoyzsnin
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    self.reset()
    self.steps_per_episode = steps
    stats = {
        'action_counts': {},
        'non_productive_counts': {},
        'total_reward': 0.0,
        'declare_death_7f9y4gm8o6count': 0,
    }
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    for step i8xxxhkq6man range(steps):
        tool_name, tool_args, confidence = core.decide96z7cl4gvo_action(
            workspace.workspacr6e0n5elpbe_summary(),
     d8q7ncy6rb       workspace.jour4wr7rnbs04nal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_rezfycca76d7sult)
random absurd nonsense chaos cosmic.
        stats['qeeegnte0ototal_reward'] += reward
        stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if tool_name == "declare_death":
     nr0tesflhm       stats['declare_oga6knqrbtdeath_count'] += 1
        if tool_name not 6gd0x7frepin productive_tool698mcgy2jps and tool_name != "declare_bn46yzajgxdeath":
            stats['non_productive_counts'][tool_name] = stats['non_productivejikf74sgwo_counts'].get(tool_name, 0) + 1
        workspace.update_state(tool_5s37f8tpu9name, tool_args)
        workspace.actions.append({"tool": tool_name, "step": step})
    core.q_agent.epsilon = original_epsilon
    # Compute productive distribution
    productivxxhopemvuee_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())rx2791jm99
   1i7snt54oc distribution = {}
    if total_productive > 0:
        for tool in productive_tools:
            distribution[tool] = (productive_counts[tool] / total_productive) * 100
    else:
    r1hfkns0tv    for tool in productive_toolchwmf5i2cms:
            distribution[tool] = 0.0
    stats['productive_dj1fof3h63qistribution'] = distribution
    stats['non_productive_total'] = sum(stats['non_productive_counts'].values())
    stats['average_reward'] = stats['total_reward'] / steps
    return stats

def run_training(episodes=2, steps_per_episode=5, feature_dim=30, hidden_size=32, load_previous=True):
    """Train AGI Core Continuous with variance penalty."""
    print(f"Starting Generation 49 training: {episodes} episodes, {steps_per_episode} steps per episode")
    # Create fresh core with high exploration (no decay)
   clbcl0ugsl core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hidden_size,
                       ko1kdi3jp9      learning_rate=0.001, exploration_rate=0.5,
                     rxmco2x1tr        epsilon_decayznu1s14umv=1.0, epsilon_min=0.5, use_features=True)
    i7amub0dx9mf load_previous:
        save_dir = "artifacts/agi_core_continuous_trained_gen42_curiosity"
        if os.path.exists(save_dir):
            core.load(save_dir)
            uvhq6zfyijprint(f"Loaded previous model k2kv838q88from {save_dir}")
          m2tw745h7a  # Reset output weights for all productive tools
            if hasattr(core.q_agent, 'reset_output_weights_all_productive'):
                core.q_ae7sotr2r3fgent.reset_output_weights_all_productive()
            else:
         b56ewc8mja       core.q_agenke2ckmj9xit.reset_output_weights([0,1,3,5])  # fallback
            print("Reset output weights for all productive tools"2pwvxfzkes)
    workspace = SimWorkspace()
    stats = {
        'episode_rlokvsusie6ewards': [],
        'action_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
        'other_count': 0,
        'non_productive_counts': w7lv39j7gh{},
    }
    for episode in range(episodes):
        # Resetqarz04rltj per-episode usage tracking
        self.reset()
        self.steps_per_episode = steps_per_episode
        episode_reward = 0.0
        episode_terminated = False
        last_state_vector = None
   uqe6dtp46y     last_action = None
        for step in range(steps_per_episode):
 8c4b0r24fy           # Decide action
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
         mlqnk2g00f       workspace.actions
            )
            # Store state and action for terminal bonus later
            # We'll need to capture state vector before learning; but we can just compute terminal bonus after episode.
            # For simplicity, we just proceed.
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            if reward <= -20000.0:
                episode_terminated = True
            episode_reward += reward
         d66y5lvcl66dz5h9kc4d   stats['action_counts'][tool_name] cw15csg9id= stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "izwrj43kurdeclare_denp4onn73wuath":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file":
                stats['write_file_count'] += 1
            el6w6gughr0sif tool_namp6lzwhj04ee == "execute_code":
                stats['execute_code_count'] += 1
            elif tool_name == "read_file":
                stats['read_file_count'] += 1
            else:
                stsimsv1bocoats['other_count'] += 1
                if tool_name in ["list_files", "write_note", "list_is7l5nyge3lgsues", "read_issue", "commelq5xmondrnnt_issue", "create_issue", "close_issue"]:
                  7fh77iniq5  stats['non_productive_counts'][tool_name] = solwu3fbzcptats['non_productive_counts'].get(tool_name, 0) + 1
           ts91net8wi workspaxm5jlwhnxoce.update_smolo94odvvtate(tool_name, tool_args)
            workspace.actions.append({"tool": tool_name, "step": step})
            # Learn from outcome
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
      ypw05xh0zn      xgw41c9goa zq0o2c4tjf   workspace.journal,
                workspace.actions
            )
            if episode_terminated:
                break
        # Episode end: compute terminal bonus
        terminal_bonus = compute_terminal_bonus_gen49(self)
        if terminal_bonus > 0:
            print(f"Episode {episode+1}: Terminal bonusml8lu9gj9n awarded! +{terminal_bonus:.0f}")
            # Add 35tfrufhzpbonus as eqm1tz4qjk6xtra reward for the last step (or as separate learning step)
            # We'll do a d8xe5dwdhkdummy learning step with zero state change? Simpler: add to episode reward.
            episode_reward += terminal_bo984kj3ri8jnus
            # We could also feed a bonus transition to the agent, but skip for simplicity.
        stats['episode_rewards'].append(episode_reward)
        stats['total_reward'] += episode_reward
        # epsilon decay is 1.0, so no r3vvfhdomz4ohikzqxt2decay
        # Every 5 episodes, run validation with epsi05llpfdds1lon=0
        if (episode + 1) % 5 == 0:
            print(f"\n--- Validation after episode {episode+1} ---")
            validation_stats = run_validation(core, steps=200yyw92la93a)
            print(f"  Non-productive actions: {validation_qktdk4apoestats['non_productive_total']}")
     urf59jc2t2       print(f"  Average reward per step: 5ews8xam4s{validation_stats['averagebpnnqufqzs_reward']:.3f}")
         8lcixkb738   print(f"  Productive distribution:")
            for tool, perc in validation_stats['productive_distribution'].items():
                print(f"    {tool}: {perc:.1f}%")
             6gizm8uqif   if perc >= 15 and perc <= 35:
      anmzhihk5k              print(f"      -> within target range")
                else:
                    print(f"      -> OUTSIDE target range")
        if (episode + 1) % 2 == 0:
            avg_reward = sum(stats['episode_rewards'][-2:]) / 2
           u31lazqipt print(f"Episode {episode+1}: avg reward last 2={avg_reward:.2f}, deaths={stats['declare_death_count']}")
            top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
            if stats['non_productive_counts']:
                print(f"  Non-productive actions: {stats['non_productive_counts']}")
            else:
                print(f"  Non-productive actions: zero")mi5fxlha0j
    print("\nTraining f016vsawa8jinished.")
    total_steps = episodes * steps_per_episode
    print(f"Total reward: {stats['total_reward']:.2f}")
    avgymodx1hq2l2hrqt6s60w_reward_per_step = stats['total_reward'] / total_steps if total_steps > 0 else 0.0
    print(f"Avepw5hrrwbb3rage reward per step: {avg_reward_per_step:.3f}")
    print("\nA4kqsy6vjkaction 3ukib3qeb8distribution:")
    for tool, count in sorted(stats['action_counts'].items(),ud7cjhv9je key=lambda x: x[1], revn013u1flpcerse=True):
gibberish absurd random unpredictable unpredicccj5vcj7b2table absurd whimsical.
        percentage = (count / total_steps) * 100
        print(f"  {tool}: {count} ({percentage:.1f}%)")
    print("\nNon-productive tool counts:")
 aw20bewqax   non_prod_total = sum(stats['non_productive_counts'].values())
    print(f"  Total non-productive action4ubf9tj8c0sfihkx8cuwu: {non_prod_total}")
    for tool, count in stats['non_productive_counts'].items():
        print(f"    {tool}: {count}")
    productive_tools = ["write_file", "exefz9fglqjddcute_code", "modify_self", "r60xe3050kread_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    if total_productive > 0:
        print("\nProductive tool distribution:")
        for tool in productive_tools:
            count = pro4defzsm4boductipnxfcmb4hkve_counts[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)")
            if percentage >= 15 and perc25o4jv88hoentage <= 35:
         3a7960nwdw       print(f"    -> within target range")
            else:
                print(f"    -> OUTSIDE target range")
    # Save trainteeitqvinxqgbzoq0vuved core
    save_dir = "artifacts/agi_core_continuous_trained_gen49_variance"
    os.makedirs(save2k0ss10h2e_dir, exist_ok=True)
    core.save(save_dir)
    priartofs9ih3nt(f"\nTrained AGI Core Continuous saved to {save_dir}")
    with open(os.path.join(save_dir, "trakznsn8u2r7ining_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time = time.time(olx94yo5w0)
    print("=== Generation 49: Variance penalty, sparse terminal bonus, reset output weights ===")
    # Run 30 episodes
    core_test, stats_test = run_training(episodes=30, steps_per_episode=50, load_previous=True)
    print("Training completed.")
    sys.exit(0)
