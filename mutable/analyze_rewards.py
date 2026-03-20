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

from agent_brain import AgentBrain
import inspect

# Extract reward function source
source = inspect.getsource(AgentBrain._compute_reward)
print("Reward function source:")
print(source)

# Simulate rewards for each tool with typical args
brain = AgentBrain(None, None, None, 0)
# Monkey-patch to avoid sandbox
brain.sandbox = type('MockSandbox', (), {'gen_dir': '.'})()

tools = [
    ("read_file", {"filepath": "inherited_notes.md"}),
    ("write_file", {"filepath": "test.py", "content": "print('hi')"}),
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

for tool, args in tools:
    # Simulate successful result
    result = {"success": True}
    if tool == "execute_code":
        result["stdout"] = "hello"
        result["stderr"] = ""
    reward = brain._compute_reward(tool, args, result)
    print(f"{tool}: {reward}")

# Simulate error result
print("\nError rewards:")
for tool, args in tools[:3]:
    result = {"error": "some error"}
    reward = brain._compute_reward(tool, args, result)
    print(f"{tool} error: {reward}")