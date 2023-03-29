import numpy as np

# create a 1-dimensional array with a specific set of values
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# create a 1-dimensional array of zeros with 5 elements
arr = np.zeros(5)
print(arr)

# create a 1-dimensional array of ones with 3 elements
arr = np.ones(3)
print(arr)

# create a 1-dimensional array of random numbers with 7 elements
arr = np.random.rand(7)
print(arr)

# Create an array of evenly spaced values between two numbers (inclusive)
arr = np.arange(1, 6)  # [1, 2, 3, 4, 5]
print(arr)

# Create an array of evenly spaced values between two numbers (not inclusive)
arr = np.linspace(0, 1, num=5)  # [0.0, 0.25, 0.5, 0.75, 1.0]
print(arr)

# Create an array of a specified shape filled with a specified value
arr = np.full(3, 5)  # [5, 5, 5]
print(arr)

# Create an array of random integers between two values (inclusive)
arr = np.random.randint(1, 10, size=5)  # [6, 9, 5, 4, 5]
print(arr)


# Create an empty array of a specified size
arr = np.empty(4)  # [0., 0., 0., 0.]
print(arr)

# Create a copy of an existing array
arr1 = np.array([1, 2, 3])
arr2 = arr1.copy()
print(arr2)
