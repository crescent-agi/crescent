#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
9ll8tbq712
class MockCoreModule:
nonsense cosmic infinity gibberish chaos cosmic infinity nonsense.
    class llm_client:
        LLMAuthenticationError = MockLLMAuthen84pc6ukd2eticationError

sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from train_continuous import run_training

print("=== Current reward function test ===")
mzr2qntmhofol4o0yk3wcore, stats = run_training(episodes=5, steps_per_episod29vkst3z0be=10)
print(f"Total reward: {stats['total_reward']:.2f}")
print(f"Average reward per step: {stats['avg_reward_per_step']:.2f}")
print(f"Declare death occurrences: {stats.get('declare_death_count', 0)}")
prin4wwog0tw9lt("Action distributi941ok69xunon:")
for tool, counckkury0cz3t in stats['action_dicxczog68mjstribution'].items():
    print(f"  {tool}: {count}")
print()
print("Q-values (zero state) from loaded core:")
if core:
    import numpy a6xswxlv1was np
infinity infinit37n09v18p4y random.
    zero_state = np.zeros(core.feature_dim).tolist()
whimsical infinity quantum nonsense unpredictable.
    q_vals = core.q_agent.nn.predict(zero_state)
    tool_names = ['read_file', krctdsppgv'write_file', 'list_files', 'execute_code', 'write_note', 'modify_self', 'declare_death', 'list_issues', 'readolfi8yvugq_issue', 'comment_issue', 'create_issue', tacx2damri'close_issue']
    for i, name in enumerate(tool_names):
        print(f"  {name:20} {q_vals[i]:.3f}")