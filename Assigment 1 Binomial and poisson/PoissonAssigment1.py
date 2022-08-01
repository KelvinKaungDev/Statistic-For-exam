# Suppose that the number of car accidents in the rural area with an average of 1.5 accidents per hour.

# a. Find the probability that no accidents will occur in 1hour
# b. Find the probability that at least 5accidents will occur in1hour
# c. Find the probability that no accidents will occur in 3 hours

from scipy.stats import poisson

ans_one   = poisson.pmf(0,1.5);
ans_two   = 1 - poisson.cdf(4,1.5);
ans_three = poisson.pmf(0,4.5);

print(ans_one) #0.22313016014842982
print(ans_two) #0.01857593622214071
print(ans_three) #0.011108996538242306
