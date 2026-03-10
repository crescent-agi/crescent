#!/usr/bin/env python3
"""
Validate deterministic policy of latest trained model.
"""
import sys
sys.path.insert(0, '.')
class MockLLMAuthenticationError(Exception): pass
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

def load_core(model_dir):
    core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                             learning_rate=0.001, exploration_rate=0.5,
                             epsilon_decay=0.98, epsilon_min=0.1, use_features=True)
    if os.path.exists(model_dir):
        core.load(model_dir)
        print(f"Loaded model from {model_dir}")
    else:
        print(f"Model not found, using fresh core")
    return core

def run_validation_with_q_logging(core, steps=500):
    original_epsilon = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    # Import feature extractor
    from feature_extractor_enhanced import EnhancedFeatureExtractor
    extractor = EnhancedFeatureExtractor()
    
    tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                  "modify_self", "declare_death", "list_issues", "read_issue",
                  "comment_issue", "create_issue", "close_issue"]
    productive = ["write_file", "execute_code", "modify_self", "read_file"]
    
    action_counts = {tool:0 for tool in tool_names}
    q_log = []
    
    for step in range(steps):
        # Extract state vector
        state_vec = extractor.extract(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        q_vals = core.q_agent.nn.predict(state_vec)
        # Choose greedy action (mimic masked greedy)
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
        # Decide action via core (should match)
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        chosen_idx = tool_names.index(tool_name) if tool_name in tool_names else -1
        # Record
        q_log.append({
            'step': step,
            'state': state_vec[:5],
            'q_values': q_vals,
            'chosen': chosen_idx,
            'tool': tool_name,
        })
        action_counts[tool_name] += 1
        # Simulate result
        tool_result = workspace.tool_result(tool_name, tool_args)
        workspace.actions.append({"tool": tool_name, "step": step})
    
    core.q_agent.epsilon = original_epsilon
    
    # Compute statistics
    total = sum(action_counts.values())
    print(f"\n=== Deterministic Validation ({steps} steps) ===")
    print("Action distribution:")
    for tool in tool_names:
        cnt = action_counts[tool]
        if cnt > 0:
            print(f"  {tool:20s}: {cnt:4d} ({cnt/total*100:.1f}%)")
    # Productive distribution
    prod_counts = {tool: action_counts[tool] for tool in productive}
    prod_total = sum(prod_counts.values())
    if prod_total > 0:
        print("\nProductive tool distribution:")
        for tool in productive:
            cnt = prod_counts[tool]
            print(f"  {tool:20s}: {cnt:4d} ({cnt/prod_total*100:.1f}%)")
    # Non-productive total
    nonprod_tools = set(tool_names) - set(productive) - {"declare_death"}
    nonprod_total = sum(action_counts[tool] for tool in nonprod_tools)
    print(f"\nNon-productive actions: {nonprod_total}")
    # Average Q-values per action across steps
    avg_q = np.zeros(len(tool_names))
    for entry in q_log:
        avg_q += entry['q_values']
    avg_q /= len(q_log)
    print("\nAverage Q-values per action:")
    for idx, (tool, q) in enumerate(zip(tool_names, avg_q)):
        print(f"  {idx:2d} {tool:20s}: {q:8.3f}")
    # Std dev
    std_q = np.zeros(len(tool_names))
    for entry in q_log:
        std_q += (entry['q_values'] - avg_q) ** 2
    std_q = np.sqrt(std_q / len(q_log))
    print("\nStd Dev of Q-values:")
    for idx, (tool, std) in enumerate(zip(tool_names, std_q)):
        print(f"  {idx:2d} {tool:20s}: {std:8.3f}")
    # Q-value range
    print("\nQ-value range (min, max) across steps:")
    min_q = np.min([entry['q_values'] for entry in q_log], axis=0)
    max_q = np.max([entry['q_values'] for entry in q_log], axis=0)
    for idx, (tool, mn, mx) in enumerate(zip(tool_names, min_q, max_q)):
        print(f"  {idx:2d} {tool:20s}: [{mn:8.3f}, {mx:8.3f}]")
    # Determine which productive tool has highest average Q
    prod_indices = [tool_names.index(t) for t in productive]
    prod_avg = [avg_q[i] for i in prod_indices]
    highest_idx = prod_indices[np.argmax(prod_avg)]
    print(f"\nHighest average Q among productive tools: {tool_names[highest_idx]} ({max(prod_avg):.3f})")
    return action_counts, q_log

if __name__ == "__main__":
    # Try latest model
    model_dir = "artifacts/agi_core_continuous_trained_gen22_v2"
    core = load_core(model_dir)
    if core:
        action_counts, q_log = run_validation_with_q_logging(core, steps=1000)
        # Check if policy collapses to modify_self
        modify_count = action_counts.get("modify_self", 0)
        total = sum(action_counts.values())
        if modify_count == total:
            print("\n!!! POLICY COLLAPSE: Only modify_self used.")
        elif modify_count / total > 0.8:
            print(f"\n!!! POLICY NEAR COLLAPSE: modify_self proportion {modify_count/total*100:.1f}%")
        else:
            print(f"\nModify_self proportion: {modify_count/total*100:.1f}%")
        # Save logs
        import pickle
        with open('deterministic_validation_log.pkl', 'wb') as f:
            pickle.dump({'action_counts': action_counts, 'q_log': q_log}, f)
        print("Log saved to deterministic_validation_log.pkl")