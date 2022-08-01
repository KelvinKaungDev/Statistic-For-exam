# Assume the minimart were collected the data of consumer enter to the store and
# it found that
# the average of 5 consumer enter to the store every hour.
# Find the probability of consumer will enter to the store at least 6 in 1 hour.
# Draw the pmf and cdf of poisson distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
mean = 5
prob =  1 - poisson.cdf(5, mean)
print(prob)     # 0.38403934516693705

x = np.arange(0, 20)

poisson_pmf =  poisson.pmf(x, mean)

plt.plot(x, poisson_pmf, color = 'blue')
plt.title(f"Poisson Distribution (mean = {mean})")
plt.grid(True)
plt.show()

poisson_cdf = poisson.cdf(x, mean)

plt.plot(x, poisson_cdf, color = 'red')
plt.title(f"Poisson Distribution (mean = {mean})")
plt.grid(True)
plt.show()
