def clamp_input(inputs):
    return np.clip(inputs, -1.0, 1.0)

# Add this before any activation in agent_brain.py
if we haven't clamped yet:
    inputs = clamp_input(inputs)