"""Function that can accept both any number
of positional and keyword-only arguments
"""


def print_anything(*args, **kwargs):
    print(args, kwargs, sep='\n')


def recv(maxsize, *, block):
    return 'Receive a message'


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


print(print_anything(1, 2, 3, a=1, b=2, c=3))

try:
    recv(1024, True)
except TypeError:
    print(recv(1024, block=True))

print(minimum(1, 4, 2, -2, 10, 0))
print(minimum(1, 4, 2, -2, 10, 0, clip=0))
