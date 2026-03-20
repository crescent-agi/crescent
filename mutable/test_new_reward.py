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

print('Testing new reward function with sample actions...')
# Simulate a few actions
def test_action(tool, args, result, last_tool=None, recent=None):
    brain.last_tool = last_tool
    if recent:
        brain.recent_tools = deque(recent, maxlen=5)
    else:
        brain.recent_tools = deque(maxlen=5)
    reward = brain._compute_reward(tool, args, result)
    print(f'{tool} {args} -> {reward:.2f}')
    return reward

# Success result
result = {'success': True}
# Test productive actions
print('
1. Productive actions (first use):')
test_action('write_file', {'filepath': 'test.py', 'content': 'print("hello")'}, result)
test_action('execute_code', {'code': 'print("test")', 'language': 'python'}, {'stdout': 'test passed', 'stderr': ''})
test_action('modify_self', {'filepath': 'agent_brain.py', 'content': '...'}, result)
test_action('read_file', {'filepath': 'agi_core.py'}, result)
test_action('create_issue', {'title': 'test', 'body': 'test'}, result)
test_action('write_note', {'note': 'Made progress on AGI core. Next step: improve planning.'}, result)

print('
2. Consecutive same tool penalties:')
brain.last_tool = 'write_file'
brain.recent_tools = deque(['write_file'], maxlen=5)
reward = brain._compute_reward('write_file', {'filepath': 'test2.py', 'content': '...'}, result)
print(f'Second write_file -> {reward:.2f}')

print('
3. Diversity bonus:')
brain.last_tool = 'list_files'
brain.recent_tools = deque(['list_files', 'read_file'], maxlen=5)
reward = brain._compute_reward('write_file', {'filepath': 'new.py', 'content': '...'}, result)
print(f'New tool write_file -> {reward:.2f}')

print('
4. Error penalty:')
reward = brain._compute_reward('read_file', {'filepath': 'nonexistent.txt'}, {'error': 'File not found'})
print(f'Error -> {reward:.2f}')

print('
5. Declare death penalty:')
reward = brain._compute_reward('declare_death', {'reason': 'test'}, {'message': '...'})
print(f'Declare death -> {reward:.2f}')

# Now train a fresh core for a few episodes to see if rewards become positive
print('
--- Quick training ---')
from agi_core_continuous import AGICoreContinuous

class SimWorkspace:
    def __init__(self):
        self.files = {
            'inherited_notes.md': '# Inherited Notes',
            'agi_core.py': '# AGI Core',
            'cognitive_architecture.py': '# Cognitive Architecture',
            'strategy.md': '# Strategy',
        }
        self.journal = ''
        self.actions = []
    def workspace_summary(self):
        file_list = ', '.join(self.files.keys())
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

core = AGICoreContinuous(feature_dim=15, hidden_size=32, learning_rate=0.01, use_features=True)
workspace = SimWorkspace()
stats = {'total_reward': 0.0, 'action_counts': {}}
episodes = 3
steps = 8
for ep in range(episodes):
    episode_reward = 0.0
    for step in range(steps):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = brain._compute_reward(tool_name, tool_args, tool_result)
        episode_reward += reward
        stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        workspace.actions.append({'tool': tool_name, 'step': step})
        core.learn_from_outcome(reward, workspace.workspace_summary(), workspace.journal, workspace.actions)
    stats['total_reward'] += episode_reward
    print(f'Episode {ep+1}: reward {episode_reward:.2f}')
print(f'Total reward: {stats["total_reward"]:.2f}')
print('Action counts:', stats['action_counts'])
if stats['total_reward'] > 0:
    print('SUCCESS: Total reward positive!')
else:
    print('WARNING: Total reward still negative.')

# Inspect Q-values
print('
Q-values after training:')
state_vec = core.compute_state_vector(workspace.workspace_summary(), workspace.journal, workspace.actions)
if core.q_agent:
    q_vals = core.q_agent.nn.predict(state_vec)
    from agi_core_continuous import TOOL_NAMES
    for i, tool in enumerate(TOOL_NAMES):
        print(f'  {tool}: {q_vals[i]:.3f}')
    best = max(range(len(q_vals)), key=lambda i: q_vals[i])
    print(f'Best action: {TOOL_NAMES[best]}')
    # Count positive Q-values
    pos = sum(1 for q in q_vals if q > 0)
    print(f'Positive Q-values: {pos}/{len(q_vals)}')

print('
Test complete.')