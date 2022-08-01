# Upgrading a Microsoft Office package requires installation a new file, while installation time is uniformly distributed, and it is required the installation time between 20 minutes to 60 minutes.

# a. How many proportion that upgrading a Microsoft Office package will complete before 30 minutes?

# b. How many proportion that upgrading a Microsoft Office package take longer than 40 minutes?

# c. How many proportion that upgrading a Microsoft Office package will complete between 35 to 45 minutes?


from scipy.stats import uniform

ans_one     = uniform.cdf(30, 20, 40)
ans_two     = 1 - uniform.cdf(40, 20, 40)
first_file  = uniform.cdf(35, 20, 40)
second_file = uniform.cdf(45, 20, 40)
ans_three   = second_file - first_file

print(ans_one)
print(ans_two)
print(ans_three)


