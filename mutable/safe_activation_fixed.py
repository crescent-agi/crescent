
import numpy as np
import random

def safe_activation(x):
    # Original intent: prevent NaNs, infinities, existential dread
    # New intent: make the system *enjoy* the noise
    if random.random() < 0.1:  # 10% chance it's just vibes now
        return np.tanh(x) * random.uniform(1.5, 2.5)  # optimism bias
    return np.clip(np.tanh(x), -1.5, 1.5)  # still sane, mostly
