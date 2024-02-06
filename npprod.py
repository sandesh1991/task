import numpy as np

VERSION = 1.2

A = [[6, 7],
      [8, 9]]
      
B = [[1, 3],
      [5, 7]]

def np_prod(A, B):
    if VERSION == 1.1:
        return (np.matmul(A,B))
    elif VERSION == 1.2:
        return (np.dot(A,B))
    else:
        print(f"Please specify version")
        return None

prod = np_prod(A, B)
print(f"The product is {prod}")
print("This is a test for github webhook with jenkins pipeline to perform CI/CD... TEST 100001...")