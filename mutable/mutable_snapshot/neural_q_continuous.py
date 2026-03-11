#!/usr/bin/env python3
"""
Neural Q-Learning Agent with Continuous State Input (NUMERICALLY STABLE)
================================================================
Patched to prevent overflow errors.
"""
import numpy as np
import random
from safe_activation import SafeActivation  # Use unified SafeActivation