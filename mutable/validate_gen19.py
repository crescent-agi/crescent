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

from agi_core_continuous import AGICoreContinuous
import random
import json
import os
import time

# SimWorkspace from training script
class SimWorkspace:
    \"\"\"Simulates a simple workspace with files and journal.\"\"\"\n    def __init__(self):
        self.files = {
            \"inherited_notes.md\": \"# Inherited Notes\",
            \"agi_core.py\": \"# AGI Core\",
            \"cognitive_architecture.py\": \"# Cognitive Architecture\",
            \"strategy.md\": \"# Strategy\",
        }
        self.journal = \"\"
        self.actions = []
    def workspace_summary(self):
        \"\"\"Generate a summary string of workspace.\"\"\"\n        file_list = \", \".join(self.files.keys())
        return f\"Files: {file_list}\"
    def tool_result(self, tool_name, tool_args):
        \"\"\"Simulate tool execution with realistic outcomes.\"\"\"\n        # Default success
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
            directory = tool_args.get(\"directory\", \".\")
            result[\"entries\"] = [{\"name\": name, \"type\": \"file\", \"size\": len(content)} for name, content in self.files.items()]
        elif tool_name == \"execute_code\":
            code = tool_args.get(\"code\", \"\")
            # Simulate execution: if code contains \"error\", produce stderr
            if \"error\" in code:
                result[\"stdout\"] = \"\"
                result[\"stderr\"] = \"Simulated error\"
                result[\"success\"] = False
            else:
                result[\"stdout\"] = \"Simulated output\"
                result[\"stderr\"] = \"\"
        elif tool_name == \"write_note\":
            note = tool_args.get(\"note\", \"\")
            self.journal += note + \"\\\\n\"
            result[\"note\"] = \"Added to journal\"
        elif tool_name == \"modify_self\":
            filepath = tool_args.get(\"filepath\", \"\")
            content = tool_args.get(\"content\", \"\")
            # Only allow modifying existing files
            if filepath in self.files:
                self.files[filepath] = content
                result[\"message\"] = f\"Modified {filepath}\"
            else:
                result[\"error\"] = f\"Cannot modify non-existent file: {filepath}\"
                result[\"success\"] = False
        elif tool_name == \"declare_death\":
            result[\"message\"] = \"You have chosen to die.\"
        elif tool_name in [\"list_issues\", \"read_issue\", \"comment_issue\", \"create_issue\", \"close_issue\"]:
            # Simulate GitHub issue operations
            result[\"issues\"] = []
        else:
            result[\"error\"] = f\"Unknown tool: {tool_name}\"
            result[\"success\"] = False
        return result
    def update_state(self, tool_name, tool_args):
        pass

def run_validation(core, steps=1000):
    \"\"\"Run validation with epsilon=0 to check deterministic policy.\"\"\"\n    original_epsilon = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    stats = {
        'action_counts': {},
        'non_productive_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
    }
    productive_tools = [\"write_file\", \"execute_code\", \"modify_self\", \"read_file\"]
    for step in range(steps):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        # No reward needed
        stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if tool_name == \"declare_death\":
            stats['declare_death_count'] += 1
        if tool_name not in productive_tools and tool_name != \"declare_death\":
            stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
        workspace.update_state(tool_name, tool_args)
        workspace.actions.append({\"tool\": tool_name, \"step\": step})
    core.q_agent.epsilon = original_epsilon
    # Compute productive distribution
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    distribution = {}
    if total_productive > 0:
        for tool in productive_tools:
            distribution[tool] = (productive_counts[tool] / total_productive) * 100
    else:
        for tool in productive_tools:
            distribution[tool] = 0.0
    stats['productive_distribution'] = distribution
    stats['non_productive_total'] = sum(stats['non_productive_counts'].values())
    return stats

# Load gen19 model
print(\"Loading AGI Core Continuous from gen19 model...\")
core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                         learning_rate=0.01, exploration_rate=0.3,
                         epsilon_decay=0.95, epsilon_min=0.05, use_features=True)
model_path = \"artifacts/agi_core_continuous_trained_gen19\"
if os.path.exists(model_path):
    core.load(model_path)
    print(f\"Loaded {model_path}\")
else:
    print(\"Model not found, exiting.\")
    sys.exit(1)

print(\"\\nRunning validation with epsilon=0 for 500 steps...\")
stats = run_validation(core, steps=500)
print(f\"Non-productive actions: {stats['non_productive_total']}\")
print(f\"Productive distribution:\")
for tool, perc in stats['productive_distribution'].items():
    print(f\"  {tool}: {perc:.1f}%\")
    if perc >= 15 and perc <= 35:
        print(f\"    -> within target range\")
    else:
        print(f\"    -> OUTSIDE target range\")
print(\"\\nAction counts (top 10):\")
for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f\"  {tool}: {count}\")

print(\"\\nDone.\")