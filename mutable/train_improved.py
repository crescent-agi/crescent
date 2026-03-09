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

# Reload agent_brain to ensure updated reward function
import importlib
import agent_brain
importlib.reload(agent_brain)

# Now import the training module (it will use reloaded agent_brain)
from train_continuous_fixed import run_training, evaluate_continuous

print('Starting improved reward training...')
core, stats = run_training(episodes=10, steps_per_episode=15)
print('\nTraining completed.')
print(f'Total reward: {stats[\"total_reward\"]:.2f}')
avg_reward = stats[\"total_reward\"] / (10*15)
print(f'Average reward per step: {avg_reward:.3f}')
print('Action distribution:')
for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
    print(f'  {tool}: {count}')

# Evaluate
print('\nEvaluating...')
avg, counts = evaluate_continuous(core, episodes=5, steps=10)
print(f'Average evaluation reward: {avg:.2f}')
print('Evaluation action counts:', counts)

# Save the trained core
import os
save_dir = 'artifacts/agi_core_continuous_improved'
os.makedirs(save_dir, exist_ok=True)
core.save(save_dir)
print(f'\nSaved improved core to {save_dir}')

# Compare with previous training stats
print('\n--- Comparison with previous training ---')
prev_stats_path = 'artifacts/agi_core_continuous_trained/training_stats.json'
if os.path.exists(prev_stats_path):
    import json
    with open(prev_stats_path) as f:
        prev = json.load(f)
    prev_avg = prev['total_reward'] / (len(prev['episode_rewards']) * 15)  # approx
    print(f'Previous average reward per step: {prev_avg:.3f}')
    print(f'Previous total reward: {prev[\"total_reward\"]:.2f}')
    print('Previous top actions:', sorted(prev['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5])
else:
    print('Previous stats not found.')

print('\nDone.')