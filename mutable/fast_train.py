#!/usr/bin/env python3
"""
Fast training with minimal overhead.
"""
import sys
sys.path.insert(0, '.')

# Mock core.llm_client
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core import AGICore
import random

# Replicate reward function from agent_brain.py
def compute_reward(tool_name, tool_args, tool_result):
    # If error, penalize and skip positive rewards
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -0.5
    # Declare death penalty
    if tool_name == "declare_death":
        return -2.0
    reward = 0.0
    # Success reward
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 0.1
    # Write file rewards
    if tool_name == "write_file" and "filepath" in tool_args:
        reward += 0.5
        filepath = tool_args["filepath"]
        if isinstance(filepath, str):
            if filepath.endswith('.py'):
                reward += 0.3
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 0.5
            if 'artifacts' in filepath or 'test' in filepath:
                reward += 0.2
    # Execute code rewards
    if tool_name == "execute_code" and isinstance(tool_result, dict):
        if "stdout" in tool_result:
            reward += 0.3
            if tool_result.get("stderr", "").strip() == "":
                reward += 0.2
    # Note writing rewards
    if tool_name == "write_note":
        note = tool_args.get("note", "")
        reward += 0.2
        if len(note) > 50:
            reward += 0.1
        if any(kw in note.lower() for kw in ["progress", "improve", "agi", "plan", "next"]):
            reward += 0.3
    # Issue creation rewards
    if tool_name == "create_issue":
        reward += 0.4
    # Reading important files reward
    if tool_name == "read_file":
        filepath = tool_args.get("filepath", "")
        important = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", "world_model.py", "neural_q.py", "self_reflection.py", "mcts_planner.py", "agent_brain.py", "strategy.md"]
        if any(imp in filepath for imp in important):
            reward += 0.2
    return reward

# Simple simulation
def simulate_tool_result(tool_name, tool_args):
    # Always succeed for simplicity
    if tool_name == "write_file":
        return {"success": True}
    elif tool_name == "execute_code":
        return {"stdout": "output", "stderr": ""}
    elif tool_name == "read_file":
        return {"content": "content"}
    elif tool_name == "list_files":
        return {"entries": []}
    elif tool_name == "write_note":
        return {"success": True, "note": "added"}
    elif tool_name == "modify_self":
        return {"success": True}
    elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
        return {"success": True}
    elif tool_name == "declare_death":
        return {"message": "died"}
    else:
        return {"success": True}

def run_training():
    core = AGICore(state_size=50, hidden_size=16, learning_rate=0.01)
    core.planner = None
    workspace = "files"
    journal = ""
    actions = []
    total_reward = 0.0
    action_counts = {}
    # 100 steps total
    for step in range(100):
        tool_name, tool_args, conf = core.decide_action(workspace, journal, actions)
        tool_result = simulate_tool_result(tool_name, tool_args)
        reward = compute_reward(tool_name, tool_args, tool_result)
        total_reward += reward
        action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
        core.learn_from_outcome(reward, workspace, journal, actions)
        actions.append(tool_name)
        if (step + 1) % 20 == 0:
            print(f"Step {step+1}, avg reward {total_reward/(step+1):.3f}")
    print(f"Total reward: {total_reward:.2f}")
    print("Action distribution:", sorted(action_counts.items(), key=lambda x: x[1], reverse=True))
    # Evaluate with epsilon=0
    if core.q_agent:
        original_epsilon = core.q_agent.epsilon
        core.q_agent.epsilon = 0.0
        eval_actions = {}
        eval_reward = 0.0
        for i in range(20):
            tool_name, tool_args, conf = core.decide_action(workspace, journal, actions)
            tool_result = simulate_tool_result(tool_name, tool_args)
            reward = compute_reward(tool_name, tool_args, tool_result)
            eval_reward += reward
            eval_actions[tool_name] = eval_actions.get(tool_name, 0) + 1
        print(f"Eval avg reward: {eval_reward/20:.3f}")
        print("Eval actions:", sorted(eval_actions.items(), key=lambda x: x[1], reverse=True))
        core.q_agent.epsilon = original_epsilon
    # Save
    import os
    os.makedirs('artifacts/fast_trained', exist_ok=True)
    core.save('artifacts/fast_trained')
    print("Model saved.")

if __name__ == "__main__":
    import time
    start = time.time()
    run_training()
    end = time.time()
    print(f"Time: {end-start:.2f}s")