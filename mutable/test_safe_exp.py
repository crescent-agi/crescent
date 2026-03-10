import numpy as np
from mutable_snapshot.safe_activation_patch import safe_exp
# Test safe exponential with extreme values
test_values = [1000, -1000, 0, 1.0, 10.0]
results = [safe_exp([v])[0] for v in test_values]
print("Safe exp results:", results)