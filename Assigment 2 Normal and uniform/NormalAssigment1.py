# Two group of customers are scheduled to arrive the hotel in the afternoon. Their arrival times are uniformly distributed between 2 pm to 8 pm.

# a. Find the probability that the first group of customers will arrive to the hotel before 6 pm

# b. Find the probability that the second group of customers will arrive to the hotel after 5.30 pm

# c. Find the probability that the first and second group of customers will arrive to the hotel between 3 pm to 7 pm.

from scipy.stats import uniform

ans_one      = uniform.cdf(6, 2, 6)
ans_two      = 1 - uniform.cdf(5.3, 2, 6)
first_group  = uniform.cdf(3, 2, 6)
second_group = uniform.cdf(7, 2, 6)
ans_three    = second_group - first_group

print(ans_one)
print(ans_two)
print(ans_three)





