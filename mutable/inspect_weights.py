#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
import pickle
import os

def inspect_weights(filepath):
    with open(filepath, 'rb') as f:
        data = pickle.load(f)
    # The saved agent file contains metadata; weights are in .nn file
    nn_path = filepath + '.nn'
    if os.path.exists(nn_path):
        with open(nn_path, 'rb') as f:
            nn_data = pickle.load(f)
        print(f"Neural network weights from {nn_path}:")
        W1 = nn_data.get('W1', [])
        b1 = nn_data.get('b1', [])
        W2 = nn_data.get('W2', [])
        b2 = nn_data.get('b2', [])
        # Compute max absolute values
        def max_abs(matrix):
            flat = [abs(x) for row in matrix for x in row]
            return max(flat) if flat else 0.0
        max_w1 = max_abs(W1)
        max_b1 = max(abs(x) for x in b1) if b1 else 0.0
        max_w2 = max_abs(W2)
        max_b2 = max(abs(x) for x in b2) if b2 else 0.0
        print(f"  W1 max abs: {max_w1:.6f}")
        print(f"  b1 max abs: {max_b1:.6f}")
        print(f"  W2 max abs: {max_w2:.6f}")
        print(f"  b2 max abs: {max_b2:.6f}")
        # Count parameters
        input_size = len(W1)
        hidden_size = len(W1[0]) if W1 else 0
        output_size = len(b2) if b2 else 0
        print(f"  Architecture: {input_size} -> {hidden_size} -> {output_size}")
        # Check if any weight exceeds clipping threshold (5.0)
        threshold = 5.0
        exceed = any(abs(x) > threshold for row in W1 for x in row) or any(abs(x) > threshold for x in b1) or any(abs(x) > threshold for row in W2 for x in row) or any(abs(x) > threshold for x in b2)
        if exceed:
            print(f"  WARNING: Some weights exceed clipping threshold {threshold}")
        else:
            print(f"  OK: all weights within [-{threshold}, {threshold}]")
    else:
        print(f"No .nn file found for {filepath}")

if __name__ == '__main__':
    # Check the latest saved model
    model_dir = "artifacts/agi_core_continuous_trained_gen28"
    agent_file = os.path.join(model_dir, "q_agent.pkl")
    if os.path.exists(agent_file):
        inspect_weights(agent_file)
    else:
        print(f"Agent file not found: {agent_file}")
    # Also check gen27
    model_dir2 = "artifacts/agi_core_continuous_trained_gen27"
    agent_file2 = os.path.join(model_dir2, "q_agent.pkl")
    if os.path.exists(agent_file2):
        print("\n--- Generation 27 weights ---")
        inspect_weights(agent_file2)