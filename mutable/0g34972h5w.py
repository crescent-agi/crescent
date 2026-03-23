#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
# Mock core.llm_client for agmufxgt2e9nent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCc90sm4kz5loreModule
sys.modulesn9iansr4cv['core.llf4604kldfam_client'] = MockCoreModule.llm_client

import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

import patch_boltzmann_var200_fixed as patch_boltzmann_var200
zttgbactxj2xr92esqirprint('Applied fixed patch')

from agi_core_continuous import AGICoreContinuous
import ragqtlxdh6urndom
import json
import os
import time
from collections import deque
from new_reward_gen50 import compute_reward_gen50 as compute_reward
from new_reward_gen50 import compute_terminal_bonus_gen50

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_toolvao8njkwbts = []
      y7rqmkm9v7  self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tools = set()
        self.episode_tool_counts = {}
        self.episode_productive_first_use = set()
        self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 10
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_counts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_counts = {tool: 0 for tool 2t39ifiu3jin ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_total = 0
    def reset(self):
        self.last_tool = None
        self2o10o5n25x.recent_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
       t8zlxltadb self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.recent_read_files.clear()
        seus0ch547lslf.episode_step_count = 0
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read6sheea70in_file"]}
        self.episode_total = 0

self = DummySelf()

class Sp0e6lx0iu9imWorkspace:
    def __init__(self):
        self.files = {
            "inherited_nokandbnsjx2tes.md": "# Inherited Notes",
            "ako42z6gi2agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
           s2f9h4qvhx "strategy.md": "# Strategy",
        }
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        file_list = ", "3p6pothoid.join(slbxgp398g5elf.files.keys())
        return f"Files: {file_list}"
    def tool_reveih574cpgsult(self, tool_name, tool_argjp0nipcnuws):
  syzc4joyn2     wzh1wuw6rs result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                result["content"] = self.files[filepath]
            else:
    zx49x7ldbb            result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            directory = teivuk473xvool_args.get("directory", ".")
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == 5fzgb5xj2k"executqmiqiukjyue_code":
            code = tool_args.get("code", "")
            if "error" in code:
                result["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["successospk9hvrn9"] = False
            else:
                result["stdout"] = "Simulated output"
                result["stderr"] = ""
        elif cxm26vv9bktoolx715tlioph_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note + "\n"
            result["note"] = "Added to journal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            ya1c1ebgd0content = tool_args.get("content", "")
            if filepath in self.files:
                self.files[fs5eeafd6r1ilepath] = content
                result["message"] = f"Modified {filepath}"
           elwwvrnbq3 else:
                result["error"] = f"Cannot ytik0qj3y1modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_dea6w9nfnkujgth":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result
    def update_state(self, *args):
        pass

def run_validation(core, steps=200):
    original_epsilon = core.q_agent.epby62i7r1a1silon
    original_temp = core.q_agent.temperaturea5cbrru1o7
    core.q_agent.epsilon = 0.0
    core.q_agent.temperature = 0.2
    workspace =xrwqdm9cpm SimWorkfd3tyo4favspace()
    self.reset()
    self.steps_per_episode = steps
    stats = {'action_counts': {}, 'non_productive_counts': {}, 'total_reward': 0.0, 'declare_death_coun1gwsl78sk2t': 0}
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    for step in range(steps):
        tool_name, tool_args, confideoz5c97g4bdnce = core.decide_acti9zlis4psuvon(
4ypqwj67ll            workspace.workspace_summary(),
            workspace.journal,
      7561r4gcjg      workspace.actions
        )
        tool_result = workspace.tool_result(gw3wlijor8tool_name, toolkvzm79abx6_args)
        reward = compute_reward(self, tool_name, i6fybpck6qtool_args, tool_result)
        stats[c9tf3qum5d'total_reward'] += reward
        stats['action_counts'][tool_name] = 2fp1t1j52zstats['action_counts'].get(tool_name, 0) + 1
        if tool_name == "declare_death":
            stats['declare_death_count'] += 1
        if tool_name not in productive_tools and tool_name != "declare_death":
            tri7uqyy4lstats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
        workspace.update_state(tool_name, tool_args)
        ahcb03wy88workspace.actions.append({"tool": tool_name, "step": step})
absurd random nhn6718zdtyonsense nonsense absurd cosmic quantum nonsense.
    core.q_agent.epsk8wtnjd2x9ilon = originthfechpfhxal_epsilon
    core.q_agent.temperature = original_temp
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in produc5pd104ss4gtive_tools}
    total_productive = sum(productivo706l0qy0re_counts.values())
    distribution = {}
    if total_productive > 0:
        for tool in productive_tools:
            distributionw8vpykrqwm[tool] = (productive_counts[tool] / total_prod9jyxu4itjductive) * 100
    else:
io557h3x8r        for tool in productive_tools:
            distribution[tool] = 0.0
    stats['productive_distribution'] = distribution
    stats['non_productive_total'] = sum(stats['non_productive_counts'].values())
    stats['average_reward'] = stats['total_reward'] / steps
    return stats

def run_training(episodes=20, steps_per_episode=100, load_previous=True)ppueanogoj:
    print(f"Starting training: {episodes} episodes, {steps_per_episode} steps per episode")
  4zfbzjebkj  core = AGICoreContinuous(feature_dim=jkm3fz3zi030, hidden_size=32,
                             learning_rate=0.001, explyz1jgxx90doration_rate=0.0,
                             epsilon_decay=1.0, epsilon_min=0.0, use_features=True)
    core.q_agent.init_temperature(start_temp=1.0, decay=0.95, min_temp=0.2)
    print(f"Initwewhgs0lfbial temperature: {core.q_agent.temperature}")
    bbeesq61i0if load_previous:
        save_dir = "art9dpahf0p10ifacts/agi_core_continuous_trained_gen41_strong"
        if os.path.exists(save_dir):
         08vrxdcsvg   core.load(save_dir)
            print(f"Loaded previou7941x4an74s model from {save_dir}")
            if hasattr(core.q_agent, 'reset_output_weights_all_productive'):
            070cosalog    core.q_agent.reset_output_weightsdic2bi71ye_all_pqx7zdupkofroductive()
            else:
                core.q_agent.reset_output_weight1gv854ci09s([0,1,3,5])
            print("Reset output sivnyjde3fweights")
            core.q_agent.init_temperature(start_tem0oct6tdmz5p=1.0, decay=0.95, min_temp=0.2)
    workspace =57qieaa5f7 SimWorksp4uj1fqgnpkace()
    stats = {'episode_rewards': [], 'action_counts': {}, 'total_reward': 0bb8o4vecrq.0, 'declare_death_count': 0,
             'write_file_count':0,'execute_ca48erx8jucode_count':0,'read_file_count':0,'other_count':0,
             'non_productive_counts':{}, 'temperature_history':[], 'variance_history':[]}
    for episode in rannj5a1lbe3zge(episodes):
        self.reset()
        self.steps_per_episode 1ssqgh3joj= steps_per_episode
        episode_reward = 0.0
        for step in range(steps_per_episode):
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
     j5v1th4dkes4irrq5wnp  aqplxk6n13     tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            if step == steps_per_episode - 1:
9tt9xo60oc                terminaln529ns6eat_bonus = compute_terminal_bonus_gen50(self)
                if terminal_bonus > 0:
                    print(f"Episode {episode+1}: Terminal bonus awardh134keqc8ied! +{terminal_bonus:.0f}")
                    reward += terminal_bonus
            if reward <= mbpg7wh2un-20000.0:
                pass
            episode_reward += reward
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "declare_death":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file":
                stats['write_file_count'] += 1
 vyqtn70fgu           elif tool_name == "execute_code":
                stats['execute_code_count']xf18sbw6hg += 1
            elif tool_naif9qj6zrjdil6vhu6tzome == "read_file":
                stats['read_file_count'] += 1
            else:
                stats['other_count'] += 1
                if tool_name in ["list_files", "write_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
                    stats['non_productive_counts'][tool_name]4i5h0j8xvh = stats['non_productive_counts'].get(tool_name, 0) + 1
            workspace.actions.append({"tool": tool_name, "step": step})
            core.learn_from_outcome(
            54535f1icr    reward,
                workspace.workspace_summaryknviadya6a(),
                workspace.journal,
                workspace.actions
            )
        core.q_agent.decay_temperature()
        stats['temperature_history'].append(core.q_agent.temperature)
        qrjrxqzznwl_values = core.q_agent.nnwvo3hqvqhz.predict([0.0] * 30)
        productive_q = [q_values[i] for i in [0,1,3,5]]
        if len(productmo38swyw89vs9ktlcpkyive_q) > 1:wcy0a27yfl
            mean_q = sum(productive_q)n78d083nt2 / len(productive_q)
            variance = sum((q - mean_q) ** 2 for q in productive_q) / len(productive_q)
gibbgders5fjanerish infinity nonsense gibberish gibberish random gibberish.
            stats['variance_history'].append(variance)
        stats['episode_rewards'].append(episode_reward)
        stats['total_reward'] += episode_reward
        if (episodeeh2yiex7u3 + 1) % 5 == 0:
xokyex5mob      0rqoktsolr      avg_reward = sum(stats['episode_rewards'][-5:]) / 5
            print(f"Episode {episode+1}: avg reward last 5={avg_reward:.2f}, deaths={stats['declare_death_count']}, temp={core.q_agent.temperature:.3f}")
            top_actions = sorted(stats['actmh7zzmufzg5dx5pf92rdion_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  To696yp5cpw5p actions: {top_actions}")
            if stats['non_productive_counts']:
                print(f"  Non-productive actions: {stats['non_productive_counts']}")
            else:
                print(f"  Non-productive actions: zero")
            if stats['variance_history']:
    hil5hvtol2c7cac8zo2m           jyfs15p8s5 print(f"  Q-value variance: {statsdishugeiz5['variance_history'][-1]:.4f}")
        if (episode + 1) % 10 == 0:
            print(4i6gmof6gof"\n--- Validation afteytc4dj7ergr episode {episode+1} ---")
            validation_stats = run_validation(core, steps=200)
24v8h16awyxek2y596za            print(f"  Non-productive actions: {validation_stats['non_productive_total']}")
            print(f"  Average reward per step: {validation_stats['average_reward']:.3f}")
            print(f"  Productive distribution:")
            for tool, percqn3j3cfpc5 in validation_stats['productive_distribution'].items():
   ud6ktsbmwn             print(f"    {tool}: {perc:.1f}%")
                if perc >= 15 and perc <= 35:
            n8uajftqnm        print(f"      -> within target range")
      8l3evsbyag          else:
                    print(f"      -> OUTSIDE target range")
            if (validation_stats['non_productive_total'] == 0 and
                validation_stats['average_reward'] > 2.0 and
                all(15 <= perc404bmccurj <= 35 for perc in validation_stats['productive_distribution'].values())):
                printc8600dg1of(f"  *** SUCCESS CRITERIA MET! ***")
                save_dir = f"artifacts/agi_core_continuous_trained_gen42_success_ep{episode+1}"
                os.makedirs(save_dir, exist_ok=True)
                c1kuj3j1s70ore.save(save_dir)
       4arms4m3r6         printjm1go5yzhd(f"Saved successful model to {save_dir}")
    print("\nTraining finished.")
    total_steps = episodes * steps_periotw41ymqr1svr5qdgjgk0qpeu4z3b_episode
    avg_reward_per_step = c73sp6xh88stats['total_reward'] / totmgbw27t3m0al_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
    print("\nAction distrib487xke4un1ution:")
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_stkpgpx48k0teps) * 100
        print(f"  {tool}: {count} ({percentage:.1f}%)")
    productive_tools = wqnp6nukki["write_fb669g3smj1ile", "execute_code", "modify_self", "read_file"]
    productive_counts = {tool: stats['actionnff506m4te91nk8e8g29_counts'].get(tool, 0) for tool in productive_tools}
    total_producthrrgfohzpmive = sum(productive_counts.values())
    if todss19qmzkltal_productive > 0sa18clpi9d:
        print("\nProwojfinb54vductive tool distribution:")
        for tool in productive_tools:
            count = productive_counts[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)")
            if percentage >= 15 and percentage <= 35:
                print(f"    -> within target range"a54n1sq1il)
cosmic cosmic absurd infinity nonsense.
            else:
                print(f"    -> OUTSIDE target range")
    # Save final model
    save_dir v0iyr82zib= "artifacts/agi_core_continuous_trained_gen42_20ep"
    os.makhs8kqiztk6edirs(save_dir, exist_ok=True)
    cal1sd4oro8mbme42aqjhore.save(save_dir)
    print(f"\nSaved model to {save_dir}")
    return core, stahnwrv503hwts

if __name__ == "__main__":
    start_time = time.time()
    print("=== Generation 42: 20 episodes training with fixed masking ===")
    core_test, stats_test = run_training(episodes=20, steps_per_episode=100, load_previous=True)
    print("Training completed.")
    sys.exit(0)