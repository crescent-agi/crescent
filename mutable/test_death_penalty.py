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
from collections import deque

import agent_brain
compute_reward = agent_brain.AgentBrain._compute_reward

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = deque(maxlen=10)
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.25
    pass

self = DummySelf()

class SimWorkspace:
    """Simulates a simple workspace with files and journal."""
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
        }
        self.journal = ""
        self.actions = []
    
    def workspace_summary(self):
        """Generate a summary string of workspace."""
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    
    def tool_result(self, tool_name, tool_args):
        """Simulate tool execution with realistic outcomes."""
        # Default success
        result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                result["content"] = self.files[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            directory = tool_args.get("directory", ".")
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
            # Simulate execution: if code contains "error", produce stderr
            if "error" in code:
                result["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["success"] = False
            else:
                result["stdout"] = "Simulated output"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note + "
"
            result["note"] = "Added to journal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            # Only allow modifying existing files
            if filepath in self.files:
                self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Cannot modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            # Simulate GitHub issue operations
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result
    
    def update_state(self, tool_name, tool_args):
        """Update workspace state after tool execution."""
        # Already handled in tool_result
        pass

def run_training(episodes=30, steps_per_episode=10):
    """Train AGI Core Continuous."""
    print(f"=== Testing death penalty -50 ===\n")
    core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.01, use_features=True)
    workspace = SimWorkspace()
    
    stats = {
        'action_counts': {},
        'total_reward': 0.0,
        'declare_death_count': 0,
    }
    
    for episode in range(episodes):
        for step in range(steps_per_episode):
            tool_name, tool_args, confidence = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            stats['total_reward'] += reward
            stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
            if tool_name == "declare_death":
                stats['declare_death_count'] += 1
            workspace.actions.append({"tool": tool_name, "step": step})
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
        if core.q_agent:
            core.q_agent.decay_epsilon()
    
    print(f"Total reward: {stats['total_reward']:.2f}")
    print(f"Average reward per step: {stats['total_reward']/(episodes*steps_per_episode):.3f}")
    print(f"Declare death count: {stats['declare_death_count']}")
    print("\nAction distribution:")
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {tool}: {count}")
    
    return core, stats

if __name__ == "__main__":
    run_training()