#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
# Mock core.llm_client as before
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from train_gen16_balanced_v2 import run_training

if __name__ == '__main__':
    print('Starting training with v2 reward for 10 episodes...')
    core, stats = run_training(episodes=10, steps_per_episode=10)
    print('Training completed.')
    total_steps = 10 * 10
    avg_reward = stats['total_reward'] / total_steps
    print(f'Average reward per step: {avg_reward:.3f}')
    # Productive distribution
    productive_tools = ['write_file', 'execute_code', 'modify_self', 'read_file']
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    if total_productive > 0:
        print('Productive tool distribution:')
        for tool in productive_tools:
            count = productive_counts[tool]
            percentage = (count / total_productive) * 100
            print(f'  {tool}: {count} ({percentage:.1f}%)')
    # Non-productive counts
    non_prod = sum(stats['non_productive_counts'].values())
    print(f'Non-productive actions: {non_prod}')
    if non_prod == 0:
        print('Great! Zero non-productive actions.')
    else:
        print('Need to eliminate non-productive actions.')