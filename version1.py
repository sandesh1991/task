import numpy as np

VERSION = 1.2

A = [[6, 7],
      [8, 9]]
      
B = [[1, 3],
      [5, 7]]

if VERSION == 1.1:
    def product(A, B):
        return (np.matmul(A,B))
elif VERSION == 1.2:
    def product(A, B):
        return (np.dot(A,B))
else:
    print(f"Please specify version")