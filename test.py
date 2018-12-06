"""
==============================
Create 3D histogram of 2D data
==============================

Demo of a histogram for 2 dimensional data as a bar graph in 3D.
"""

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np


x = [1,2,3]
y = [1,2,3]
z = [1,2,3]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.bar3d(x,y,z, color='g', zsort='average')

plt.show()
