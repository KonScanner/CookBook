"""
For more avanced types:
https://docs.python.org/3/library/typing.html
"""
a = [1, 2, 3, 4, 5]
print(a.__class__.__name__)  # list

b = 5.0
print(b.__class__.__name__)  # float
b = int(b)
print(b.__class__.__name__)  # int

c = {
    "example": a
}
print(c.__class__.__name__)  # dict
