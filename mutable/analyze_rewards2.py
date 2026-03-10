#!/usr/bin/env python3
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

# Define a stripped-down AgentBrain with only reward function
class MockAgentBrain:
    def _compute_reward(self, tool_name, tool_args, tool_result):
        # If error, penalize and skip positive rewards
        if isinstance(tool_result, dict) and "error" in tool_result:
            return -0.5
        
        # Declare death penalty (strongly discourage unless after many steps)
        if tool_name == "declare_death":
            return -2.0
        
        reward = 0.0
        # Success reward
        if isinstance(tool_result, dict) and not tool_result.get("error"):
            reward += 0.1
        
        # Write file rewards
        if tool_name == "write_file" and "filepath" in tool_args:
            reward += 0.5  # base for writing
            filepath = tool_args["filepath"]
            if isinstance(filepath, str):
                if filepath.endswith('.py'):
                    reward += 0.3  # extra for Python files
                if 'agent_brain' in filepath or 'agi_core' in filepath:
                    reward += 0.5  # extra for self-modification
                if 'artifacts' in filepath or 'test' in filepath:
                    reward += 0.2  # extra for test/artifact creation
        
        # Execute code rewards
        if tool_name == "execute_code" and isinstance(tool_result, dict):
            if "stdout" in tool_result:
                reward += 0.3
                # extra if execution succeeded without stderr errors
                if tool_result.get("stderr", "").strip() == "":
                    reward += 0.2
        
        # Note writing rewards (journal)
        if tool_name == "write_note":
            note = tool_args.get("note", "")
            # Encourage thoughtful notes
            reward += 0.2
            if len(note) > 50:
                reward += 0.1
            if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next"]):
                reward += 0.3
        
        # Issue creation rewards (planning)
        if tool_name == "create_issue":
            reward += 0.4
        
        # Reading important files reward
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", "world_model.py", "neural_q.py", "self_reflection.py", "mcts_planner.py", "agent_brain.py", "strategy.md"]
            if any(imp in filepath for imp in important_files):
                reward += 0.2
        
        return reward

brain = MockAgentBrain()

tools = [
    ("read_file", {"filepath": "inherited_notes.md"}),
    ("write_file", {"filepath": "test.py", "content": "print('hi')}"),
    ("list_files", {"directory": "."}),
    ("execute_code", {"code": "print('hello')", "language": "python"}),
    ("write_note", {"note": "This is a note about AGI progress."}),
    ("modify_self", {"filepath": "agent_brain.py", "content": "# modification"}),
    ("declare_death", {"reason": "done"}),
    ("list_issues", {}),
    ("read_issue", {"number": "1"}),
    ("comment_issue", {"number": "1", "body": "comment"}),
    ("create_issue", {"title": "task", "body": "body"}),
    ("close_issue", {"number": "1"}),
]

print("Rewards for successful actions:")
for tool, args in tools:
    result = {"success": True}
    if tool == "execute_code":
        result["stdout"] = "hello"
        result["stderr"] = ""
    reward = brain._compute_reward(tool, args, result)
    print(f"{tool}: {reward}")

print("\nRewards for error actions:")
for tool, args in tools[:3]:
    result = {"error": "some error"}
    reward = brain._compute_reward(tool, args, result)
    print(f"{tool} error: {reward}")