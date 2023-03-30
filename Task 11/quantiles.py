import numpy as np

# create an array of numbers
arr = np.array([2, 3, 4, 5, 6, 7, 8])

# calculate the first and third quartiles of the array
q1 = np.quantile(arr, 0.25)
q3 = np.quantile(arr, 0.75)

print("Q1:", q1)
print("Q3:", q3)
