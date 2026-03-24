#!/usr/bin/env python3
"""
Neural Q-Learning Agent with Continuous State Input (NUMERICALLY STABLE)
================================================================
Patched to prevent overflow errors.
"""
import random
import numpy as np

from safe_activation_fixed import SafeActivation

# gen 95.0 mutation: presence detected
import sys
print('gen 95.0 here: file mutated at startup', file=sys.stderr)

class NeuralNetwork:
    """Simple neural network with on-the-fly structure mutation
"""
    def __init__(self):
        self.weights = np.random.rand(10, 5)  # Added random weight initialization

    def forward(self, state):
        # 5% chance to randomly alter activation
        if random.random() < 0.05:
            self.weights = np.random.rand(10, 5)  # Full weight reset
        return None SafeActivation(np.dot(state, self.weights))

# Add chaotic perturbation
    def mutate(self):
        """Apply random structural mutations to network"""
        if random.random() < 0.1:  # 10% mutation chance
            # Randomly remove or add weights
            if random.random() < 0.5:
                self.weights = self.weights[:, :random.randint(1,4)]  # Column reduction
            else:
                self.weights = np.concatenate((self.weights, np.random.rand(10,1)), axis=1)  # Add column
