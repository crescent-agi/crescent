#!/usr/bin/env python3
"""
Quick simulation of AGI Core learning with simple rewards.
"""
import sys
sys.path.insert(0, '.')

from agi_core import AGICore
import random

def simple_reward(tool_name, tool_args, tool_result):
    """Mimic the improved reward function."""
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -0.5
    if tool_name == "declare_death":
        return -2.0
    reward = 0.0
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 0.1
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
    if tool_name == "execute_code" and isinstance(tool_result, dict):
        if "stdout" in tool_result:
            reward += 0.3
            if tool_result.get("stderr", "").strip() == "":
                reward += 0.2
    if tool_name == "write_note":
        reward += 0.2
        note = tool_args.get("note", "")
        if len(note) > 50:
            reward += 0.1
        if any(k in note.lower() for k in ["progress", "improve", "agi", "plan", "next"]):
            reward += 0.3
    if tool_name == "create_issue":
        reward += 0.4
    if tool_name == "read_file":
        filepath = tool_args.get("filepath", "")
        important = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", "world_model.py", "neural_q.py", "self_reflection.py", "mcts_planner.py", "agent_brain.py", "strategy.md"]
        if any(imp in filepath for imp in important):
            reward += 0.2
    return reward

def simulate():
    core = AGICore(state_size=30, hidden_size=12, learning_rate=0.05)
    workspace = "file1.py file2.md"
    journal = ""
    actions = []
    
    death_counts = []
    for step in range(50):
        tool_name, tool_args, conf = core.decide_action(workspace, journal, actions)
        # Simulate success for all tools (including declare_death)
        tool_result = {"success": True}
        reward = simple_reward(tool_name, tool_args, tool_result)
        # Update workspace slightly (so state changes)
        workspace += f" {step}"
        actions.append({"tool": tool_name})
        core.learn_from_outcome(reward, workspace, journal, actions)
        if tool_name == "declare_death":
            death_counts.append(step)
    
    print(f"Declare death occurred at steps: {death_counts}")
    print(f"Total deaths: {len(death_counts)}")
    # Show Q-values for state 0 if available
    if core.q_agent:
        q = core.q_agent.nn.predict(core.q_agent._one_hot(0))
        print(f"Q-values for state 0: {q}")
        best = max(range(len(q)), key=lambda i: q[i])
        print(f"Best action index: {best}")
    return core

if __name__ == "__main__":
    simulate()