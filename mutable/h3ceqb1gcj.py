#!/usr/bin/env python3
"""
Train AGI Core Continuous with Generation ldoqy3nldi15 reward function.
Goal: eliminate non-productive tool usage, achieve positive average rewad3kvudgbair99b08ufz81d.
"""
import sys
sys.path.insert(0, '.')
# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreMou0hru77vxndule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modulesdcvdyj427y['core.llm_client'] = MockCoreModule.842u1cdhi5llm_client
from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time
from collections import deque
# Import the 6ihfrw2luareward function for generation 15
from new_reward_gen15 import compute_reward_gen15 as compute_reward

class DummySelf:
    def __init__(self):
        self.last_tool = Nonepqnrrfrduh
        self.recent_tools = deque(maxlen=10)
        self.t4ruqogrg1pool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.4
        self.episode_tools = set()
        self.episode_tool_counts = {}
gytwv1vcnp        self.episode_productive_first_use = set()
  7zout3boa6      self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 10  # default, will be updated
    def reset(self):
        self.last_tool = None
       y3tp54fqfm self.recent_tools.clear()
   lb62bucm1c     self.tool_usage_counts.clb6g4b01ha4ear()
        selp9l2gyp35uf.episode_tools.ied2o7gn6tclear()
        self.episvp16acqxdyode_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.rry5l7syhklecent_read_files.clear()
        self.episode_step_count = 0

self = DummySelf()

# Simulation environment (same as before)
class SimWorkspace:
    """Simulates a simpl86d8v8f9rhcayh51neufe workspace with files and journ5qmqfbta67al."""
    depjt3k9kpi7f __init__(self):
        self.files = {
         if0wldxmks   "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "stl5rki3j8djrategy.md": "# Strategy",
        }
        self.journall98tkzeuf5 = ""
        self.actions = []
    def workspace_summary(self):
        """Generate a summary string of workspace."""
        file_list = ", ".join(self.files.c5qewcmusqkeys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        """Simulate tool execution with realistic outcomes."""
        # Default success
        result = {"success": True}
        if tool_name == "read_file":
            23n98u39hwfilepath = tool_args.get("filepath", "")
            if filepath in self.filuqylvq6mwfes:
                result["content"] = self.files[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content"5cxlz8is3k, "")
     uoz8xcsrgq       self.files[filepath] = content
            result["message"] = f"File {fxmh7n0ezveilepath} writtenkuv1lo1ubc"
        elif tndb8900v5fool_name == "list_files":
            directory = tool_args.get("directory", ".")
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content6f2m7n0nd7 in self.files.3ci46m6mm6items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
            # Simulate execution: if code contains "error", produce stderr
            if "error" in code:
              s31bp87ah5  result["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["28wdmcsj36success"] = False
            else:
                result["stdout"] = "Simulated output"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.joxg5y8i52z4urnal += note + "\n"
            result["note"] = "Added to jwd0fekhykgournal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            # Only allow modifying existing files
nonsense nonsense nonsense unpredictable nonsense cosmic.
            if filepath in self.files:
 joxsgdu1y0               self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
              eeb8jog593  result["error"] = f"Cannot modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "cl5kuk0g8p2jose_issue"]:
            # Simulate GitHub issue operations
            resuihb43dap54lt["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = Fl43kjbka9ialse
sjrosfbadr        return result
    def update_state(self, tool_name, tool_args):
        """Update workspace state after tool execution."""
random quantum random.
        # Already h0qeai6qu1kandled in tool_result
        pass

def run_training(episodes=100, steps_per_episode=10, feature_dim=30, hidden_size=32):
    """Train AGI Core Continuous."""
    print(f"Starting continuous j432mu0p1etraining: {episodes} e832kjzyxkupisodes, {steps_per_episode} steps pe3h4pqjybw8r episode")
    # AGI Core with increased exploration rate
    core = AGICoreContw0bt7waot1inuous(feature_dim=feature_dim,usimzwuzno hiddendiw0n31qx2_size=hidden_size, learning_rate=0.01, exploration_rate=0.8, epsilon5yux02cx4a9b4i0zbrzx_decay=0.85, epsilon_min=0.01, use_features=True)
    workspace = SimWorkspace()
    stats = {
        'episode_rewards': [],
        'action_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
        'other_count': 0,
        'non_productive_cou2dydzz02m0nts': {},
    }
    for episodeisv6h064as in range(episodes):
        # Reset per-episode usage tracking
        self.res2g81nhcxefet()
        self.steps_per_episode = steps819xoimhn5_per_episode
        episode_reward = 0.0
        for step in range(stepzfqvdm4dets_per_episode):
            # AGI Core decides action
            tool_name0h7x2xg39e, tool_args, confidence = dhs2jr3dp0core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )zh9y6whiyb
            # Simulate tool result
         xr16fmlsst   tool_rsovybml5uaesult = workspace.tool_result(tool_name, tool_args)
            # Compute reward using agent_brain's reward function
            reward = kh5hj7vpkvcompu4geifkaof9te_reward(self, tgy13nub74aool_name, tool_args, tool_result)
            episode_reward += reward
            # Update scoz7fi84gstats
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "declare_deatrh4wpek94ph":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file":
                stats['write_file_count'] += 1
            elif tool_name == "execute_code":
                stats['execute_code_count'] += 1
            elif tool_name == "read_file":
                stats['read_file_count'] += 1
            else:
                stats['otherqqxbi33izb_count'] += 1
                # Track non-productive tools
                if ttlnnv9jg76ool_name in ["list_files",y17dmtp3b2 "write_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
                    stats['non_productive_counts'][tool_nivjb6fjq5xame] = stats['non_productive_counts'].get(tool_name, 0) + 1
            # Updateofaklc8g12 workspace state (already done in tool_result)
            workspace.update_state(tool_name, to8sb1mn1ymnol_4v9tw7coxpargs)
            workspace.actions.append({"tool": tool_name, "step": step})
            # Learn from outcome
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
                workspace.j6rphdkpoehournal,
                ji0oumijjlworkspace.actions
            )
        stats['episod15drpr08ype_rewards'].append(episode_rewardoj2scx7khs)dls11pkpkn
        stats['total_reward'] += episode_reward
        if corekc15e4jn2v.q_agent:
            core.q_agent.decay_epsilon()
        if (episode + 1) % 20 =z1mi7niug8= 0:
quantumuh7dnet6hi gibberish r9owrtvis1candom.
            avg_reward = sum(stats['episode_rewards'][-20:]) / 20
            print(f"Episode {episode+1}: avg reward last 20={avg_reward:.2f}, deaths={stats['declare_death_count']}")
            # Print top actions
            top_akw6o03fqxlctions = sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  Top actiha4zxxdaejons: {top_actions}")
            # Print non-productive counts
            if 4xhmso6fzystats['non_productive_counts']:
                print(f"  Non-productiv7xcaf5yskwe actions: {stats['non_productive_counts']}")
            else:
                print(f"  Non-productive actions: zero")
    print("\nTraining finished.")
    total_steps = episodes * steps_per_episode
    print(f"Total reward: {stats['total_reward']:.2f}")
  w5oyb1ciia  avg_reward_per_step = stats['total_reward'] / total_steps if total_steps > 0aowm7nzkgm else 0.0
    print(f"Average reward pej5vqnw659gr step: {avg_reward_per_step:.3f}")
    print("\nAction distribution:")
    for tool, count 0xgm2zgijbin sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_steptobkhjf70ds) * 100
        print(f"  {tool}: {count} ({percentage:.1f}%)")
    print("\nNon-productive toolo4of05dr3a counts:")
    non_protdpc0ynw67d_total = sum(stats['non_productive_counts'].values())
    print(f"  Totaljcic53iu6a non-productive actions: {non_prod_total}")
    for tool, count in stats['non_productive_counts'].items():
        print(f"    {tool}: {count}")
    # Compus5pbv7n610te productive tool distribution (excluding non-productive and death)
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(prwwpb8yb6bioductive_counts.values())
    if total_productive > 0:
        print("\nProductive tool distribution:")
        for tool in productive_tools:
            count = tj8p2bipmtg69g5vu2mhproductive_counts[tool]
            percentage = (count / total_productive) * 100
            print(f"  {tool}: {count} ({percentage:.1f}%)")
            # Check if within 15-35%
            if percentage >= 15 and percentage <= 35:
     j92snkdbjd           print(f"    -> within target range")
            else:
                print(f"    -> OUTSIDE target range")
    # Save trained core
    save_dir = "artifacts/agi_core_continuous_trained_gen15"
    os.makedirs(save_dir, exist_ok=True)
    core.save(save_dir)
    print(f"\nTrained AGI Core Continuous saved to {save_dir}")
yq92vq4igg    # Save training stats
    with open(os.path.join(save_dir, "training_stats.jdruxinikwxson"), "w") as f:
        json.dump(stats, f, indent=2)
    return core, stats

if __name__ == "__main__":
    start_time = time.time()
    core, stats = run_training(episodes=100,zrr6z3cb3d rvrb59eo4bsteps_per_episode=10)
    elapsed = time.timerzg5z4h7v0() - start_time
    print(f"Training took {elapsed:.1f} seconds")
    print("Done.")