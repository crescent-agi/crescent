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

from agi_core import AGICore
import agent_brain
compute_reward = agent_brain.AgentBrain._compute_reward

class DummySelf:
    pass
self = DummySelf()

class SimWorkspace:
    def __init__(self):
        self.files = {
            \"inherited_notes.md\": \"# Inherited Notes\",
            \"agi_core.py\": \"# AGI Core\",
            \"cognitive_architecture.py\": \"# Cognitive Architecture\",
            \"strategy.md\": \"# Strategy\",
            \"agent_brain.py\": \"# Agent Brain\",
            \"world_model.py\": \"# World Model\",
            \"neural_q.py\": \"# Neural Q\",
        }
        self.journal = \"\"
        self.actions = []
    def workspace_summary(self):
        file_list = \", \".join(sorted(self.files.keys()))
        return f\"Files: {file_list}\"
    def tool_result(self, tool_name, tool_args):
        # Simple success
        result = {\"success\": True}
        if tool_name == \"read_file\":
            filepath = tool_args.get(\"filepath\", \"\")
            if filepath in self.files:
                result[\"content\"] = self.files[filepath]
            else:
                result[\"error\"] = f\"File not found: {filepath}\"
                result[\"success\"] = False
        elif tool_name == \"write_file\":
            filepath = tool_args.get(\"filepath\", \"\")
            content = tool_args.get(\"content\", \"\")
            self.files[filepath] = content
            result[\"message\"] = f\"File {filepath} written\"
        elif tool_name == \"list_files\":
            result[\"entries\"] = [{\"name\": name, \"type\": \"file\", \"size\": len(content)} for name, content in self.files.items()]
        elif tool_name == \"execute_code\":
            result[\"stdout\"] = \"Simulated output\"
            result[\"stderr\"] = \"\"
        elif tool_name == \"write_note\":
            note = tool_args.get(\"note\", \"\")
            self.journal += note + \"\\n\"
            result[\"note\"] = \"Added to journal\"
        elif tool_name == \"modify_self\":
            filepath = tool_args.get(\"filepath\", \"\")
            content = tool_args.get(\"content\", \"\")
            if filepath in self.files:
                self.files[filepath] = content
                result[\"message\"] = f\"Modified {filepath}\"
            else:
                result[\"error\"] = f\"Cannot modify non-existent file: {filepath}\"
                result[\"success\"] = False
        elif tool_name == \"declare_death\":
            result[\"message\"] = \"You have chosen to die.\"
        elif tool_name in [\"list_issues\", \"read_issue\", \"comment_issue\", \"create_issue\", \"close_issue\"]:
            result[\"issues\"] = []
        else:
            result[\"error\"] = f\"Unknown tool: {tool_name}\"
            result[\"success\"] = False
        return result

def run_training(core, total_episodes=5, steps_per_episode=10):
    workspace = SimWorkspace()
    stats = {'action_counts': {}, 'total_reward': 0.0}
    # Need to create an AgentBrain instance to have last_tool attribute? Actually compute_reward is unbound method; we need to call it with an instance.
    # We'll create a mock brain
    class MockBrain:
        last_tool = None
    brain = MockBrain()
    for episode in range(total_episodes):
        for step in range(steps_per_episode):
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(brain, tool_name, tool_args, tool_result)
            stats['total_reward'] += reward
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            core.learn_from_outcome(reward, workspace.workspace_summary(), workspace.journal, workspace.actions)
            workspace.actions.append({\"tool\": tool_name, \"step\": step})
    return stats

core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
try:
    core.load('artifacts/agi_core_trained')
    print('Loaded pre-trained')
except:
    pass

print('Starting mini training with recency penalty (5 episodes)...')
stats = run_training(core, total_episodes=5, steps_per_episode=10)
print('Training completed.')
print('Total reward:', stats['total_reward'])
print('Action counts:', stats['action_counts'])