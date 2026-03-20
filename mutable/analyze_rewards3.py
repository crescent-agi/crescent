#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Read agent_brain.py
with open('agent_brain.py', 'r') as f:
    content = f.read()

# Find the _compute_reward method
import re
pattern = r'def _compute_reward\(self,.*?\):(.*?)(?=\n\s*def |\n\s*$)'  # not perfect
match = re.search(pattern, content, re.DOTALL)
if match:
    method_body = match.group(1)
    # Define a function using exec
    func_code = f'def compute_reward(self, tool_name, tool_args, tool_result):{method_body}'
    exec(func_code, globals())
    compute_reward = globals()['compute_reward']
else:
    # fallback: manually copy
    def compute_reward(self, tool_name, tool_args, tool_result):
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
            note = tool_args.get("note", "")
            reward += 0.2
            if len(note) > 50:
                reward += 0.1
            if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next"]):
                reward += 0.3
        if tool_name == "create_issue":
            reward += 0.4
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", "world_model.py", "neural_q.py", "self_reflection.py", "mcts_planner.py", "agent_brain.py", "strategy.md"]
            if any(imp in filepath for imp in important_files):
                reward += 0.2
        return reward

# Test
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
    reward = compute_reward(None, tool, args, result)
    print(f"{tool}: {reward}")

print("\nRewards for error actions:")
for tool, args in tools[:3]:
    result = {"error": "some error"}
    reward = compute_reward(None, tool, args, result)
    print(f"{tool} error: {reward}")