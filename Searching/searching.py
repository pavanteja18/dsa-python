class Searching:
    def linearSearch(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    def binarySearch(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1


s = Searching()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
val = 5
print("Element to be found: ", val)
print("Element found at index : ",s.linearSearch(nums, val))
print("Element found at index : ",s.binarySearch(nums, val))
