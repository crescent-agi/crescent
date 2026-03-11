def clip_to_safe_range(x, min=-10, max=10):
    return max(min(x, max), min)

def validate_input_range(x, expected_type=float):
    if not isinstance(x, expected_type):
        raise ValueError(f"Expected {expected_type}, got {type(x)}")