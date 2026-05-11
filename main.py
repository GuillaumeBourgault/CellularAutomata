import time
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib
import itertools

GRID_SIZE = (10, 10)
RECTANGLE_SIZE = 1
FT = [False, True]


def build_grid(m: np.ndarray, grid_size=GRID_SIZE) -> matplotlib.figure.Figure:
    fig, ax = plt.subplots(figsize=grid_size)
    ax.set_xlim(grid_size[0] + 1)
    ax.set_ylim(grid_size[1] + 1)
    ax.set_aspect("equal", "box")
    delta = m.shape[0] - GRID_SIZE[1] if m.shape[0] > GRID_SIZE[1] else 0
    for y in range(grid_size[1]):
        if y >= m.shape[0]:
            ax = add_empty_row_to_fig(ax, y, GRID_SIZE[0])
        else:
            ax = add_row_to_fig(ax, m[y + delta], y, GRID_SIZE[0])
    ax.invert_xaxis()
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    return fig


def add_row_to_fig(
    ax: matplotlib.figure.Figure, r: np.array, y: int, width: int
) -> matplotlib.figure.Figure:
    for x in range(width):
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
    ax: matplotlib.figure.Figure, y: int, width: int
) -> matplotlib.figure.Figure:
    for x in range(width + 1):
        rect = plt.Rectangle(
            [x + 1, y + 1],
            RECTANGLE_SIZE,
            RECTANGLE_SIZE,
            facecolor="white",
            edgecolor="black",
        )
        ax.add_patch(rect)
    return ax


def build_rule(rule_number: int) -> dict:
    assert rule_number < 2 ** (2**3)
    x = itertools.product(FT, FT, FT)
    y = bin(rule_number)[2:].zfill(8)
    rule = {x: y == "1" for x, y in zip(x, y)}
    return rule


def show_rule(rule: dict, rule_placeholder) -> None:
    fig, ax = plt.subplots(2, 4)
    positions = itertools.product(range(2), range(4))
    for key, pos in zip(rule.keys(), positions):
        ax[pos].xaxis.set_major_locator(plt.NullLocator())
        ax[pos].yaxis.set_major_locator(plt.NullLocator())
        ax[pos].set_xlim(3 + 1)
        ax[pos].set_ylim(2 + 1)
        ax[pos].set_aspect("equal", "box")
        ax[pos].invert_xaxis()
        r = np.array(key)
        ax[pos] = add_row_to_fig(ax[pos], r, 0, 3)
        r = np.array([False, rule[key], False])
        ax[pos] = add_row_to_fig(ax[pos], r, 1, 3)
    plt.tight_layout()
    rule_placeholder.pyplot(fig)
    plt.close(fig)


st.title("Live Updating Matplotlib Plot")
rule_placeholder = st.empty()
rule = build_rule(34)
show_rule(rule, rule_placeholder)
plot_placeholder = st.empty()
m = np.random.rand(1, GRID_SIZE[1]) > 0.5
for frame in range(1000):
    fig = build_grid(m)
    plot_placeholder.pyplot(fig)
    plt.close(fig)
    time.sleep(0.2)
    r = np.random.rand(1, GRID_SIZE[1]) > 0.5
    m = np.vstack([m, r])
    break
