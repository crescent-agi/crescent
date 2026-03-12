import numpy as np

print("Testing activation functions with extreme values...")
test_cases = [
 (np.exp(1000), "exp(1000)"),
 (np.exp(-1000), "exp(-1000)"),
 (np.log(1e-100), "log(1e-100)"),
 (np.log(1e100), "log(1e100)"),
 (np.tanh(1000), "tanh(1000)"),
 (np.tanh(-1000), "tanh(-1000)"),
 (np.tanh(0.001), "tanh(0.001)"),
 (np.tanh(-0.001), "tanh(-0.001)"),
 (np.sin(1000), "sin(1000)"),
 (np.sin(-1000), "sin(-1000)"),
 (np.sin(0.001), "sin(0.001)"),
 (np.sin(-0.001), "sin(-0.001)"),
]

for value, name in test_cases:
    try:
        # Compute using numpy (fallback if PyTorch is unavailable)
        result = np.exp(value) if 'exp' in name else np.log(value) if 'log' in name else np.tanh(value) if 'tanh' in name else np.sin(value)
        print(f"{name}: {result:.4e}")
    except Exception as e:
        print(f"{name} failed with error: {e}")
        # Log the failure to activation_log.txt
        try:
            with open("activation_log.txt", "a") as f:
                f.write(f"{name}: {e}\n")
        except Exception as log_error:
            print(f"Failed to log error: {log_error}")

print("Activation stress test completed.")