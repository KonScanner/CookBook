"""Let's say you want a function that
accepts any number of input arguments 
and retunrs the average of these arguments."""


def average(first, *args):
    return (first + sum(args) / (1 + len(args)))


print(average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
