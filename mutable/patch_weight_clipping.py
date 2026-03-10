#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
from neural_q_continuous import NeuralNetwork
original_backward = NeuralNetwork.backward

def backward_with_clipping(self, inputs, hidden, output, target):
    # Call original backward
    original_backward(self, inputs, hidden, output, target)
    # Clip weights and biases to range [-5, 5]
    for i in range(self.input_size):
        for j in range(self.hidden_size):
            if self.W1[i][j] > 5.0:
                self.W1[i][j] = 5.0
            elif self.W1[i][j] < -5.0:
                self.W1[i][j] = -5.0
    for j in range(self.hidden_size):
        if self.b1[j] > 5.0:
            self.b1[j] = 5.0
        elif self.b1[j] < -5.0:
            self.b1[j] = -5.0
    for j in range(self.hidden_size):
        for k in range(self.output_size):
            if self.W2[j][k] > 5.0:
                self.W2[j][k] = 5.0
            elif self.W2[j][k] < -5.0:
                self.W2[j][k] = -5.0
    for k in range(self.output_size):
        if self.b2[k] > 5.0:
            self.b2[k] = 5.0
        elif self.b2[k] < -5.0:
            self.b2[k] = -5.0

NeuralNetwork.backward = backward_with_clipping
print('Patched NeuralNetwork.backward with weight clipping.')