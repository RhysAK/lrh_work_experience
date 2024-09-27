#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:54:31 2024

@author: rhysarmahkwantreng
"""

#import the necessary modules
import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np 
import statsmodels.api as sm
from scipy.interpolate import griddata


#read csv file into a pandas data frame
data = pd.read_csv('/Users/rhysarmahkwantreng/Documents/LRH Code/data_rhys.csv')
data 

#extracting data from data frame
x = data['x']
y = data['y']
z = data['value']

#creating the figure 
fig = plt.figure(figsize = (13, 10))
ax = plt.axes(projection ="3d")


# Create a grid for interpolation
x_grid, y_grid = np.meshgrid(np.linspace(min(x), max(x), 50),np.linspace(min(y), max(y), 50))

# Flatten the grid for LOESS input
grid_points = np.column_stack((x_grid.ravel(), y_grid.ravel()))

# Combine x and y as input features for LOESS
points = np.column_stack((x, y))

# Apply LOESS smoothing on 3D data
smoothed = sm.nonparametric.lowess(z, points[:, 0], frac=0.4)

# Interpolate smoothed values over the grid
z_grid = griddata(points, smoothed[:, 1], (x_grid, y_grid), method='linear')

#creating the 3-D plot
ax.scatter3D(x, y, z, color = "blue")

# Surface plot for LOESS-smoothed data
surf = ax.plot_surface(x_grid, y_grid, z_grid, cmap ='plasma',alpha=0.7)

# create title and labels for the plot 
plt.title("simple 3D scatter plot",fontsize = 20, fontweight ='bold')
ax.set_xlabel('X-axis',fontsize = 20, fontweight = 'bold')
ax.set_ylabel('Y-axis',fontsize = 20, fontweight ='bold')
ax.set_zlabel('Values',fontsize = 20, fontweight ='bold')

# Rotate the view for better clarity of the 3D structure
ax.view_init(elev=30, azim=120)

# Adjust the layout for better spacing and readability
plt.tight_layout()

# Add a color bar for the surface plot
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

plt.show()


