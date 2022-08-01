
# Assume the data with normally distributed with mean at 2 and standard deviation at 5.
# Find the probability of number less than 4.
# Draw the pdf and cdf of normal distribution


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sb

mean = 2
standard_deviation = 5

# -------------------------------------------------------------------------------------

prob =  norm.cdf(4, mean, standard_deviation)
print(prob)     # 0.6554217416103242

# -------------------------------------------------------------------------------------

data = np.arange(-20, 25)

normal_pdf =  norm.pdf(data, mean, standard_deviation)

plt.plot(data, normal_pdf, color = 'blue')
plt.title(f"Normal Distribution (mean = {mean}, standard_deviation = {standard_deviation}))")
plt.grid(True)
plt.xlabel('Numbers')
plt.ylabel('Probability Density')
plt.show()

# -------------------------------------------------------------------------------------

data = np.arange(-20, 25)

normal_cdf =  norm.cdf(data, mean, standard_deviation)
plt.plot(data, normal_cdf, color = 'red')
plt.title(f"Normal Distribution (mean = {mean}), (standard_deviation = {standard_deviation})")
plt.grid(True)
plt.xlabel('Numbers')
plt.ylabel('Probability Density')
plt.show()

# -------------------------------------------------------------------------------------
