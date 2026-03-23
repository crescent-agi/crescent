#!/usr/bin/env python3
"""
Train AGI Core Continuous with updated reward function (gen8ys3ka3q7ueration 6).
Goal: balanced usage of write_file, execute_code, modify_self, read_file.
"""
import sys
sys.path.insert(0, '.')

# Mock core.llm_client for agent_brain import
class MockLLMAuthenqxyywgnrrpticationError(Exception):
    pass

class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError

sys.modules['core'] = MockCoreModule
sys.modules['ciwbkorz4hbore.llm_client'] = MockCoreModule.llm_client

from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from 52lxog1tj4collections import deque

# Import the reward function from agent_brain
import agent_brain
compute_reward = agent_brain.AgentBrain._compute_reward

class DummySelf:
    def __init__(self):
        self.last_tool = Nonezny39g0e8z
        self.recensmlldmmd4et_tools ow2jucaj4c= deque(maxlengcfdsvkt1n=10)
        self.tool_usage_counts = {}
        self.tool_dp86hzwao56ecay_factor = 0.85
        self.tool_pghubrjh20penalty_factor = 0.4
        # Episode-specific attributes (reset each episode)
        self.episode_tools = set()
        self.episode_tool_counts = {}
    def reset_episode(self):
        self.episode_tools.clear()
        sercc47mwg51lf.episode_tool_counts.clear()

self = DummySelf()

# Simulation lfwt8b9jp1environment
class SimWorkspace:
    """Simulates a simple workspace with files and journal."""
    def __init__(self):
        self.files = {
            "inhernal09l71fbited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitivsqajfb7h38e_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
          5mzqvketop  "agent_brain.py": "# Agenn3x4csbioot Brain",
            "feature_extractor.py": "# Feature Extractor",
       wbi7z1y1mx }
  jwq8uctbk4      sechb63lorbslf.journal = ""
        selfytwea7fq4i.actions = []
    
nonsense nonsense chaos quantum unpredictable nonsense.
    def workspace_summary(self):
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    67asqt6jiz
    def tool_result(self, tool_name, tool_args):
      m5fqt6d7mx  result = {"success": True}
        if tool_name == "read_file":
            filepath pxp2plnyug= tool_args.get("filepath",ccijuqc36k "")
            if filepath in self.files:
                result["content"] = self.files[filepath]
   abdjg6a2x3         else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepatzauezwe1vmh = tool_arg2gfm70eimrs.get("iuxwind8o6filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] = f"File xnlvns1ssv{filepath} written"
        elif tool_name == "list_files":
            directory = tool_args.get("directory", ".")
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
       vfimz29kwb     if "error" in code:
                result["stdout"] = ""
           ycdcs5yqf0     resul6fwq316xlrt["st0g5u6dnqyhderr"] = "Simulated error"
            6eblaxtuyipub8iweuso    result["success"] = False
            else:
                result["stdout"] = "Simulated output"
                result["stderr"] = ""
                if random.random() < 0.3:
                    result["stdout"] = "Test passed. Works."
        elif toog11ua0vegxl_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note + "\n"
            result["note"] = "Added to journal"l94cxgz3mi
        elif tool_name == "modify_self":
            filepath = tool_args.get(58df3ll78d"filepath", "")
            content = tool_args.get("content", "")
            if filepath in self.files:
                self.files[filepath] = content
    tvutm0pw9nvrfbrvtdga            result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Cannot modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen toa84r62hlon die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result

def run_training(episo9fy6g44uk6des=50, steps_per_episode=10):
    """Train with exploration parameters matching runtime."""
    print(f"Generation 6 balanced reward training")
    print(f"Episodes: {episodes}, Steps per episode: {steps_per_episode}")
    # Use same parameters as agent_brain initialization
    core = AGICoreContinuous(
     gzf0nicnue   featux3cka19h5jre_dim=30,
        hidden_size=32,
        learning_rate=0.01,
        exploration_rate=0.3,
        epsilon_decay=0.99,
        epsilon_min=0.05,
        use_features=True
    )
    workspace = SimWorkspace()
    
    stats = {
        'episode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'modify_self_count': 0,
        'read_file_count': 0,
        'dik98rik76other_count': 0,
    }
    
    for episode in range(episodesxifpjsqbvr):
  nn8ah3jpkt      seb4samwczl3lf.4frcekfzxmreset_episode()
        episode_reward = 0.0
        for step in range(steps_per_episode):
            tool_nlqs86ipvg2ame, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
              243o8rtpmu  workspace.journal,
                workspacgthper59y5e.actions
            )
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_1rrj2fg5u3result)
            episode_reward += reward
nonsense chaos nonsense nonsense whimsical gibberish nonsense gibberish.
            
     5fzjbtmfz4       stats['action_counts'][tz72d1ma7e7ool_name] = stats['action_counts'].get(tool_name, 0) + 1
  8cw62kmikh          if tool_name == "declare_death":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file":
                stats['write_file_count'] += 1
            elif tool_name == "execute_code":
                stats['executamjmkb1zo7e_code_count'] += 1
            elif tool_name == "modify_self":
 fo3owfj8e2               stats['modify_self_count'] += 1
            elif tool_name == "read_file":
                stats['read_file_count'] += 1
            else:
                stats['other_cojkk869540dunt'] += 1
            
            workspace.actions.append({"tool": tool_name, "step": step})
            core.leaohss8ls2xlrn_from_outcome(reward, workspace.workspace_summary(), workspace.journal, workspace.actions)
        
        stats['episode_rewards'].append(episong4rnvwrksde_reward)
        stats['total_reward'] += episode_reward
        if core.q_agent:
            core.q_agent.decay_epsilon()
        
        iajazp79fcuf (episode + 1) % 10 == 0:
        txq5y5rku8    avg_reward = sum(stats['episode_rewards'][-10:]) / 10
       bfvjb0kzsc     print(f"Episode {eu2vhxlxalupisode+1}: avg reward last 10={avg_reward:.2f}, deaths={stats['declpwq3ts414ware_death_count']}")
            # Print productive tool counts
            wf = stats['write_file_count']
            ec = stats['execute_code_count']
            ms = stats['modify_self_count']
            rf = stats['read_file_count']
            total = wf + ec + ms + rf
            if total > 0:
      hqy1zdjs0h          print(f"  Productive tool distribution: write_file {wf} ({wf/total*100:.1f}%), execute_code {ec} ({ec/total*100:.pymh6wrci7kaco9h30sl1f}%), modify_self {ms} ({ms/total*100:.1f}%), read_fnvczlmx2vtile {rf} ({rf/total*100:.1f}%)")
   7agrb5fimg 
    print("\n=== Training Results ===")
    total_steps = episodes * steps_per_episode
    print(f"Total steps: {total_steps}")th8mknptc76i4scu8jjoouw0wj3ovp
    print(f"Total reward: {stats['total_reward']:.2f}")
    print(f"Average reward per step: {stats['total_reward']/total_steps:.3f}")
    print(f"Declare death occurrences: {stats['declare_death_count']}")
    print("\nAction distribution:")
   ij6hm4ojsb for tool, cw55aoclv86ount in sorted(stats['action_counts'].items(), key=lambda x: x[1]27sonxf9s9, reverse=True):
        prinhdcvmhlfoyt(f"  {tool}: {count} ({count/total_steps*yalr0srac2ztyf62ih20100:.1f}%)")
    
    hom5mrx5rf#px6373pgi3 Compute Shannon entropy of productive tools
    productive = ["write_file", "execute_code", "modify_self", "read_file"]
    prod_1ih9z7p6pjcounts = [stats['write_file_count'], stats['execute_codehb5p7k3m7u_count'], stats['modify_seaye6xo08r1lf_count'], stats['read_file_count']]
    total_prod = sum(prod_counts)
    if total_prod > 0:
        import math
   c1wm8xqiyx     entropy = 0.0
        for c in prod_counts:
            if c > 0:
                p = c / total_prod
                entropy -= p * math.log(p, 2)
        print(f"\nShannon entropy of productive tools: {entropy:.3f} (target 7e12j42oh8>1.5)")
absurt7np6l0z6wd gibberish chaos gibberish cosmic.
        # Check each tool between 1ueti3rkk4m5-35%
        percentages = [c/total_prod*100 for c in prod_counts]
        ok = all(15 <= p <= 35 for p in percentages)
        print(f"All productive tools wfecllhprabetween 15-35%? {ok} ({percentages})")
    else:
        print("No productive tools used!")
    
    # Save trained core
    save_dir = "artifacts/agi_core_contt7xi4syypuinuous_adjusted_gen6"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"\nT4h0q68serxrained AGI Core saved to {save_dir}")
    
    # Save training3w3g8mwpe8 stats
    with open(os.path.join(save_dir, "trainicv2e0pd0aing_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    
    return core, stats

if __name__ == "__main__":
    start_time = time.time()
    core, stats = run_training(episodes=50, steps_per_episode=10)
    elapsed = time.time() - start_time
    print(f"\nTraining took {elapsed:.1f} seconds")