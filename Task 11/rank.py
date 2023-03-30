import numpy as np

# create an array of numbers
arr = np.array([2, 3, 4, 5, 6, 7, 8])

# calculate the rank of each number in the array
rank = np.argsort(arr).argsort() + 1

print("Rank:", rank)
