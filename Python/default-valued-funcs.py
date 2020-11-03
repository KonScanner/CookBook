"""
Define a function or method 
where one or more of the arguments
are optional and have a default value.
"""


def spam(a, b=42):
    return a, f"The answer to the universe is {b}"


def spam2(a, b=None):
    """Creting b as a dict when None"""
    if b is None:
        b = {}
    return a, type(b)


_no_value = object()


def spam3(a, b=_no_value):
    """If b is not a specific object"""
    if b is _no_value:
        print('No b value supplied.')
        return a, b
    return


print(spam(1), spam(1, 2), sep='\n')
print(spam2(1, None))
print(spam3(1, _no_value))
