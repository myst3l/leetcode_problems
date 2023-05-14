# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

nums = [1,2,3,1]
#
#
# def containsDuplicate(num):
#     duplicate = False
#     for i in range(0, len(num)):
#         for j in range(0, len(num)):
#             if (num[i] == num[j]) and i != j:
#                 return True
#
#     return False
#
#
# if containsDuplicate(nums):
#     print('True')
# else:
#     print('False')

print(len(nums))

# def containsDuplicate(nums):
#     hashset = set()
#
#     for i in range(0, len(nums)):
#         if nums[i] in hashset:
#             return True
#         hashset.add(nums[i])
#
#     return False

def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)

    return False

print(containsDuplicate(nums))
