#!/usr/bin/env python3

# Crescent's enhanced Q-network layer with overflow protection
from helper import safe_sigmoid

class QNetwork:
    """Q-network with clamped activation to prevent numerical overflow"""

    def forward(self, x):
        """Apply clamped sigmoid to inputs before forward pass"""
        clamped_x = [safe_sigmoid(v) for v in x]
        # Existing network logic here would continue...
        return clamped_x

# Test integration
if __name__ == "__main__":
    test_values = [1.5, -2.8, 25, -30, 0]
    print("Testing QNetwork:")
    for v in test_values:
        print(f"Input: {v:.2f} -> Clamped: {safe_sigmoid(v):.4f}")