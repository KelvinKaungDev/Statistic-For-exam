# Aretail store claimed that the average number of customerswill enter to the store at 5 customers per hour.

# a.Find theprobability that 3 customers will enter to the storein 1 hour
# b.Find the probability that at most 10 customers will enter to the storein 1 hour
# c.Find the probability that no customers will enter to the store in 30 minutes

from scipy.stats import poisson

ans_one   = poisson.pmf(3,5);
ans_two   = poisson.cdf(10,5);
ans_three = poisson.pmf(0,2.5);

print(ans_one) #0.22313016014842982
print(ans_two) #0.01857593622214071
print(ans_three) #0.011108996538242306
