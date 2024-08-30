#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:50:01 2024

@author: rhysarmahkwantreng
"""
#import the necessary models
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from scipy.optimize import curve_fit

#dummy data 
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# performs the linear regression
slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)

#function computes the y value for a given x value based on the linear model
def myfunc(x):
  return slope * x + intercept

#Run each value of the x array through the function. This will result in a new array with new values for the y-axis:
mymodel = list(map(myfunc, x))

#create the scatter plot
plt.scatter(x, y, color='blue', label='Data points')

#create the linear regression line
plt.plot(x, mymodel,color='red', label='Fitted line')

#Label the graph 
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()

#Non-Linear regression 

# Generate sample data
np.random.seed(0)
x = np.linspace(-5, 5, num=50)
y = 2.0 + 1.5 * x + 3.0 * x**2 + np.random.normal(scale=3.0, size=x.shape)

# Define the nonlinear function
def quadratic_func(x, a, b, c):
    return a + b * x + c * x**2


# Fit the nonlinear model
popt, pcov = curve_fit(quadratic_func, x, y)

# Visualize the results
plt.scatter(x, y, label='Data')
plt.plot(x, quadratic_func(x, *popt), 'r-', label='Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()