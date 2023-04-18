#program to do arithmetic operations on matrix using numpy.
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 5], [6, 7]])

print("First matrix",A)
print("Second matrix",B)
print("Addition of two matrix",np.add(A, B))
print("Subtraction of two matrix",np.subtract(A, B))
print("Multiplication of two matrix",np.multiply(A, B))
print("Division of two matrix",np.divide(A, B))