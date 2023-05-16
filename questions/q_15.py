# Given an integer array nums,
# return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

nums = [-1,0,1,2,-1,-4]

# def threeSum(self, nums):

ans = []
set1 = set()
nolist = [set() for i in range(0, int(len(nums)/3))]
print(nolist)

# for i in range(0, len(nums)):
#     holder = []
#     for j in range(0, len(nums)):
#         for k in range(0, len(nums)):



# nolist[0].add(0)
# nolist[1].add(1)
# nolist[1].add(0)
# nolist[3].add(0)
# print(nolist)
#
# print(nolist[0]&nolist[1]&nolist[3])

# counts = 0
# for i in range(0, len(nums)):
#     holder = []
#     for j in range(0, len(nums)):
#         for k in range(0, len(nums)):
#             if nums[i] + nums[j] + nums[k] == 0 and (i!=j and j!=k and i!=k) and len(nolist[i]&nolist[j]&nolist[k])==0:
#                 ans.append([nums[i],nums[j],nums[k]])
#                 nolist[i].add(counts)
#                 nolist[j].add(counts)
#                 nolist[k].add(counts)
#                 counts+=1
# print(ans)
# print(nolist)



