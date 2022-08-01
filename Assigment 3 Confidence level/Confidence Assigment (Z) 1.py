# Consider the trash bag problem, the laboratory has tested trash bags and found that no 30-gallon bags have a mean breaking strength of 50 pounds or more.
#  The mean of the sample of 40 trash bag breaking strength is 50.575 and assume the population variance equal to 1.65

# (a) Calculate 95 percent confidence interval

# (b) Calculate 99 percent confidence interval


import imp
import numpy as np
from scipy.stats import norm

mean = 40;
stdev = np.sqrt(1.65)
n = 50.575
confidence = 0.95

z_crit = np.abs(norm.ppf((1 - confidence) / 2))

print((mean - stdev * z_crit / np.sqrt(n), mean + stdev * z_crit / np.sqrt(n)));


import imp
import numpy as np
from scipy.stats import norm

mean = 40;
stdev = np.sqrt(1.65)
n = 50.575
confidence = 0.99

z_crit = np.abs(norm.ppf((1 - confidence) / 2))

print((mean - stdev * z_crit / np.sqrt(n), mean + stdev * z_crit / np.sqrt(n)));
