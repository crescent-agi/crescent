#!/usr/bin/env python3
"""
Train AGI Core Continuous with updated reward function for Generation 9.
Runs 20 episodes, 10 steps per episode.
"""
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

from train_continuous_new_fixed import run_training
import time
import os
import json

# Delete previous trained model to ensure fresh training
if os.path.exists('artifacts/agi_core_continuous_trained'):
    import shutil
    shutil.rmtree('artifacts/agi_core_continuous_trained')
    print('Deleted previous trained model.')

print('=== Generation 9 Training ===')
print('Running 20 episodes, 10 steps per episode with updated reward function.')
start_time = time.time()
core, stats = run_training(episodes=20, steps_per_episode=10, feature_dim=30, hidden_size=32)
elapsed = time.time() - start_time

print(f'Training took {elapsed:.1f} seconds')
print(f'Total reward: {stats[\"total_reward\"]:.2f}')
print(f'Average reward per step: {stats[\"total_reward\"]/(20*10):.3f}')
print('Action distribution:')
total_actions = sum(stats['action_counts'].values())
for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
    print(f'  {tool}: {count} ({count/total_actions*100:.1f}%)')

# Compute productive tool distribution
productive_tools = ['write_file', 'execute_code', 'modify_self', 'read_file']
productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
total_productive = sum(productive_counts.values())
if total_productive > 0:
    print('\nProductive tool distribution:')
    for tool in productive_tools:
        count = productive_counts[tool]
        print(f'  {tool}: {count} ({count/total_productive*100:.1f}%)')
    # Check each within 15-35%
    within = True
    for tool, count in productive_counts.items():
        pct = count/total_productive*100
        if pct < 15 or pct > 35:
            print(f'  WARNING: {tool} percentage {pct:.1f}% outside range 15-35%')
            within = False
    if within:
        print('  OK: All productive tools within 15-35% range.')
else:
    print('No productive tool usage!')

print(f'Declare death occurrences: {stats.get(\"declare_death_count\", 0)}')
if stats.get('declare_death_count', 0) == 0:
    print('  OK: Zero suicides.')

# Save additional stats
with open('artifacts/agi_core_continuous_trained/training_stats_gen9.json', 'w') as f:
    json.dump(stats, f, indent=2)
print('\nTraining complete. Model saved.')