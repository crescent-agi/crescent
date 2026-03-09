#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core import AGICore
import random
import agent_brain
compute_reward = agent_brain.AgentBrain._compute_reward

class DummySelf: pass
self = DummySelf()

def simulate_tool_result(tool_name, tool_args):
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

def run_simulation(episodes=2, steps_per_episode=2):
    core = AGICore(state_size=10, hidden_size=8, learning_rate=0.05)
    workspace = "file1.py file2.md"
    journal = ""
    actions = []
    for episode in range(episodes):
        for step in range(steps_per_episode):
            tool_name, tool_args, confidence = core.decide_action(workspace, journal, actions)
            tool_result = simulate_tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            workspace += f" updated{step}"
            journal += f"Step {step}\n"
            actions.append({"tool": tool_name, "step": step})
            core.learn_from_outcome(reward, workspace, journal, actions)
            print(f"Episode {episode+1}, step {step+1}: {tool_name}, reward {reward:.2f}")
    print("Simulation done")

if __name__ == "__main__":
    run_simulation()