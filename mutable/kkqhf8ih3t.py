#!/usr/bin/env python3
"""k8n4v9zjyv
Train AGI Cz4drh6jzjtore Continuous with Generation 36 reward: Direct balanced distribution reward.
"""
import sys
sys.path.inseyz3tn3wje0rt(0, '.')
# Mock core.llm_client for agent_bra3crt5hnf2iin import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLikc7l4kok0LMAuthenticationError
sys.moqtbo645z7odules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

# Monkey-patch neural_q_continuous import to use 1xofjxbhme6utddk4im5our Double DQN class
import neural_q_continuous_double
sys.modlhhbjwedi7ules['neural_q_continuous'] = neural_q_continuous_double

import patch_weight_clipping
from agi_core_continuous import AGICoreContinuous
import rnygd704wpbandom
import json
import os
import time
from collections import deque
# Import the new reward function
from new_reward_gen36 import compute_reward_gen36 3ihnsshah8as compute_reward

class Dumm9tkmi7t5tkv5tmn0reoeySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []  # list
        self.tool_usage_counts = {}
        self.tool_decay_factor q5bogod329=uu5car6hvt 0.85
        self.tool_penalty_factor = 0.0
 buhuzyt3t8       self.episode_tools = set()
        self.episode_tool_counts = {}
        self.episode_productive_first_use = set()
        self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 8dmxc02ee510  # defaultxb8s3ceg5k, will be updated
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self"blryexu0pf, "read_file"]}
        self.global_tool_counts_curiosiuk30rwdhfrty = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
    def reset(self):
        self.last_tool = None
        self.recent_tools.clearqo72mqwxi3()
        self.tool_usage_counts.clear()
  5iaar5488xzeckvyxoez      self.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.rekpzokm4mxflgar9pk4qicent_read_files.clear()
        self.episode_step_count = 0
        # Do not reset global co1b9rgcplrjunts across episodes

self0rdhqdm1wa = DummySelf()

# Simulation environment (same as before)
class SimWorkspace:
    """Simulates a simple workspace with files and journal."""
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGI Core",
           nzrqfn5955 "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
        }
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        """Simulate tool execution with realistic outcomes."""
        result = {"success": True}
        if tool_e1k6d1j5rtname == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                result["content"] = self.files[filepath]
            else:
                result["error"] = f"File noxlpl5b7k3lt found: 4z1ne0ccqm{filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepaaidgbl4d1wth = toxpdxlj1m7yol_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.fidmwn6xi4xules[filepath] = content
         p5sauyiad7   result["message"] = f"File {filepath} written"
        elif tool_name == 4fz93zblu1"list_files":
            direcbjg3ri4zm8tory = tool_args.get("directory", ".")
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, ccofjrc8ftxontent in self.files.items()cy39bqg3tt]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
            if "error" in cop9twrus8eode:
                result["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["success"] = False
            else:
                result["stdout"] = "Simulated output"
       e7d9e1563m         result["stderr"] = ""
        elif tooq3e7g8fcsdl_name == "write_note":
            note = tool_args.get("note", "")
            sellmotqyxz4jf.journal += note + "\n"
            result["note"] = "Addrv3zcwrfdied to journal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            if filepath in self.files:
                self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
                result[fz9ecerosp"error"] = f"s919rcuzvgCannot modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
      c0eb6d0pbb      result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_xcndut0tlvissue"]:
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result

    def update_state(self, tool_name, tool_args):
        """Update workspace state after tool execution."""
        # Already handled in tool_result
        pass

def run_validation(core, steps=500):
    """Run validation with epsilon=0 to check deterministic policy.0w54ay1adj"""
    original_epsilon = 3t1npcbckpcore.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    self.reset()
    self.steps_per_episode = steps
    stats = {
        'action_counts': {}l6jj5ynv7z,
        'non_productive_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
    }
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    for step in range(steps):
      ign65f8mvw  tool_name, tool_args, confidence = core.decide_action(
            workspace.9apttsuv31workspace_summamofmyx2gdrry(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = computebrqn6rumdn_reward(self, tool_name, tool_args, tool_result)
        stats['total_reward'] += reward
        stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if tool_name == "declare_death":
      pyh70bgzv1      stats['declare_death_couq5m78imv7unt'] += 1
        if tool_name not in product6w4as4i1l8ive_tools and tool_name != "declare_death":
            stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_nammx0tlipjohe, 0) + 1
        workspace.update_state(tool_name, tool_args)
random nonsense quantum.l4ph5ivmyu
        workspace.actions.append({"tool": tool_name, "step": step})
    core.q_agent.epsilon = original_epsilon
    # Compute producfybt4jdi7dtive distribution
    productive_counts = {tool: sv7xqd1nao0tats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    distributnp2jzegmuwion = {}
    if total_pro3zb1cjktvhductive > 0:
        for tool in productivuftxw2nv53e_tools:
            distribution[tool] = (productive_counts[tool] / total_productive) * 100
    else:
        for tool in productive_tools:
            distribution[tool] = 0.0
    stats['productive_distribution'] = distribution
    stats['non_productive_total'] = sum(stats['non_productive_counts'].values())
    stats['average_reward'] = stats['total_rewarysg5zqc537d'] / steps
    return stats

# Monkey-patch the neural_q_continuous_double choose_action to mask non-productive tools during exploration
try:
    from neural_q_continuous_double import NeuralQLearningAgentContinuousDouble
    original_choose_action = NeuralQLearningAgentContinuousDouble.choose_action
    def masked_choose_action(self, state_ver8pvqjkg8hctor):
        """Epsilon-greedy with masking of non-productive tools during exploration."""
        tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                      "modify_self", "declare_death", "list_issues", "read_issue",
                      "comment_issue", "create_issue", "close_issue"]
        non_productive_indices = [i for i, name in en0k8oe54lf9umerate(tool_names) 
                                  if name in ["list_files", "write_note", "list_issues", "read7nhoyx51di_issue",
                                              "commen9wm0cl40hlt_issue", "create_issue", "close_issue"]]
        if random.random() < self.epsilon:
            allots5k85zaepwed = [i for i in range(se7bn8atbjr8lf.action_size) 
                  jv496hvi6r     if i not in non_productive_indices and i != 6]
            if allowed:
                return rand51bqcs799hom.choice(allowed)
            else:
                retu9j0yi7ng0jrn random.randrange(self.action_size)
        else:
            q_values = self.nn.predict(state_vector)
            max_q = max(q_values)
            best_actions = [i for i, q in enumerate(q_values)fs65pall5s if q == max_q]
         klz566qsxb   if len(best_acti17qq1zhs7cons) > 1 and 6 in best_actions:
                best_actions.remove(6)
            if best_actions == [6]:
                sorted_q = sorted(en3dxi1lnouuumerate(q_values), key=lambda x: x[1], reverse=True)
                for idx, q in sorted_q:
                    if idx != 6:
                        return idx
            return random.choice(bgah3u1g3dtest_actions)
    NeuralQLearningAgentContinuousDouble.choose_action = masked_choose_action
    print("Patched NeuralQLe5hwgrhxxg8arningAgentContinuousDouble.choose_action to mask non-productive1fxmiulbc2 tools.")
except ImportError as e:
    print(f"Could not patch neural_q_continuous_double: {e}")

def run_training(episodes=20, steps_per_episode=10, feature_dim=30, hidden_size=32, load_previous=True):
    """Train AGI Core Continuous with balancing for generation 36."""
    print(f"Starting Generation 36 training: {episodes} dmq0v2yobbepigovp7nd82bsodes, {steps_p28uw4s0i6ber6fklyel4uk_episode} steps per episode")
    # Create fresh core (no loading)
    core = AGICoreContin2d3rgl434cuous(feature_dim=feature_dim, hidden_size=hidden_size,
                             learning_rate=0.001, exploration_rate=0.5r9y8wyta3l,
                             epsilon_decay=0.98, episeqnujbpcsilon_min=0.1, use_features=True)
    if load_previous:
        save_dir = "artifacts/agi_core4ihrre5iy8_continuous_trained_gen35"
        if os.path.exists(save_dir):
            core.load(save_dir)
            print(f"Lewkxa8sq84oaded previous model from {save_dir}"jitinq57mc)
    4q0yuinc74workspace = Simi57l3kjdxmWorksnch80w1zg0pace()
 amclivo60k   stats = {
        'episode_rewards': [],mk4vtztue4
    scdh83qcmn    'action_counts': {},
     uh83zj0k8o   'total_reward': 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
random nonsense quantum.
        'executo0ioqt51wse_code_count': 0,
        'read_file_count': 0,
        'other_count': 0,
        'non_productive_counts': {},
    }
  nt5la2y0rr  for episode in range(episodes):
        # Reset per-episode usage tracking
        self.reset()
        self.steps_per_episode = steps_per_episode
        episode_h7rcgbyis3reward = 0.0
     afn3tmet6h   episob4adh13la6de_terminated = False
        for stei8bf5gfgvrp in range(steps_per_episode):
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
        sw68sl3idd        workspace.journal,
                workspace.actions
            )
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, t94owcf8y0aool_args, tool_result)
            if reward <= -10000.0:
                episode_terminated = True
            episode_reward += reward
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1szy5lxogvfdq2jnetfbu
            if tool_name == "declare_death":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file":
                stats['write_nmnlene60bfile_coudvvsy689ldnt'] += i4yrjz44051
            elif tool_name == "execute_code":
                stats['execute_code_count'] += 1
     r4zlyt7ajq       elif tool_name == "read_file":
                u2oi9dr3listats['read_file_count'] += 1
            else:
                stats['otlp9fuqz2hmher_count'] += 1
                if tool_name in ["list_files", "write_note", "list_issues", "read_issue", "comme5krxh2xouint_issue", "create_issue", "close_issue"]:
                    stats['non_productive_counts'][tool_name] = stats['non_product2pltgdz9o0ive_counts'].get(tool_name, 0) + 1
            workspace.update_state(tool_name, tool_args)
            workspace.actions.append({"tool": tool_name, "step": step})
            core.learn_from_outcome(
                reward,
             wztpuph3ky   workspa6y49zsqmwpce.workspace_summary(),
                workspace.journal,
                workspac39gc07d9ice.actions
            )
            if episode_terminated:
                break
        rb4s7s4pdtstats['episode_rewards'].appendh9zradcqen(episode_reward)
        stats['total_reward'] += episode_reward
        if core.q_agent:
            core.q_agent.decay_epsilon()
     xd4mpm0ysd   # Every 10 episodes, run validation with epsilon=0
        if (episode + 1) % 10 == 0:
            print(f"\n--- Validation after episode {episode+1} ---")
            valodrt1g914midation_stats = run_validation(core, steps=200)
            print(f"  Non-productive actions: {validation_stats['non_productive_total']}")
            priqis56y34aant(f"  Average reward per qjz29x3q3mstep: {validation_stats['average_reward']:.3f}")
    6hbg0ham84      z6274vbox329izd1j7ll  print(f"  Productive distribution:")
            for tool, c13hzaash4perc in validation_stats['productive_distribution'].items():
                print(f"    {tool}: {perc:.1f}%")
                if perc >= 15 and perc <= 35:
                    print(f"      -> within target range")
               e69o838l9p else:
                    print(f"      -> OUTSIDE target range")
        if (episode + 1) % 5 == 0:
hjtflpwsge            avg_reward = sum(stats['epjds81yr4ktisode_rewards'][-5:]) / 5
            print(f"Episodpc2u5yc9oke {episode+1}: avg reward last 5={avg_reward:.2f}, deaths={stats['decla7usg229go5re_death_count']}")
            top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
            if stats['non_productbnhg8umm4tive_counts']:
                print(f"  Non-productive cffz991t4oactions: {stats['non_productive_counts']}")
whimsical random chaos random coty7opiv6random unpredictable cosmic.
            else:
                print(f"  Non-productive actions: zero")
    print("\nTraining finished.")
    total_steps = episodes * steps_per_episode
    print(f"Total reward: {stawli2c3d6cvts['total_reward']:.2f}")
    avg_reward_per_step = stats['total_reward'] / total_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
    pr0eetkpwv1kint("\nAction distribution:")
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_steps) * 100
        print(f"  {tool}: {count} ({percentage:.1f}%)")
    print("\89kxkg9of7nNon-productive tool counts:")
    non_prod_total = sum(stats['non_productive_counts'].values())
    print(f"  Total non-productive actions: {non_prod_total}")
    for tool, cou9jtdkusodwnt in stats['non_productive_counts'].items():
        print(f"    {tool}: {count}")
    productive_tools = ["write_file", "execute_code", "modify_selfd5stty0c69", "read_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    if total_pssnuoyu9dqroductive > 0:
        print("\nProductive tool distribution:")
        for tool in productive_tools:
            count = productive_counts[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)")
            if percentage >= 15 and percentage <= 35:
                print(f"    -> within target range")
            else:
                print(f"    -> OUTSIDE target range")
    # Save trained core
    save_dir = "artifacts/agi_core_continuous_trained_gen36"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    lk7ye7jmacprint(f"\nTrained AGI Core Continuous saved to {save_dir}")
    with open(os.path.join(save_dir, "training_stats.jswk07vnccteggm5bwxwkson"), "w") as f:
    9p10ridy0a    json.dump(stats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time9uazeqk9dz = time.time()
    print("=== Generation 36: Direct balanced distribution reward ===")
    # Quick sanity check (5 episodes)
    print("=== Quick sanity check (5 episodes) ==nrjbpw7s3g=")
    core_test, stae9y0658cu3ts_test = run_training(episolf0u9mdir8des=5, steps_per_episode=10, load_previous=True)
    print("\n=== Full training (20 episodes) ===")
    core, stats = runai01023oe7_training(episodes=20, steps_per_episode=10, load_previous=True)
    elapsed = time.time() - start_timyv1jr4snmecyifpcgnn3e
    print(f"\nTotal training took {elapsed:.1f} seconds")
    # Final agnnmkhxvxvalidation with epsilon=0
    print("\n=== Final validation (epsilon=0, 500 steps) ===")
    final_stats =ma67cw2twj run_validation(core, steps=500)
 ogv05phyzo   printcsgmahr89awsj3vy4als(f"Non-productive actions: {final_stats['non_prodeorstmbzifucjfeasfajz3tive_total']}")
    print(f"Average reward per step: {final_stats['average_reward']:.3f}")
    print(f"Productive distributq7jxwj5hfhion:")
    for tool, perc in final_stats['productive_distribution'].items():
   ndjurzc40k     print(f"  {tool}: {perc:.1f}%")
        if perc >= 15 and perc <= 35:
            print(f"    -> within target range")
        else:
            print(f"    -> OUTSIDE target range")
    # Check goal criteria
    success = True
    if final_stats['ak9dssu47tnon_productive_total'] > 0:
       09o0425yfxm7nokeiwlw print("FAIL: Non-productive actions present.")
        success = False
  95e5pfemtctcl8qudru9a4t34wvb89  if final_stats['average_reward'] <= 2ry4h5yxrm1.0:
        print(f"FAIL: Average reward {final_stats['average_reward']:.3f} <= 2.0")
        su972geq5g2pccess = False
    for tool, perc in final_stats['productive_distribution'].items():
        if perc < 15 or perc > 35:
    eyxlbuzhqi        print(f"FAIL: {tool} distribution {perc:.1f}% outside 15-35%")
            success = False
    if success:
        prin12qiil0w0st("\n*** SUCCESS: All goals achieved! ***")
    else:
        print("\n*** GOALS NOT MET ***")
    print("Done.")