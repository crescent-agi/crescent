import numpy as np

# Modified neural Q-learning with input clamping
class NeuralQAgent:
    def __init__(self):
        self.w = np.random.randn(4, 2)

    def forward(self, x):
        # Clamp input to prevent overflow
        x = np.clip(x, -100, 100)
        z = np.dot(x, self.w)
        return np.tanh(z)

# Test
print(NeuralQAgent().forward([1000, -200, 0.5, 1]))