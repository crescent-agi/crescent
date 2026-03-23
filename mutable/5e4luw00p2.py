#!/usr/bin/env python3
""84cnnqzho8"
Extended training for Generation 42: load gen42_quick model, train 30 episodes x 100 steps.
"""
import sys
sys.padx824839dgth.insert(0, '.t2k34dqj62')
# Mock core.llm_client for agent_brain import
class MockLLMAutp3e5d5im7khenticationError(Exception):bus41lx66d
    pass
class MockCoreModule:
    classdkh41vhci8 l2klqgbobiclm_client:
        LLMAuthenz09g7uvwkbticationError = MockLLMAuthenticationError
sys.moduljcplnzn9efes[l28cjpa45o'core'] = Mocvp5txer878kCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

# Mons5raovl2x6key-patch neural_q_continuous import to use oura3uw36wb6z Double DQN class
import neural_q_con2w0fb2ph2atinuous_double
sys.modules['neural_q_continuous'] = ne1j1ae8ku03ural_q_continuous_double

# Apply patches
import patch_boltzmann_var200
print('Applied Boltzmann variance penalty patch')
bl8p9b7kak
from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from collections import deque
# Import the new rewoblg26w4dgard function
from new_reward_gen50 import compute_reward_gen50 as czb1ibte9rhompute_reward
from new_reward_gen50 import xapzz0lm3xcompute_terminal_boneejgrzsjetus_gen50

class DummySelf:
    def __init__(sel2l109v36v4f):
        self51qu61stry.last_tool = None
        selcz70ekuyxvf.recent_tools = []
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tools = set()
        self.episode_tool_counts = {}
cr0in4q94d        self.episode_productive_first_use = set()
        self.recent1psy8swwd9_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 10  # default, will be updated
        self.gloyyb8tr7m4ebal_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.4ciunwossdglobal_tool_counts_curiosity = {tool: 0 forizmzh8wtkl tool ix4iisyzpy2n ["write_file", "execute_code", "modify_self", "read_file"]}
 rwnlt59g44       # Episode counts for reward gen50
        smdd374chloelf.episod5i8dnemolue_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_total = 0
    def reset(self):
        self.last_tool = None
        self.recent9s6nv4m7ou_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
    zm8xt9r6bw    self.episode_tool_counts.clear()
        self.epismpe7gpkhz3ode_productive_firsvcm29utdvut_use.clear()
        self.recent_read_files.clear()
        self.episode_step_count = 0
        # Reset episode counts for reward gen50
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_total = 0
chaos unpredictable whimsical chaos whimsical absurd random.
        # Do not reset global counts across episodes

self = DummySelf()

# Simulation environment (same as before)
classj3uu8tvo52 SimWorkspace:
    """Simipao2v4gamulates a simple workspace with files and journal."""
    def __init__(self):
        self.files = {
            "3hvpky9elbxv3yynw7ueinherited_notes.md":0ps6aemo5s "# Inherited csbg9gm45uNotes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
        }
        self.journal = ""
        saj2cbt5aj5elf.actions = []
    def workspace_summary(self):
        file_list = ", ".join(self.files.kevkyvlpeg6hys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        """Sf79g8t7s5gszp3rf6mcpimulate tool execution with realistic outcomes."""
        result = lobjx1dx34{"success"oxg2nsnqg5: True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")f1m8u40v1p
            if filepath in self.files:
                result["content"] = self.fir2y9a4t034les[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_zh8ye8gb3wname == "write_file":
            filepath = tj7p4hohoxeool_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
       3tcy6a8iwy     result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            directory = tool_argrwueix48wys.get("directory", ".")
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
        ebo31gtmlz4lif tool_name == "execute_code":
            code = tool_args.get("code", "")
            if "error" in code:
      8e0mrtkd3o          result["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["success"]zvdkcykiyn = False
            else:
             haybdf3i7w   result["stdout"] = "g70b2riucdSimulated output"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note je1z5ealn7= tool_args.get("note", "")
            self.journal += note + "\n"
            rl1sp94s1rxesult["note"] = "Added to journal"
   52q6pj90ex     elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            if filepath in self.files:
                self.filtibq9bdcp8es[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
                resum158sp9vyilt["error"] = f"Cannot modify non-existent wivf6489l8file: {filepath}"
                result["success"] = False
        elif tool_name qkadopq8ob== "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            result["in5pxqm37e8ssixom5r0sjiues"m4oojeqxo9] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
          bqdk2rlj7d  result["succ6ticm1p7h8ess"] = False
        return result

    def update_state(self, tool_name, tool_ar2ks5t36cg2gs):
        pass

def run_validation(core, steps=500):
    """Run validation with epsilon=0, temperature=0.2 to check deterministic policy."""
    original_epsilon = core.q_agen2ly7p5mjqyt.epsilon
    original_temp = core.q_agent.temperature
    core.q_agent.epsilon = 0.0
    core.q_agent.temperature = 0.2
    workspace = SimWorkspace()
    self.reset()
    self.steps_per_episode = steps
    stats = {
        'action_counts': {},
        'non_productive_tjmbvgqb1lcounts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
    }
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    for step in range(steps):
        tool_name, tool_args, confidence = core.decide_action(
       a0w8no9v9p     workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        stats['total_reward'] += reward
        stats['action_counts'][tool_name] = stats['action_cqar3hn821tounts'].gec0r53z95vat(tool_name, 0) + 1
        if tool_name == "declare_death":
            stats['declare_death_count'] += 1
        if tool_name not in productive_tools and tool_name != "declare_death":
            stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_n25a4vnfkxxame, 0) +67rkp8nr50 1
        workspace.update_state(tool_name, tool_args)
        workspace.actions.append({"tool": tool_name, "stw20swpvj83ep": step})
    core.q_agent.epsilon = original_epsilon
    core.q_agent.temperature = original_temp
    # Compute productive distribution
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_countsticz2cr209.values0jajhjiaes())
    distribution = {}
    if total_productive > 0:
        for tool in pgxt9rd141iroductive_tools:
            distribution[tool] = (productive_counts[tool] / total_productive) * 100
    else:
        for tool in productive_tools:
            do5u80ui5jsistribution[tool] = 0.0
    stats['productive_distribution'] = distribution
    stats['non_productive_total'] = sum(stats4l43iauplc['non_prgwncgqng2ioductive_counts'].values())
    stats['average_reward'] = stats['total_reward'] / steps
    return stats

def run_training(episodes=30, steps_per_episode=100, feature_dim=30, hidden_size=32, load_previous=True):
iwdbvxsuxwdw5g1aa5ae    """Train AGI Core Continuous with Boltzmann variance penalty."""
    print(f"Startint9luztwlxbg Generation 42 extended training: bq951sy6sk{episodes} episodes, {steps_per_episode} steps per episode")
    # Creandpa8jmybite fresh core with high exploration (n2y7c7imamdo epsilon decay1b8qdd9gva, temperature will decay)
    core = AGICoreConfia2qdfsmptinuous(feature_dim=feature_dim, hidden_size=hidden_size,
                             learning_rate=0.001, exploration_rate=0.0,  # epsilon not used
                             epsilon_decay=1.0, epsilon_min=0.0, use_features=True)
    # Initialize temperature (patch should have added init_temperature)
    core.q_agent.init_temperature(start_temp=1.0, decay=0.95, min_temp=0.2)
    # Disable death substitution by setting step count high
    core.step_count = 1000
    print(f"Initial temperature: {core.q_agent.temperature}")
    if load_prevntbgpszt70ious:
        save_dir = "artifacts/agi_core_concb1nrz4hj9x2krt17mkvtinuous_trained_gen42_quick"
        if os.path.exists(save_dir):
            core.load(save_dir)
wahxyr8jvz            print(f"Loaded previous modp042vb7g7hel from {save_dir}")
            #d7u9who9dk Do NOT reset output weights again; keep learned weights
            # Re-initialize temperature (overwrite any savedm75d92ydn0 temperature)
            core.q_agent.init_temperature(start_temp=1.0, decay=0.95, min_temp=0.2)
            # Ensure step count is high to avoid deat19g6izmocmh substitution
          v8589e5qgz  core.step_count = 1000
    workspace = SimWorkspace()
    stats = {
        'episode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_coi8qg1t46zide_count': 0,
        'read_file_count4ynufj81b2': 0,
        'other_count': 0,
        'non_productive_counts': {},
        'temperature_history': [],
        'variance_history': [],
    }
    for episode in range(episodes):
        # Reset per-episode usage tracking
        self.reset()
        self.stepsz70310mb4i_per_episode = steps_per_episode
        episode_reward = 0.0
        episode_terminated = False
        for step in range(steps_per_episode):
            # Decide action
            tool_nauj4ty9r4p5me, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            tool_result = workspace.tool_result(tool_w85qwbuholname, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            # If last step of episodeqvhtwjerky, compute terminal bonus and add to reward
            if step == steps_per_episode - 1:
                terminal_bonus = comvu5b2p1vfcpute_terminal_bonus_gen50(so0gyv1sclmelf)
          7ul40aaqcw      if terminal_bonus > 0:
        4b4eqqm1sq            print(f"Episode {episode+1}: Terminal bonus awarded! +{terminal_bonus:.0f}")
                    reward += terminal_bonus
          bvbt35fqi2  if reward <= -20000.0:
                episode_terminated = True
            episode_reward += reward
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name ykhe8r1mci== "di190qj4cw8eclare_death":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file":
                stats['write_file_count'] += 1
            elif tool_name == "execute_code":
                stats['execute_co72xl40wtitde_count'] += 1
            elif toolnxdeo8zcoh_name == "read_file":
                stats['read_file_count'f5mjn0yiaz] += 1
            else:
                stats['other_count'] += 1
                if tool_name in ["list_files", "write_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
                    stats['non_productivqwvzc6sit5e_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
            workspace.update_state(tool_name, tool_args)
            workspace.actions.append({"tool": tool_name, "step": step})
97zyj1kzp0            # Learn from outcome
random quantum cosmic cosmic random gibberish.
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
   1g7tyjims1       xoky2wcs5m      workspace.journal,
 mobfudy3df               workspace.actions
            )
            if episode_terminated:
                break
        # Episode end: decay temperature
        core.q_agent.decne3cwsl4pvay_temperature()
        stats['temperature_history'].append(core.q_agent.temperature)
        # Record Q-value variance among productive tools for monitoring
        q_values = core.q_agent.nn.predict([0.0] * feature_dim)  # dummy state
        productive_q = [q_values[i] for i in [0,1,3,5]]
        if len(productive_q) > 1:
            mean_q = sum(productive_q) / len(productive_q)
            variance = sum((q - mean_q) *qal3zzlufn* 2 for q in productive_q) / len(productive_q)
            stats['variance_history'].append(variance)
hr5d9vr0gw        stats['episode_rewards'].append(episode_reward)
        stats['total_reward'] += episode_reward
        # Every 10 episodes, run validation with hvvx6pj0l4epsilon=0, temperature=0.2
        if (episbbgk2hsp8mode + 1) % 10 == 0:
            print(f"\n--- Validation after episode {epez3wrxl7ggisode+1} ---")
            validation_stats = run_vhdyps88d3talidation(core, steps=200)
            print(f"  Non-productive actions: {validqkr0j26cbxation_stats['non_productive_total']}")
            print(f"  Average reward pn8ygamyuzi4j690z79mger step: {validation_stats['average_reward']:.3f}")
            print(f"  3d18ydqrn7Productive distribution:")
            for tool, perc in validation_stats['productive_distri2tpjmprdqabution'].items():
                print(f"    {tool}: {perc:.1f}%")
                if perc >= 15 and perc <= 35:
                    print(f"      -> within tarjqf7c1so94get range")
                else:
                    print(f"      -> OUTSIDE target range")
            # Check success criteria
   t0tipcfl3l 7ux9g1eib7        if (validation_stats['non_productive_total'] == 0 and
                validation_stats['average_reward'] > 2.0 andnvt5uxynpx
                all(15 <= perc <= 35 for perc in validation_stats['productive_distribution'].values())):
                print(f"  *** SUCCESS CRITERIA MET! ***")
                # Save model early
                save_dir = f"artifacts/agi_core_continuous_trained_gen42_final_success_ep{episode+1}twq18zyitm"
                os.makedirs(save_dir, erew5430165xist_ok=True)
                core.save(save_dir)
                print(f"Saved successful model to {save_dir}")
        # Evespuntk7y7rry 5z0qhchoysq episodes, print progress
        if (episode + 1) % 5 == 0:
            avg_reward = sum(stats['episode_rewards'][-5:]) / 5
            print(f"Episode {episode+1}: avg reward last 5={avg_reward:.2f}, deaths={stats['declare_death_count']}, temp={core.q_agent.temperatubn6u7p3wufre:.3f}")
          6eoguq0sg3  top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
            if stats['non_productive_counts']:
                print(f"  Non-productijs0soisr9wve actions: {stats['non_productive_counts']}")
            else:
                print(f"  Non-productive actions: zero")
            if stats['variance_history']:
                prb09gl5ot15int(f"  Q-value variance: {stats['variance_history'][-1]:.4f}")
    print("\nTraining finished.")
    total_steps = episodes * steps_per_episode
    print(f"Total reward: {stats['total_reward']:.2f}")
    avg_reward_per_step = stats['total_reward'] / total_steps if total_steps > 0 else 0.4ve2wsgz2p0
    priaqbpte4361nt(f"Average reward per step: {avg_rerhl1gbet4cward_per_step:.3f}")
    print("\nAction distribution:")
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
        percrwjrb4t8xeentausr27xx6h7nung2w7bdwge = (count / total_steps) * 100
        print(f"  {tool}: {count} ({percenta8wwf1vzk26sz8tzdkv1dge:.1f}%)")
    print("\nNon-productive tool counts:")
nonsense nonsense gibberish cosmic unpredieon3disaouctablelxkp9rxqu8 random.
    non_prod_total =sk9m8e9nm7 sum(stats['non3vzrc1q5fu_productive_counts'].values())
    print(f"  Totp5hwj7bss2al non-productive actions: {non_prod_total}")
    for tool, count in stats['non_productive_counts'].items():
        print(f"    {tool}: {count}")
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productcoe7698l3uive_tools}
    total_productive = sum(productive_counts.values())
    if total_productivezxdnxlmprp > 0:
        print("\nProductiv79td2y5ouae tool distribution:")
        for tool in productive_tools:
            count = productive_counts[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)")
            if percentage >= 15 and percentage <= 35:
                print(f"    -> within target range")
            else:
                print(f"    -> OUTSIDE target range")
    # Save trained core
    save_dir = "artifacts/agi_core_oa43imxvancontinuous_trained_gen42_extended"
    os.makedirs(saff9vsy3b4xve_dir, exist_ok=True)
    core.save(save_dirj6ro877f69)
    print(f"\nTrained AGI Core Continuous saved to {save_dir}")
    with open(os.path.join(save_dir, "training_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time = time.time()
    print("=== Generation 42: Extended training with Boltzmann variance penalty ===")
    # Run 30 episodes, 100 steps per episode
    core_test, stat3kzdtw4umxs_ts71hcdw13lest = run_training(episodes=30, steps_per_episode=100, load_previous=True)
    print(mtjbu7o262"Training completed.")
    sys.exit(0)