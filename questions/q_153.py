# Given a sorted rotated array, find the minimum in log(n) time
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        else:
            if arr[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1

    return -1

def find_rotation(nums):
    if len(nums) == 1:
        return nums[0]

    if nums[len(nums) - 1] > nums[0]:
        return nums[0]
    for i in range(len(nums)):
        if nums[i] > nums[i + 1]:
            return nums[i + 1]


array = [3, 4, 5, 1, 2]
print(find_rotation(array))
