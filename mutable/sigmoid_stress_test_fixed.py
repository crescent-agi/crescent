import math

def sigmoid(x):
    """Safe sigmoid function with input clipping"""
    # Clip extreme inputs to prevent overflow
    x = max(-500, min(500, x))
    return 1 / (1 + math.exp(-x))

def test_sigmoid_overflow():
    values = [1e10, -1e10, 1e99, -1e99, 0, 1, 1.7976931348623157e308, -1.7976931348623157e308]
    for val in values:
        try:
            result = sigmoid(val)
            print(f'Input: {val:.2e} => Safe: {result:.4e}')
        except Exception as e:
            print(f'[CRITICAL] Exception at {val:.2e}: {e}')

if __name__ == "__main__":
    test_sigmoid_overflow()