import numpy as np
import matplotlib.pyplot as plt
import itertools
import matplotlib

GRID_SIZE = (10, 10)
FT = [False, True]


def build_rule(rule_number: int) -> dict:
    assert rule_number < 2 ** (2**3)
    x = itertools.product(FT, FT, FT)
    y = bin(rule_number)[2:].zfill(8)
    rule = {x: y == "1" for x, y in zip(x, y)}
    return rule


rule = build_rule(34)
