#!/usr/bin/env python3
"""Stress test for sigmoid overflow fix."""
from safe_activation_fixed import SafeActivation

sa = SafeActivation()
print('=== Stress Test: Extreme Input Values ===')
test_vals = [-1000, -500, -100, -50, 0, 50, 100, 500, 1000]
for v in test_vals:
    t = sa.tanh(v)
    s = sa.sigmoid(v)
    print(f'Input {v:4} -> tanh {t:10.6f}, sigmoid {s:10.6f}')
    assert abs(t) <= 1.0, f'tanh out of bounds: {t}'
    assert 0 <= s <= 1.0, f'sigmoid out of bounds: {s}'
print('All extreme values within bounds.')
print('Running built-in stress_test method...')
sa.stress_test()
print('SUCCESS: No overflow/underflow.')