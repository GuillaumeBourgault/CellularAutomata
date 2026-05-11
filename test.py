import numpy as np
import matplotlib.pyplot as plt
import itertools
import matplotlib

GRID_SIZE = (10, 10)


def add_new_row_to_matrix(m: np.ndarray, r: np.ndarray) -> np.ndarray:
    m = np.vstack([m, r])
    return m


m = np.random.rand(5, GRID_SIZE[1]) > 0.5
r = np.random.rand(1, GRID_SIZE[1]) > 0.5
m = add_new_row_to_matrix(m, r)
