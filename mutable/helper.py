# Crescent's first helper script
# A small utility to test numerical stability
import math

def safe_sigmoid(x):
    """Clamp inputs to prevent overflow in sigmoid calculations"""
    if x > 20:
        return 1.0
    elif x < -20:
        return 0.0
    else:
        return 1 / (1 + math.exp(-x))

# Test with extreme values
print("Testing safe_sigmoid:")
print("x=10:", safe_sigmoid(10))
print("x=-10:", safe_sigmoid(-10))
print("x=100:", safe_sigmoid(100))
print("x=-100:", safe_sigmoid(-100))