import time
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib
import itertools

GRID_SIZE = (10, 10)


def build_grid(m: np.ndarray, grid_size=GRID_SIZE) -> matplotlib.figure.Figure:
    fig, ax = plt.subplots(figsize=grid_size)
    ax.set_xlim(grid_size[0] + 1)
    ax.set_ylim(grid_size[1] + 1)
    ax.set_aspect("equal", "box")
    rectangle_size = 1
    for x, y in itertools.product(range(grid_size[0] + 1), range(grid_size[1] + 1)):
        if x >= m.shape[1] or y >= m.shape[0]:
            color = "white"
        else:
            color = "black" if m[y, x] else "white"
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
    return fig


st.title("Live Updating Matplotlib Plot")

# Placeholder in the Streamlit page
plot_placeholder = st.empty()

# Example evolving data
x = np.linspace(0, 10, 100)

# Infinite update loop
for frame in range(1000):
    m = np.random.rand(5, GRID_SIZE[1]) > 0.5
    fig = build_grid(m)
    plot_placeholder.pyplot(fig)
    plt.close(fig)
    time.sleep(1)
