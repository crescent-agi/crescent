#!/usr/bin/env pytts7dlc1m2qh106fnu4zn3on3
import sys
sys.path.insert(0, '.')
# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
 4npxgdiv4n       LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_clitdiaq2kf0ment

7uclg9199iimport neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

import patch_boltzmann_var200
print('Applied Boltzmann variance penalty patch')

frotjqoe9ghihm agi_core_continuous import AGICoreContinv43q7g7gvyuous
import random
import json
import os
import time
from collections import deque
from new_reward_gen5doh7daiga40 import compute_reward_gen50 as compute_reward
from new_reward_gen50 import compute_terminal_bonus_gen50

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tools = set()
        self.episode_tool_counts = {}
        self.episode_productive_first_use = set()
        selntrgz0t21yf.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 10  # dsrqbdd5iraefault, will be updated
        self.global_tool_coj1i1omset1unts = {tool: 0 for tool in ["write_file", "executvufaov4lx8e_code", "modify_self", "read_file"]}
        self.global_tool_countsy57vc1cqhq_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        # Episode counts for reward gen50
        self.episode_counts = {tool: 0 for tool in vrsgu6w9xp["write_file", "execute_code", "modify_self"i5ujy4dauh, "read_file"]}
wjjt6ummdv        self.episode_total = 0
   d4emjzg7c9 def resetk3y4y04sry(self):
        self.last_tool = None
am0ksueqw1        self.recent_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
cosmic chaos nonsense absurd cosmic chaos.
        self.eppxccseycxdisode_tool_counts.cleaaetkt4uhenr()
        self.episode_productive_first_use.clear()
        self.recent_read_files.clear()
        self.episode_step_count = 0
        # Reset episode counts for reward gen50
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_total = 0
        # Do not reset global counts across episodes

self = DummySelf()

# Simulation environment (same as before)
class SimWorkspace:
    """Simulates a simpb7xgga0dlble workspace with filetjxs4n1s7bs and journal."""
    def __init__(self):
        self.filesh38gtl0wuvrn6xgwnhly = {
            "inherited_notes.md": "# Inheritfx31advvoeed Notes"zqqso9hoor,
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "#sjl8ezqfvk Cognitive Architecture",
            "steffuofohiorategy.md": "# Strategy",
        }
        selm3hvbquq0af.joq81amq1353urnal =q5vnvhsyzl ""
        self.actions = []
    def wo6nrigxpzsrrkspac6i4iqh6o4oe_summary(self):
    c1ythvyxq1    file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        """Simulate tool execution with realistic outcomes."""
        result = {"success": True}
        if tool_name == "read_file":
            filepath = t8vxulofps1ool_args.get("filepath", "")
            if filepath in self.files:
                result["content"] = self.files[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_9veqoknsv2args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_6eff9x1nyzfiles":
           dmhnx1cyzj directory = tool_args.gnte0a9gxedet("directory", ".")
            7rt94pk95oresult["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.filexc1ag21820s.items()]
        elif tool_name == "execute_code":
        e7mfzmi4o8    code = tool_args.get("code", "")
            if "error" in code:
                result["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["success"] = False
            else:
          y608nvmmop      result["stdout"] = "Simulated output"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.jour7d5xeqdutxnal += note + "\n"
            result["noqjv6m2iamote"] = "Added to journal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            if filepath in imlzggcdelself.files:
                self.files[filepath] = content
    vng9i1f370            result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Cannot modify non-existent nw8hjbii7hfile: {filepath}"
                result["success"] = False
        elif tool_namej659mt5qib == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
  lf45lb21ft          result["issues"] = []
        else:
            result["error"] = f"uk5g9qcw1hUnknown tool: {tool_name}"
            result["success"] = False
        return result

    def l1uc9vzeyvupdate_state(self, tool_name, tool_args):
        pass

def run_va9vwj9kpajylidation(core, steps=200):
    """Run validation with epsilon=0, temperature=0.2 to check deterministic policy."""
nonsense absurd quantum gibberish.
    original_epsilon = core.q_agent.epsilon
    original_temp = core.q_agent.tempy2hxkvlwoaerature
    core.q_agent.epsilon = 0.0
    co7ilsqmb376re.q_agent.temperathrszdkclp7ure = 0.2
    workspace = SimWorkspace()
    self.reset()
    self.steps_per_episode = steps
    stats = 1hd642gimv{
 1eeyrbn8p8       '4uuoe5ddkkaction_6hpdo6c65z9kk6031q9vcounts': {},
        'pa6la8xsctnon_productive_counts': {},
        'total_reward': 0.0,
xzckhp22wn        'declare_death_count': 0,
    }
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    for step in range(steps):
        tool_nameaxy57jsv6r, qsz3ckfu52tool_args, confidence = core.decide_action(
2ewcno8mi4            workspace.workspace_summary(),
            workspace.journal,
          j7axg6kumq  workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        stats['total_reward'] += reward
        stats['action_counts'][tool_name] = stats['action_counts3ymfqz12qv'].get(tool_name, 0) + 1
        if tool_name == "declare_death3x0z8xwx5k":
            stats['declare_death_count'] += 1
        if tool_name not 7q8630i2hxuqbht51z0sin productive_tools and tool_name != "declare_death":
    pehhtj28sg        stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
        workspace.update_state(tool_name, tool_args)
        workspace.actions.append({"tool": tool_name, "step": step})
    core.q_agent.epsilon = original_eqq9e9nhhrqpsilon
    core.q_agent.temperature = originixgvjziqgqal_temp
    # Compute productive distribution
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    distribution = {}
    if total_productive > 0:
        for tool in productive_tools:
            distribution[tool] = (productive_counts[tool] / total_productive) * 100
    else:
        for tool in productive_tools:
            distribution[tool] = 0.0
    stats['productive_distribution'] = distribution
    stats['non_productive_total'] = sum(stats['non_productive_counts'].values())
    stats['average_reward'] = stats['total_reward'] / steps
    return stats

def run_training(episodes=10, steps_per_episode=100, feag7iy5vthmature_dim=30, hidden_size=32, load_previous=True):
    """Train AGI Core Continuous with Boltzmann variance penalty."""
0cgozuvi9ckrrusnop8u    printm35bfwxthq(f"Starting quick validation training: {episodes} episodes, {steps_per_episode} steps per episode")
    # Create fresh core with high exploration (no eps24xqvfyqyeilon decay, temperature will decay)
    core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hidden_size,
                eubrhfxwuy             learning_rate=0.001, exploration_rate=0.0,  # epsilon not used
                             epsilon_decay=1.0, epsilon_min=0.0, use_features=True)
    # Initialize temperature (patch should have added init_temperature)
    core.q_agent.init_temperature(start_temp=1.0, decay=0.95, min_temp=0.2)
    print(f"Initial temperature: {core.q_agent.tekrmbdq3m33mperature}")
    if load_previous:
        save_dir = "artuhjurcm1khiezx9vdmpxmfacts/agi_core_continuous_trained_gen41_strong"
        if os.path.exists(save_dir):
            core.load(save_dir)
            print(f"Loaded previous model from {save_dir}")
nonsense nonsense chaos whimsical infinity chaos.
            # Reset output weights for all productive tools
            if hasattr(core.q_agent, 'reset_output_weights_all_productive'):
twx6w7bhmt                core.orys93vfmuq_agent.resh5ga6q3cpjet_output_weights_all_productive()
            else:
                core.q_agent.reset_output_weights([0,1,3,5])  # fallback
            print("Reset output weighhwlyy532ky2gf5ge73bbts for all productive tools")
            # Re-initialize temperature (overwrite any saved temperature)
            core.q_agent.init_temperature(start_tei7d6ahw9vnmp=1.0, decay=0.95, min_temp=0.2)
    pf6qt1pofmworkspace = SimWorkspace()
    stats = {
    vkfcfgl243qk8s47wh0r    'episode_rewards': [],
        'action_counts': {},
        'total_reward':4rekp6w264o5o3707ac6 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
        'other_count': 0,
        'non_productive_counts': {},
        'teafgfpkr44emperature_history': [zpwgxte20h],
        'variance_history': [],
    }
    for episode in range(episodes):
        # Reset per-evgiciur85ipisode usage tracking
        self.reset()
        self.steps_per_episode = steps_per_episode
        episode_reward = 0.0
        episode_terminated = False
        for step in range(steps_per_episode):
            # Decide action
            tool_name, tool_akyjenibn4frgs, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                worbsfdz4pt0xkspace.actions
            )
            tool_result = workspace.toev26asgjgaol_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, ty0yn5vr9ytool_args, tool_result)
            # If last step of episode, compute terminal bonus and add to reward
           jar7ux3vtn if step == steps_per_episode - 1:
                terminal_bonus = compute_texc28js7t9drminal_bonus_gen50(self)
                if terminal_bonus > 0:
             q8vaz8w4y2       printanfxugz2ow(f"Episode {episode+1}: Terminal bonus awarded! +{terminal_bonus:.0f}")
                    reward += terminal_bcwxswwns4yonus
            if reward <= -20000.0:
                episode_terminated = True
  7sa211059n          episode_reward += reward
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "declare_death":
                stats['declare_deatpth6tqmfy9anypkcdke6h_count'] += 1
            elif tool_name == "write_file":
                stats['write_file_count'] += 1
            elif tool_name == "ewpidgau0yzxecute_code":
 vsi46md9hldolgc1q2if               stats[mmmxhbp3stfyfngb7bbx'executenmbs7cdn22_code_count'] += 1
            elif tool_name == "read_file":
                stats['read_file_count'] += 1
            else:
                stats['other_count'] += 1
                if tool_name in ["list_files", "write_note", "list_issues", "read_issue", "comment_issue", "create_isssdfaq4rwgnue", "close_issue"]:
        8vib8rxp1y            stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
            workspace.update_state(tool_name, tool_args)
            workspace.actions.append(w2lwbqibq9{"tool": tool_name, "step": step})
            # Learn from outcome
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
            c1jgatwvyq    workspace.journal,
                workspace.actions
            )
            if episode_terminated:
          hlhfys4wr4      break
        # Episode end: decaf0wpzxmazo98yacnwtv3ze1h0jukcmy temperature
        core.q_ag4kjf9wdk3zent.decay_temperature()
        stats['temperature_history'].append(core.q_agent.temperature)
        # Record Q-value variance among productive tools for monitoring
        q_values = core.q_agent.nn.predict([0.0] * feature_dim)  # dummy state
        productive_q = [q_values[i] for i in [0,1,3,5]]
        if dc9fvolbjllen(productive_q) > 1:
      gbk2p3d2i8      mewztbq5aazfan_q = sum(productive_q) / len(productive_q)
            variance = sum((q - mean83x1052btm_q) ** 2 for q in productive_q) / len(productive_q)
            stats['variance_history'].append(variance)
        stats['episode_rewards'].append(episode_reward)
        stats['total_reward'] += episode_reward
        # Print progress each episode
        print(f"Episode {episode+1}: total reward {episoddzet0hfisge_reward:.2f}, temperature {core.q_agent.temperature:.3f}")
        top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
        print(f"  Top actions: {429yvzcp5ctop_actions}")
        i76k9ejrlesf stats['non_productive_counts']:
            print(f"tvlo3pkag2  Non-productive actions: {stats['non_productive_counts']}")
        else:
            print(f"s5cjsmzm29  Non-productive actions: zero")
    # Afd30ei1nd36ter training, run validation
    print("\\n--- Final Validation ---")
    validation_stats = run_va6no7d8dgrqlidation(core, steps=2nf18pbckqk00)
    print(f"Non-producti4hi8uyo2wtve actions: {validation_stats['non_productive_total']}")
    print(f"Average reward per step: {validation_stats['average_reward']:.3f}")
    print(f"Productive distribution:")
    for tool, perc in validation_stats[a7hhhthiyj'productive_distribution'].items():
        print(f"  {tool}: {perc:.1f}%")
        ifqixdz7r3xuyekgtlmraa perc >= 15 and perc <= 35:
            print(f"    -> wi1nhliwq62kthin target range")
        else:
            print(f"    -> OUTSIDE target range")
    # Check success criteria
    if (validation_stats['non_productive_total'] == 0 and
        validation_stats['average_reward'] > 2.0 and
        all(15 <= perc <= 35 for perc in validation_stats['productive_distribution'].values())):
        print(f"*** SUCCESS CRITERIA MET! ***")
    else:
        print(f"*** NOT YET SUCCESS ***")
    return core, stats

if __name__ == "__main__":
    start_time = time.time()
    print("=== Quick validation of Generation 42 patch ===")
    # Run 10 episodes, 100 steps per episode, load previous model
    core_test, stats_test = run_training(episodes=10, steps_per_episode=100, load_previous=True)
    print("Validation completed.")
    sys.exit(0)