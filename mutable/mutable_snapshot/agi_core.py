# Import helper stability functions
from helper_stability import safe_exp, clamp_value

# Update reward calculation with stability fixes
class AGICore:
    def compute_reward(self, state):
        # Safely handle score calculations
        clamped_score = clamp_value(state['score'], low=-1e6, high=1e6)
        # Use safe exponential instead of raw math.exp
        reward_base = safe_exp(clamped_score / 1000.0)
        # Apply final scaling
        return reward_base * 0.001

# Apply this pattern to all state evaluation paths