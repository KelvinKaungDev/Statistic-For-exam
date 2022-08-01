# Assume you are randomly number by normally distributed with mean at 0 and variance at 4.
# Find the probability of number will greater than 2.
# Draw the pdf and cdf of normal distribution


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
import seaborn as sb

mean = 0
standard_deviation = 2  # standard deviation = square root of variance

# -------------------------------------------------------------------------------------

prob =  1 - uniform.cdf(2, mean, standard_deviation)
print(prob)     # 0.3085375387259869

# -------------------------------------------------------------------------------------

data = np.arange(-60, 60)

normal_pdf =  uniform.pmf(data, mean)

plt.plot(data, normal_pdf, color = 'blue')
plt.title(f"Normal Distribution (mean = {mean}, standard_deviation = {standard_deviation}))")
plt.grid(True)
plt.xlabel('Numbers')
plt.ylabel('Probability Density')
plt.show()

# -------------------------------------------------------------------------------------

data = np.arange(-90, 90)

normal_cdf =  uniform.cdf(data, mean, standard_deviation)
plt.plot(data, normal_cdf, color = 'red')
plt.title(f"Normal Distribution (mean = {mean}), (standard_deviation = {standard_deviation})")
plt.grid(True)
plt.xlabel('Numbers')
plt.ylabel('Probability Density')
plt.show()

# -------------------------------------------------------------------------------------
