import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# create a normal distribution object
mu = 0
sigma = 1
dist = norm(mu, sigma)

# generate a random sample from the distribution
sample = dist.rvs(1000)

# calculate the CDF of the sample
x = np.sort(sample)
y = np.arange(len(x)) / float(len(x))

# plot the CDF
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('CDF')
plt.title('Cumulative Distribution Function')
plt.show()
