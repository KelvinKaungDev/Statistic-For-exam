
from pickle import TRUE
import scipy
from scipy.stats import binom
import matplotlib.pyplot as plt

# setting the values of n and p
n = 30
p = 0.5 # Here p = 0.5 as it is a binomial distribution with two outcomes(equal chances of success and failure)

# defining list of r values
r_values = list(range(n + 1))

# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]

# plotting the graph 
plt.title(label="Binomial Distribution of Occurrences",
fontsize=15, color="red")
plt.hist(r_values, bins=10)
plt.grid(TRUE)
plt.xlabel("Values", fontsize=13)
plt.ylabel("Probabilities", fontsize=13)
plt.show()
