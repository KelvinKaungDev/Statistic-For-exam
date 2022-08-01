# Assume you are rolling a dice 12 times and you want to find out the probability of getting 3 as an outcome 5 times.

# Find the probability of getting 3 as an outcome 5 times.
# Draw the pmf and cdf of binomial distribution.


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 12
p = 0.167      #  1 / 6 ( dice )
x = np.arange(0, n+1)

prob = binom.pmf(5, n, p)
print(prob)


binomial_pmf = binom.pmf(x, n, p)
print("binomial_pmf", binomial_pmf)

plt.plot(x, binomial_pmf, color = 'blue')
plt.title(f"Binomial Distribution (n = {n}, p = {p})")
plt.grid(True)
plt.show()

binomial_cdf = binom.cdf(x, n , p)

plt.plot(x, binomial_cdf, color = 'red')
plt.title(f"Binomial Distribution (n = {n}, p = {p})")
plt.grid(True)
plt.show()

