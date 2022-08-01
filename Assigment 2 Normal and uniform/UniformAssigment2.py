# In the movie of Forrest Gump, the public school require the IQ test for admittance. If the IQ test scores are normally distributed with mean 100 and standard deviation at 16.

# a. How many percentages of people would qualify for admittance to the public school when IQ test score higher than 110?

# b. How many percentages of people would qualify for admittance to the public school when IQ test lower than 85?

# c. If the IQ test of Forrest Gump between 90 to 115, how many percentages that he will qualify to the public school?


import imp
from scipy.stats import norm

ans_one   = 1 - norm.cdf(110, 100, 16)
ans_two   = norm.cdf(85, 100, 16)
first_Iq  = norm.cdf(90, 100, 16)
second_Iq = norm.cdf(115, 100, 16)
ans_three = second_Iq - first_Iq

print(ans_one)
print(ans_two)
print(ans_three)
