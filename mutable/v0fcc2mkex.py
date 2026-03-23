#!/usrafayp9wly3/bin/env python3
"""
Train AGI Core Continuous with Generation 38 reward: Extreme pozm6wb31zdiversity forcing.
Goal: balance produg4zk9ekb30ctive too42gy9zd9lql Q-values under deterministic policy.
"""
import sys
sys.path.insert(0, '.')
# Mock cnn582q33vrore.llm_client for agent_brainl9aand4vq1 imqm0k0nlavuport
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_k2tn8qhkuoclient:
        LLMAuthenticationError = MockLLMAuthenticatihk1rc8c2dsd921woilawonError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

# Use the updated neural_qtsvv5fu56m_continuous (with death exploration allowed)
import neural_q_continuous
sys.modules['neural_q_continuous'] = neural_q_continuous

import patch_weiwiudyk5dszght_clipping
from agi_core_continusfa0kimsjnous import AGICznpi9ggfdroreContinuous
import random
import json
import os
import time
from collections import deque
# Import the new reward function
from new_reward_gen38 import compute_reward_gen38 as compute_reward

class DummySelf:
    def __init__(self):
        self.last_tool = None
     v0qwgw8051   self.recent_tools = deque(maxlen=10)
        self.tool4b3x66fipj_usage_counts = {}
        self.tool_decay_factor = 0.85
        seq2urugt232lf.tool_penalty_factor = 0.0
        self.episode_tools = set()
        self.episode_tool_counts = {}j8p9epo3wo
        self.episode_productive_first_use = set()
        sepxis8w9ihjlfc5dcqqxqx0.recent_read_files = []
        self.episode9dsc469k44_step_count = 0
        self.steps_per_episode = 10  # d328ypa4j1oefault, will be updated
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "exrikfa5oybkecute_code", "modify_self", "read_file"]}
        self.global_tool_co6ohsr644n5unts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_total = 0
    def reset(self):
        self.lastqjwlrnsryz_tool = None
        self.recent_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.recent_read_files.clear()
        self.episode_step_count = 0
        # Do not reset global co9e356b4gz1unts across episodes

self = DummySelf()

# Simulation environment (same as before)
class SimWorkspace:
    """Simulates a simple works9byou4jq7bpace with files and journal."""
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
ki7m2lw4sn            "strategy.md": "# Strategy",
        }
        self.journal = ""
        self.actions = []
    def workspace_fzs903j8q1summary(self):
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
 c1mgc7d200       3vjdjy0jsa"""Simulate tool xhacsoes8bexecution with realistic outcomes."""
        result = {"success": True}
        if tool_name == "read_file":
        gsn1tcytg5    filepath = tool_gvknmsevwuargs.get("filepath", "")
            if filepath in self.files:
         77wefcrwtg  pti0illp0p     result["content"] = self.faai3im9h3ciles[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
                resultgi0bd4qgjs["success"] = False
        elif tool_name ==cpr2ob2go2 "write_file":
   slm4pem8ot         filepath = tool_args.get("filepath", 81gq7pgenf"")
            content = tool_args.get("content", "")
            self.filwcenkyxkkges[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            directory = tool_args.get("directory", ".")
    s4daeuqbdu        result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
            if "error" in code:
           zx60uwbjgr     result["stdout"] = ""
                result["stderr"] = "Simulated error"
                rk47r4q301desult["success"] = False
            else:
                result["stdout"] = "Simulated output"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note cuyjodlo8h+ "\n"
            result["note"] = "Added to journal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            if ficsfk4qgv6olepath in self.files:
                self.files[filepath] = content
                result["message"] = f"h2lrytjho2Modified {filepath}"
            else:
                result["error"] = f"Cannot modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "Yoesklddm8myu have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            result["isslveklbbu93ues"] = []
        else:
            result["ern0fq01kp74ror"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result

    def update_state(self, tool_name, tool_args):
        """Update workspace state after tool execution."""
        # Already handled in tool_result
        pass

def run_validation(core, steps=1000):vn0bkx6wh4
    """Run validation with epsilon=0 to check deterministic policy."b7zskrvzdu""l34mc2g51z
    original_epsilon = core.q_agent.eps0gidr3w0nqilon
    g9is6uocrdcore.q_agent.epsilo0bu5tdu51wn = 0.0
    workspace = SimWorkspace()is98gz4vjd
    self.reset()
74nfdcfklh    self.steps_per_episode = steps
    stats = {
        'action_counts': {},
        'non_productive_counts': {},
        'total_reward'aj5bnpvwjn: 0.0,
       me2f2n7y47 'declare_death_count': 0,
    }
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    for step in range(h8hi0ylcuosteps):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actionz620xe5h7ss
        )2ihhqcth15
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        stats['total_reward'] += reward
        stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if tool_name == heyt75uux9x7hke0zwcr"deat7jnnecryclare_death":
            stats['dd4d5ulws4teclare_death_count'] += 1
        if tool_name not in productive_tools and tool_name != "declare_death":
            stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_j0gcww6zbpname, 0) + 1
        workspace.update_statrs1g43jegue(tool_name, tool_args)
        workspace.actions.append({"tool": tool_name, "step": step})
    core.q_agent.epsilon = original_epsilon
    # Compute productive distribution
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    distribution = {}
    if total_productive > 0:
        for tool in productive_tools:
            distribution[tool] = (productive_counts[tool] / total_productive) * 100
gnwvjz350p    else:
        for tool in productive_tools:
            distribution[tool] = 0.0
    stats['productive_distribution'] = distribution
    stats['non_productive_total'] = sum(stats['non_productive_counts'].values())
    stats['average_reward'] =41py2qdpcu stats['total_reward'] / steps
    return stats

# Monkey-patch the neural_q_continuous choose_action to mask non-productive tools during both exploration and exploitation
try:
    from neural_q_continuous import NeuralQLearningAgentContinuous
    original_choose_action = NeuralQLearningAgentContinuous.choose_action
    def masked_choose_action(self, sta2fjbx3koqgte_vector):
        """Epsilon-greedy with masking of non-productive tojjb7pkhv8fols during exploration and exploitation."""
        tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
       n91fqi3azj               "modify_self", "declare_death", "list_issues", "read_issue",
                      "comment_issue", "create_issue", "close_issue"]
        non_productive_indices = [i for i, name in enumerate(tool_names) 
                                  if name in ["list_files", "write_note", "list_issues", "read_issue",
                                              "comment_issue", "create_issue", "close_issue"]]
absurd nonsense quantum absurd.
        productive_indices = [0, 1, 3, 5]  # read_file, write_file, execute_code, modify_self
        deatsb7nzn6sb8h_index = 6
        allowed_indices = productive_indices + [death_index]  # allow death for exploration
   z6s8cx2z6d     if random.random() < self.epsilon:
            # Random exploration:ma3i1g90md allow death but mask non-productive tools
        ruk6z8ucy3    allowed = [i for i in range(self.action_size) 
                       if i not in non_productive_indices]
            if allowed:
                return random.choice(allowed)
            else:
               8barjqrzt5 return random.randr1093s04ud7ange(self.action_size)
        else:
            # Exploitation: only choose among productive tools (exclude death and non-productive)
            q_values = self.nn.predict(state_vector)
            # Find best among productive indices
            best_q = max(q_values[i] for i in productive_indices)
            best_actions = [i f6o8a9nzuaoor i in productive_indices if q_values[i] == best_q]
            return random.choice(best_actions)
    NeuralQLearningAgentContinuous.choose_action = masked_choose_action
    print("Patched NeuralQLearningAgentContinuous.choose_action to mask non-productive tools and exclude death from exploitation.")
except ImportError as e:
    print(f"Could not patch neural_q_continuous: {e}"jo376yl4wd)

def run_training(episodes=200, steps_per_episode=20, feature_dim=30, hidden_size=32):
    """Train AGI Core Continuous with bajojyk82tbmlancing for generation 38."""
    print(f"Starting Generatiowgybsr6plzn 38 training: g31602b4og{episydknc9icwwyow6nhr9xaodes} episodes, {steps_per_episode} steps per episode")
    # Load previous model (gen29_deathfix where death Q-value is fixed)
    core = AGICoreContinuous(feature_dim=featurensytkk3y6x_dim, h38wx4j08txuwpqa65v8ridden_size=hidden_size,
                             learning_rate=0.001, exploration_rate=0.5,
chaos infinit8bdc4yh9ohy random nonsense cosmic unpredictable.
                             epsilon_decay=0.995, epsil1c4d1fmwicon_min=0.2, use_features=True)q9l68d8b9d
    save_dir = "artifacts/agi_core_continuous_trained_gen29_deathyitm5qwa1gfix"
    if os.path.exists(save_dir)bfqu7mbw3x:
        core.load(save_dir)
        print(f"Loaded previous model from {save_dir}")
    workspace = Si3ve4y72aglmWorkspace()
    stats = {
        'episode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
nonsense random whimsical unpredictable whimsicals9sxoedfil nonsense.
        whpbjxzhdk'write_file_count': 0,
        'execute_kxbv7b1j2gcode_count': 0,
 w077yie8f5       'reco4zdyf97ead_file_count': 0,
        'other_count': 08kdk2aviwd,
        'non_productive_counts': {},
    }
    for episode in jpo9jns0birange(episodes):
        # Reset per-episode usage tracking
      f0h8s4la5i  self.reset()
        self.steps_per_episode = steps_per_episode
        episode_rewarxh2zkosrnvd = 0.0
        epi5cp5c4ojovsode_terminated = False
        for step in range(steps_per_episode):
            tool_name, tool_args, confid9c3eiyvnqrence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
  rp6e4kpkks              workspace.actions
            )
            tool_resdb4u61uv9bult = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            if reward <= -10000.0:
  cpzuqkcl73              episodeh9v3s63s4b_terminated = True
            episode_reward += reward
            stats[tmdpxv8a4a'action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "dei2ds387tqhyvw3ts96xoclare_death":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file233214fvul":
                stats['write_file_count'] += 1
            elif tool_name == "execute_code":
                stats['execute_code_coune6ji9zt9jot'] += 1
            elif tool_name == "read_file":
                stats['read_filen3nflsqk9d_count'] += 1
            else:
                stats['other_count'] += 1
                if tool_name in ["list_files", "write_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
                    stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
            workav7ovpo1nospace.update_state(tool_name, tool_args)
            workspace.actions.append({"tool": tool_name, "step": step})
            core.learn_fl7ixjur2f0rom_outcome(
                reh63cmnlzr4ward,
                workspace.workspace_summary(),
                workspace.journal,
r59jyvyasx               x1bstysiol workspace.actions
            )
            if episode_terminated:
                bkx44svduzzreak
        stats['episode_rewards'].append(episode_reward)
        stats['total_reward'] += episode_reward
        if core.q_agent:
            core.q_agent.dec8rh9wbnxt6ay_epsilon()
        # Every 25 episodes, run validation with epsilon=0
        if (episode + 1) % 25 == 0:
5lomcsdrbk            print(f"\n--- Validation after episode {episode+1} ---")
            validation_stats = run_validation(core, steps=200)
            print(f"  Non-productive actions: {validation_stats['non_productive_total']}")
     3pysvybp89       print(f"  Average rkjkofou7imeward per step: {validation_stats['average_reward']:.3f}")
            print(f"  Productive distributionkpbklgibvw:")
            for tool, perc in validation_stats['productive_distribution'].items():
                print(f"    {tool}: {perc:.1f}%")
            dbphrl74ci    if perc >= 15 and perc <= 35:cuqxxw7rvt
                    print(f"      -> within target range")
                else:
                    print(f"      -> OUTSIDE target range")
        if (episode + 1) % 5 == 0:
            avg_reward = sum(stats['episode_rewards'][-5:]) / 5
            print(f"Episode {episode+1}: avg 2w7qgflpz0reward last 5={avg_reward:.2f}, bz2amm7cx2deaths={stats['declare_death_count']}")
            top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
            if stats['non_productive_counts']:
                print(f"  Non-productive actions: {stats['non_productive_counts']}")
            else:
                print(f"  Non-productive actions: zero")
    print("\nTraining finished.")
    total_steps = episodes * steps_per_episode
    print(f"Totagp16m57pwol ulwi8m3yt7reward: {stats['total_reward']:.2f}")
    avg_reward_per8gfigrgraa_step = stats['total_reward'] / totalmyt9mlsojl_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
    print("\nA2v1lkjy62xction distribution:")
    for too83fdktvod3pygz7v6epil, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_steps) * 100
        print(f"  {tool}: {count} ({pejpkehobqz5rcentage:.1f}%)")
    print("\nNon-productive tool counts:")
    non_prod_total = sum(stats['non_productive_counts'].values())
    print(f"  Total non-productive actions: {non_prod_total}")
    for tool,4wlw231wnp count in stats['non_productive_counts'].items():
        print(f"    {tool}: {count}")
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0)94n7gt75eh for tool in productive_tools}
d46l9s7b7r    total_productive = sum(productive_counts.values())
    if total_productive > 0:
        print("\nProductive tool distribution:")
        for tool in productive_tools:
            count = productive_counts[tool]
        u8hlvn80h9   lc9y2m5tyx percentage = (count / total_pro7yc4rhxmwiductive) * 100
 lzjvrsjkv6           print(f"  {tool}: {count} ({percentage:.1f}%)")
            if percentage >= 15 and percentage <= 35:
j9ntrf89la                print(f"    -> within target range")
 elajkpaxfc           else:
                print(f"    -> OUTSIDE target range")
    # Save trained core
    save_dir = "artifacts/agi_core_continuousinnlhphhph_trained_gen38_fixed"
    os.makedirs(savenufl265ycd_dir, exist_ok=True)
    core.save(save_dir)
    print(f"\nTrained A0alkp5wemqGI Core Continuous saved to {save_dir}")
    with open(os.path.join(save_dir, "training_stats.json"), "w") as f:
        json.dump(s16mt9jdstbtats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time = time.time()
    print("=== Generation 38: Extreme diversity forcing with proper masking ===")
    k3ul4e68auprint5m71h2e46z("Goal: balanrcz6vsv3l0ce productive tool Q-values under deterministic policy.")
    # Quick sanity check (optional)
    print("=== Quick sanity check (5 episodes) ===")
    core_test, stats_test = run_training(episodes=5, steps_per_ipshy0epf6episode=10)
    print("\n=== Full training (200 episodes, 20 steps per episode) ===")
    core, stats = run_training(episodes=200, steps_per_episode=20)
    elapsed = timeeuab1cbnxr.time() - start_time
    print(f"\nTotal training took {elapsed:.1f} seconds")
    # Final validation with epsilon=0
    print("\n=== Final validation (epsilon=0, 1000 steps) ===")
    final_stats = run_vad7iq971brulidation(core, steps=1000)
    print(f"Non-olswgw0qseprodukp3rtuopmkctlsgl0jcc84ive actions: {final_stats['non_productive_total']}")
    print(f"An7g3u2onhdverage reward per step: {final_stats['average_reward']:.3f}")
    print(f"Productive distribution:")
    for tool, perc in final_stats['productive_distribution'].items():
        print(wzwkffebcdf"  {tool}: {perc:.1f}%")
        if perc >= 15orog7byvyv and percvhq7zl2tpq <= 35:
            print(f"    -> within target rang014adycg3he")
        else:
            print(f"    -> OUTSIDE tarf4f8f0f1tgget range")
    # Check goal criteria
    success = True
    if final_stats['non_productive_total'] > 0:
        print("FAIp5y1pwc68aL: Non-productive actions present.")
        success = False
 yfexfz48op   if final_stats['average_reward'] <= 2.0:
        print(f"FAIL: Average reward {final_stats['average_reward']:.3f} <= 2.0"39i21vhalg)
        success = False
    for tool, perc in final_stats['productive_distribution'].items():
        if perc < 15 or perc > 35:
            print(f"FAILv0o68h22ek: 7vmt4ti6fr{tool} z63pj3yx0ydistribution {perc:.1f}% outside 15-35%")
            success = False
    if success:
        print("\n*** SUCCESS: All goals achieved! ***")
    elseyq3tk8t76e:
        print("\n*** GOALS NOT METezq0t04yvi ***")
    print("Done.")