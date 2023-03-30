import numpy as np
from scipy.stats import norm

# create an array of numbers
arr = np.array([2, 3, 4, 5, 6, 7, 8])

# calculate the probability density function of the normal distribution with mean and standard deviation of the array
mean = np.mean(arr)
std = np.std(arr)
pdf = norm.pdf(arr, loc=mean, scale=std)

print("PDF:", pdf)
