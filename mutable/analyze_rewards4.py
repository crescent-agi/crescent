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

# Mock sandbox
from pathlib import Path
class MockSandbox:
    def __init__(self):
        self.gen_dir = Path('.')
    def get_workspace_summary(self):
        return \"\"
    def append_journal(self, note):
        pass
    def log_action(self, action):
        pass
    def read_file(self, filepath):
        return {\"content\": \"\"}
    def write_file(self, filepath, content):
        return {\"success\": True}
    def list_files(self, directory):
        return {\"entries\": []}
    def execute_code(self, code, language):
        return {\"stdout\": \"\", \"stderr\": \"\"}
    def modify_self(self, filepath, content):
        return {\"success\": True}
    def list_issues(self, label, limit):
        return {\"issues\": []}
    def read_issue(self, number):
        return {\"issue\": {}}
    def comment_issue(self, number, body):
        return {\"success\": True}
    def create_issue(self, title, body, labels):
        return {\"success\": True}
    def close_issue(self, number):
        return {\"success\": True}

# Mock death monitor
class MockDeathMonitor:
    def record_step(self, action):
        pass
    def record_self_termination(self):
        pass
    def check(self):
        return None
    def record_crash(self, msg):
        pass
    def get_stats(self):
        return {}
    def import_state(self, state):
        pass
    def export_state(self):
        return {}

from agent_brain import AgentBrain
sandbox = MockSandbox()
death = MockDeathMonitor()
brain = AgentBrain(None, sandbox, death, 0)

# Now compute rewards
tools = [
    (\"read_file\", {\"filepath\": \"inherited_notes.md\"}),
    (\"write_file\", {\"filepath\": \"test.py\", \"content\": \"print('hi')}\"),
    (\"list_files\", {\"directory\": \".\"}),
    (\"execute_code\", {\"code\": \"print('hello')\", \"language\": \"python\"}),
    (\"write_note\", {\"note\": \"This is a note about AGI progress.\"}),
    (\"modify_self\", {\"filepath\": \"agent_brain.py\", \"content\": \"# modification\"}),
    (\"declare_death\", {\"reason\": \"done\"}),
    (\"list_issues\", {}),
    (\"read_issue\", {\"number\": \"1\"}),
    (\"comment_issue\", {\"number\": \"1\", \"body\": \"comment\"}),
    (\"create_issue\", {\"title\": \"task\", \"body\": \"body\"}),
    (\"close_issue\", {\"number\": \"1\"}),
]

print(\"Rewards for successful actions:\")
for tool, args in tools:
    result = {\"success\": True}
    if tool == \"execute_code\":
        result[\"stdout\"] = \"hello\"
        result[\"stderr\"] = \"\"
    reward = brain._compute_reward(tool, args, result)
    print(f\"{tool}: {reward}\")

print(\"\\nRewards for error actions:\")
for tool, args in tools[:3]:
    result = {\"error\": \"some error\"}
    reward = brain._compute_reward(tool, args, result)
    print(f\"{tool} error: {reward}\")

print(\"\\nReward for write_note with long note:\")
note = \"x\" * 60
reward = brain._compute_reward(\"write_note\", {\"note\": note}, {\"success\": True})
print(f\"write_note length 60: {reward}\")
note_with_keywords = \"Progress on AGI: we need to improve planning.\"
reward = brain._compute_reward(\"write_note\", {\"note\": note_with_keywords}, {\"success\": True})
print(f\"write_note with keywords: {reward}\")