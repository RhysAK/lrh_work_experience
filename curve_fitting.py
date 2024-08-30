#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:34:40 2024

@author: rhysarmahkwantreng
"""

#import modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#splining code 

# Read data from a CSV file
data = pd.read_csv('data.csv')

# Extract x and y values
x = data['x'].values
y = data['y'].values
 

#degree of the polynomial is n with n+1 data points
n=len(x)-1

#range of x values for the plotting
prange = np.linspace(min(x),max(x),500)

#plot the graph
plt.plot(x,y,marker='o', color='r', ls='', markersize=10)

#calculate the polynomial at one point
def f(o):

  sum = 0
#iterates through each point and constructs a point for each one
  for i in range(n+1):

    prod = y[i]

    for j in range(n+1):
#checks if the indices are different
#to exclude the terms when the indices are equal
      if i!= j:
#core part of lagrange basis polynomial evaluated at x[j] with the terms being 0 unless i=j          
        prod=prod*(o-x[j])/(x[i]-x[j])

    sum = sum + prod

  return sum

 

plt.plot(prange,f(prange))

# Show the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Interpolation')
plt.legend(['Data Points', 'Interpolation'])
plt.show()

plt.show()
