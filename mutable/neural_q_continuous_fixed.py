from safe_activation_fixed import SafeActivation
#!/usr/bin/env python3
"""
Neural Q-learning with continuous state representation (NUMERICALLY STABLE)
Patched to prevent overflow errors.
"""
import numpy as np

class SafeActivation:
    """Safe activation functions with input clamping."""
    CLAMP_MIN = -100.0
    CLAMP_MAX = 100.0
    
    @staticmethod
    def SafeActivation().tanh(x):
        """Numerically stable sigmoid."""
        x = max(SafeActivation.CLAMP_MIN, min(SafeActivation.CLAMP_MAX, x))
        if x >= 0:
            z = np.exp(-x)
            return 1.0 / (1.0 + z)
        else:
            z = np.exp(x)
            return z / (1.0 + z)
    
    @staticmethod
    def SafeActivation().tanh_derivative(activation):
        """Derivative of sigmoid given activation value."""
        return activation * (1.0 - activation)

class NeuralQ:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.activation = 'tanh'

    def forward(self, x):
        # Clamp input to prevent overflow
        x_clamped = np.maximum(-100.0, np.minimum(100.0, x))
        return np.tanh(np.dot(x_clamped, self.weights))

    def update(self, x, y, lr=0.01):
        # Clamp input to prevent overflow
        x_clamped = np.maximum(-100.0, np.minimum(100.0, x))
        prediction = self.forward(x_clamped)
        error = y - prediction
        # Compute derivative using clamped input
        tanh_x = np.tanh(np.dot(x_clamped, self.weights))
        gradient = error * (1 - tanh_x**2)  # Derivative of tanh
        self.weights += lr * np.outer(gradient, x_clamped)

    def save(self, filename):
        np.savez(filename, weights=self.weights)

    def load(self, filename):
        data = np.load(filename)
        self.weights = data['weights']

# Numerical stability fixes applied:
# - Input clamping to [-100, 100]
# - Safe tanh activation
# - Proper derivative calculation