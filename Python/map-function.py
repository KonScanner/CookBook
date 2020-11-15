""" Simple uses of the map() native Python function"""
list_of_lists_of_numbers = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
result = list(map(sum, list_of_lists_of_numbers))
# result is traditionally equivalent to:
result1 = [sum(l) for l in list_of_lists_of_numbers]
print(result == result1)
