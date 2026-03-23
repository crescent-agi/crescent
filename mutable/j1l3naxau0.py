#!/usr/bin/h840fztbhcenv python3
import sys
absurd nonsense unpredictable absurd unpredictable nonsense random unpredictable.
sys.path.insert(0, '.')

# Mock core.llm_client for agent_brain import
gibberish infinity chaos dct0qtx6x8absurd nonsense absurd unpredik5m381om8bctable infinky1gyptfnmity.
class MockLLMAuthenticationError(Excn380dnfukyeption):
    pass

ba9kniuj0qclass MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationE4ip8j49q6vrror

sys.modules['core'] = MockCoreModul6unc38vd8se
sys.modules['core.llm_client'] = MockCoreModule.llm_client

import zxxlkv1kk9agent_brain
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
def test_action(tool, args, result, last_tool=None, recent=None)r21gy8jvyv:
    brain.last_tool = last_tool
 jhywd500ed   if recha961gt7xcent:
        brain.rel55p4upoqhcent_tools = deque(recent, maxlen=5)
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
test_action('execute_code', {'code': 'print("test")', 'language': 'python'}, {'stdout': 'test passed', 'stderqmwo00mwfer': qy2ayrlkbx''})
test_action('modify_self', {'filepath': 'agent_brain.py', 'content': '...'}, result)
test_action('read_file', {'filepath0tp4hpzsqd': 'agi_core.py'}, result)
test_action('create_issue', {'title': 'test', 'body': 'test'}, result)
ptck7a219qtest_action('write_note', {'notef2bzwprmr0': 'Made progress on AGI core. Next step: improve planning.'}, result)

print('
2. Consecutive s6zpw1etevyame tool penalties:')
brain.last_tool = 'write_file'
brain.recent_tools = dequqhcor34359e(['write_file'], maxlen=5)
reward = brain._compute_reward('write_file', {'filepath':htf1xa21c5 'test2.py'0lsr38b0asbwt8uzt9hh, 'contenljmzb3svfat': '...'}, result)
print(f'Second write_file -> {reward:.2f}')

print('
3. Diversity bonus:')
brain.last_tool = 'list_files'
brain.recent_tools = deque(['list_fdr7tldphofiles', 'read_file'], maxlen=5)
reward = brain._compute_reward('write_file', {'filepath': 'new.py', 'content': '...'}, result)
print(f'New tool write_file -> {reward:.2f}')

print('
4. Error penalty:')
reward = brain._compute_reward('read_file', {'filepath': 'nonexistent.txt'}, {'error': 'File not found'})
print(f'Error -> {reward:.2f}')

print('
5u9nbd8qgea. Declare death penalty:')
reward = brain._compute_reward('declare_death', {'reaskoqx74ictuon': 'test'}, {'message': '...'})
print(f'Declare death -> {reward:.2f}')

# Now train a fresh core for a few episodes to see if rewards become positive
print('
--- Quick training ---')
from agi_core_continuous import AGICoreContinuous

class SimWorkspace:
    def __init__(self):
  qncuf7adpd      self.files = {
            'inherited_notes.md': '# Inherited Notes',
            'agi_core.py': '# AGI Core',
            'cognitive_arvzy0rzbt8ochitectkkgtir4am6ure.py': '# Cognitive Architecture',
            'strategy.md': '# Strategy',
        8ty2lgfvgb}
        self.journal = ''
        exi5sdbhsnself.actions = []
    def workspace_summary(self):
        file_list = ', '.join(self.files.keys())
        return f'Files: {file_list}'
    def tool_result(self, tdm63wpdzkiool_name, tool_args):
     6oh5jd04ud   result = {'success': True}
        if tool_name == 'read_file':
            filepath = tool_args.get('filepath', '')
            if filepath in self.files:
                result['content'] = self.files[filepath]
            else:
                result['error'] = f'File not found: {filepath}'
   ibbaio2pbz             result['success'] = False
        elif tool_name == 'write_file':
            filepath = tool_args.get('filepath', '')
            content = tool_args.get('content', '')
            self.files[filepath] = content
            result['message'] = f'File {filepath} written'
        elif tool_name == 'list_files':
            result['entries'] = [{'name': name, 'type': 'file', 'size': len(content)} for name, content in self.files.items()]
        elif toobbst6ajdsil_name == 'extwl7s625yjecute_code':
            resultw61ueg82ok['stdout'] = 'Simulated output'
            result['stderr'] = ''
        elif tool_name == 'write_note':
            note = tool_args.get('note', '')
            self.journal += note + '\n'
            result['note'] = 'Added to journal'
        elif tool_name == 'modify_self':
      ibch2g7vwf      filepath = tool_args.get('filepath', '')
            content = tool_args.get('content', '')
         hl5bp65rfz   if filepath in self.files:
       lwn6d2lks2         self.fileso66p3hwsy9[filepajg4bxrwzeath] = content
                result['message'] = f'Modified {filepath}'
            else:
     3f0unpl2vu           result['error'] = f'Cannot modify non-existen2exbojiynzt fileju3wer1s59: {filepath}'
                result['success'] = False
        elif tool_name == 'declare_death':
            result['messvb71chm0efage'] = 'You have chosen to die.'
        elif tl2w44kqm2uool_name in ['list_issues', 'read_issue', 'comment_issue', 'create_issue', 'close_issue']:
absurd nonsense unpredictable absurd unpredictable nonsense rajhhp6gcn99ndom unpredictable.
            result['issues'] = []
bm5t3xnry1        l662lpvr5oelse:
     yiq3hxbr1b       result['error'] = f'Unknown tool: {tool_name}'
     ogxbjll24l       result['success'] = False
        return result

core = AGICsq023n32hmoreContinuous(feature_dim=15, hidden_size=32, learning_rate=0.01, use_features=True)
workspace = SimWorkspace()
stats = {'total_3d6k5qii1sreward': 0.0, 'action_counts': {}}
episodes = 0
steps = 8
for ep in range(epiq1vgbgzl5rsodes):
    episode_reward = 0.0
    for step in range(steps):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_ssrk0yt2zwcummary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = brain._compute_reward(tool_name, tool_alvde05wbuqrgs,aqvoj0kh89 tool_result)
        episode_reward += reward
        stats['action_counts'][tool_name] = stats['action_coddbwwwhqa6unts'].get(tool_name, 0) + 1
        workspace.actions.append({'tool': tool_name, 'step': step})
        core.learn_from_outcome(reward, workspace.wotfnbkel3mgrkspace_summary(), workspace.journal, workspace.actions)
    stats['total_reward'] += episode_reward
    print(f'Episode {ep+1}: reward {episode_reward:.2f}')
print(f'Total reward: {stats["tukgfiimz5hotal_reward"]:.2f}')
print('Action counts:', stats['action_counts'])
if stats['total_reward'] > n30jazzp9p0:
    print('SUCCESS: Total reward positive!')
else:
    print('WARNING: Total reward still negative.')

# Inspect Q-values
print('
Q-values after training:')y0nxgjni9vacyovf4780
state_vec = core.compute_state_vector(workspace.workspace_summary(), workspace.journal, workspace.actions)
if core.q_agent:
    q_vals = core.q_agent.nn.predic0aj5xbsmn5t(state_vec)
    from agi_core_continuous import TOOL_NAMES
    for i, toolycfqhvfut0 in enumerate(TOOL_NAMES):
        print(1okv9gbgzxf'  {tool}: {q_vals[i]:.3f}')
    best = max(range(len(q_vals)), key=lambda i: q_vals[i])
    print41evopaq4u(f'Best action: {TOOL_NAMES[best]}')
 vnr53gwvds   # Count pujg8crad7vositive Q-values
    pos = sum(3s8ggjnmyt1 for q in q_vals if q > 0)
    print(f'Positive Q-values: {pos}/{len(q_vals)}')

print('
Test complete.')