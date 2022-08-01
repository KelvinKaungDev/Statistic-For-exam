

data = [3, 8, 13, 18, 23]
weights = [2, 6, 13, 17, 12]

import numpy as np

# mean
# Mean is average of a given set of data
def weighted_mean(data, weights):
    return np.average(data, weights=weights)

print("weighted_mean = ",weighted_mean(data, weights))          # weighted_mean =  16.1

# variance
# Variance is the sum of squares of differences between all numbers and means.
def weighted_var(data, a):

    return np.average((data - weighted_mean(data, weights)) ** 2, weights = a)

print("weighted_var = ", weighted_var(data, weights))           # weighted_var =  29.89

# skeweness
def weighted_skewe(data, weights):
    return (
            np.average
            (( data - weighted_mean(data, weights)) ** 3, weights = weights )
            /
            weighted_var(data, weights) **1.5

        )

print("weighted_skewe = " ,weighted_skewe(data, weights))       # weighted_skewe =  -0.49119458387677234

# kurtosis
def weighted_kurt(data, weights):
    return (
        np.average((data - weighted_mean(data, weights)) ** 4, weights = weights)
        /
        weighted_var(data, weights)**2)

print("weighted_kurt = " ,weighted_kurt(data, weights))         # weighted_kurt =  2.537478169368873

# 1st quantile, 3rd quantile, interquratile range (between 3rd and 1st)
def weighted_percentile(data, percents, weights = None):
    ind = np.argsort(data)          # Returns the indices that would sort an array. 0 1 2 3
    d = data[ind]                   # 3, 8, 13, 18, 23
    w = weights[ind]                # 2, 6, 13, 17, 12

    p = 1. * w.cumsum() / w.sum() * 100
    y = np.interp(percents, p, d)
    return y

first_quantile = weighted_percentile(
                    np.array([3, 8, 13, 18, 23]),
                    25,
                    weights= np.array([2, 6, 13, 17, 12])
                    )

third_quantile = weighted_percentile(np.array([3, 8, 13, 18, 23]), 75, weights= np.array([2, 6, 13, 17, 12]))

IQR = third_quantile - first_quantile

print()
print("1st quantile = ",first_quantile, end = " , ")
print("3rd quantile = ", third_quantile, end = " , ")
print("IQR = ", IQR)

# 1st quantile =  9.73076923076923 ,
# 3rd quantile =  17.852941176470587 ,
# IQR =  8.122171945701357
