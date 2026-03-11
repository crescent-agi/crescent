import math

def safe_sigmoid(x):
    """
    Numerically stable sigmoid function with input clamping to prevent overflow.
    Clamps inputs to [-500, 500] range before applying sigmoid.
    """
    # Clamp inputs to prevent overflow in exp()
    x_clamped = max(-500, min(500, x))
    return 1.0 / (1.0 + math.exp(-x_clamped))

def safe_tanh(x):
    """
    Numerically stable tanh function with input clamping.
    """
    x_clamped = max(-500, min(500, x))
    return math.tanh(x_clamped)

def safe_relu(x):
    """
    Safe ReLU (Rectified Linear Unit) - no clamping needed as it's linear.
    """
    return max(0, x)

def safe_softmax(x):
    """
    Numerically stable softmax function for vector inputs.
    """
    x_clamped = [max(-500, min(500, val)) for val in x]
    max_val = max(x_clamped)
    exps = [math.exp(val - max_val) for val in x_clamped]
    sum_exps = sum(exps)
    return [exp_val / sum_exps for exp_val in exps]