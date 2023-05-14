from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]


def groupAnagrams(strs):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    hashtable = {}
    compare = {}
    answer = []
    res = defaultdict(list)

    for letter in alphabet:
        hashtable[letter] = 0

    compare = [hashtable.copy() for i in range(0,len(strs))]

    for i in range(0, len(strs)):

        for j in strs[i]:
            compare[i][j] += 1

        res[tuple(compare[i].values())].append(strs[i])


    # while len(compare) > 0:
    #     toRemove = []
    #     holder = [strs[0]]
    #     temp = compare[0]
    #     compare.pop(0)
    #     strs.pop(0)
    #     for j in range(0, len(compare)):
    #         if temp == compare[j]:
    #             holder.append(strs[j])
    #             toRemove.append(j)
    #
    #     if len(toRemove) > 0:
    #         for k in reversed(range(0, len(toRemove))):
    #             compare.pop(toRemove[k])
    #             strs.pop(toRemove[k])
    #
    #     answer.append(holder)
    # return answer
    return res.values()

print(groupAnagrams(strs))
# ----------------------------------------------------------------------------------------------------------------

#
# nums = [5,3,4,5]
# # [[3], [5, 5], [4]]
# #
# res = defaultdict(list)
#
# for c in nums:
#     res[c].append(c)
#
# print(res.values())
#
#






# answer = []
#
#
# while len(nums) > 0:
#     toRemove = []
#     holder = [nums[0]]
#     temp = nums[0]
#     nums.pop(0)
#     for j in range(0, len(nums)):
#         if temp == nums[j]:
#             holder.append(nums[j])
#             toRemove.append(j)
#
#     # print('\nto remove:')
#     # print(toRemove)
#     # print('nums:')
#     # print(nums)
#     # print('ans:')
#     # print(answer)
#     if len(toRemove) > 0:
#         for k in reversed(range(0,len(toRemove))):
#
#             nums.pop(toRemove[k])
#
#     answer.append(holder)
#
# print(answer)







