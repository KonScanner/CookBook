""" Multiprocessing allows you to do 'thread-like' operations
using processes instead of using threads. """

from multiprocessing import Pool


def f(x):
    return x**x


if __name__ == "__main__":
    p = Pool(10)
    print(p.map(f, [1, 2, 3, 4, 5]))
