# The article of Marketing Science investigatedthe output of advertising agencies.
# Suppose that a random of 400 advertising agencies gives an average percentage share of billing volume equal to 7.46% and population variance equal 1.42%.

# a Calculate 95 percent confidence interval

# b Calculate 99 percent confidence interval

import imp
import numpy as np
from scipy.stats import norm

mean = 7.46;
stdev = np.sqrt(1.42)
n = 400
confidence = 0.95

z_crit = np.abs(norm.ppf((1 - confidence) / 2))

print((mean - stdev * z_crit / np.sqrt(n), mean + stdev * z_crit / np.sqrt(n)));




import imp
import numpy as np
from scipy.stats import norm

mean = 7.46;
stdev = np.sqrt(1.42)
n = 400
confidence = 0.99

z_crit = np.abs(norm.ppf((1 - confidence) / 2))

print((mean - stdev * z_crit / np.sqrt(n), mean + stdev * z_crit / np.sqrt(n)));