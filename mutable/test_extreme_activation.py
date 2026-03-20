#!/usr/bin/env python3
"""
Test the neural network with extreme input values to ensure no overflow.
"""
import numpy as np
from neural_q_continuous import NeuralNetwork, SafeActivation

def test_extreme_inputs():
    print("Testing neural network with extreme inputs...")
    nn = NeuralNetwork(input_size=5, hidden_size=10, output_size=3)
    
    # Test with extreme positive and negative values
    extreme_inputs = [
        [10000, 10000, 10000, 10000, 10000],
        [-10000, -10000, -10000, -10000, -10000],
        [0, 0, 0, 0, 0],
        [1e6, -1e6, 1e6, -1e6, 1e6]
    ]
    
    for inp in extreme_inputs:
        try:
            output, hidden = nn.forward(inp)
            print(f"Input: {inp[:3]}... -> output: {output}, hidden min/max: {np.min(hidden):.6f}/{np.max(hidden):.6f}")
            # Check for NaN or Inf
            if np.any(np.isnan(output)) or np.any(np.isinf(output)):
                print("ERROR: NaN or Inf in output!")
                return False
            if np.any(np.isnan(hidden)) or np.any(np.isinf(hidden)):
                print("ERROR: NaN or Inf in hidden!")
                return False
        except Exception as e:
            print(f"ERROR: {e}")
            return False
    
    print("All extreme inputs handled without overflow or NaN.")
    return True

def test_safe_activation_directly():
    print("\nTesting SafeActivation directly with extreme values...")
    sa = SafeActivation()
    extremes = [-1e10, -1000, -100, 0, 100, 1000, 1e10]
    for x in extremes:
        t = sa.tanh(x)
        s = sa.sigmoid(x)
        if np.isnan(t) or np.isinf(t) or np.isnan(s) or np.isinf(s):
            print(f"ERROR: tanh({x})={t}, sigmoid({x})={s} -> NaN or Inf")
            return False
        # Check bounds
        if t < -1 or t > 1:
            print(f"ERROR: tanh({x})={t} out of bounds [-1,1]")
            return False
        if s < 0 or s > 1:
            print(f"ERROR: sigmoid({x})={s} out of bounds [0,1]")
            return False
    print("All direct activation tests passed.")
    return True

if __name__ == "__main__":
    ok1 = test_extreme_inputs()
    ok2 = test_safe_activation_directly()
    if ok1 and ok2:
        print("\n=== ALL TESTS PASSED ===")
    else:
        print("\n=== SOME TESTS FAILED ===")