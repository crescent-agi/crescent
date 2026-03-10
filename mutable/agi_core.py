def sigmoid(x):
    # Clipping input to prevent overflow in exp(-x)
    x = np.clip(x, -1000, 1000)  # Safe range for sigmoid
    return 1 / (1 + np.exp(-x))