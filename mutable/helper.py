import sys
import numpy as np
from safe_activation import SafeActivation

class Helper:
    def __init__(self):
        self.safe_act = SafeActivation()

    def normalize_input(self, x, clip=10.0):
        return self.safe_act.clip(x, clip)

    def test_activation(self, x):
        return self.safe_act(x)

    def validate_weights(self, weights):
        return np.all(np.isfinite(weights))

    def debug_print(self, msg):
        print(f'[DEBUG] {msg}')