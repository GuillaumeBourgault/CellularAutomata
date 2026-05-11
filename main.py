import time
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib
import itertools

GRID_SIZE = (10, 10)
RECTANGLE_SIZE = 1


def build_grid(m: np.ndarray, grid_size=GRID_SIZE) -> matplotlib.figure.Figure:
    fig, ax = plt.subplots(figsize=grid_size)
    ax.set_xlim(grid_size[0] + 1)
    ax.set_ylim(grid_size[1] + 1)
    ax.set_aspect("equal", "box")
    delta = m.shape[0] - GRID_SIZE[1] if m.shape[0] > GRID_SIZE[1] else 0
    for y in range(grid_size[1]):
        if y >= m.shape[0]:
            ax = add_empty_row_to_fig(ax, y)
        else:
            ax = add_row_to_fig(ax, m[y + delta], y)
    ax.invert_xaxis()
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    return fig


def add_row_to_fig(
    ax: matplotlib.figure.Figure, r: np.array, y: int
) -> matplotlib.figure.Figure:
    for x in range(GRID_SIZE[0]):
        color = "black" if r[x] else "white"
        rect = plt.Rectangle(
            [x + 1, y + 1],
            RECTANGLE_SIZE,
            RECTANGLE_SIZE,
            facecolor=color,
            edgecolor="black",
        )
        ax.add_patch(rect)
    return ax


def add_empty_row_to_fig(
    ax: matplotlib.figure.Figure, y: int
) -> matplotlib.figure.Figure:
    for x in range(GRID_SIZE[0] + 1):
        rect = plt.Rectangle(
            [x + 1, y + 1],
            RECTANGLE_SIZE,
            RECTANGLE_SIZE,
            facecolor="white",
            edgecolor="black",
        )
        ax.add_patch(rect)
    return ax


st.title("Live Updating Matplotlib Plot")

# Placeholder in the Streamlit page
plot_placeholder = st.empty()

# Example evolving data

# Infinite update loop
m = np.random.rand(1, GRID_SIZE[1]) > 0.5
for frame in range(1000):
    fig = build_grid(m)
    plot_placeholder.pyplot(fig)
    plt.close(fig)
    time.sleep(0.2)
    r = np.random.rand(1, GRID_SIZE[1]) > 0.5
    m = np.vstack([m, r])
