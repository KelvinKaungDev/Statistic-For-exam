# In the series of NCIS shown the murder case in Los Angeles, a shoe expert stated that the height of men with a shoe size 12 between 180 cm to 190 cm. Suppose that the height of all men wearing size 12 shoes are normally distributed with a mean of 185 cm and standard deviation at 2.5 cm.

# a. Find the probability the murder case in Los Angeles is correct.

# b. Find the probability the murderer has height taller than 192 cm.

# c. Find the probability that the murderer shorter than 178 cm.

import imp
from scipy.stats import norm

first_height  = norm.cdf(180, 185, 2.5)
second_height = norm.cdf(190, 185, 2.5)
ans_one       = second_height - first_height
ans_two       = 1 - norm.cdf(192, 185, 2.5)
ans_three     = norm.cdf(178, 185, 2.5)

print(ans_one)
print(ans_two)
print(ans_three)
