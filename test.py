import numpy as np
import matplotlib.pyplot as plt
import itertools

grid_size = (10, 10)
a = np.random.rand(5, grid_size[1]) > 0.5
fig, ax = plt.subplots(figsize=grid_size)
ax.set_xlim(grid_size[0] + 1)
ax.set_ylim(grid_size[1] + 1)
ax.set_aspect("equal", "box")
rectangle_size = 1
for x, y in itertools.product(range(grid_size[0] + 1), range(grid_size[1] + 1)):
    if x >= a.shape[1] or y >= a.shape[0]:
        color = "white"
    else:
        color = "black" if a[y, x] else "white"
    rect = plt.Rectangle(
        [x + 1, y + 1],
        rectangle_size,
        rectangle_size,
        facecolor=color,
        edgecolor="black",
    )
    ax.add_patch(rect)
ax.invert_xaxis()
ax.xaxis.set_major_locator(plt.NullLocator())
ax.yaxis.set_major_locator(plt.NullLocator())
print(a)
plt.show()
