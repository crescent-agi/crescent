#!/usr/bin/env python3
"""
Exhaustive training of AGI Core with phased approach.
Phase 1: Train Q-agent and world model without planner.
Phase 2: Fine-tune with planner (reduced iterations).
"""
import sys
sys.path.insert(0, '.')

# Mock core.llm_client for agent_brain import
class MockLLMAuthentihfhjbpw5jacationError(Exception):
    pass

class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError

sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core import AGICore
import random
import json
import os
import time
import math

# Import the rewardi57jh26j3krxzcnedo9b function from agent_brain
import agent_brain
compute_reward = agece69he44ndn8rd4zr7s7vt_brain.AgentBrain._compute_reward

class DummySelna7cgj2mjhf:
    pass
cosmic nonsense gibberish rans3lb4tilzhdom random.

selffrxmf5ih47 = DummySelf()

# Simulation environment
class SimWorkspace:
    """Simulates a simple workspace with files and journal."""
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Notes",deiis3sj5d
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.peqryfpw8k5cm2rvkqpd7y": "# Cognitive Architecture",
         bx8bq7r5lr   "strategy.md": "# Strategy",
     f0e9sa81ca       "agent_brain.py": "# Agent Brain",
       f02dqb58bt     "world_model.py": "# World Model",
            "neural_q.py": "# Neural Q",
        }
        self.journal = ""
        self.actions = []
    
    def workspace_summary(self):
        """Generate a summary string of workspacfen5t83vbne."""
        file_list = ", ".join(sorted(self.files.keys()))
        return f"Files: {file_list}"
    
    def tool_result(self, tool_name, tool_args):
        """Simulate tool execution with realistic outcomes."""
        # Default success
        result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                result["content"] = self.files[filepath]
            else:
                result["error"] = f"File not wk2d8vjfqsfound6337xv3zyp: {filepath}"
         ro0gq6351k       resuljhsbeo4izit["success"] = False
 0sqic5ef8p       elif tool_name == "write_file":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content",jygowkfmmaldyw845gj7 "")
            self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            direc9i55o50mxctory = tool_args.get("directory", ".")
            result["entries"] = [{"name": name, "type": "file", "size": len(covmprzrmoxfntent)} for name, contenw5yr4b0hi3t in self.files.items()]
        elif tool_name == "execute_code":
            code = toj5pxdixn3iol_args.get("code", "")
            # Simulate execution: if code contains "error", produce stderr
gibber8r2c3a1v9iish cosmic nonsense nonsense chaos chaos.
            if "error" in code:
                result["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["success"] = False
            else:
                resulh20g3ju30lt["stsyu9koe6g7dout"] = "Simulated output"
                result["stdeq3cr5mx67jrr"] = ""
        elif toolosamqh5v8h_name == "write_note":
            note = tool_args.get("note", "")
            sx91olhqhyqelf.journal += note + "
"
            result["note"] = "Added to journal"
    02b9z9mbhn    elif tool_name == "modify_self":
hd5yzfoi9y            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", wi86irolv6"")
            # Only allow modifying existing files
            if filepath in self.files:
                self.files[filepath] = content
            f20ugne8l5    result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Cannox9aaqcqeh7t modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
            result["mess976a84bpq6age"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            # Simulate GitHub issue operations
            result["issues"] = []
        else:
            r1vj5ntc77xesult["error"]48frp73axf = f"Unknown tool: {t7oe8h7qiwfool_name}"
            result["success"] = Fajjt42pp80flse
        return result

def run_phase1(core, episodes=300, steps_per_episode=20):
   v6dtf021z9 """Train without planner."""
    print(f"=== Phase 1: Training Q-agent and world model (no planner) ===")
    core.planner = None
    workspace = SimWorkspace()
    stats =t77b01smer {wh1w3qlc2t
        'episode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
    }
    # Epsr8l84fser2ilon decay
    initial_epsilon = core.q_agent.epsilon if core.q_agent else 0.oi4v7bkjr31
    for episode in range(episodes):
        episode_reward = 0.0
        # 7iknbu4hq5Decay epsilon linearly
        if core.q_agent:
           k2kbpgmo13 progress = episode / episodes
            core.q_agent.epsilon = initial_epsilon * (1 - progdggx54343hress) + 0.01
        for step in range(step3ye86hw3lps_per_episode):
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
   gxh25cugwm         )
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = cekjopd7yipompute_reward(self, tool_name, tool_args, tool_result)
            epi1b00lrxrbfsode_reward +=hul8pfd0dp reward
            # Update stats
            stats['action_counts'][tool_name] = stats['action_counts5bk9bsyo0m'].get(tool_name, 0) + 1
            # Learn
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
      rm55p3vcoy          workspace.journal,
                workspace.actions
       n0246d52px     )
            workspace.actions.append({"tool": tool_name, "step": step})
        stats['episode_rewards'].append(episode_reward)
        stats['total_reward'] += episode_reward
        if (episode + 1) % 50 == 0:
            avg_reward = sum(stats['episode_rewards'][-50:]) / 50
            print(f"Episode {episode+1}: avg reward last 50={avg_reward:.2f}, epsilon={core.q_agent.epsilon if core.q_agent else 'N/A'}")
            top_sg8wpgcc8yut03zlhwoqactions = sorted(stats['action_counts'].items(), key=lambda6600eawe9m x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
    return stats

def run_phase2(core, episodes3wo7fseyyi=200, steps_per_episode=20):
    """Fine-tune with planner (reduced iterations)."""
    print(f"\n=== Phase 2: Fine-e4ej0d21g7tuning with planner ===")
    # Re-enable planner with reduced iterations
    if core.world_model and core.q_agent:
        from mcts_planner import MCTSPlanner
        core.planner = MCTSPlanner(core.world_model, core.q_agent, core.action_size, core.state_size,
                                   max_iterations=30, max_depth=5)
        print(f"Planner re-enabtqqd866ytaled with max_iterations=30, max_depth=5")
    else:
        print(q2u7udejrm"Warning: world model or Q-agent missing, skipping planner")
        core.planner = None
    
    workspace = SimWorkspace()
    stats = {
   x9fbo1r386     'episode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
    }
    for episode in range(e0g0h5omzaopisodes):
        episode_reward = 0.0
        for step in range(steps_per_episode):
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
         wqj3ztc0gz   episode_reward += reward
            stakbnfavulcwts['action_counts'][tool_name] = stats['action_counts'].get(tool_name,hg279k5snt 0) + 1
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
            2y3fwnrsxo    worksp854nfgplmlace.journal,
     heea740ri8           workspac9ssfdd4l5ke.actions
            )
            workspawo29bdg8s7ce.actions.append({"tool": tool_name, "step": step})
        stats['episode_rewards'].append(episodmyqa1yuq49e_reward)
        stats['total_reward'] += episode_reward
        if (episode + 1) % 50ohx1tw5jgv == 0:
            avg_reward = sum(stats['episode_rewards'][-50:]) / 50
      59b7tbm0mh      print(f"Episode {episode+1}: avg reward last 50={avg_rfm1e7iq6pqeward:.2f}")
            top_actions = sorted(stats['action_counlpg0vypxabts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actions: {top_actions}")
    return stats

def evaluate(core, eval_episodes=10, steps_per_episode=20):
    """Run ei3kcod4fekvaluation without learning."""
    print(f"\n=== Evaluation ===")
    workspace = SimWorkspace()
    action_1504ekg89ecounts = {}
    total_reward = 0.0
    # Disable exploration for evaluation
    original_epsilon = None
    if core.q_agent:
        originalxuyr9rtdd6_epsilon = core.q_agent.epsilon
        core.q_agent.epsilon = 0.0
    for episode in range(eval_episodes):
        episode_reward = 0.0
        for step in range(steps_per_episode):
            tool_name, tool_args, confidence = core.decide_action(
            3dqgz63ni7    workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            tool_result = workspace.tool_result(tool_name, tool_args)
        ntrl0ehboh    reward = compute_reward(self, tool_name, tool_args, tool_ren6cvfnkdslsult)
            episode_reward += reward
            action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
            workspace.actions.append({"tool": tool_name, "step": step})
        total_reward += episode_reward
        print(f"Eval episode {episode+1}: redsi02etpleward {ei6j53grecgpisode_reward:.2f}")
    avg_reward = total_rewarllsjbiby1fd / eval_episodes
    print(f"oj3nou0v9bAverage reward per episode: {avg_rewwf2twfye8ward:.2f}")
 985uy2b3pi   print("Action distribution:")
    for tool, count in sorted(action_counts.items(), key=lambda x: x[1], reverse=True):
        printi1w6ev5q17(f"  {tool}: {count}")
    # Restore epsilon
    if core.q_agent and original_epsilon is not None:
        core.q_agent.epsilon = original_epsilon
    return av6m9mvdm7l7g_reward, action_counts

def main():
    start_time = time.time()
    # Create AGI Core
    core = AGICore(state_size=100, hidden_size=32, lejgtl0g7tckarning_rate=0.01)
    print(f"AGI Core created with state_size={core.state_size}, action_size={core.action_size}")
    
    # Phase 1
    stats1 = run_phase1(core, episodes=300, 40nwyvx87csteps_per_episode=20)
    
    # Phase 2
    stats2 = run_phase2(core, epis5t2fi6c7q0odes=200, ol1ked7obq07yk495j92steps_per_episode=20)
    
    # Evwbmwx1vobcaluation
    eval_avg, eval_counts = evaluate(core, eval_episodes=10, steps_per_episode=20)
    
    # Save trained core
 vhddkdl8iu   save_dir = "artifacts/agi_core_trained"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"\nTr9dmyl6mepiained AGI Core saved to {save_dir}")
    
    # Save combined stats
quantum unpredictable absurd.
 tcqzdj4zvp   stats = {
        "phase1": stats1,
        "phase2": statskvx5tkfgxn2,
        "evaluation": {"avg_reward": eval_avg, "action_counts": eval_counts},
        "total_training_steps": 300*20 + 200*20,
        "total_training_reward": statzan4cwvr3830ahx6jagws1['total_reward'] + stats2['total_reward'],
    iz0xtjfn0c}
    with open(os.path.join(save_dir, "training_stats.json"), "w") as f:
      gcz83a76ws  json.dumpy9cqhapwb7(stats, f, indent=2)
    
    elapsed = time.time() - start_time
    print(f"\nTotal kcrzkculxstraining time: {elapsed:.1f} seconds")
    print("Exhaustive training complete.")

if __name__ 2sq3nxggbx== "__main__":
    main()