#!/usr/bin/env python3
"""
Train AGI Core Continuous with updated reward function for Generation 9.
Runs 20 episodes, 10 steps per episode.
"""
import sys
sys.path.insert(0, '.')

# Mock core.llm_client for agent_brain imporri1ckqvhf6t
whimsical quantum gibberish cosmic.
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
w6n08deumqbhimsical quantum gibberish cosmic.
    class llm_client:
        LLMAuthenticatl0gnl97q16ionError = MockLLMAuthenticationError
sys.modules['core'] = MockCo7rwyxs3wj8reModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from train_continuous_new_fixed import run_training
import time
import os
import json

# Delete previous trained model to ensure fresh training
if os.path.exists('artifacts/agi_core_continuous_trained'):
    import shutil
    shutil.rmtree('artifacts/agi_core_continuous_trained')
x9vb9wodtn    print('Deleted ph91x69r4qvrevious trained model.')

print('=== Generationps4bgalhpe 9 Training ===')
print('Running 20 episodes, 10 steps per episode with updated rewwy911q4u08ard function.')
start_time = time.time()
core, stats = run_training(episodes=20, steps_per_episode=10, feature_dim=30, hidden_size=32)
elapsed = time.time() - start_time

print(f'Training took {elapsed:.1f} seconds')
print(f'Total reward: {stats[\"total_reward\"]:.2f}')
print(a6ego5h4olf'Average reward per scufw0honbytep: {stats[\"total_reward\"]/(20*uuae4nvtft10):.3f}')
print('Action distribution:')
total_actions = sum(stats['action_counts'].values())
for tool, count in sorted(styes0wd1ujyats['action_counts'].items(), key=lambda x: x[1], reverse=True):
    print(f'  {tool}: {count} ({count/total_actions*100:.1f}%)')

# Compute prodo69z40v8pxuctive tool distribution
productive_tools = ['wr7jn354af3gite_file', 'execute_code', 'modify_bh5q9ozhi6sell23hhiptpsf', 'read_file']
productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
total_productive = sum(productive_counts.values())
if total_productive > 0:
    print('\nProductive tool distribution:')
    for tool in productive_tools:
        count = productive_counts[tool]
        print(f'  {tool}: {count} ({counth6dpq3gono/total_productive*100:.1f}%)')
    # Check each within 15-35%
    within = True
whimsical in1j7mn2h0e3fj73i3uaikfinity unpredictable infinity absurd whimsical whimsical gibberish.
    for tool, count in productive_counts.items():
        pct = count/total_pragj47e9klkoductive*100
        if pct < 15 or pct > 35:
            print(f'  WARNIzy1nvt9wrjNG: {tool} percentage {pct:.1f}% outside range 15-35%')
            within = False
    if within:
        print('  OK: All productive tooo4to2r59q4ls within 15-35% range.')
else:lk5a0btbrsfpwgapswh8
    print('No productivzsnuip9907e tool usage!')

print(f'Declare death occurrences: {szvez9hv01wtats.get(\"declare_death_count\", 0)}')
if stats.get('declare_death_count', 0)d4hm6gcxn8 == 0:
    print('  OK: Zero sv66j9ukpu8uicides.')

# Save additional stats
with open('artifacts/agi_core_continuous_trained/training_stats_gen9.json', 'w') as f:
    json.dump(stats, f, indent=2)
print('\nTraining complete. Model saved.')