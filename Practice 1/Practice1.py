# Assume you are draw a number 1 to 10 for 50 times.
# Calculate mean, median and mode. Draw a boxplot of data.

from statistics import median
import numpy as np
import random
import matplotlib.pyplot as plt


randomlist = []
for i in range (0,50):
    n = random.randint(1, 10)
    randomlist.append(n)

from scipy import stats

mean = np.mean(randomlist)
median1 = np.median(randomlist)
mode = stats.mode(randomlist)

print(randomlist)       # [10, 1, 1, 7, 1, 9, 4, 4, 3, 3, 3, 1, 4, 10,
                        #   3, 2, 6, 8, 9, 7, 2, 5, 9, 2, 9, 4, 6, 4, 6,
                        #   5, 8, 9, 7, 1, 3, 7, 1, 6, 4, 2, 7, 9, 5, 7,
                        #   10, 3, 9, 1, 5, 8]

print(len(randomlist))  # 50
print(mean)             # 5.2
print(median1)          # 5.0
print(mode)             # ModeResult(mode=array([1]), count=array([7]))
                        # mode refers to the most repeating element in the array
                        # count (how many times the mode number appeared (7 times)).

box_plot_data = [randomlist]
plt.boxplot(box_plot_data)
plt.grid(True)
plt.show()

