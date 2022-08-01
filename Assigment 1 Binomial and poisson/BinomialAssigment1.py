# Thirty percent of all customers who enter to a retail store will make apurchase. 
# Suppose that six customers enter to the store and 
# make a purchase decision independently.a.
# Findthe probability that exactly 4 customers make a purchaseb.
# Find the probability that at most 2customers make a purchasec.
# Find the probability that 3 or more customers make a purchase


from scipy.stats import binom;

ans_one   = binom.pmf(4,6,0.3);
ans_two   = binom.cdf(2,6,0.3);
ans_three = 1 - binom.cdf(2,6,0.3);

print(ans_one); #0.059535
print(ans_two); #0.74431
print(ans_three); #0.25569
