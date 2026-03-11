#!/usr/bin/env python3
"""
Stress test for SafeActivation to verify overflow protection.
"""
import sys
sys.path.append('.')
from safe_activation import SafeActivation

class SafeActivationStressTest:
    def __init__(self):
        self.sa = SafeActivation()
    
    def test_extreme_values(self):
        """Test extreme values for all activation functions."""
        print("=== Extreme Value Stress Test ===")
        test_values = [
            -1e6, -1e5, -1e4, -1e3, -1e2, -1e1, -1, -0.1, 0, 0.1, 1, 10, 100, 1000, 10000, 100000, 1000000
        ]
        print(f"{'Input':<10} {'tanh':<15} {'sigmoid':<15} {'Status':<10}")
        print("-" * 55)
        
        all_good = True
        for x in test_values:
            try:
                t = self.sa.tanh(x)
                s = self.sa.sigmoid(x)
                
                # Check bounds
                if not (-1 <= t <= 1):
                    status = "T_RANGE"
                    all_good = False
                elif not (0 <= s <= 1):
                    status = "S_RANGE"
                    all_good = False
                elif not (float('-inf') < t < float('inf')):
                    status = "T_NAN"
                    all_good = False
                elif not (float('-inf') < s < float('inf')):
                    status = "S_NAN"
                    all_good = False
                else:
                    status = "OK"
                
                print(f"{x:<10} {t:<15.6f} {s:<15.6f} {status}")
            except Exception as e:
                print(f"{x:<10} {'ERROR':<15} {'ERROR':<15} {str(e)}")
                all_good = False
        
        print("\n" + "="*55)
        if all_good:
            print("[SUCCESS] All activation functions handled extreme values correctly!")
        else:
            print("[FAILURE] Some activation functions failed extreme value test!")
    
    def test_derivative_stability(self):
        """Test that derivatives remain stable with extreme activations."""
        print("\n=== Derivative Stability Test ===")
        test_activations = [-1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 10.0, 100.0, 1000.0]
        
        print(f"{'Activation':<10} {'tanh_deriv':<15} {'sig_deriv':<15}")
        print("-" * 45)
        
        all_good = True
        for act in test_activations:
            try:
                td = self.sa.tanh_derivative(act)
                sd = self.sa.sigmoid_derivative(act)
                
                # Check bounds
                if not (0 <= td <= 1):
                    status = "T_RANGE"
                    all_good = False
                elif not (0 <= sd <= 0.25):  # sigmoid derivative max is 0.25
                    status = "S_RANGE"
                    all_good = False
                else:
                    status = "OK"
                
                print(f"{act:<10} {td:<15.6f} {sd:<15.6f} {status}")
            except Exception as e:
                print(f"{act:<10} {'ERROR':<15} {'ERROR':<15} {str(e)}")
                all_good = False
        
        print("\n" + "="*45)
        if all_good:
            print("[SUCCESS] All derivatives stable with extreme activations!")
        else:
            print("[FAILURE] Some derivatives unstable!")
    
    def test_array_stability(self):
        """Test array inputs for numpy compatibility."""
        try:
            import numpy as np
            print("\n=== Array Input Stability Test ===")
            
            # Test with numpy arrays
            test_array = np.array([-1e6, -1e3, 0, 1e3, 1e6])
            print(f"Input array: {test_array}")
            
            t = self.sa.tanh(test_array)
            s = self.sa.sigmoid(test_array)
            
            print(f"tanh output: {t}")
            print(f"sigmoid output: {s}")
            
            # Check for NaNs and Infs
            if np.any(np.isnan(t)) or np.any(np.isinf(t)):
                print("[FAILURE] tanh produced NaN or Inf!")
            elif np.any(np.isnan(s)) or np.any(np.isinf(s)):
                print("[FAILURE] sigmoid produced NaN or Inf!")
            else:
                print("[SUCCESS] Array inputs handled correctly!")
        except ImportError:
            print("\n[SKIP] numpy not available for array test")
        except Exception as e:
            print(f"\n[FAILURE] Array test error: {e}")
    
    def test_derivative_consistency(self):
        """Test that derivatives match numerical approximations."""
        print("\n=== Derivative Consistency Test ===")
        
        def numerical_derivative(f, x, h=1e-5):
            return (f(x + h) - f(x - h)) / (2 * h)
        
        test_values = [-5, -1, 0, 1, 5]
        print(f"{'x':<8} {'numerical':<15} {'analytical':<15} {'diff':<15}")
        print("-" * 60)
        
        all_good = True
        for x in test_values:
            try:
                # Test tanh derivative
                act_tanh = self.sa.tanh(x)
                ana_tanh = self.sa.tanh_derivative(act_tanh)
                num_tanh = numerical_derivative(self.sa.tanh, x)
                diff_tanh = abs(num_tanh - ana_tanh)
                
                # Test sigmoid derivative
                act_sig = self.sa.sigmoid(x)
                ana_sig = self.sa.sigmoid_derivative(act_sig)
                num_sig = numerical_derivative(self.sa.sigmoid, x)
                diff_sig = abs(num_sig - ana_sig)
                
                print(f"{x:<8.2f} {num_tanh:<15.6f} {ana_tanh:<15.6f} {diff_tanh:<15.2e}")
                print(f"{' ':<8} {num_sig:<15.6f} {ana_sig:<15.6f} {diff_sig:<15.2e}")
                
                if diff_tanh > 1e-4 or diff_sig > 1e-4:
                    all_good = False
            except Exception as e:
                print(f"{x:<8} {'ERROR':<15} {'ERROR':<15} {str(e)}")
                all_good = False
        
        print("\n" + "="*60)
        if all_good:
            print("[SUCCESS] All derivatives consistent with numerical approximations!")
        else:
            print("[FAILURE] Some derivatives inconsistent!")
    
    def run_all_tests(self):
        """Run all stress tests."""
        print("=== SafeActivation Stress Test Suite ===\n")
        self.test_extreme_values()
        print()
        self.test_derivative_stability()
        print()
        self.test_array_stability()
        print()
        self.test_derivative_consistency()
        print()
        print("\n=== Stress Test Complete ===")

if __name__ == "__main__":
    test = SafeActivationStressTest()
    test.run_all_tests()