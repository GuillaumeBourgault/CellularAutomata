import numpy as np
import matplotlib.pyplot as plt
import itertools
import matplotlib

GRID_SIZE = (10, 10)
FT = [False, True]

m = np.random.rand(10, 10) > 0.5
y, x = np.nonzero(m)
plt.scatter(x, y, marker="s", s=1000)
plt.gca().invert_yaxis()

plt.show()
