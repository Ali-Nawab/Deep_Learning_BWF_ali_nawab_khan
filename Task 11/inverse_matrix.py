import numpy as np

# create a matrix
A = np.array([[1, 2], [3, 4]])

# calculate the inverse
B = np.linalg.inv(A)

print(B)
# Output: [[-2.   1. ]
#          [ 1.5 -0.5]]
