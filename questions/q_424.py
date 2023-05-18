s = "AABABBA"
k = 1
# s = "ABAB"
# k=2
# s = "AAAB"
# k = 0
# s = "AABA"
# k = 0
# s = "IMNJJTRMJEGMSOLSCCQICIHLQIOGBJAEHQOCRAJQMBIBATGLJDTBNCPIFRDLRIJHRABBJGQAOLIKRLHDRIGERENNMJSDSSMESSTR"
# k = 2


l = 0
# maxlength = 0
# mostfreq = 0
longest = 0
table = {}
# def mostf(table):
#     maxx = 0
#     for i in table:
#         max((maxx,table[i]))
#     return maxx


# for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#     table[letter] = 0

# mostf(table)
for r in range(0, len(s)):
    table[s[r]] = 1 + table.get(s[r], 0)
    while (r-l+1) - max(table.values()) > k:
        table[s[l]] -= 1
        l += 1

    # table[s[r]] += 1
    longest = max(longest, r-l+1)
print(table)
print(longest)


# letters = set()
# maxl = 0
#
# for i in s:
#     letters.add(i)
#
# for letter in letters:
#     print('for ' + letter)
#     counter = 0
#     solstring = ""
#     for i in range(0, len(s)):
#         if s[i] == letter:
#             solstring += s[i]
#             maxl = max(maxl, len(solstring))
#             print('adding ' + s[i] + '. New sol is: ' + solstring)
#         else:
#             j = 0
#             while counter >= k and j < len(solstring):
#                 if solstring[j] != letter:
#                     print('removed till ' + solstring[j])
#                     solstring = solstring[j+1::]
#                     counter -= 1
#                     print('New sol is: ' + solstring)
#                 else:
#                     solstring = solstring[j+1::]
#                 j += 1
#             if counter < k:
#                 solstring += s[i]
#                 maxl = max(maxl, len(solstring))
#                 print('adding ' + s[i] + '. New sol is: ' + solstring)
#                 counter += 1
#     print(solstring)
# print(maxl)