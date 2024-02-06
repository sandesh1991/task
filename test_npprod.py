import numpy as np
import pytest
from npprod import np_prod  

def test_prod():
    A = [[6, 7],
         [8, 9]]
    B = [[1, 3],
         [5, 7]]
    
    expected = np.dot(A, B)
    
    result = np_prod(A, B)
    
    np.testing.assert_array_equal(result, expected)

try:
    test_prod()
    print("Test passed.")
except AssertionError as e:
    print(f"Test failed: {e}")
    exit(1)