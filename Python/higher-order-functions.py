"""You can reduce duplication
by using higher order functions.

For example, turning add_two(), into

add_n()

See bellow:
"""


def add_two(x: int) -> int:
    if isinstance(x, int):
        return x + 2
    eval("help(add_two)")
    raise TypeError("Use integers!")


def _test_add_two():
    assert add_two(-2) == 0
    assert add_two(0) == 2
    assert add_two(2) == 4


_test_add_two()
# A higher order function that would add n to x would be:


def add_n(n: int) -> int:
    """add_x(x: int) -> int
    """
    def add_x(x: int) -> int:
        if isinstance(x, int) and isinstance(n, int):
            return x+n
        eval("help(add_n)")
        raise TypeError("Use integers!")
    return add_x


def _test_add_n():
    assert add_n(50)(30) == 80
    assert add_n(30)(-30) == 0
    assert add_n(-50)(-30) == -80


_test_add_n()
add_n(20)(1.5)
