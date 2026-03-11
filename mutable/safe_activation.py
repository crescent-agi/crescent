#!/usr/bin/env python3
"""
SafeActivation module - re-export from safe_activation_fixed.
This file is retained for backward compatibility.
"""
from safe_activation_fixed import SafeActivation

# For convenience, also export the global functions
def safe_activation(x):
    return SafeActivation().tanh(x)

def safe_sigmoid(x):
    return SafeActivation().sigmoid(x)

def safe_tanh_derivative(activation_value):
    return SafeActivation().tanh_derivative(activation_value)

def safe_sigmoid_derivative(activation_value):
    return SafeActivation().sigmoid_derivative(activation_value)