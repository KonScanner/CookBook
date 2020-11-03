from timeit import timeit
import sys


class ClosureInstance(object):
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        # Update instance dictionary with callables
        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))
    # Redirect special methods

    def __len__(self):
        return self.__dict__['__len__']()

# Example use


def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)
    return ClosureInstance()


class Stack2(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


s = Stack()
print(s)
s.push(10)
s.push(20)
s.push('Hello')
print(len(s))
s.pop()
s.pop()
s.pop()

# Test involving closures
s = Stack()
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))
# Test involving a class
s = Stack2()
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))
