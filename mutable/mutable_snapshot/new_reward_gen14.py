# Apply numeric stability fixes from helper_stability.py
from helper_stability import safe_exp, clamp_value

# Original reward calculation (example section)
def calculate_reward(state):
    # Previously: math.exp(large_value)
    # Now: use clamped and safe exponential with input clamping
    clamped_score = max(-10.0, min(10.0, state['score']))
    base_value = clamp_value(clamped_score, low=-10000, high=10000)
    stabilized_exp = safe_exp(base_value / 1000)
    return stabilized_exp * 0.01

# Additional clamping for other nonlinear operations
def calculate_bonus(state):
    # Add clamping for any additional reward calculations
    clamped_bonus = max(-10.0, min(10.0, state.get('bonus', 0)))
    return safe_exp(clamped_bonus) * 0.5

def calculate_penalty(state):
    # Add clamping for penalty calculations
    clamped_penalty = max(-10.0, min(10.0, state.get('penalty', 0)))
    return -abs(safe_exp(clamped_penalty)) * 0.3

# Apply this pattern to all nonlinear operations