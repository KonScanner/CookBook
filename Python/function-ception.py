"""
Functions can take other functions as
their input. For example, `filter` or `map`.

See examples:
"""


def apply(f, arg):
    """Essentially a __call__ function
    that takes in arguments the function
    and the function's parameters."""
    return f(arg)


def t(x):
    return x


assert apply(t, 1) == 1

# On a more interesting note:


def filter_map(arr, predicate, mapper):
    """
    arr: List
    predicate: function() -> bool
    mapper: mapping function.

    filter_map, first filters the list
    (keeping only the list items that make the predicate return True)
    and then applies the mapping function to each other element.
    """
    output = []
    for item in arr:
        if predicate(item):
            new_item = mapper(item)
            output.append(new_item)
    return output


# example:
assert filter_map([4, 1, 2, 3, 5], lambda x: x > 2, t) == [4, 3, 5]
assert sorted(filter_map([4, 1, 2, 3, 5], lambda x: x > 2, t)) == [3, 4, 5]
