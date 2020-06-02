import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("Time taken for func {}: {}".format(func.__name__, total))
        return rv
    return wrapper
