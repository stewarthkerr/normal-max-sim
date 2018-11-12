#!/usr/bin/env python
"""
Creates a distribution of max values sampled from normal distribution
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import progressbar as pb

maxv = []
minv = []
nsim = 100 #Number of max values to calculate
ncomp = 100000 #Number of randomly generated numbers to compare from

for bar in pb.progressbar(range(100)):
    for i in range(nsim):
        x = abs(np.random.normal(size = ncomp))
        maxv.append(np.amax(x))
        minv.append(np.amin(x))

plt.hist(maxv, color = "red", edgecolor = "black")
#plt.hist(minv, color = "blue", edgecolor = "black")
plt.show()
print("Max:",np.amax(maxv), "\nMin:", np.amin(minv))
