import numpy as np
import matplotlib.pyplot as plt

# Scatterplot

x = np.array([53, 59, 65, 78, 82, 79, 84, 77])
y = np.array([156, 167, 173, 178, 189, 194, 171, 185])

# Set the figure size in inches
plt.figure(figsize=(10,6))

plt.scatter(x, y, color = "black")

# Set x and y axes labels
plt.xlabel('Weights(x)')
plt.ylabel('Heights(y)')

plt.title('Scatter Title')

plt.show()
#----------------------------------------------------------------------------
# Regression Model

import numpy as np
from scipy import stats

x = np.array([53, 59, 65, 78, 82, 79, 84, 77])
y = np.array([156, 167, 173, 178, 189, 194, 171, 185])

slope, intercept, r, p, std_err = stats.linregress(x, y)    

print("The regression model is y = ",intercept, "+ ", slope, " * weights") 
# The regression model is y =  117.06364732681229 +  0.8258073160927241  * weights

# --------------------------------------------------------------------------
# line of linear Regression    
def regression_model(x):
    return slope * x + intercept

mymodel = list(map(regression_model, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
# --------------------------------------------------------------------------

# Mean Squre Error (MSE)
import numpy as np

polynomialorder = 1 
model = np.polyfit(x, y, polynomialorder)

modelpredictor = np.polyval(model, x)     # The regression model is y =  117.06364732681229 +  0.8258073160927241  * weights

print("modelpredictor ", modelpredictor)

absError = modelpredictor - y   # Error = y^ - y 


SE = np.square(absError)    # Square error

MSE = np.mean(SE)           # Mean Square error

print("MSE = ", MSE)          # MSE =  56.71171110813352


