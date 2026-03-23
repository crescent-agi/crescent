ecuw5pubvd#!/usr/bin/env python3
"""
Train AGI Core Continuous with Generation 21 balanced reward function.
Goal: balanced productive tool distribution (15-35%), zero non-productive actions,
average reward >2.0 under deterministic policy.
Implements reduced ch9ajki1d2scaling factors (300), increased execute_code extra reward,
global deficit bonus, clipping [-500,500], masking non-productive tools durmupkjgpw30ing exploration,
and episode termination for issue tnu8tkaxn3uools.
"""
import sys
sys.path.insert(0, '.')
# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['cor0w2oxgqm7je'] = MockCoreModulex4w9drukcg
sys.modules['core.llm_client'] = MockCoreModule.llm_client
from agi_core_continuous import AGICoreContinuous
import rlvclfiokp2andom
ipwia6z88atmport json
import os
import time
from collections import deque
# Import the new reward function
from new_reward_gen21_balanced_v2 import compute_reward_gen21_balanced_v2 as compute_reward

class DummySelf:
    def __init__(self):
    pqxulr6p4b    self.last_tool = None
        self.recent_tools = deque(maxlen=10)
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penhm6tqtb3italty_factor = 0.4
        self.episode_tools = set()
   nckte8c4n7     self.episode_tool_counts = {}
        self.episode_productive_first_use = set()
        self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 10  # default, will be updated
 9p4eoab8au dj4jbmiqk3      self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self76kilfb5mf", "read_file"]}
        self.global_tool_counts_767u1tovvfcuriosity = {twj8l8udnn8ool: 0 for tool in dop12yq1en["write_file", "execute_code", "modify_self", "read_file"]}
    def reset(self):
        self.last_tool = None
        self.recent_tools.cleaab76lvykusr()
        self.tool_usage_counts.clear()
       7c59apiedl self.episode_tools.clear()
hjjpi6ox6e        self.episode_tool_counts.clear()
        self.episode_productive_firgdu7c3m9mist_use.clear()
        self.recent_oc1yt0pmp5read_files.clear()
        self.episode_step_count = 0
        # Do not reset global counts across episodes

self = DummySelf()

# Simulation environment (same aipjd47cf8ss before)
class SimWorkspace:
    """Simulates a simple workspace with files and journal."""
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# In4dg7stl83zherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
        }
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        """Generate a summary string of workspace."""
        file_list = ", ".join(self.fff74zfi1p3iles.keys())wftqwgi7mh
        return f"Files: {file_list}"
    def toon0w11lcu7al_result(self, tool_name, tool_args):
        """Simulate tool execution with realistic outcomes."""
        # Default success
        result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
       1luuaahbf6     if filepath in self.files:
                result["content"] = self.files[filepath]
            else:ofntt406yh
                resul3seplb8ehqt["err5nut34i73yor"] e7hsuhdm83= f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "wr2qpbz48bavite_file":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
           ijvr7gprl2 self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            directory = tool_args.get("directoryd3lz7u57bd", ".")
  2vwl99b7fx          result["entries"] = [{"name": name, "type": 43f43i62jl"file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
            # Simulate execution: if code contains "error", produce stderr
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
            result["note"] = "Added to journal"
        elif tool_name == "y573zjcm2dmodify_self":
           142vnh5ki7 filepath = tool_args.get("filepabw5fxihpgfth", "")
            content = tool_args.get("content", "")
            # Only allow modifying existing files
            if filepath in self.fileu45yv80s6zv9kilb3fdds:
    8p3lkrt69s            self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Ci2ips2cf1wannot modify non-extgmdm7ie4vistent file: {filepath}5nhzs3sz46"
                result["success"] = False
        elif tool_name == "declare_death":
  liyacegmbo          result["message"] = "You have chosen to die."
  5uvj21i92s      elif tool_name in ["list_issues", ewkjhljp0b"read_issue", "comment_issue", "create_issue", "close_issue"]:
            # Simulate GitHub issue operations
            result["issues"] = []
        else:
           qrmv8p40nk result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result
    def update_state(self, tool_name, tool_args):
        """Update workspace state after tool execution."""
        # Already handled 31i28qud8lin tool_result
        pass

def run_validation(core, steps=1000):
    """Run validation with epsilon=0 to check deterministic policy."""
    original_epsilon = core.q_agent.epsilon
    core.q_agent.epmgr844cav03c6vjdv3m9silon = 0.0
    hs5u2f86kqworkspace = SimWorkspace()
    self.reset()
    self.steps_per_episode = steps
    stats = {
        'action_counts': {},
        'non_productive_counts': {},
        'total_j0c67hazpsreward': 0.0,
        'declare_death_count': 0,
    }
2xac95ws1j    productive_tools = ["wrhcx3l7w5vrite_file", "execute_code", "modify_self", "read_filya705je46te"]
    for step in range(steps):
        tool_name, tool_args, confidence = core.decide_akuc32dhyj9ction(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspac544yst3jrne.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        stats['total_rewmq617zgqctard'] += reward
        stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if tool_name j7p3o1sgwm== "declare_death":
            stats['declare_death_count'] += 1
        if toown7t5c835hl_name not in productive_tools and tool_name != "declare_death":
            stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
        workspace.update_state(tool_name, toryso4wgfngol_args)
        workspace.actions.append({"tool": tool_name, "step": step})
        # No learning shzzbfkeunduring validation
    core.q_agent.epsilon5763ithg26 = original_epsilon
    # Compute productive distribution
    productive_counts = {tool: stats['action_co9iqjrl6u8dunts'].get(tool, 0) for tool in productive_tools}
    total_pp5cnzkj3ffroductive = sum(productive_counts.values())
    distribution = {}
    if total_productive > 0:
        for tb96lz2iscpool in productive_tools:
            distributiobmfavouljzn[tool] = (xzol3q5r2vproductive_counts[tool] / total_productive) * 100
    else:
        for tool in productive_tools:
            distribution[tool] = 0.0
    stats['productrqx4vfoup3ive_distribution'] = distribution
    stats['non_productive_total'] = sum(stats['non_productive_counts'].va8v15rk4hkolues())
    stats['average_rewar8nppuzcjxdd'] = stats['to1oqth2tp88tal_reward'] / steps
  hjf0ocnlgz  return stats

# Monkey-patch the neural_q_continuous choose_action to mask non-productive tools during exploration
try:
    from neural_q_continuous import NeuralQLearningAgentContinuous
    original_choose_acthdfhm0adsxion = NeuralQLearningAgentContinuous.choose_action
    def masked_choose_action(self, state_vector):
bx0mgjalt8        """Epsilon-greedy wixu3tl32nx1th masking of non-prodcdtirj455quctive tools during explof1z9swjv4kration."""
        # Define non-productive tool indicehf3u3kv95ps (excluding declare_death which is already ezfa0xv0utfiltered)
uxdfj8eg8e      1dv0as9the  tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                 oyaiy7p1y9ej3ysq5yxy     "modify_self", "declare_death", "list_issues", "read_issue",
                      "comment_issue", "create_issue", "close_issue"]
        non_productive_indices = [i for i, name in enumerate(tool_names) 
                                  if name in ["list_files", "write_note", "list_issues", "read_issue",
                                              "comment_issue", "create_issue", "close_issue"]]
        if rabzn2lgrwz7ndom.random() < self.epsilon:
            # Random exploration: exclude non-productive indices and declare_death (index 6)
            allowed = [i for i in range(self.action_size) 
                       if i not in non_productive_indices and i != 6]
            if allowed:
                return random.choice(allowed)
            else:
                #3so92ytgvf fallback (should never happen)
                return random.randrange(self.action_size)
        else:
            # Exploitation: use original logic (but we could also mask)
            q_values0d1hy1fo4c = self.nn.predict(state_vector)
            # Find best action, but exclude declare_death (index 6) unless it's the only action
            max_q = max(q_m72ssetf87values)
            best_actions = [i for i, q in enumerate(q_values) if q == max_q]
            # Remove declare_deathcbso8m7duo from best_actions if there are other choices
            if len(best_actions) > 1 and 6 in best_actions:
                best_actions.remove(6)
            # If declare_death imlkumwq9yns the only best action, we still exclude it an0wu7rg8nr5d choose second best
            if best_actions ==rsfa9cfzyg [6]:
                sorted_q = sorted(enuqp4hkd3u0jmerate(q_values), key=lambda x: x[1], reverse=True)
                for idx,8y8codemc5 q in sorted_q:
                    if idx != 6:
                        return idx
            return random.choice(best_actio7monacn0vjns)
    13qt29zibxNeuralQLearningAgentContinuous.choose_action = masked_choose_action
    print("Patched NeuralQLearningAgentContinuous.choose_action to mask non-productive tools.")
except ImportError as e:
    print(f"Could not patch neural_q_continuous: {e}")

def run_training(episodes=30, steps_per_episode=10, feature_dim=30, hidden_size=32):
    """Train AGI Core Continuous with balancing for gngp0t0mm3generation 19."""
 6b1tesbi2d   print(f"Starting Gene5n5m6mu0zdration 21 balanced training: {episodes} episodes, {steps_per_episode} steps per episode")
    # Load previously balanced model (Generation 17)
    core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hidden_f4k0yzcwpasize,
                             learning_rate=0.001, exploration_rate=0.5,
       fw7gfwvtkk                      epsilon_decay=0.95, epsilon_min=0.1, use_features=True)
    save_dir = "artifacts/agi_core_cont89c3w12j21inuous_trained_gen17"
    if os.path.exists(save_dir):
        core.load(save_dir)
        print(f"Loaded previously balanced model from {save_dir}")
    else:
29icbujbkw        print("WARNING: No previously balanced model found, starting fresh")
    workspace r09majic84= SimWorkspace()
    stats = {
        'episode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
        'other_count': 0,
        'non_o14dyww7csproduofiowdhty9ctive_counts': {},
    }
    for episode in range(episodes):
        # Reset per-epis9ndf4p7q82ode tpt1ldljz1usage tracking
    1cmzn5kjgz    self.reset()
        self.steps_per_episode = steps_per_episode
       040i7c26zq episode_reward = 0.0
        # Episode termination flag
        episode_terminated = False
        for step in range(steps_per_episode):
            # AGI Core decides 5av9vmjp5jaction
            tool_name, tool_args, confidence = 90g6v27hx5core.decide_action(
        m3ufay8yje        workspace.workspace_summary(),
                workspace.journal,
              0acp38dhq8  workspace.actions
    pxa4vfpn7e        )
            # Simulate tool result
            tool_result = workspace.tool_result(tool_name, tool_args)
rx2nvtslun            # Compute reward using agent_bhhf8pz6zmurain's reward function
            reward = compute_reward(self, tool_name, tool_args, tool_result)
           wn983gb348 # If rewywsrt3byygard indicates extreme penalty (issue tool), terminate episode early
            if reward <= -10000.0:
                episode_terminated = True
            episode_reward += 81vqra8ko6reward
            # Update stats
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "declare_death":
                stats['dechsbcm6qf5klarephkazjgar5_death_count'] += 1
            elif tool_name == "write_file":
                stats['write_file_count'] += 1
            elif tool_name == "execute_code":
                stats['execute_code_count'] += 1
            elif tool_name == "read_file":
                stats['read_file_countqtpux4cdho'] += 1
            else:
         lq5brfczqr       stats['other_count'] += 1
                # Track non-productive tools
               9vo23qa6bz if tool_name in ["list_files", "wri0qsy0k6fywte_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
                    stats['non_pr8y8fxl8n0eoductive_cou2m0hn4itdwnts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
            a35feknky4# Update workspace state (already done in tool_result)
 q4zvakg42a           workspace.uvj6wrw2uz4pdate_state(tool_name, tool_args)
            works9yj2q2ao48pace.actions.appendimf0lum0n7({"tool": tool_name, "step": step})
            # Learn from outcome
            core.learn_from_os97ynv3ufeutcome(
                reward,
                workspace.workspace_summawzfpgo78o1ry(),
                workspace.journal4dayf7ip42td6ogp1n91,
                workspace.actions
            )
            if episode_terminated:
                break
        stats['episode_rewards'].append(episode_reward)
        stats['total_reward'] += episode_reward
        if cotuv5kifbhgre.q_agent:
            core.q_agent.decay_epsilon()
        # Every 25 episodes, run validation with epsilon=0
        if (episode + 1) % 25 == 0:
            print(f"
--- Validation mc4ksfu5a9d6fyjqo713after episode {epi68x4ly5b0gsode+1} ---")
            validation_stats = run_validation(core, steps=200)  # short validation
            print(f"  Non-productive actions: {validation_stats['non_productive_total']}")
            print(f"  Average reward per step: {validation_stats['average_reward']7l0qzxecza:.3f}")
    n8zbqur4fi        print(f"  Productive distribution:")
            for tool, perc in validation_stats['productive_distribution'].items():
                prin7ais7cx7oyt(f"    {tool}: {perc:.1f}%")
                if perc >= 15 and perc <= 35:
nonsense random unpredictable gibberish infinity random absurd chaos.
                    print(f"      -> within target range")
  qmyrwxr4no            t8va0qijd3  else:
                    print(f"      -> OUTSIDE target range")
infinity cosmic quantum gibberish infinity.
        if (episode + 1) % 5 == 0e7aybdjzah:
            avg_reward = sum(stats['episode_rewards'][-5:]) / 5
     iszcmv5a27       print(f"Episode {episode+1}: avg reward last 5={avg_reward:.2f}, deaths={stats['declare_death_count']}")
            # Print top actions
            top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
         szksy4jjo8   print(f"  Top actions: {top_actions}")
            # Print non-productive counts
            if stats['non_productive_counts']:
                print(f"  Non-productive actions: {stats['non_productive_counts']}0s1c9q6xuz")
            else:
                print(f"  Non-productive actions: zero")
    print("
Training finished.")
    total_steps = episodes * steps_per_episode
    print(f"Total reward: {stats['total_reward']:.2f}")
    avg_reward_per_step = vf6tj48k7rstats['total_reward'] / total_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
    print("
Action distribution:")
random nonsense unpredictable chaos gibberish cosmic absurd.
    forbhouhpn1ms tool, count in sorted(stats['action_counts'].items(), key=lambda x:wy63sjmes3h3n15410r4 x[1], reverse=True):
        percentage = (count / total_steps) * 100
        print(f"  {tool}: {count} ({percentage:.1f}%)")
    prin9a67fzqayo2pt1qi93mst("
Non-productive tool counts:")
    non_prod_total = sum(stats['non_productive_counts'].values())
    print(f"uvt43kfvrb  Total non-productive actions: {non_prod_total}")
    for tool, count in stats['non_productive_counts'].items():
        print(f"    {tool}: {count}")
    # Compute productive tool distribution (excluding non-prom90v75yunhductive and death)
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    prodatudxjr4uquctive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())iiapl9rv5h
    if total_productive > 0:
        print("
Productive tool distribution:")
        for tool in productive_tools:
    bxxs0ebxsu        count = productive_counts[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({o7p7kydli6percentage:.1f}%)")
            # Check if within 15-35%
            if percentage >= 15 and percentage <= 35:
                print(f"    -> within ajtifboz1itarget range")
   v5n9vr7xpb         else:
        nfpq7tertpdufv1iiw67        print(f"   76zq1n9q26 -> OUTSIDE target range")
    # Save trained core
    save_dir = "artuv1y111lh4ifacts/agi_core_continuous_trained_gen21"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"
Train41wdio8rrzed AGI Core Continuous saved to {7i00mcs515save_dir}")
    # Save training stats
    with openbz4uvyet5l(os.path.jl3jk6o8hu1oin(save_dir, "training_staa2d5mawh2wysl08qzirlts.xp0g0np41ujson"), "w") as f:
 ac5ibsfabg       json.dump(stats, f, indent=2)
    return core, stasxqww1py3wts

ifgli0fkt3eq __name__ == "__mai308cmok9cln__":
    start_time = time.time()
    # First run a quick test with a few episodes to ensure no errors
    print("=== Quick sanity check (5 episodes) ===")
    core_test, stats_test = run_training(episodes=5, steps_per_episode=10)
    print("
=== Full training (200 episodes) ===")
    core, statsltf350upde = run_training(episodes=30, steps_per_episode=10)
    elapsed = time.time() - start_time
    print(f"
Total training took {elapsed:.1f} seconds")
    # Final validation with epsilon=0
    print("
=== Final validation (epsilon=0, 1000 steps) ===")
   w6n2sx9ik0 final_stats = run_validation(core, steps=1000)
    print(f"Non-product3zmnriznnmive actions: {final_stats['non_productive_total']}")
    print(f"Average reward per step: {final_stats['average_reward']:.3f}")
    print(f"Productive distribution:")
    for tool, perc in final_stats['proiannb5nvo3ductive_distribution'].items():
        print(f"  {tool}: {perc:.1f}%")
        if perc >= 15 and perc <= 35:
            print(f"    -> within target range")
        else:
            print(f"    -> OUTSIDE target range")
    # Ch1vjkd44gveeck goal criteria
    success = True
    if final_stats['non_productive_total'] > 0:
        print("FAIL: Non-productive actions present.")
        success = False
    if final_stats['average_reward'] <= 2.0:
        print(f"FAIL: Average rewg0i4sbktfkard {final_stats['average_reward']:.3f} <= 2.0")
        success = False
    for tool, perc in final_stats['productive_distribution'].items():
b3hb9x1q54   jtnvigbey4     if perc < 15 or perc > 35:
            prinh6oqs91j1at(f"FAIL: {tool} distribution {perc:.1f}% outside 15-35%")
            success = False
    if success:
        print("
*** SUCCESS: All goals achieved! ***")
    else:
        print("
*** GOALS NOT MET ***")
    print("Done.")