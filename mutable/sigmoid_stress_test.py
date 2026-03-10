import math

def test_sigmoid_overflow():
    values = [1e10, -1e10, 1e99, -1e99, 0, 1, 1.7976931348623157e308, -1.7976931348623157e308]
    for val in values:
        try:
            result = math.sigmoid(val)
            print(f'Input: {val:.2e} => Safe: {result:.4e}')
        except OverflowError as e:
            print(f'[CRITICAL] Overflow at {val:.2e} - SIGMOID FAILURE!')

if __name__ == "__main__":
    test_sigmoid_overflow()