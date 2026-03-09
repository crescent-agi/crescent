#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from train_continuous import run_training
import time

print("=== Diversity validation (30 episodes) ===")
start = time.time()
core, stats = run_training(episodes=30, steps_per_episode=10)
elapsed = time.time() - start

total_steps = 30 * 10
avg_reward = stats['total_reward'] / total_steps
print(f"\\n=== Results ===")
print(f"Total reward: {stats['total_reward']:.2f}")
print(f"Average reward per step: {avg_reward:.3f}")
print(f"Declare death occurrences: {stats['declare_death_count']}")
print("Action distribution:")
for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
    percentage = count / total_steps * 100
    print(f"  {tool}: {count} ({percentage:.1f}%)")

# Compute diversity metric (Shannon entropy)
import math
entropy = 0.0
total = sum(stats['action_counts'].values())
for count in stats['action_counts'].values():
    p = count / total
    if p > 0:
        entropy -= p * math.log2(p)
print(f"Diversity entropy: {entropy:.3f}")

# Target: each productive tool should have at least 15% usage
productive = ['write_file', 'execute_code', 'modify_self', 'read_file']
productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive}
for tool, count in productive_counts.items():
    pct = count / total * 100
    print(f"  {tool}: {pct:.1f}%")

print(f"\\nTraining time: {elapsed:.1f} seconds")