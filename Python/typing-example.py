"""Let the user know
what variables type() of variables
the function expects"""


def int_addition(x: int, y: int) -> int:
    assert isinstance(x, int)
    assert isinstance(y, int)
    return x + y


print(int_addition(2, 3))
print(help(int_addition))
print(int_addition.__annotations__)
