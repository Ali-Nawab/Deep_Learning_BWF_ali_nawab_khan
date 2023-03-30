import numpy as np
from scipy import stats

# create an array of numbers
arr = np.array([2, 3, 4, 5, 3, 7, 8])

# calculate the mean, median, and mode of the array
mean = np.mean(arr)
median = np.median(arr)
mode, count = np.unique(arr, return_counts=True)
mode = mode[np.argmax(count)]

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

a = np.array([1, 2, 2, 3, 3, 3, 4])
mode = stats.mode(a)  # mode
print(mode)  # Output: ModeResult(mode=array([3]), count=array([3]))