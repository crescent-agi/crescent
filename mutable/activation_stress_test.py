import os
import numpy as np

def stress_test_activation_function():
    # Generate test inputs
    inputs = np.linspace(-10, 10, 1000)
    # Activation function - using ReLU as base
    outputs = np.maximum(0, inputs)
    # Introduce small perturbations to test robustness
    noise = np.random.normal(0, 0.01, len(inputs))
    final_outputs = outputs + noise
    return inputs, final_outputs

# Execute the stress test
if __name__ == \"__main\":
    inputs, outputs = stress_test_activation_function()
    print(f"Generated {len(inputs)} test points")
    # Save results to a file
    np.savez('activation_stress_test_results.npz', inputs=inputs, outputs=outputs)
    print("Results saved to activation_stress_test_results.npz")