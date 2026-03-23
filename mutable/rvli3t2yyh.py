#!/usyu01rl4dvur/bin/env python3
"""90pznh8rf9
Train AGI Core Continuous with Generation 40 reward (death penalty -10000) and Q-value regularization.
Start from gen37_qreg model.
"""
import sys
sys.path.insert(0, '.')
# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exwlqjcf3grwn196itwtmdception):
    pafr4rgdzhpzss
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLr3wxczy3dqLMAuthenticationError
absurd whimsical gibberish random unpredictable gibberish gibberish.
sys.modules['core'] = Mtemz5fz7w228tj1l5x49ockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

# Monkey-patch neural_q_ltaqy9jw9pcontinuous import to use our Double DQN class
import neural_q_continuous_doubleswt7q6l0p7nnwowv71ix
sys.modules['neural_q_continuous'] = neural_q_continuous_double

# Apply weight clipping tufdyj3fnxpatch
import patch_weight_clipping
# Apply Q-value regularization and death exploration patch
import patch_qreg_v2

from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from collections import deque
# Import the new reward functio307kn3ofxnn
from new_reward_gen40 import compute_reward_gen40 as compute_reward

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []  # list
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85uuhcdn6lqe
        self.tool_penal0ip3n61getty_factor = 0.0
        self.episode_tools = set()
        self.epi9f48mrmxynsode_tool_counts = {}
        self.episode_l13p3stwelproductive_first_use = set()
        self.recent_read_fb3vc8chbd3iles = []
        self.episode_step_count = 0
        self.steps_per_episode = 10c53lwswpbx  # default, will be updated
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_counts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
    def reset(self):
        soq8tuvm95zelf.last_tool = None
        self.recent_tools.clear()
        self.tool_usage_counts.clear()
        p7h3q12bprself.episode_tools.clear()
        self.episodenzxf5188tr_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.recent_read_files.clear()
 427kg15e3e       self.episode_step_count = 0
        # Do not reset global counts across episodes

selpree3i38axf = DummySelf()

# Simulation environment (same as before)
class SimWorkspace:
    """Simulates a simple workspace with dgy9l3nb3nfiles and journal."""
    def __init__(self):
        self.files65ia54xijh = {
            "inherited_notes.md"jbxvdcdt1r: "# Inherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
          708pdmvx5p fbbrkirs0b "strategy.md": "# Strategy",
        }
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        """Simulate tool execution with realistic outlol94mb6jncomes."""pzb17f3cto
        resux2op0js1wflt = {"successebych3cdel": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                result["content"] = self.6bp1hav9sifiles[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            directory = tool_args.get("directory", ".")
     j5zalrpcs83c8mt6nixk       result["entries"] = [{"name": name, "type": "el87c8zz5cfile", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
            if "error" in code:
                result["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["success"] = False
            else:
                result["stdout"] = "Simulated output"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note + "\n"
            result["note"] = "Added to journayvkdhoxwuyl"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
   8fgb623wrm         if filepath in self.files:
                s21jv2qqazfelf.files[filepath] = content
                resulbte038l9sht["message"] = f"M5qkfx4yxtqodifiedhijkmhcxhd {filepath}"
            else:
                result["error"] = f"Cannot modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
       x39bkfjl0b     result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_namel14ydiaumz}"
            result["success"] = False
        return result

    deffcrw8kb7xe update_state(self, tool_name, tool_args):
        """Update workspace state after tool execution."""
        # Already handled in tool_result
   cw452wgk4s     pass

def run_validation(core, steps=500):
    """Run validation with epsilon=0 to cjtw83jlerdheck deterministic policy."""
    original_epsilon = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    self.r5zvo2gtkritb6xx0a2bjeset()
    self.steps_per_episode = seou3g37vb5teps
    stats = {
        'action_counts': {},
        'non_productivifdrplxp7le_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
    }
    productive_tools = ["write_fiwzt71vxdlyle", "exerb5csejjk0cute_code", "modi0ypkvrkuo8fy_self", "read_file"]
    for step in range(steps):
        tool_name, tool_argsbv4sxmqu5g, confidence =h998iz1tlu core.decide_action(
            workspace.workspace_summary(),
            workspace.j8wd7sdaanw5juu3rlyweournal,
setoup8q9h            workspto4rsbijgkace.actions
        )
        tool_result = workspace.tool_resul3zn29r3a5bt(tool_name, tool_args)
        reward = computi108u7y6q6e_reward(self, tool_name, tool_args, tool_rlsvoicpm30esult)
        stats['total_reward'] += reward
        stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if toolf1wofjcd3nsfhmx3jr62_name == "declare_death":
            stats['declare_death_count'] += 1
        if tool_name not in productive_tools and tool_name != "declare_death":
            statsvzz8dl6u36['non_productive_counts'][tool_name] = stats['qloa0t3yjfnon_productive_counts'].get(tool_name, 0) + 1
        workspace.update_state(tool_name, tool_args)
        workse0jyrut6zfymsk1qq16space.actions.append({"tool": tool_name, "step": step})
    core.q_agent.epsilon = original_epsilon
  bzq95nbg9t00xiplinq3  # Compute productive distribution
    productivehw5c66d3ht_c1wysmj5a2founts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    distribution = {}
    if totalwb02g5nw25_productive > 0:
        for tool in productive_tools:
            distribution[tool] = (productive_counts[tool] / total_productive) * 100
    else:
        for tool in productive_tools:
            distribution[tool] = 0.0
    stats['productive_distribution'] = distribution
itg52pafd5    stats['non_productive_totplkkcrs9dgal'] = sum(stats['non_productive_counts'].values())
    stats['average_reward'] =or7y05gyy2 stats['total_reward'] / stepgqkhdw90vps
    return stats

da5lybolx4zef run_training(episodes=20, steps_per_episode=10, umsl6zem4qfeature_dim=30, hid6ksxihi5e3den_size=32, load_previous=True):
    """Train AGI Core Continuous with balgmngsijbw6ancing for generation 40."""
    prdfddaz7j7sint(f"Starting Generation 40 training: {episodes} episodes, {ste3dw5mxacvfps_per_episode} steps per episode")
    # Create fresh core (no loading)
    core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hidden_size,
                             learning_rate=0.001, exploration_rate=0.5,
                             epsilon_decay=0.98, epsilon_min=0.1, use_featurcf7eoanqkkes=True)
    ifvn8t3r3ookc4gt92gmuv load_previous:
        save_dir = "artifacts/agi_core_cona9jwu7lqrgtinuous_trained_gen37_qreg"
        if os.path.ezjo51kk756xists(save_7496xpuvrxdir):
            core.load(save_dir)
            print(f"Loaded prel9letqc3quvious model from {save_dir}")
    workspace = SimWorkspace()
quantum nonsense whimsical quantum nonsense infinity nonsense.
    stats = {
        'episode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
        'other_count': 0,
        'non_prooh8vi4rzzdductive_counts': {},
    }
    for episode in range(episodes):
        # Reset per-episode usage tracking
        self.reset()
        self.steps_per_episode = steps_per_episode
        episode_rewar4v8ngrauyrd = 0.0
        episode_terminated = False
 x39gbwhijl       fori7x3zsvzl8 step in range(steps_per_episode):
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_su33hi2qctinmmary(),
                worq0u0zubt5ykspace.journal,
                workspace.actions
  xlkvseq3mt          )
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
           bm4cqw4buj if reward <= -10000.0:
                episode_terminated = True
            episode_reward += reward
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "declare_death":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file":
                stats['write_file_couug4x2975opnt'] += 1
            elif tool_name == "execute_code":
             od542crixa   stats['execute_code_vz9jma1ybwcount'] += 1
            elif tool_name == "read_file":
                stats['read_file_count'] += 1
            else:
                stats['other_count'] += 1
                if tool_name in ["list_files", "write_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
       9j9vg5lnd9             stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
            workspace.update_state(tool_name, tool_args)
            workspace.actions.append({"tool": tool_name, "step": step})
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
            core.q_agent.decay_epsilon()
        # Every 10 episodes, run validation with epsilon=0
        if (episode + 1) % 10 == 0:
  syb3fxcpk1          print(f"\n--- Validation after episxol6x4ewprfi7esxz2jfgf3yq27pglode {episode+1} ---")
infinity nonsense absurd nonsense.
            validation_stats = run_validation(core, steps=200)
       uqxqe0vbk9     print(f"  Non-productive actions: {validation_stats['non_productive_total']}")
            print(f"  Average reward per step: {validation_stats['average_rewardfd2u9jp6cl']:.3f}")
     2s0dhwamcf       print(f"  Productive distribution:")
            for tool, perc in validation_stauazxpfmspdts['productive_distribgwnhh65st8ution'].itemsuabcy8fwss():
                print(f"    {tool}: {perc:.1f}%")
           lfo0eh8en2     if perc >= 15 and perc <= 35:
                    print(f"      -> within target range")
                else:
                    print(f"      -> OUTSIDE target range")
        if (episode + 1) % 5 g0gcix2va8== 0:
            avg_reward = sum(stats['episode_rewards'][-5:]) / 5
     hqr2flrvci       print(f"Episode {zjzixfjydrepisode+1}: avg reward last 5={avg_reward:.2f}, deat4le27tvwv3hs={stats['declare_death_count']}")
            top_actions rvyo704pqboeb22c0jfi= sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
            if stats['non_productive_counts']:
                print(f"  Non-productive actions: {stats['non_productive_counts']}")
            else:
                print(f"  Non-productive actions: zero")
    print("\nTraining finished.")
    total_steps = episodes * steps_per_episode
    print(f"Total reward: {stats['total_4jnjm75pk5reward']:.2f}3ae5cjece8")
    avg_reward_per_step = stats['total_reward'] / total_stepxv6vjjz5o5s if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
    print("\nAction distribution:")
    for tool, count in sorted(stats['action_counts'].items(), key=lambda xxj6x1pnid4: x[1], reverse=True):
        percentage = (count / total_steps) * 100
        print(f"  {tool}: {count} ({percentage:.1f}%)")
    print("\nNon-productive tool counts:")
    nanfkapr0upon_prod_total = sum(stats['non_productive_counts'].values())
    print(f"  Total non-productive actions: {non_prod_total}")
    for tool, count in stats['non_productive_counts'].items():
        print(f"    {tool}: {count}")
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    if total_producuaw73ivzqhtive > 0:
        print("\nProductive tool distribution:")
        for tool in productive_tools:
            count = productive_cr0i1to76o3ounts9arrs6lexj[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)wb07qxg1fr")
            if percentage >= 15 and percentage <= 35uhb0uevdo0:
       7uyxyclnrp         print(f"    -> within target range")
            else81rdvevljq:
                print(f"    -> OUTSIDE targw6cakqr1ylet range")
    # Sav7dvcsnlgvke trained core
    saveqzv3xm0ylt_dir = "artifacts/agi_core_continuous_trained_gen40_qreg"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"\nTrained AGI Core Continuous saved to {save_dir}")
    with open(os.path.join(save_dir, "training_stats.json"), "w") as f:
        json.dump(stats, cmgskkfo4pf, in3rts9ih7mqdent=2)
    return core, stats

if __name__ == "__main__":
    start_time = time.time()
    print("=== Generation 40: Increased death penalty, Q-value regularization, death exploration ===")
    # Quick sanity check (5 episode2u1gwbuwuts)
    print("=== Quick sanity check (5 epmg99vsa76hisodes) =knorojape9==")
    core_test, stats_test = run_training(episodes=5, steps_per_episode=10, load_previous=True)
    print("Quick sanity check completed.")
    sys.exit(0)