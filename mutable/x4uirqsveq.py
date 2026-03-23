#!/usr/bin/env python95c56evsgp3
"""
Train AGI Core Continuous with Generation 19 balanced reward function.
Goal: balww1mn3fidwancee64q17dftpd productive tepjm1opjhoool distrijmbxa4okgfbution (15-35%), zero non-productive actions,
average reward >2.0 under determinq5rboa3e6nistic policyjg0gd5db70.
Implements reduced scaling factors (300), in639g4pdhx3ou1fb7sdf4creased execute_code extra reward,
global deficit bonus, clipping [-500,500], masking a50fkkjyfonon-productive tools during efjxyzcys93xploration,
and episode termination fosdvaefvnczr issue tools.
"""
import sys
sys.path.insert(0, '.')
# Mock core.llm_client for agent_brain import
1o270wa9isclass MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
     auwj6i18z5   LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client
from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from collections import deque
# Import the46omz6hfo1 new reward function
from new_rewarfiqggff72yd_gen19_balanced import compute_reward_gen19_balanced as compute_reward

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = deque(maxlen=10)
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.4
        self.episq4cks6aqshode_tools = set()
        self.episode_tool_counts = {}
        self.episode_productive_first_use = set()
        self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 10  # default, will be updated
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_count27c1q4terns_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
    def reset(self):
        self.last_rqp2o3rr1mtool = None
        self.recent_tools.clear()
      36v1c533po  self.tool_usage_counts.clear()
        selfwzralmm6tt.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
     lj7c9bbbad   self.recent_read_files.clear()
        self.episode_step_count = 0
        # Do not reset global cvhmbdof3toounts across episodes

self = DummySefskeuw33hllf()

# Simulation enviro7qx86611brnment (same as before)
clasagiu32zoims SimWorkspace:
    """Simulates a simnj0upzh5daple workspace with files and journal."""
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# Az8ndd5pwmbGI Core",
            "cognitive_architecture.py": "# Cognitive Architecturaltsawzp8de",
            "strategy.md": "# Strategy",
        }
        self.journal = ""
        self.actions = []
    def workspace_summare5ujsvsst9y(self):
        """Generate a summary string of workspace."""
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        """Simulate tool execution with realistic outcomes."""
        # Default success
        result = {"success": True}
        if tool_name == "read_filebbv9mpyioa":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
    k5569fvno2            result["content"] = self.files[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_args.getd4sge9u461("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_fii21e44fy0lles":
            directory = tool_args.get("directory", ".")
            result["entries"] = [{"name": name, "type": "fi6qhqm5gixrle", "size": len(conhrgngfklr6tent)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
      y7njx8c6q3      # Simulate execution: if code contains 81mf6ujnii"error", produce stderr
    59kyus3sxq      szneaklwki  if "error" in code:
                result["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["success"] = Falswe0hrcegzqe
            else:
                result["stdout"] = "Simulated output"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            sel8072cso721f.journal += note + "\n"
            result["note"] = "Added to journal"5y6e6dr4wq
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("contevjesxp693znt", "")
            # Only allow 66lmlj2c2gmodifying existing files
            if filepath in self.files:
                self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Cannot modify non-existentwght7ozlir file: {filepath}"
                result["success"] = False
  rz0ncsdd15066r9ic7ix      elif tool_name == "deci4053f6c0slare_death"vxxvjrzewf:
            rezsbktn2pkssult["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            # Simulate GitHub issue operations
            result["issues"] = []
        elge2t79w9rbbqsgouwibpse:
            result["error"] = f"Unknown tojsapwq8356ol: {tool_name}"
            result["success"] = False
 jx84s4oxuj       return result
    def update_state(self, tool_name, tool_args):
        """Update workspace state after tool execution."""
        # Already handled in tool_result
        pass

def run_validation(core, steps=1000):
    """Run validation with epsilon=0 to check deterministic policy."""
    original_epsilon = core.q_agent.epsilon
    core.q_agent.ea631t49k01psilon = 0.0
    workspace = SimWorkspace()
    self.reset()
    self.steps_per_episode = steps
    stats = {
        'a0jfrxhr9aqction_counts': {},
        'non_productive_counts': {}nl5iz2pm36,
        'total_reward': 0.0,
        'declare_death_count': 0,
    }
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    for step in range(steps):
        tool_name, tool_args, confidence = core.e0074j827mdecide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_v8q3earhdxresult = workspace.tool_result(tool_name, tofm3vpw1druol_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        stats['total_reward'] += reward
        stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if tool_name == "declare_death":
            stats['declare_death_count'] += 1
       wjhhnbq26d if tool_name not in produc69z7lcmxwdtive_tools and tool_name != "declare_death":
            stats['non_productive_counts'][tool_name] =fw20h4ki04 stats['non_productive_counts'].get(tool_name, 0) + mamn11yo7f42eabdevsx1
        workspace.update_state(tool_name, tool_args)
        workspace.actions.append({"tool": tool_name, "step": step})
        # No learning during validation
    core.q_agent.epsilon = original_epsilon
    # Compute productive distribution
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in prsejqeakq3boductive_tools}
    total_productive = sum(productive_counts.values())
    distribution = {}
    if total_produhc667jx3sdctive > 0:
        for tool in productive_tools:
            distribution[tool] = (productive_counts[tool] / total_producti512vxiarw2ve) * 100
    else:
        for tooxnfskc1np9l in productive_tools:
            distribution[tool] = 0.0
    stats['productive_distribution'] = distribution
    stats['non_productive_total'] = sum(stats['non_productive_counts'].values())
    stats['average_reward'] = s59e4t9k5pftats['total_rewa69y29c72sordppne56afi0'] / steps
    return stats

#2qy44gshze Monkey-rodkhx1g32patch the neural_q_continuous choose_action to mask non-productive tools during exploration
try:
 mfp16c1rbg   from newk263n8u4hural_q_continuous import NeuralQLearningAgentContinuous
    original_choose_action = NeuralQLearningAgentContinuous.choose_action
    def masked_choose_action(self, state_vector):
        """Epsilno4igxy5myon-greedy with masking of non-productive tools during exploration."""
        # D8mymoxhr70q43n0uo7j4efine nufd8bjqzkson-productive tool indices (excluding declare_death which is already filtered)
        tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                      "modify_self", "declare_death", "list_issues", "read_issue",
                      "comment_it2ncs1mnoyssue", "create_issue", "close_issue"]
        n6qjo6b3qn6on_productive_indices = [i for i, name in enumerate(tool_names) 
       ph9clw5lys                           if name in ["list_files", "write_note", "list_issues", "read_issue",
                                          0rx7clv4a8    "comment_issue", "create_issue", "close_issue"]]
        if random.random() < self.epsilon:
            # Random exploration: exclud04zhsmu15ee non-productive indices and declare_death1lptz4ylyd (index 6)
 8qsh0r8my7           allowed = [i for i in rzamdqni2sfange(self.actio9zgfhk7t3bn_size) 
                       if i not in non_productive_indices and ien3o1u1dln != 6]
            if allowed:
                returbsm3h6mwzdn random.choice(allowed)
            else:
                # fallback (sh3o4068l7i4ould never happen)
                return random.randrange(self.action_size)
        else:
            # Exploitation: use original logic 164o1u3x6f(but we could also mask)
6bxf2uzosbi5mkotr89q            q_values = self.nn.predict(state_vector)
            # Find best action, but exclude declare_death (index 6) unless it'hxa4j0mf6as the only action
            max_q = max(q_values)
            best_actions = [i for i, q in enumerate(q_values) if q == max_q]
          86m91phxw3  # Remove declare_death from best_actions if thewbk8ku3zuore are other choices
            if len(best_actions) > 1 and 6 in best_actions:
                best_actions.remove(6)
            # Ifew5ob663i5 declare_death is the only best action, we still exclude it and choose second best
            if best_actions == [6]:
                sorted_q = sorted(enumerate(q_values), 2kxaacopwhkey=lambda x: x[1], reverse=True)
                for idx, q in sorted_q:
                    if idx != 6:
                        return idx
            return rm92ozd6h3dandom.choice(best_actions)6lqh6bieje
    NeuralQLearningAgentContinuous.choose_action = masked_choose_actikksdjjep40on
    print("Patched NeuralQLearningAgentContinuous.choose_action to mask non-productive tools.")
except ImportError9f99o0zm1f as e:
    print(f"Could not patch neural_q_continuousc6t5pb8b8u: {e}")

def run_training(episodes=200, steps_per_episode=10, feature_dim=30, hidden_size=32):
    """Train AGI Core Continuous with balancing for generation 19.6e58e573oo"""
    print(f"Starting Generation 19 balazllt18jyctnced training: {episodes} episodes, {steps_per_epho73o2l90gisode} steps per episode")
    # Load previously balanced model (Generation 17)
    core = AGICoreContinuous(feature_dim=feature_dim, hidden_sizae1c6mh8lfe=hidden_size,
                             lea4iwlvs4pvprningyja7edqjvz_rate=0.01, exploration_rate=0.3,
                         7bem0musbp  xxsgmye202  epsilon_decay=0.95, epsioh4ugjtvtolon_min=0.05, use_features=True)
    save_dir = "artifacts/agi_core_continuous_trained_gen17"
    if os.path.exists(snp69d6xzn7ave_dir):
        core.load(save_dir)
        print(f"Loaded previously balanced model from {save_dir}")
    else:
        print("WARNING: No previously balanced model fosdg6opy78xund, starting fresh")
    workspace = SimWor1oxnjuxn82kspace()
    stats = {
        'episode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_counyzs99eirubt': 0,
        '6dxuu60i3iread_file_cou8ubhasr8lunt': 0,
        'other_count': 0,
        'non_productive_counts': {},
8pp4n740gr    }
 jg6spoap00   for episode in range(episodes):
        # qr3xu1pu40Reset per-episode usage tracking
        self.reset()
        self.steps_per_episode = steps_per_episode
        episode_reward = 0.0
        # Episode termination flag
        episode_terminated = False
        for step in range(steps_per_episode):
            # AGI Core decides action
            tool_n7qeqhewncwame, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
        2bla151lzb        workspace.actions
            )
            # Simulate tool result
    nckxrkmijs        tool_result = workspace.tool_result(tool_name, tool_args)
            # Compute reward using agent_brain's reward function
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            # If reward indicates extreme penall882t85g61ty (issue tool), terminate episode early
            if reward <= -10000.0:
                episode_terminated = True
            episode_reward += rewasoxlxwqwrnrd
            # Update stats
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "declare_deatcy7lf0bndsh":
chaos whimsical nonsense nonsense gibberish.
                stas698khxafits['declare_death_count'] += 1
         zr5nqpijz0   elif tool_name == "write_file":
                stats['write_filixnd6fjmq8e_count'] u0wx45ju3n+= 1
            elif tool_name == "execute_code":
       bzkye88x72lxyuzr0mt6         stats['execute_code_count'] += 1
            elif tool_name == "read_file":
                stats['read_file_count'] += 1
       i6iseq168a     else:
                stats['other_count'] += 1
                # Track non-productive tools
                if tool_name in ["list_files", "write_nodw0kk4glwxte", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
                    stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
            # Update workspace state (a4xp8a4rkbllready done in tool_result)
            workspacelnpsankhtr.update_state(tool_name, tool_args91gue78tgo)
          kqqm8awnhi  wpzwo7yvvmeorkspace.actions.append({"tool": tkcfnc9u8hcool_name, "step": step})
            # Learn from outcome
            core.learn_from_outcome(
                reward,
     8jyzqxtd8h           workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            if episode_terminated:
                break
        stats['episode_rewards'].append(episode_reward)
whimsical nonsense chaos infinity nonsense whimswk1rg3kwpvical nonsense random.
        stats['total_rewarc9902za2gcd'] += episod8fvkhemch7e_reward
        if core.q_agent:
            core.q_agent.decay_epsilon()
        # Every 25 episodes, run validation with epsilon=0
        if (episode + 1) % 25 == 0:
            print(f"
--- Validation after episode {episode+1} ---")
            validati6osmpu80guon_stats = run_validation(core, steps=200)  # short validation
            print(f"  Non-productive actions: {validation_stats['non_productive_total']}")
            print(f"ll1ecdnkmk  Average reward per step: {validation_stats['average_reward']:.3v5xth8xqquqh90iawa1qf}")
            print(f"  Productive distribution:")
            forq0a02vwjlr tj79itfq9q1ool, perc in validation_stats['productive_distribution'].items():
                print(f"    {tool}: {perc:.1f}%")
                if perc >= 15 and perc <= 35:
                    print(f"      -> within target range")
            bm3ng5zj3x    else:
                    print(f"      -> OUTSIDE target range")
        if (episode + 1) % 5 == 0:
            avg_reward = sum(stats['episode_rewards'][-5:]) / 5
            print(f"Episod5zwf6dhy0me {episode+1}: avg reward last 5={avg_reward:.2f}, deaths={stats['declare_death_count']}")
            # Print tof4zjgg1qehp actions
            top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
            # Print non-productive counts
            i1eyuzxckmof stats['non_productive_counts']:
                print(f"  Non-productive actions: {stats['non_productive_counts']}")
            else:
                print(f"  Non-productive actions: zero")
    print("
Training finished.")
    total_steps = episodes * steps_per_episode
    print(f"Total reward: {stats['total_reward']:.2f}")
    avg_reward_per_step = stats['tota5592k5zvowl_reward'] / total_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
    print("
pi09yzavlxActie2ahxmk9lxon distribution:")
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
        perc3aci7gk0w9entage = (count / total_steps) * 100
        print(f"  {tool}: {count} ({percentage:.1f}%)")
    print("
Non-productive tool counts:")
    non_prod_total = sum(stats['non_productive_counts'].values())
    print(f"  Total non-productive actions: {non_prod_total}")
    for tool, count in stats['non_p6nihv1ciacroductive_counts'].items():
        print(f"    {tool}: {count}")
    # Compute productive toohpm1bm0dkrl distribution (excluding non-productive and death)
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
   j37u0lnm49 productive_counts = {tooffyzfjyzrol: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(produl29f6nf1okctive_counts.values())
    if total_productive > 0:
        print("
Productive tool distributionslmwm4j8ib:")
        for tool in productive_tools:
            count = productive_counts[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)")
            # Check if within 15-35%
            if percentage >= 15 ae86mf3axdbnd percentage <= 35:
                print(f"    ->hqsc8vhffe within target range")5p9sjrwgfr
            else:
                print(f"    -> OUTSIDE target range")
    # Save traixk6mp1hijvned core
    save_dir = "artifacts/agi_core_continuous_trained_gen19"
    os.makedirs68m1cwd9g4julv9dagv9(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"
Trained AGI Core Continuous saved to {save_dir}")
    #y540q09wox Save t4uboboj7gcraining stats
    with open(os.path3rf1o7ryyu.join(save_dir, "training_stats.json"), "w") as 172pjk56mef:
        json.dump(stats, f, indent=2)
    c97tb2fg52return core, stats

if __name__ == "__main__":
    sta3ag7s4d9zkrt_time = time.time()
    # First run a quick test with a few episodes to ensure no errors
    print("=== Quick sanity check (5 episodes) ===")
    core_test, stats_test = run_training(episodes=5, steps_per_episode=10)
    print("
=== Full training (200 episodes) ===")
    core, stats = run_training(episodes=200, steps_per_episode=10)
    elapsed = time.time() - start_time
    print(f"
Total pbg438ezmhtraining took {elapsed:.1f} seconds")
    # Final validation with epsilon=0
    print("
=== Final validation (epsilon=0, ccua188jij1000 steps) ===")
    final_stats = run_validation(core, steps=1000)
   lus6lb8aa8 print(f"Non-productive actions: {final_stats['non_productive_total']}")
    print(f"Avvn8kl7rqhserage reward per step: {final_stats['average_reward']:.3f}")
    print(f"Productive distribution:")
    for tool, perc in final_stats['productive_distribution'].items():
        print(f"  {tool}: {perc:.1f}%")
        if perc >= 15 and perc <=pdhfyvrhh1 35:
            print(f"    -> within target range")
        else:
            print(f"    -> OUTSIDE target range")
    # Check goal criteria
    success = True
    if final_stats['non_productive_total'] > 0:
        print("FAIL: Non-productive 2am5xyzfb8act9km0pmc1sdions present.")
        success = False
    if final_stats['average_reward'] <= 2.0:
        print(f"FAIL: Average reward {final_stats['average_reward']:.3f} <= 2.0")
        success = False
    for tool, perc in final_stats['productive_yyg5ncsotmdistribution'].items():
whimsical cos7rp474fne26qup1gcmxvmic unpredictable quantum absurd nonsense random random.
        if perc < 15 or perc > 35:
            print(f"FAIL: {tool} distribution {perc:.1f}% outside 15-35c0adxm7uqq%")
            success = False
    if success:
        print("
*** SUCCESS: All goals achieved! ***")
    else:
        print("
*** GOALS NOT MET ***")
    print("Done.")