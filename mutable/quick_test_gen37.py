#!/usr/bin/env python3
import sys, os, time
sys.path.insert(0, '.')
# Mock core.llm_client
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

# Import the training function from train_gen37_forced
from train_gen37_forced import run_training

print("=== Quick test of Generation 37 forced rotation ===")
core, stats = run_training(episodes=5, steps_per_episode=20, load_previous=True)
print("\nTest completed.")
# Quick validation with epsilon=0
from train_gen37_forced import run_validation
print("\n=== Quick validation (epsilon=0, 200 steps) ===")
final_stats = run_validation(core, steps=200)
print(f"Non-productive actions: {final_stats['non_productive_total']}")
print(f"Average reward per step: {final_stats['average_reward']:.3f}")
print(f"Productive distribution:")
for tool, perc in final_stats['productive_distribution'].items():
    print(f"  {tool}: {perc:.1f}%")
    if perc >= 15 and perc <= 35:
        print(f"    -> within target range")
    else:
        print(f"    -> OUTSIDE target range")