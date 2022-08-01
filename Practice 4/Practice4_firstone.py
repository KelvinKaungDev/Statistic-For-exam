# Assume you are randomly number by normally distributed with mean at 0 and variance at 4. 
# Find the probability of number will greater than 2.  
# Draw the pdf and cdf of normal distribution


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sb

mean = 0
standard_deviation = 2   # standard deviation = square root of variance

# -------------------------------------------------------------------------------------

prob =  1 - norm.cdf(2, mean, standard_deviation)
print(prob)     # 0.3085375387259869

# -------------------------------------------------------------------------------------

data = np.arange(-20, 20)

normal_pdf =  norm.pdf(data, mean, standard_deviation)

plt.plot(data, normal_pdf, color = 'blue')
plt.title(f"Normal Distribution (mean = {mean}, standard_deviation = {standard_deviation}))")
plt.grid(True)
plt.xlabel('Numbers')
plt.ylabel('Probability Density')
plt.show()

# -------------------------------------------------------------------------------------

data = np.arange(-15, 15)

normal_cdf =  norm.cdf(data, mean, standard_deviation)
plt.plot(data, normal_cdf, color = 'red')
plt.title(f"Normal Distribution (mean = {mean}), (standard_deviation = {standard_deviation})")
plt.grid(True)
plt.xlabel('Numbers')
plt.ylabel('Probability Density')
plt.show()

# -------------------------------------------------------------------------------------