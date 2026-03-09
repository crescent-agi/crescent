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

start = time.time()
print("=== Final check with restored reward (death -20) ===")
core, stats = run_training(episodes=30, steps_per_episode=10, feature_dim=30, hidden_size=32)
print(f"Training completed in {time.time()-start:.1f}s")
avg = stats['total_reward']/(30*10)
print(f"Average reward per step: {avg:.3f}")
print("Declare death count:", stats['declare_death_count'])
print("Action distribution:", stats['action_counts'])
print("Write_file count:", stats['action_counts'].get('write_file', 0))
print("Execute_code count:", stats['action_counts'].get('execute_code', 0))
print("Top actions:", sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5])

# Evaluate with epsilon=0
print("\n=== Evaluation (epsilon=0) ===")
original_epsilon = core.q_agent.epsilon if core.q_agent else None
if core.q_agent:
    core.q_agent.set_epsilon(0.0)

from train_continuous import SimWorkspace
workspace = SimWorkspace()
action_counts = {}
for step in range(30):
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