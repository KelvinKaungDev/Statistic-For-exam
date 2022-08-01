# The registration office claimed that 80% of all students are satisfied to the service.
# In order to test this claim, a random sample of 10 students is selecteda.

# Find the probability that exactly 6 students are satisfyb.
# Find the probability that atleast 7students are satisfyc.
# Find the probability that 4 or less students are satisfy


from scipy.stats import binom;

ans_one   = binom.pmf(6,10,0.8);
ans_two   = 1 -  binom.cdf(6,10,0.8);
ans_three = binom.cdf(4,10,0.8);

print(ans_one);
print(ans_two);
print(ans_three);
