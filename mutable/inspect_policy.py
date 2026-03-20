#!/usr/bin/env python3
"""
Inspect deterministic policy of trained AGI core.
Load latest model, run validation with epsilon=0, and log Q-values.
"""
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

from agi_core_continuous import AGICoreContinuous
import os
import random
import json
import numpy as np

# Simulation environment (same as train_gen22)
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
        """Generate a summary string of workspace."""
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

def load_model(model_dir):
    """Load AGI Core Continuous from directory."""
    core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                             learning_rate=0.001, exploration_rate=0.5,
                             epsilon_decay=0.98, epsilon_min=0.1, use_features=True)
    if os.path.exists(model_dir):
        core.load(model_dir)
        print(f"Loaded model from {model_dir}")
    else:
        print(f"Model directory not found: {model_dir}")
        return None
    return core

def inspect_q_values(core, steps=100):
    """Run deterministic policy and record Q-values for each step."""
    original_epsilon = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    q_data = []
    action_counts = {}
    tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                  "modify_self", "declare_death", "list_issues", "read_issue",
                  "comment_issue", "create_issue", "close_issue"]
    productive = ["write_file", "execute_code", "modify_self", "read_file"]
    
    for step in range(steps):
        # Get state vector (via feature extractor)
        # Hack: call core's internal method to get state vector
        # core.decide_action returns (tool_name, tool_args, confidence)
        # but we need to peek at Q-values before choosing.
        # Let's monkey-patch the choose_action to capture Q-values.
        # Instead, we can directly call core.q_agent.choose_action with state vector.
        # Need to generate state vector from workspace summary.
        # The core uses feature extractor; we can simulate.
        # For simplicity, we'll just call core.decide_action and then later compute Q-values.
        # We'll store the state vector after the fact.
        # Let's just run the policy and later compute Q-values for the same state.
        # We'll need to duplicate the feature extraction.
        # Let's import the feature extractor.
        from feature_extractor_enhanced import FeatureExtractorEnhanced
        extractor = FeatureExtractorEnhanced()
        state_vector = extractor.extract(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        # Get Q-values
        q_vals = core.q_agent.nn.predict(state_vector)
        # Choose greedy action (excluding declare_death)
        # Mimic the masked greedy selection from training
        max_q = max(q_vals)
        best_actions = [i for i, q in enumerate(q_vals) if q == max_q]
        if len(best_actions) > 1 and 6 in best_actions:
            best_actions.remove(6)
        if best_actions == [6]:
            sorted_q = sorted(enumerate(q_vals), key=lambda x: x[1], reverse=True)
            for idx, q in sorted_q:
                if idx != 6:
                    greedy = idx
                    break
        else:
            greedy = random.choice(best_actions)
        # Now actually decide action via core (should match greedy)
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        # Verify that tool_name matches greedy index
        chosen_idx = tool_names.index(tool_name) if tool_name in tool_names else -1
        if chosen_idx != greedy:
            print(f"WARNING: greedy index {greedy} ({tool_names[greedy]}) != chosen {tool_name}")
        # Record
        q_data.append({
            'step': step,
            'state_vector': state_vector[:5],  # first few dimensions
            'q_values': q_vals,
            'chosen_action': chosen_idx,
            'chosen_tool': tool_name,
        })
        action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
        # Simulate tool result (doesn't matter)
        tool_result = workspace.tool_result(tool_name, tool_args)
        workspace.actions.append({"tool": tool_name, "step": step})
    core.q_agent.epsilon = original_epsilon
    
    # Analyze Q-values across steps
    print(f"\n=== Q-value Analysis over {steps} steps ===")
    # Compute average Q per action
    avg_q = np.zeros(len(tool_names))
    count = 0
    for entry in q_data:
        avg_q += entry['q_values']
        count += 1
    avg_q /= count
    print("Average Q-values per action:")
    for idx, (tool, q) in enumerate(zip(tool_names, avg_q)):
        print(f"  {idx:2d} {tool:20s}: {q:8.3f}")
    # Compute standard deviation
    std_q = np.zeros(len(tool_names))
    for entry in q_data:
        std_q += (entry['q_values'] - avg_q) ** 2
    std_q = np.sqrt(std_q / count)
    print("\nStd Dev of Q-values per action:")
    for idx, (tool, std) in enumerate(zip(tool_names, std_q)):
        print(f"  {idx:2d} {tool:20s}: {std:8.3f}")
    # Show action distribution
    print(f"\nAction distribution (counts):")
    total = sum(action_counts.values())
    for tool in tool_names:
        cnt = action_counts.get(tool, 0)
        if cnt > 0:
            print(f"  {tool:20s}: {cnt:4d} ({cnt/total*100:.1f}%)")
    # Productive distribution
    prod_counts = {tool: action_counts.get(tool,0) for tool in productive}
    prod_total = sum(prod_counts.values())
    if prod_total > 0:
        print(f"\nProductive tool distribution:")
        for tool in productive:
            cnt = prod_counts[tool]
            print(f"  {tool:20s}: {cnt:4d} ({cnt/prod_total*100:.1f}%)")
    return q_data

if __name__ == "__main__":
    # Try latest model
    model_dir = "artifacts/agi_core_continuous_trained_gen22_v2"
    core = load_model(model_dir)
    if core:
        inspect_q_values(core, steps=200)