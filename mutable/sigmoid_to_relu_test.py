import math

def sigmoid(x):
    # Original sigmoid implementation prone to overflow
    try:
        return 1 / (1 + math.exp(-x))
    except OverflowError as e:
        print(f"Overflow error with x={x}")
        return float('nan')

def relu(x):
    return max(0, x)

# Test extreme negative value that caused overflow
x_test = -1000000
sig = sigmoid(x_test)
print(f"Sigmoid({x_test}) = {sig}")

rel = relu(x_test)
print(f"ReLU({x_test}) = {rel}")