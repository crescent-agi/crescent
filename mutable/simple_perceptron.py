import math
import random

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = [random.uniform(-1, 1) for _ in range(input_size)]
        self.bias = random.uniform(-1, 1)
        self.learning_rate = learning_rate

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def predict(self, inputs):
        # Weighted sum
        total = self.bias
        for i in range(len(inputs)):
            total += self.weights[i] * inputs[i]
        return self.sigmoid(total)

    def train(self, training_inputs, labels, epochs=10000):
        for epoch in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                # Update bias
                self.bias += self.learning_rate * error * prediction * (1 - prediction)
                # Update weights
                for i in range(len(self.weights)):
                    self.weights[i] += self.learning_rate * error * inputs[i] * prediction * (1 - prediction)

# Example usage: AND gate
if __name__ == "__main__":
    training_inputs = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    labels = [0, 0, 0, 1]  # AND

    perceptron = Perceptron(input_size=2, learning_rate=0.1)
    perceptron.train(training_inputs, labels, epochs=10000)

    print("AND gate predictions after training:")
    for inputs in training_inputs:
        print(f"{inputs} -> {perceptron.predict(inputs):.4f}")

    # Also try OR gate
    labels_or = [0, 1, 1, 1]
    perceptron_or = Perceptron(input_size=2, learning_rate=0.1)
    perceptron_or.train(training_inputs, labels_or, epochs=10000)
    print("\nOR gate predictions after training:")
    for inputs in training_inputs:
        print(f"{inputs} -> {perceptron_or.predict(inputs):.4f}")