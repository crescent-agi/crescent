#!/usr/bin/env python3
"""
Simulate AGI Core learning with improved reward function.
"""
import sys
sys.path.insert(0, '.')

# Mock core.llm_client for agent_brain import (not needed if we don't import agent_brain)
# We'll just import the reward function from agent_brain, which requires the mock.
class MockLLMAuthenticationError(Exception):
    pass

class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError

sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core import AGICore
import random

# Import the reward function from agent_brain
import agent_brain
compute_reward = agent_brain.AgentBrain._compute_reward

class DummySelf:
    pass

self = DummySelf()

def simulate_tool_result(tool_name, tool_args):
    """Simulate a successful tool result for most tools."""
    # For simplicity, assume all tools succeed except declare_death (which we treat specially)
    if tool_name == "declare_death":
        return {"success": True, "message": "You died."}
    elif tool_name == "write_file":
        return {"success": True}
    elif tool_name == "execute_code":
        return {"stdout": "Simulated output", "stderr": ""}
    elif tool_name == "read_file":
        return {"content": "Simulated content"}
    elif tool_name == "list_files":
        return {"entries": []}
    elif tool_name == "write_note":
        return {"success": True, "note": "Added to journal"}
    elif tool_name == "modify_self":
        return {"success": True}
    elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
        return {"success": True}
    else:
        return {"success": True}

def simulate_workspace_change(workspace, tool_name, tool_args):
    """Update workspace string based on action."""
    # Very simple: just append a token
    if tool_name == "write_file" and "filepath" in tool_args:
        filepath = tool_args["filepath"]
        if isinstance(filepath, str):
            workspace += f" {filepath}"
    return workspace

def simulate_journal_change(journal, tool_name, tool_args):
    if tool_name == "write_note":
        note = tool_args.get("note", "")
        journal += f"{note}\\n"
    return journal

def run_simulation(episodes=100, steps_per_episode=10):
    core = AGICore(state_size=50, hidden_size=16, learning_rate=0.05)
    workspace = "file1.py file2.md"
    journal = ""
    actions = []
    
    stats = {
        'declare_death_count': 0,
        'write_file_count': 0,
        'execute_code_count': 0,
        'read_file_count': 0,
        'other_count': 0,
        'total_reward': 0.0,
    }
    
    for episode in range(episodes):
        episode_reward = 0.0
        for step in range(steps_per_episode):
            # AGI Core decides action
            tool_name, tool_args, confidence = core.decide_action(workspace, journal, actions)
            # Simulate tool result
            tool_result = simulate_tool_result(tool_name, tool_args)
            # Compute reward using agent_brain's reward function
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            episode_reward += reward
            
            # Update stats
            if tool_name == "declare_death":
                stats['declare_death_count'] += 1
            elif tool_name == "write_file":
                stats['write_file_count'] += 1
            elif tool_name == "execute_code":
                stats['execute_code_count'] += 1
            elif tool_name == "read_file":
                stats['read_file_count'] += 1
            else:
                stats['other_count'] += 1
            
            # Simulate workspace and journal updates (simplified)
            workspace = simulate_workspace_change(workspace, tool_name, tool_args)
            journal = simulate_journal_change(journal, tool_name, tool_args)
            actions.append({"tool": tool_name, "step": step})
            
            # Learn from outcome
            core.learn_from_outcome(reward, workspace, journal, actions)
        
        stats['total_reward'] += episode_reward
        if (episode + 1) % 20 == 0:
            print(f"Episode {episode+1}: total reward {episode_reward:.2f}, deaths {stats['declare_death_count']}")
    
    print("\\nSimulation finished.")
    print("Action counts:", stats)
    print(f"Average reward per step: {stats['total_reward']/(episodes*steps_per_episode):.3f}")
    
    # Show Q-values for a few states (if Q-agent exists)
    if core.q_agent:
        print("\\nSample Q-values for state 0:")
        q_vals = core.q_agent.nn.predict(core.q_agent._one_hot(0))
        print(q_vals)
        best_action = max(range(len(q_vals)), key=lambda i: q_vals[i])
        print(f"Best action index: {best_action}")
    
    return core, stats

if __name__ == "__main__":
    core, stats = run_simulation(episodes=50, steps_per_episode=10)
    # Save the trained core
    import os
    os.makedirs('artifacts/agi_core_trained', exist_ok=True)
    core.save('artifacts/agi_core_trained')
    print("Saved trained AGI Core to artifacts/agi_core_trained")