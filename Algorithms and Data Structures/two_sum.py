""" You are given an array of n integers and a number k. Determine whether there is a pair
of elements in the array that sums to exactly k"""


def twoSum(nums, target):
    """ Hashmap solution:
    Hashmaps are good cause:
    put things in it -> o(1)
    retrieve things from it (given you have the key) -> o(1)
    key == value of array
    value == value of indices
    """

    dict = {}
    for i, num in enumerate(nums):
        if target - num in dict:
            return [dict[target - num], i]
        dict[num] = i
    return "something went wrong"


nums = [1, 3, 7]
target = 8

print(twoSum(nums=nums, target=target))
