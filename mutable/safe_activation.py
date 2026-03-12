import math

class SafeActivation:
    def tanh(self, x):
        return math.tanh(x)
    
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))
    
    def tanh_derivative(self, x):
        return 1 - x**2
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)