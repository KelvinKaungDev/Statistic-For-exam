# Assume the average of students submit the assignment at 4 students in each day. 
# Find the probability of student at most 6 submit the assignment in within 1 day. 
# Draw the pmf and cdf of poisson distribution


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

mean = 4

# prob2 = poisson.pmf(2, mean)
# print(prob2)
# 
# prob3= poisson.pmf(3, mean)
# print(prob3)
# 
# prob4 = poisson.pmf(4, mean)
# print(prob4)
# 
# prob5 = poisson.pmf(5, mean)
# print(prob5)
# 
# prob6 = poisson.pmf(6, mean)
# print(prob6)
# 
# total = prob + prob2 + prob3 + prob4 + prob5 + prob6  # cdf of this g
# print(total)

prob = poisson.cdf(6, mean)
print(prob)  # 0.8893260215974264


x = np.arange(0, 120)

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