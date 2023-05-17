# Given an integer array nums,
# return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

nums = [-1, 0, 1, 2, -1, -4]

# nums = [5, -5, 4, 1, 0]
# nums = [0,1,1]
# nums = [0,0,0]

# def threeSum(nums):
#     nums = sorted(nums)
#     ans = set()
#     answer = []
#     compi = 100
#     compj = 100
#     compk = 100
#     pos1 = set()
#     pos2 = set()
#     pos3 = set()
#
#     for i in range(0, len(nums)):
#         # compi = nums[i]
#         if compi != nums[i-1]:
#             compi = nums[i]
#             if i not in pos1:
#                 for j in range(0, len(nums)):
#                     if compj != nums[j] and i != j:
#                         compj = nums[j]
#                         for k in range(0, len(nums)):
#                             if nums[i] + nums[j] + nums[k] == 0 and (i != j and i != k and j != k):
#                                 sortedd = sorted([nums[i], nums[j], nums[k]])
#                                 temp = tuple(sortedd)
#                                 if temp not in ans:
#                                     ans.add(temp)
#                                     answer.append(sortedd)
#         pos1.add(i)
#     print(pos1)
#     print(pos2)
#     return answer

nums = sorted(nums)
def twoSum(numbers, target):
    hashtable = set(numbers)

    for i in range(0, len(numbers)):

        if target - numbers[i] in hashtable:
            for j in range(0, len(numbers)):
                if numbers[j] == target - numbers[i] and i!=j:
                    return [numbers[i],numbers[j]]


done = set()
for i in range(0,len(nums)):
    if nums[i] not in done:
        done.add(nums[i])
        print(str(nums[i]) + str(twoSum(nums, -nums[i])))
