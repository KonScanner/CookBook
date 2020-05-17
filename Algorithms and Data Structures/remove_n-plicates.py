def solution(data, n):
    """ Google foobar question:
        Remove n-plicates from list"""
    from collections import Counter
    count = Counter()
    result = []
    for i in data:
        count[i] += 1

    result = [i for i in data if count[i] <= n]

    return result


# >>> [1,4,7,10,56]
print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 6, 7, 10, 56, 8, 8], 1))
