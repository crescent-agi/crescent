import numpy as np

class NeuralQ:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.activation = 'tanh'

    def forward(self, x):
        return np.tanh(np.dot(x, self.weights))

    def update(self, x, y, lr=0.01):
        prediction = self.forward(x)
        error = y - prediction
        gradient = error * (1 - np.tanh(x)**2)  # Derivative of tanh
        self.weights += lr * gradient.dot(x.T)

    def save(self, filename):
        np.savez(filename, weights=self.weights)

    def load(self, filename):
        data = np.load(filename)
        self.weights = data['weights']

# Replace all sigmoid activations with tanh
# Add variance penalty term to reward function
# Implement activation range monitoring during training
