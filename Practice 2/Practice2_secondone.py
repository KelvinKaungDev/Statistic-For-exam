# Assume you are toss a coin 20 times and you want to
# find the probability of getting head for 8 times.
# Draw the pmf and cdf of binomial distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 20
p = 0.5     # 1 / 2 (coin)
x = np.arange(0, n+1)

prob = binom.pmf(8, n, p)
print(prob)     # 0.1201343536376954


binomial_pmf = binom.pmf(x, n, p)

plt.plot(x, binomial_pmf, color = 'blue')
plt.title(f"Binomial Distribution (n = {n}, p = {p})")
plt.grid(True)
plt.show()

binomial_cdf = binom.cdf(x, n , p)

plt.plot(x, binomial_cdf, color = 'red')
plt.title(f"Binomial Distribution (n = {n}, p = {p})")
plt.grid(True)
plt.show()

