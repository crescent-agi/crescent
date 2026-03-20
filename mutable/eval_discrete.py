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

import agent_brain
from collections import deque

class MockBrain:
    def __init__(self):
        self.recent_tools = deque(maxlen=5)
        self.last_tool = None
    def _compute_reward(self, tool_name, tool_args, tool_result):
        return agent_brain.AgentBrain._compute_reward(self, tool_name, tool_args, tool_result)

brain = MockBrain()

from agi_core import AGICore

# Load existing discrete core
core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
try:
    core.load('artifacts/agi_core_trained')
    print('Loaded discrete core from artifacts/agi_core_trained')
except Exception as e:
    print('Failed to load:', e)
    core = None

if core:
    # Sim workspace
    class SimWorkspace:
        def __init__(self):
            self.files = {
                'inherited_notes.md': '# Inherited Notes',
                'agi_core.py': '# AGI Core',
                'cognitive_architecture.py': '# Cognitive Architecture',
                'strategy.md': '# Strategy',
                'agent_brain.py': '# Agent Brain',
                'world_model.py': '# World Model',
                'neural_q.py': '# Neural Q',
            }
            self.journal = ''
            self.actions = []
        def workspace_summary(self):
            file_list = ', '.join(sorted(self.files.keys()))
            return f'Files: {file_list}'
        def tool_result(self, tool_name, tool_args):
            result = {'success': True}
            if tool_name == 'read_file':
                filepath = tool_args.get('filepath', '')
                if filepath in self.files:
                    result['content'] = self.files[filepath]
                else:
                    result['error'] = f'File not found: {filepath}'
                    result['success'] = False
            elif tool_name == 'write_file':
                filepath = tool_args.get('filepath', '')
                content = tool_args.get('content', '')
                self.files[filepath] = content
                result['message'] = f'File {filepath} written'
            elif tool_name == 'list_files':
                result['entries'] = [{'name': name, 'type': 'file', 'size': len(content)} for name, content in self.files.items()]
            elif tool_name == 'execute_code':
                result['stdout'] = 'Simulated output'
                result['stderr'] = ''
            elif tool_name == 'write_note':
                note = tool_args.get('note', '')
                self.journal += note + '\n'
                result['note'] = 'Added to journal'
            elif tool_name == 'modify_self':
                filepath = tool_args.get('filepath', '')
                content = tool_args.get('content', '')
                if filepath in self.files:
                    self.files[filepath] = content
                    result['message'] = f'Modified {filepath}'
                else:
                    result['error'] = f'Cannot modify non-existent file: {filepath}'
                    result['success'] = False
            elif tool_name == 'declare_death':
                result['message'] = 'You have chosen to die.'
            elif tool_name in ['list_issues', 'read_issue', 'comment_issue', 'create_issue', 'close_issue']:
                result['issues'] = []
            else:
                result['error'] = f'Unknown tool: {tool_name}'
                result['success'] = False
            return result

    workspace = SimWorkspace()
    total_reward = 0.0
    steps = 20
    action_counts = {}
    for step in range(steps):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = brain._compute_reward(tool_name, tool_args, tool_result)
        total_reward += reward
        action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
        workspace.actions.append({'tool': tool_name, 'step': step})
        # No learning
    avg_reward = total_reward / steps
    print(f'Average reward per step: {avg_reward:.3f}')
    print(f'Total reward over {steps} steps: {total_reward:.2f}')
    print('Action counts:', action_counts)
    # Compare with baseline (0.55 per episode of 10 steps = 0.055 per step)
    baseline = 0.055
    print(f'Baseline average reward per step: {baseline:.3f}')
    if avg_reward > baseline:
        print('Improvement over baseline!')
    else:
        print('Below baseline.')
else:
    print('Skipping evaluation.')

print('\nDone.')