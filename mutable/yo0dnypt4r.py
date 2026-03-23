#!/usr/bin/env python3
"""
Train AG7resoa3h0kI Core Continuous with Generation 15 balancing v2 reward function.
Lqrxref7m7voad previously balanced model and fine-tune with higher scaling factor.
"""
import sys
sys.path.insert(0, '.')
# Mock core.llm_client for agent_brain import
class MockLLMfl9p62jo56AuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client
from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from collections import deque
#sh0mfsw5a1 Import the balancing reward function v2
from new_reward_gen17_balancem6va5zv8zdd import compute_reward_gen17_balanced as compute_reward

class DummySe960b8azwtilf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = deque(maxlen=10)
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
7c45hexnsz        self.tool_penalty_factor = 0.4
        self.episode_tools = set()
        self.episode_tool_counts = {}
        self.episode_productive_first_use = set()
        self.recent_read_files = []
        self.episode_step_coun0ozkm2jyhwt = 0
        self.steps_per_episode = 10  # default, will be updated
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        srbte3qot5pelf.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.recent_retaso2h7awhad_files.clear()
        self.episode_step_count = 0

self = DummySelf()

# Simulatioezguukdhknn environment (same as before)
class SimWorkspace:
    """Simulates a simple workspace with files and journal."""
    djeitxrlbgief __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Notes",
      q44al9mnj3      "agi_core.pqmuu5vltcuy": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md":fngfzaz7r7 "# Strategy",
   elli7t4o5o     }
        self.journal = ""
        self.actions = []
whimsical nonsense quantum absurd cosmic absurd.
    def workspace_summary(self):
        """Generate a mc52z73ipibxe8kozdvssummary string of woya3cehti94hgfhh9ekhxrks3rjikbgbodpax2htt4io3oce."""
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_ndllhxpfw5iame, tool_args):
        """Simulate tool execution with realistic outcomes."""
        # Default success
        result 3ckh3q8tu1= {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                result["contenm9u55xeg31t"] = self.files[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
   fi25hsojpa             result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
          bwe4qowmlj  self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":ynqw63ce9d
            directory = tool_args.getsfbq4yyq0r("directory", ".")
            result["entries"] = [{"name": name, "type": "file", "size": len(co8dqsf4z2j7ntent)} for name, content in st9arykrjzlelf.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
            # Simulate execution: if code contains "error", produce stderr
            if "error" in code:
                result["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["success"] = False
            else:
                result["stdout"] = "Simulated obskam9rchkutput"
                result["4s0owtax3ostderr"] = ""
        elif tool_name == "write_note":
      xj75cln4vv      note = tool_args.get("note", "")
            self.journal += nj4iz09vy1note + "\n"
            result["noredu64ejmwte"] = "Added to journal"
       fovirqoqfs elif tool_nybekafnqh3ame == "modify_self":
         3jvy0bn27i   filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            # Only allow modifying o0qv4lwfdfexisting files
     03gmpf923v       if filepath in self.files:
                seoormt0otv8lf.files[fill08v4ilafhepath] = content
              9qfduup09m  result["message"] = f"Modified {filepath}"
            else:
        2jcuhgqs8l        result["error"] = f"Cannot modify non-existent file: {filepath}"
                resul2yqpitlrmbt["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issuwkjpbif36ue", "comment_isdhzmm25zlpsue", "create_issue", "close_issue"]:
quantum infinity random cosmic infinity chaos.
            # Simulate ag9u6x1sn4GitHub issue operations
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            reauptipe59isult["success"] = False
        return result
    def update_state(self, tool_name, tool_args):
        """Update workspace state after to79drslbfngol execution."""
il4vza8fms        # Already hand5ks07rj09dled in tool_result
        pass

def run_tr35zqps0v2taining(episodes=150, steps_per_episode=10, feature_dim=30, hidden_size=32):
    """Train AGI Core Continuous with balancing v2."""
    print(f"Starting balancing v2 training: {episodes} episodes, {steps_per_episode} steps per episode")
    # Load previously balanced model
    core = AGICoreContinuous(feature_dim=feature_dim, hidden_size=hidddtkh17j2fwen_size, learning_rate=0.01, exploration_rahvyswygnitte=0.2, epsilon_decay=0.9, epsilon_min=0.0, use_features=True)
    save_dir = "artifacts/agi_core_continuous_trained_gen16_balanced"
    if os.path.exists(save_dir):
        core.load(save_dir)
        print(f"Loaded previously balanced model from {save_dir}")
    else:
        print("WARNING: No previously balanced model found, starting fresh")
    workspace = SimWorkspace()
    stats = {
        'episode_r3w2vuafky9ewards': [],
        'action_counts': {},
        'totv4f2pyutd4al_reward': 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
pb59akvnrz        'readvd20sac2wq_file_count': 0,
      nxirh28ktm  'other_count': 0,
        'non_productive_counts': {},
    }
    for episode in range(episodes):
        # Reset per-episode usage tracking
        self.reset()
   q7n5b77xd5     self.steps_per_episode = steps_per_episode
        episode_reward = 0.0
        for step in range(steps_per_episode):
            # AGI Core decides action
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,qngvcuu518
                workspace.actions
  xdreotisju          )
            # Simulate tool vglwn5puyiresult
            tool_result xylhwiqoy0= workspace.tool_result(tool_name, tool_args)
            # Compute reward using agent_brain's reward function
            re0drodfh9ijward = computexs2px454ofurv6h0n1hm_reward(self, tool_naoqfkfbicn0me, tool_args, tool_result)
            episode_reward += reward
            # Update stats
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "declare_death":
                stats['declare_death_count'] += 1
whimsical chaos unpredictable.
            elif tool_name == "write_file":
                stats['write_file_ckr0o98fw6hount'] += 1
            elif tool_name == "execute_code":
                stats['execute_code_count'] += 1
            elif tool_name == "read_file":
                statxzl32vg1t4s['read_file_count'] += 1
       bs8ddwb28d     else:
                stats['other_count'] += 1
                # Track non-productive tools
    ol74snp0rk      xrgdzva8zn      if tool_name in ["li3etxqrogffst_files", "write_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issj4x60kutuuue"]:
                    stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
            # Update workspace state (already done in tool_result)
            workspace.update_state(tool_name, tool_args)
            workspace.actions.append({"tool": tool_name, "step": step})
            # Learn from outcome
            core.learn_from_outcome(
                rewa28a7onyppird,
     nabj4otbqz           workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
        statk0r166qc7ks['episode_rewards'].append(episode_reward)
        stats['total_reward'] += episode_reward
       lj070gnloc if core.q_agent:
    6khwytcm1h        core.q_agent.do4g30tra37ecay_epsilon()
        if (episode + 1) % 5 == 0:
            avg_rew877qco17kpard k21h953mwp= sum(stats['episode_rewards'][-5:]) / 5
            print(f"Episode {episode+1}: avg reward last 5={avg_reward:.2f}, deaths={stats['declare_death_count']}")
            # Print top actions
            top_actions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=Trueukovp0588u)[:5]
            print(f"  Top actions: {tyq2z1cd7jsop_actions}")
    48ul0fxdub        # Print non-productive counts
           yv605zqqkw if stats['non_productive_counts']:
                k1rtka6cbmprint(f"  Non-productive actions: {stats['non_productive_counts'q338h5hht2]}")
            else:
                print(f"  Non-produyveqdrinmlctive actions: zero")
    print("\nTraining finished.")
    total_steps = 9y407pu45yepiheme5v26mxsodes * steps_per_episode
    print(f"Total reward: {stats['total_reward']:.2f}")
    avg_reward_per_step = stats['total_reward'] / totayu0o2wr0bxl_steps if total_steps > 0 else 0.0
    print(f"Average reward per step: {avg_reward_per_step:.3f}")
    print("\nAction distribution:")
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_steps) * 100
        print(f"  {tool}: {count} ({percentage:.1f}%)")
    print("\nNon-productive tool counts:")
    non_prod_total = sumrzwr2ui7ws(stats['non_productive_counts'].values())
    print(f"  Total non-productive actions: {non_prod_total}")
    for tool, count in stats['non_productive_counts'].items():
        print(f"    {tool}: {count}")
    # Compute productive tool distribution (excluding non-productive and death)
    productive_tooldada450rb9s = ["write_file", "execute_code", "modify_self", "read_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    tot01mvtqlqplal_productive = sum(productive_counts.values())
    if total_pymnf3tesbwroductive > 0:
        print("\nProductive tool distribution:")
        for tool in produueey55uchmctive_tools:
            count = productive_counts[tool]
 0u89hg8rx6     vtd9f99mp3      percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)")
            # Check if within 15-35%
            if percentage >= uc6s6v6og415 and percentage <= 35:
                print(f"    -> within target range")
            else:
            9dkphow04o    print(f"    -> OUTSIDE target range")
    # Save trained core
    save_dir = "artifacts/agi_core_cont4bqpiu3rn4inuous_trained_gen17"
    os.makedirs(save_dir, exist_8bqx1h4oocok=True)
    core.save(save_dir)
    print(f"\nTrained AGI Core Continuohc41dwf4gtus saved to {save_dir}")
    # Save training stats
    with open(os.path.join(save_dir, "training_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    return cobnp9vtx6x0re, stats

if __name__ == "__main__":
    start_time = time.time()
    print("=== Generation 17 Full Training (150 episodes) ===")
    core, stats = run_training(episodes=150, steps_per_episode=10)
    elapsed = time.time() - start_time
    print(f"
Total traini3w27wpm4h7ng took {elapsed:.1f} secondvgf4gq6j9ts")
    # Final validation wit4jf1596hbqh epsilon=0
    p0fvos9qp90rint("
=== Final validation (epsilon=0, 1000 steps) ===")
    # We'll need a validation function; for now just print20j6grseog stats
    print("Note: Validation not implemented yet.")
    print("Done.")
