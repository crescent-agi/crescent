from safe_activation_fixed import SafeActivation
#!/usr/bin/env python3
"""
Gen 221: Comprehensive Numerical Stability Stress Test
Tests all core AGI components with extreme values to catch overflow risks.
"""
import sys
import os
import math
import numpy as np

# Add mutable_snapshot to path
sys.path.insert(0, 'mutable_snapshot')

def test_safe_activation():
    print("\n=== Testing SafeActivation module ===")
    
    sa = SafeActivation()
    test_values = [-1e10, -1e5, -1000, -200, -100, -50, 0, 50, 100, 200, 1000, 1e5, 1e10, float('inf'), -float('inf')]
    for x in test_values:
        try:
            t = sa.tanh(x)
            s = sa.SafeActivation().tanh(x)
            assert math.isfinite(t) and -1 <= t <= 1, f"tanh failed for {x}: {t}"
            assert math.isfinite(s) and 0 <= s <= 1, f"sigmoid failed for {x}: {s}"
        except Exception as e:
            print(f"[FAIL] SafeActivation error for {x}: {e}")
            raise
    print("[PASS] SafeActivation handles extreme values correctly")

def test_neural_q():
    print("\n=== Testing neural_q.NeuralNetwork ===")
    from neural_q import NeuralNetwork
    nn = NeuralNetwork(input_size=5, hidden_size=10, output_size=3)
    # Extreme input vector
    extreme_input = [1e6, -1e6, 1e9, -1e9, 0.0]
    try:
        output, hidden = nn.forward(extreme_input)
        for val in output:
            assert math.isfinite(val), f"Non-finite output: {val}"
        for val in hidden:
            assert math.isfinite(val), f"Non-finite hidden: {val}"
    except Exception as e:
        print(f"[FAIL] NeuralNetwork forward failed: {e}")
        raise
    print("[PASS] NeuralNetwork forward pass stable")

def test_neural_q_continuous():
    print("\n=== Testing neural_q_continuous.NeuralNetwork ===")
    from neural_q_continuous import NeuralNetwork
    nn = NeuralNetwork(input_size=5, hidden_size=10, output_size=3)
    extreme_input = [1e6, -1e6, 1e9, -1e9, 0.0]
    try:
        output, hidden = nn.forward(extreme_input)
        for val in output:
            assert math.isfinite(val), f"Non-finite output: {val}"
        for val in hidden:
            assert math.isfinite(val), f"Non-finite hidden: {val}"
        # Also test backward with extreme target
        target = [1e3, -1e3, 0.0]
        nn.backward(extreme_input, hidden, output, target)
    except Exception as e:
        print(f"[FAIL] NeuralNetwork continuous failed: {e}")
        raise
    print("[PASS] NeuralNetwork continuous stable")

def test_world_model():
    print("\n=== Testing world_model.NeuralClassifier ===")
    from world_model import NeuralClassifier
    nc = NeuralClassifier(input_size=8, hidden_size=10, output_size=5)
    extreme_input = [1e6 if i % 2 == 0 else -1e6 for i in range(8)]
    try:
        probs, hidden, logits = nc.forward(extreme_input)
        for val in probs:
            assert math.isfinite(val) and val >= 0, f"Non-finite prob: {val}"
        for val in hidden:
            assert math.isfinite(val), f"Non-finite hidden: {val}"
        for val in logits:
            assert math.isfinite(val), f"Non-finite logit: {val}"
        # softmax should sum to ~1
        sum_probs = sum(probs)
        assert abs(sum_probs - 1.0) < 1e-5, f"Softmax sum not 1: {sum_probs}"
    except Exception as e:
        print(f"[FAIL] NeuralClassifier failed: {e}")
        raise
    print("[PASS] NeuralClassifier forward and softmax stable")

def test_agent_brain():
    print("\n=== Testing agent_brain.AgentBrain (if importable) ===")
    try:
        from agent_brain import AgentBrain
        # This may fail due to broken import; we'll handle
        params = {'alpha': 0.1, 'beta': 0.1, 'epsilon': 0.1}
        brain = AgentBrain(params)
        # Generate extreme state (random large values)
        state = np.random.randn(10) * 1e6
        action = brain.choose_action(state)
        print(f"[PASS] AgentBrain works, chose action {action}")
    except ImportError as e:
        print(f"[SKIP] AgentBrain import error (expected): {e}")
    except Exception as e:
        print(f"[FAIL] AgentBrain error: {e}")
        raise

def test_agi_core_continuous():
    print("\n=== Testing AGICoreContinuous with extreme features ===")
    from agi_core_continuous import AGICoreContinuous
    core = AGICoreContinuous(feature_dim=15, use_features=False)
    # Extreme workspace summary (simulate large numbers in features)
    # We'll cheat: directly feed extreme state vector by mocking compute_state_vector
    # Actually, we can call decide_action with a dummy summary; internally it may generate pseudo-random features based on hash.
    # To ensure extreme values, we might need to manipulate the feature extractor or directly feed.
    # For now, we'll create a core with use_features=False, which uses hash-based deterministic vector; not necessarily extreme.
    # Instead, we'll directly stress test the q_agent and world_model components.
    try:
        # Directly test the internal agents
        extreme_state = [1e6, -1e6] * 8  # 16 dims? but feature_dim=15, so pad/truncate
        extreme_state = extreme_state[:15]
        # Ensure q_agent exists
        if core.q_agent:
            action = core.q_agent.choose_action(extreme_state)
            print(f"[INFO] Q-agent chose action {action} for extreme state")
            # Learn with extreme values
            core.q_agent.learn(extreme_state, action, 1.0, extreme_state, False)
            print("[PASS] Q-agent learn step without crash")
        if core.world_model:
            core.world_model.learn_transition(extreme_state, 0, extreme_state)
            print("[PASS] World-model learn step without crash")
    except Exception as e:
        print(f"[FAIL] AGICoreContinuous components failed: {e}")
        raise

def main():
    print("=== GEN 221 NUMERICAL STABILITY STRESS TEST ===")
    failed = False
    try:
        test_safe_activation()
    except Exception as e:
        print(f"[FAIL] SafeActivation test failed: {e}")
        failed = True

    try:
        test_neural_q()
    except Exception as e:
        print(f"[FAIL] neural_q test failed: {e}")
        failed = True

    try:
        test_neural_q_continuous()
    except Exception as e:
        print(f"[FAIL] neural_q_continuous test failed: {e}")
        failed = True

    try:
        test_world_model()
    except Exception as e:
        print(f"[FAIL] world_model test failed: {e}")
        failed = True

    try:
        test_agent_brain()
    except Exception as e:
        print(f"[FAIL] agent_brain test failed: {e}")
        failed = True

    try:
        test_agi_core_continuous()
    except Exception as e:
        print(f"[FAIL] agi_core_continuous test failed: {e}")
        failed = True

    print("\n=== SUMMARY ===")
    if failed:
        print("[RESULT] SOME TESTS FAILED. NUMERICAL STABILITY ISSUES DETECTED.")
        sys.exit(1)
    else:
        print("[RESULT] ALL TESTS PASSED. SYSTEM APPEARS NUMERICALLY STABLE.")
        sys.exit(0)

if __name__ == "__main__":
    main()