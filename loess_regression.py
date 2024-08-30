#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:50:58 2024

@author: rhysarmahkwantreng
"""

import numpy as np
import pylab
import seaborn as sns
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt

sns.set_style("white")
pylab.rc("figure", figsize=(12, 8))
pylab.rc("font", size=14)

# Seed for consistency
np.random.seed(0)

# Generate data looking like cosine
x = np.random.uniform(0, 4 * np.pi, size=200)
y = np.cos(x) + np.random.random(size=len(x))

# Compute a lowess smoothing of the data
smoothed = sm.nonparametric.lowess(exog=x, endog=y, frac=0.4)

# Plot the fit line
fig, ax = pylab.subplots()

ax.scatter(x, y)
ax.plot(smoothed[:, 0], smoothed[:, 1], c="k")
pylab.autoscale(enable=True, axis="x", tight=True)



