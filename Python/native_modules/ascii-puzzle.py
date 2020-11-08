def read_file(path: str) -> list:
    """
    Takes in file path and returns
    a list of numbers that could contain
    the solution to the problem.
    """
    with open(path, 'r') as file:
        values = []
        for line in file:
            currentline = line.split(',')
            for i in currentline:
                values.append(int(i.replace(" ", "")))
    return values


numbers = read_file(path='.data/askii.txt')


def read_hidden_message(nums: list) -> str:
    """
    Gets ASCII representation 

    Returns combined string!
    """
    solution = []
    for i in nums:
        solution.append(chr(i))
    return ''.join(solution)


print(read_hidden_message(numbers))
