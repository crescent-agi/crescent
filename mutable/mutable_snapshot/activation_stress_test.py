import numpy as np
import torch

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

 # Add sigmoid tests with extreme values
 (1000, "sigmoid(1000)"),
 (-1000, "sigmoid(-1000)"),
 (1e-100, "sigmoid(1e-100)"),
 (-1e100, "sigmoid(-1e100)"),
]

for value, name in test_cases:
    try:
        # Compute using PyTorch
        if "exp" in name or "log" in name:
            result = torch.exp(value) if "exp" in name else torch.log(value)
        elif "tanh" in name:
            result = torch.tanh(value)
        elif "sin" in name:
            result = torch.sin(value)
        elif "sigmoid" in name:
            result = torch.nn.Sigmoid()(torch.tensor(value).float())  # Ensure this matches your implementation
        print(f"{name}: {result.item():.4e}")
    except Exception as e:
        print(f"{name} failed with error: {e}")
        # Log the failure to activation_log.txt
        with open("activation_log.txt", "a") as f:
            f.write(f"{name}: {e}\n")

print("Activation stress test completed.")