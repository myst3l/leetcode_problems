# Given a string s, return true if it is a palindrome, or false otherwise.
import re
s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = " "
# s = "0P"
# s= ".,"
# s="ab_a"

def isPalindrome(s):
    s = re.sub('[^0-9a-zA-Z]', '', s).lower()
    print(s)
    return s == s[::-1]


# def isPalindrome(s):
#     l = 0
#     r = len(s) -1
#
#     while r > l:
#         while l<r and not s[l].isalnum():
#             l += 1
#
#
#         while r>l and not s[r].isalnum():
#             r -= 1
#
#         print('l: ' + s[l])
#         print('r: ' + s[r])
#         if s[l].lower() != s[r].lower():
#             return False
#
#         l += 1
#         r -= 1
#
#     return True


# def isPalindrome(s):
#     forward = ''
#
#     for char in s:
#         if char.isalnum():
#             forward += char.lower()
#
#     return forward == forward[::-1]

print(isPalindrome(s))


