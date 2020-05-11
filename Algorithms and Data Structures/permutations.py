""" Permutations O(lon(n)), O(n)"""


def permute(nums):
    result = []

    def _permuteHelper(start):
        if start == len(nums) - 1:
            result.append(nums[:])
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            _permuteHelper(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    _permuteHelper(0)
    return (len(result), result)


nums = [1, 2, 3, 4]
perms = permute(nums)
print(
    f'Number of possible permutations for {nums} is: {perms[0]}\nPossible Permutations:\n{perms[1]}')
