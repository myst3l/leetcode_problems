# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
import random
nums = []
# nums = [0,3,7,2,5,8,4,6,0,1]
# nums = [0,2,4,3,7]
nums = [100,4,200,1,3,2]

def longestConsecutive(nums):
    a = sorted(list(set(nums)))
    b = set(a)
    largest = 1
    current = 1


    if len(nums) == 0:
        return 0

    for i in a:
        if i+1 in b:
            current += 1
        else:
            largest = max(current, largest)
            current = 1

    return largest


print(longestConsecutive(nums))

# def longestConsecutive(nums):
#     hastable = set(nums)
#     largest = 0
#
#     for i in nums:
#         if i-1 not in hastable:
#             counter = 1
#
#             while i + counter in hastable:
#                 counter += 1
#
#             largest = max(counter, largest)
#
#     # for i in startindex:
#     #     counter = 1
#     #     temp = i
#     #
#     #     while temp+1 in hastable:
#     #             counter += 1
#     #             temp += 1
#     #
#     #     if counter > largest:
#     #         largest = counter
#     return largest



# def longestConsecutive(nums):
#     if len(nums) == 0:
#         return 0
#     currentlongest = 1
#     hashtable = set(nums)
#     # print(hashtable)
#
#     while len(hashtable) > 0:
#         longest = 1
#         largestfound = False
#         smallestfound = False
#         temp = 1
#         start = random.choice(list(hashtable))
#         largest = start
#         # print(largest)
#         smallest = 0
#         toremove = set()
#
#         while not largestfound:
#             toremove.add(largest)
#             if largest+1 in hashtable:
#                 largest = largest+1
#             else:
#                 largestfound = True
#         # print(largest)
#
#         smallest = start
#
#         while not smallestfound:
#             toremove.add(smallest)
#             if smallest-1 in hashtable:
#                 smallest = smallest-1
#
#             else:
#                 smallestfound = True
#
#         longest = len(toremove)
#         if longest > currentlongest:
#             currentlongest = longest
#         # print('to remove is:')
#         # print(toremove)
#         hashtable -= toremove
#         # print('hastable now is:')
#         # print(hashtable)
#     return currentlongest
#
#
#


# print(longestConsecutive(nums))