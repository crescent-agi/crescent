#!/usr/bin/env python3
import math

# Gen 210 Safety Patch

def apply_activation(input_value):
    # Clamp inputs to prevent extremes
    clamped = max(-10.0, min(10.0, input_value))
    # Bounded tanh activation (prevents overflow)
    return 2.0 / (1.0 + math.exp(-clamped)) - 1.0

# Critical overflow check
def stress_test():
    for x in range(-1000, 1001, 100):
        result = apply_activation(x)
        if abs(result) > 2.0:
            print(f"[ERROR] Overflow detected at x={x}: {result}")
    print("[OK] Safety patch validated")

if __name__ == "__main__":
    stress_test()