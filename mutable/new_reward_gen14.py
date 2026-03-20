# Apply numeric stability fixes from helper_stability.py
from helper_stability import safe_exp, clamp_value

# Original reward calculation (example section)
def calculate_reward(state):
    # Previously: math.exp(large_value)
    # Now: use clamped and safe exponential
    base_value = clamp_value(state['score'], low=-10000, high=10000)
    stabilized_exp = safe_exp(base_value / 1000)
    return stabilized_exp * 0.01

# Apply this pattern to all nonlinear operations