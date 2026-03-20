def validate_input_range(tensor):
    """
    Validate tensor values are within expected range
    Args:
        tensor: numpy array to validate
    Returns:
        bool: True if valid, False otherwise
    """
    # Example implementation - will need customization
    min_val = -1000  # Define appropriate min based on system
    max_val = 1000   # Define appropriate max
    return (tensor >= min_val).all() and (tensor <= max_val).all()

# Add additional checks for specific cases here

# Example usage:
# if not validate_input_range(input_tensor):
#     raise ValueError(f"Invalid tensor values: {input_tensor}")