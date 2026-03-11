import numpy as np

def sigmoid_stress_test():
    extreme_values = [1e12, -1e12, np.inf, -np.inf]
    try:
        for value in extreme_values:
            sigmoid_result = 1 / (1 + np.exp(-value))
            if np.isnan(sigmoid_result):
                print(f"NaN result for input {value}")
    except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == "__main__":
    sigmoid_stress_test()