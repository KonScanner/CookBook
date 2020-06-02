from numpy import arange
from typing import Callable, List

Vector = List[float]


def partial_difference_quotient(f: Callable[[Vector], float],
                                v: Vector,
                                i: int,
                                h: float) -> float:
    """Returns the i-th partial difference quotient of f at v"""
    w = [v_j + (h if j == i else 0)    # add h to just the ith element of v
         for j, v_j in enumerate(v)]

    return (f(w) - f(v)) / h


def estimate_gradient(f: Callable[[Vector], float], v: Vector,
                      h: float = 0.0001):
    """ Computationally expensive:
    if v = len(n), eval f on 2n inputs."""
    return [partial_difference_quotient(f, v, i, h)
            for i in range(len(v))]


def f(v):
    """ Test Function 
    f = x^2 + y^2 - 3 at y = 3"""
    x, y = v
    return (x*x) + (y*y) - 3


x = 3
y = 3
v = [x, y]
grad = estimate_gradient(f, v, h=0.00001)
print(grad)
