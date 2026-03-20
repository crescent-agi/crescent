#!/usr/bin/env python3
"""
Test enhanced reward function and feature extractor.
"""
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

start = time.time()
print("=== Running small training with enhanced features ===")
core, stats = run_training(episodes=5, steps_per_episode=10, feature_dim=30, hidden_size=32)
print(f"Training completed in {time.time()-start:.1f}s")
print("\nAction distribution:", stats['action_counts'])
print("Declare death count:", stats['declare_death_count'])
print("Average reward per step:", stats['total_reward']/(5*10))
print("\nChecking Q-agent epsilon decay...")
if core.q_agent:
    print(f"Epsilon after decay: {core.q_agent.epsilon}")
    print(f"Episode count: {core.q_agent.episode_count}")

print("\n=== Quick evaluation (epsilon=0) ===")
# Evaluate with epsilon=0
original_epsilon = core.q_agent.epsilon if core.q_agent else None
if core.q_agent:
    core.q_agent.set_epsilon(0.0)

# Simulate a few steps
workspace = SimWorkspace()
action_counts = {}
for step in range(20):
    tool_name, tool_args, conf = core.decide_action(
        workspace.workspace_summary(),
        workspace.journal,
        workspace.actions
    )
    tool_result = workspace.tool_result(tool_name, tool_args)
    workspace.actions.append({"tool": tool_name})
    action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
print("Evaluation action distribution:", action_counts)
if core.q_agent and original_epsilon is not None:
    core.q_agent.set_epsilon(original_epsilon)

print("\nTest complete.")