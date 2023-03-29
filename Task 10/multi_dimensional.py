import numpy as np

# create a 2-dimensional array of zeros with 3 rows and 4 columns
arr = np.zeros((3, 4))
print(arr)

# create a 2-dimensional array of ones with 2 rows and 3 columns
arr = np.ones((2, 3))
print(arr)

# create a 2-dimensional array of random numbers with 4 rows and 5 columns
arr = np.random.rand(4, 5)
print(arr)

# create a 2-dimensional array with a specific set of values
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

# create an identity matrix of size 3x3
arr = np.eye(3)
print(arr)

# create a diagonal matrix from a 1-dimensional array
arr = np.diag([1, 2, 3, 4])
print(arr)


# create a 2-dimensional array filled with a specific value
arr = np.full((2, 3), 7)
print(arr)

# create a 2-dimensional array with a specific shape, filled with random values from a normal distribution
arr = np.random.randn(2, 3)
print(arr)

# create a 2-dimensional array with a specific shape, filled with random integers between a low and high value
arr = np.random.randint(0, 10, (3, 3))
print(arr)

# create a 2-dimensional array with a specific shape, filled with values from a range
arr = np.arange(12).reshape(3, 4)
print(arr)

# create a 2-dimensional array by stacking two 1-dimensional arrays horizontally or vertically
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
arr = np.hstack((a.reshape(-1, 1), b.reshape(-1, 1)))  # horizontally
print(arr)
arr = np.vstack((a.reshape(-1, 1), b.reshape(-1, 1)))  # vertically
print(arr)
