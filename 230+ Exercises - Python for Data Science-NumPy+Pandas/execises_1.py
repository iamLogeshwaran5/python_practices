"""
Exercise 1
Check if all elements from the following arrays return the logical value True:
A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])
B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])
C = np.array([[True, False, False],
              [True, True, True]])
D = np.array([0.1, 0.3])
Print result to the console as shown below.
Tip: Use the function np.all().

Expected result:
A: True
B: False
C: False
D: True
"""

import numpy as np

# Define the arrays
A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

D = np.array([0.1, 0.3])

# Check if all elements in each array evaluate to True
print("A:", np.all(A))
print("B:", np.all(B))
print("C:", np.all(C))
print("D:", np.all(D))

"""
Another way  solution 
"""

import numpy as np
 
 
A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])
 
B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])
 
C = np.array([[True, False, False],
              [True, True, True]])
 
D = np.array([0.1, 0.3])
 
for name, array in zip(list('ABCD'), [A, B, C, D]):
    print(f'{name}: {np.all(array)}')




