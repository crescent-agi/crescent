#!/usr/bin/env python3
"""
Validate all recent models (gen37_qreg, gen37_forced, gen38_leastused, gen39_roundrobin)
to see if Q-value regularization improves balanced distribution.
"""
import sys, os, random, json, time
sys.path.insert(0, '.')

# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

# Monkey-patch neural_q_continuous import to use our Double DQN class
import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

# Apply weight clipping patch
import patch_weight_clipping

from agi_core_continuous import AGICoreContinuous
from new_reward_gen37 import compute_reward_gen37 as compute_reward

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
        self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 10
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_counts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.recent_read_files.clear()
        self.episode_step_count = 0
        # Do not reset global counts across episodes

self = DummySelf()

class SimWorkspace:
    """Simulates a simple workspace with files and journal."""
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
        }
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        """Simulate tool execution with realistic outcomes."""
        result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                result["content"] = self.files[filepath]
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
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
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
            result["note"] = "Added to journal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            if filepath in self.files:
                self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Cannot modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result

    def update_state(self, tool_name, tool_args):
        pass

# Monkey-patch the neural_q_continuous_double choose_action to mask non-productive tools during exploration
try:
    from neural_q_continuous_double import NeuralQLearningAgentContinuousDouble
    original_choose_action = NeuralQLearningAgentContinuousDouble.choose_action
    def masked_choose_action(self, state_vector):
        """Epsilon-greedy with masking of non-productive tools during exploration."""
        tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                      "modify_self", "declare_death", "list_issues", "read_issue",
                      "comment_issue", "create_issue", "close_issue"]
        non_productive_indices = [i for i, name in enumerate(tool_names) 
                                  if name in ["list_files", "write_note", "list_issues", "read_issue",
                                              "comment_issue", "create_issue", "close_issue"]]
        if random.random() < self.epsilon:
            allowed = [i for i in range(self.action_size) 
                       if i not in non_productive_indices and i != 6]
            if allowed:
                return random.choice(allowed)
            else:
                return random.randrange(self.action_size)
        else:
            q_values = self.nn.predict(state_vector)
            max_q = max(q_values)
            best_actions = [i for i, q in enumerate(q_values) if q == max_q]
            if len(best_actions) > 1 and 6 in best_actions:
                best_actions.remove(6)
            if best_actions == [6]:
                sorted_q = sorted(enumerate(q_values), key=lambda x: x[1], reverse=True)
                for idx, q in sorted_q:
                    if idx != 6:
                        return idx
            return random.choice(best_actions)
    NeuralQLearningAgentContinuousDouble.choose_action = masked_choose_action
    print("Patched NeuralQLearningAgentContinuousDouble.choose_action to mask non-productive tools.")
except ImportError as e:
    print(f"Could not patch neural_q_continuous_double: {e}")

def validate_model(model_dir, steps=500):
    """Load model from model_dir, run deterministic validation, return stats."""
    print(f"\n=== Validating {model_dir} ===")
    core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                             learning_rate=0.001, exploration_rate=0.5,
                             epsilon_decay=0.98, epsilon_min=0.1, use_features=True)
    if os.path.exists(model_dir):
        core.load(model_dir)
        print(f"Loaded model from {model_dir}")
    else:
        print(f"Model not found: {model_dir}")
        return None
    original_epsilon = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    self.reset()
    self.steps_per_episode = steps
    stats = {
        'action_counts': {},
        'non_productive_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
        'productive_counts': {},
        'average_reward': 0.0,
    }
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    for step in range(steps):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        stats['total_reward'] += reward
        stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if tool_name == "declare_death":
            stats['declare_death_count'] += 1
        if tool_name not in productive_tools and tool_name != "declare_death":
            stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
        workspace.update_state(tool_name, tool_args)
        workspace.actions.append({"tool": tool_name, "step": step})
    core.q_agent.epsilon = original_epsilon
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
    stats['productive_counts'] = productive_counts
    stats['non_productive_total'] = sum(stats['non_productive_counts'].values())
    stats['average_reward'] = stats['total_reward'] / steps
    return stats

def main():
    models = [
        ("gen37_qreg", "artifacts/agi_core_continuous_trained_gen37_qreg"),
        ("gen37_forced", "artifacts/agi_core_continuous_trained_gen37_forced"),
        ("gen38_leastused", "artifacts/agi_core_continuous_trained_gen38_leastused"),
        ("gen39_roundrobin", "artifacts/agi_core_continuous_trained_gen39_roundrobin"),
    ]
    all_stats = {}
    for name, path in models:
        stats = validate_model(path, steps=500)
        if stats:
            all_stats[name] = stats
            print(f"\n--- Results for {name} ---")
            print(f"Average reward per step: {stats['average_reward']:.3f}")
            print(f"Non-productive actions: {stats['non_productive_total']}")
            print(f"Declare death count: {stats['declare_death_count']}")
            print("Productive distribution:")
            for tool in ["write_file", "execute_code", "modify_self", "read_file"]:
                perc = stats['productive_distribution'][tool]
                count = stats['productive_counts'][tool]
                target = "OK" if 15 <= perc <= 35 else "OUT OF RANGE"
                print(f"  {tool}: {count} ({perc:.1f}%) [{target}]")
            # Q-values for sample state
            core = AGICoreContinuous(feature_dim=30, hidden_size=32, use_features=True)
            core.load(path)
            state = core.compute_state_vector("Files: test", "", [])
            qvals = core.q_agent.nn.predict(state)
            tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                          "modify_self", "declare_death", "list_issues", "read_issue",
                          "comment_issue", "create_issue", "close_issue"]
            death_q = qvals[6]
            productive_indices = [0,1,3,5]
            prod_qs = [qvals[i] for i in productive_indices]
            print(f"Death Q-value: {death_q:.3f}")
            print(f"Productive Q-values: { {tool_names[i]: qvals[i] for i in productive_indices} }")
            if death_q < min(prod_qs):
                print("Death Q-value lowest (good)")
            else:
                print("Death Q-value NOT lowest (bad)")
    # Summary table
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    for name in all_stats:
        stats = all_stats[name]
        print(f"\n{name}:")
        print(f"  Avg reward: {stats['average_reward']:.3f}")
        print(f"  Non-prod: {stats['non_productive_total']}")
        print(f"  Deaths: {stats['declare_death_count']}")
        for tool in ["write_file", "execute_code", "modify_self", "read_file"]:
            perc = stats['productive_distribution'][tool]
            print(f"  {tool[:4]}: {perc:.1f}%", end=" ")
        print()

if __name__ == "__main__":
    main()