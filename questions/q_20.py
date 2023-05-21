s = "()"
# s = "(]"
def isValid(s):
    if len(s) % 2 != 0:
        return False
    hashtable = {'}':'{',']':'[',')':'('}
    stack = []
    for char in s:
        if char in hashtable.keys():
            if not stack or hashtable[char] != stack.pop():
                return False
        else:
            stack.append(char)
    return True


# def isValid(s):
#     if len(s) % 2 != 0:
#         return False
#     stack = []
#     left = set(['(', '{', '['])
#
#     for char in s:
#         if char in left:
#             stack.append(char)
#         if char == ')':
#             if not stack or stack.pop() != "(":
#                 return False
#         if char == ']':
#             if not stack or stack.pop() != "[":
#                 return False
#         if char == '}':
#             if len(stack) == 0 or stack.pop() != "{":
#                 return False
#     if len(stack) != 0:
#         return False
#     return True
print(isValid(s))