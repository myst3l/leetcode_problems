# s = "abcabcbb"

# s = "pwwkew"
# s = "bbbbb"
# s = " "
# s = "au"
# s = "dvdf"
s = "pwwkew"
"abcefgheijkl"
def lengthOfLongestSubstring(s):
    if len(s) == 1:
        return 1

    hashtable = set()
    l = 0
    r = 0
    maxlength = 0

    while r < len(s):

        if s[r] not in hashtable:
            hashtable.add(s[r])
            # print(hashtable)
        else:
            maxlength = max(len(hashtable), maxlength)
            while s[l] != s[r]:
                hashtable.remove(s[l])
                l += 1
            # while s[r] in hashtable:
            #     hashtable.remove(s[l])
            #     l += 1
            # hashtable.add(s[r])



        r += 1
    maxlength = max(len(hashtable),maxlength)
    print(maxlength)
    return maxlength

lengthOfLongestSubstring(s)
# maxl = 0
# for i in range(0, len(s)):
#     hashtable = set()
#     hashtable.add(s[i])
#     for j in range(i, len(s)):
#         if s[j] not in hashtable:
#             # print("i: " + str(s[i]))
#             # print("j: " + str(s[j]))
#             hashtable.add(s[j])
#             # print(hashtable)
#         else:
#             print(hashtable)
#             maxl = max(maxl, len(hashtable))
#             hashtable = set()
#             hashtable.add(s[j])
#
#     maxl = max(maxl, len(hashtable))
#
# print(maxl)
# print(hashtable)