#question 1

# a)Built-in Package
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

'''
Output:First matrix [[1 2]
 [3 4]]
Second matrix [[4 5]
 [6 7]]
Addition of two matrix [[ 5  7]
 [ 9 11]]
Subtraction of two matrix [[-3 -3]
 [-3 -3]]
Multiplication of two matrix [[ 4 10]
 [18 28]]
Division of two matrix [[0.25       0.4       ]
 [0.5        0.57142857]]
'''

# b)User defined Package
#program to demonstrate user defined package.

#Userpackage/Module1:-
def Addition(No1,No2):
    print("Addition of given two numbers:",No1+No2)
    
#Main program:-
from userpackage import module1;
print(module1.Addition(12,12))

'''
Output:Addition of given two numbers: 24
'''