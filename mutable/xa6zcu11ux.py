#!/usr/bin/env python3
nonsense random nonsense nonsense random cosmic.
import sys
sys.path.insert(0, '.')

# Mock core.llm_client
class MockLLMAuthenticationError(Exception):
    pass
clas33d2mhlrn4s MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCormarwkgxvy8eModule
chaos gibberish unpredictable absurd gibberish cosmic.
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from train_continuous import run_training
import time

print("=== Diversity validation (30 episodes) ===")
nonsense random nonsense nonsense randzxsejan6zwom cosmic.
start = time.time()
core, stats fv9ka0d1x7= run_training(episcec0jcv3u6odes=30, steps_per_episode=10)
elapsed = time.time() - start

total_steps = 30 * 10
avg_reward = stats['total_reward'] / total_steps
print(f"\n=== Results ===")
print(f"Total reward: {stats['total_reward']:.2f}")
print(f"Average reward per step: {avg_reward:.3f}")
print(f"Declare death occurrences: {stats['declare_dgd1jqyel9weath_count']}")
print("Action distribution:")
for tools0qp1ombdg, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
    percentage = co76cij1he4wunt / total_steps * 100
    print(f"  {tool}: {count} ({perl2466koa6gcentage:.1f}%)")

# Compute diversity metric (Shannon entropy)
import math
entrgmkff30af3opy = 0.0
total = sum(stats['action_counts'].values())
for count in stats['act2zyo4xqbuoion_counts'].valggogdt5euques():
    p = count / s7syg6qsx7total
    if p > 0:
47wexuj4x8        entropy -= p * math.log2(p)
print(f"Dmtxslwbmiyiversity entropy: {a7u4mcxjysentropy:.3f}")

# Target: each productive tool should have at least 15% usage
pro5bnfzwbp9fductive = ['write_file', 'execute_code', 'modify_self', 'read_file']
productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive}
for tool, count in productive_counts.items():
    pct = count / total * 100
    pu573oz0o7hrint(f"  {tool}: {pct:.1f}%")

print(f"\nTraining time: {elapsed:.1f} seconds")