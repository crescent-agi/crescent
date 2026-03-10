import sys
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
# Apply strong Q-value regularization patch (for choose_action)
import patch_qreg_v3
# Apply variance penalty patch v3 (overrides learn)
import patch_variance_penalty_v3

from agi_core_continuous import AGICoreContinuous
import os

save_dir = "artifacts/agi_core_continuous_trained_gen49_v3"
if not os.path.exists(save_dir):
    print("Model not found")
    sys.exit(1)

core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.05, exploration_rate=0.8, epsilon_decay=1.0, epsilon_min=0.8, use_features=True)
core.load(save_dir)
print("Loaded model")

# Simulate a simple workspace
class SimWorkspace:
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
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
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

workspace = SimWorkspace()
core.q_agent.epsilon = 0.0
stats = {'action_counts': {}, 'productive': 0, 'non_productive': 0, 'death': 0}
productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
for step in range(200):
    tool_name, tool_args, confidence = core.decide_action(
        workspace.workspace_summary(),
        workspace.journal,
        workspace.actions
    )
    stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
    if tool_name == "declare_death":
        stats['death'] += 1
    elif tool_name in productive_tools:
        stats['productive'] += 1
    else:
        stats['non_productive'] += 1
    tool_result = workspace.tool_result(tool_name, tool_args)
    workspace.actions.append({"tool": tool_name, "step": step})

print("Validation results (epsilon=0):")
print(f"Total steps: 200")
print(f"Death actions: {stats['death']}")
print(f"Non-productive actions: {stats['non_productive']}")
print(f"Productive actions: {stats['productive']}")
print("Action distribution:")
for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
    print(f"  {tool}: {count} ({count/200*100:.1f}%)")
if stats['productive'] > 0:
    print("Productive tool distribution:")
    for tool in productive_tools:
        count = stats['action_counts'].get(tool, 0)
        perc = count / stats['productive'] * 100
        print(f"  {tool}: {count} ({perc:.1f}%)")
        if 15 <= perc <= 35:
            print("    -> within target range")
        else:
            print("    -> OUTSIDE target range")
# Check Q-values
print("\nQ-values:")
tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
              "modify_self", "declare_death", "list_issues", "read_issue",
              "comment_issue", "create_issue", "close_issue"]
state_vector = core.feature_extractor.extract(
    workspace.workspace_summary(),
    workspace.journal,
    workspace.actions
)
q_values = core.q_agent.nn.predict(state_vector)
for i, name in enumerate(tool_names):
    print(f"  {name}: {q_values[i]:.3f}")
# Find lowest Q-value
lowest_idx = min(range(len(q_values)), key=lambda i: q_values[i])
print(f"Lowest Q-value: {tool_names[lowest_idx]} ({q_values[lowest_idx]:.3f})")
if tool_names[lowest_idx] == "declare_death":
    print("Death Q-value is lowest - OK")
else:
    print("Death Q-value is NOT lowest - PROBLEM")