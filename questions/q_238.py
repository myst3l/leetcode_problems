nums = [-1,1,0,-3,3]


def productExceptSelf(nums):
    ans = [1]*len(nums)
    leftproduct = 1
    rightproduct = 1

    for i in range(0, len(nums)):
        ans[i] = leftproduct
        leftproduct *= nums[i]


    for i in reversed(range(0, len(nums))):
        ans[i] = ans[i]*rightproduct
        rightproduct = rightproduct*nums[i]

    return ans

# def productExceptSelf(nums):
#     a = [0] * len(nums)
#     ans = [1] * len(nums)
#     zeros = 0
#     product = 1
#     leftproduct = 1
#     rightproduct = 1
#     count = set()
#
#     for i in range(0, len(nums)):
#         if nums[i] == 0:
#             zeros += 1
#
#     if zeros > 1:
#         ans = [0] * len(nums)
#         return ans
#
#     for i in range(0, len(nums)):
#         if nums[i] != 0:
#             product = product * nums[i]
#
#     if zeros == 1:
#         for i in range(0, len(nums)):
#             if nums[i] != 0:
#                 ans[i] = 0
#             else:
#                 ans[i] = product
#     else:
#         for i in range(0, len(ans)):
#             ans[i] = int(product/nums[i])
#
#     return ans
#

print(productExceptSelf(nums))