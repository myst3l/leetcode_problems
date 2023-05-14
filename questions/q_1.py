# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

nums = [2,7,11,15]
target = 9

# dict = {}
# dict[7] = 1
# dict[2] = 0
# for i in range(0, len(nums)):
#     dict[i] = nums[i]
#

# print(dict)
# print(dict[7])

def twoSum(nums, target):
    hashtable = {}
    for i in range(0, len(nums)):
        if target-nums[i] in hashtable:
            return [i, hashtable[target-nums[i]]]
        hashtable[nums[i]] = i

print(twoSum(nums,target))

# def twoSum(nums, target):
#     hashtable = set(nums)
#     for i in range(0, len(nums)):
#         if (target-nums[i]) in hashtable:
#             for j in range(0, len(nums)):
#                 if (nums[j] == (target-nums[i])) and i != j:
#                     return [i, j]






# def twoSum(nums, target):
#     for i in range(0, len(nums)):
#         for j in range(i, len(nums)):
#             if (nums[i] + nums[j] == target) and i != j:
#                 return [i, j]
#