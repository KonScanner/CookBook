
import random as rn
rn.seed(321)


class GetRange:

    def _getRange(self, arr, target):
        """First and Last Indices of an Element in a Sorted Array.
        """
        first = self.binarySearchIterative(arr, 0, len(arr) - 1, target, True)
        last = self.binarySearchIterative(arr, 0, len(arr) - 1, target, False)
        return [first, last]

    def binarySearch(self, arr, low, high, target, findFirst):
        if high < low:
            return -1
        mid = low + (high - low) // 2
        if findFirst:
            if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                return mid
            else:
                return (
                    self.binarySearch(arr, mid + 1, high, target, findFirst)
                    if target > arr[mid]
                    else self.binarySearch(arr, low, mid - 1, target, findFirst)
                )

        elif (mid == len(arr) - 1 or target < arr[mid + 1]) and arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return self.binarySearch(arr, low, mid - 1, target, findFirst)
        else:
            return self.binarySearch(arr, mid + 1, high, target, findFirst)

    def binarySearchIterative(self, arr, low, high, target, findFirst):
        while True:
            if high < low:
                return - 1
            mid = low + (high - low) // 2
            if findFirst:
                if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                    return mid
                if target > arr[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            elif (mid == len(arr) - 1 or target < arr[mid + 1]) and arr[mid] == target:
                return mid
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1


# arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 9, 9, 15]
arr = [rn.randint(1, 100) for _ in range(500)]
arr.sort()
x = 12

print(GetRange()._getRange(arr, x))
