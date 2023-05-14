
s = "anagram"
t = "nagaram"



def isAnagram(s, t):
    if len(s) != len(t):
        return False
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = {}
    test = {}

    for letter in alphabet:
        string[letter] = 1
        test[letter] = 1



    for letter in s:
        if letter in string:
            string[letter] += 1
        else:
            string[letter] = 1
    # print(string)

    for letter in t:
        if letter in test:
            test[letter] += 1
        else:
            test[letter] = 1
    # print(test)

    if string == test:
        return True
    else:
        return False


print(isAnagram(s,t))


# def isAnagram(s, t):
#     hashtable = set()
#     check = set()
#     hashCopy = 0
#     checkCopy = 0
#
#     if len(t) < len(s):
#         return False
#
#     for i in range(0, len(s)):
#         if s[i] in hashtable:
#             hashCopy += 1
#         hashtable.add(s[i])
#
#
#     for i in range(0, len(t)):
#         if t[i] not in hashtable:
#             return False
#
#         if t[i] in check:
#             checkCopy += 1
#
#         check.add(t[i])
#     if len(check) < len(hashtable):
#         return False
#     if hashCopy != checkCopy:
#         return False
#
#     print(hashtable)
#     print(check)
#     print(hashCopy)
#     print(checkCopy)
#     return True
