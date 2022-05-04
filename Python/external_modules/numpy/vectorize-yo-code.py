# Why vectorization is important, especially for machine learning or simulation tasks


import numpy as np
import time as t

n = int(1e6)
x = np.random.rand(n)
y = np.random.rand(n)


def timer(function):
    def wrapper(*arg, **kw):
        tic = t.time()
        res = function(*arg, **kw)
        toc = t.time()
        return (toc-tic), res, function.__name__
    return wrapper


@timer
def vectorized(x, y):
    return np.dot(x, y)


@timer
def forLoopVersion(x, y, n):
    return sum(x[i]*y[i] for i in range(n))


time, result, func_name = vectorized(x, y)
print(f"Function : {func_name}, Result : {result}, Time : {time*1e3} ms")

time, result, func_name = forLoopVersion(x, y, n)
print(f"Function : {func_name}, Result : {result}, Time : {time*1e3} ms")
