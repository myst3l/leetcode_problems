# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded back to the original list of strings.
# Q 659 on lintcode
strs = ["lintingverybig","code","love","you"]


def encode(strs):
    encrypted = ""
    for i in range(0, len(strs)):
        encrypted += str(len(strs[i])) +'#' +strs[i]
    return encrypted


def decode(encrypted):

    ans = []
    while len(encrypted) > 0:
        numberlength = 1
        reached = False

        while not reached:
            if encrypted[numberlength] == '#':
                reached = True
            else:
                numberlength += 1

        wordlength = int(encrypted[0:numberlength])
        ans.append(encrypted[numberlength+1:numberlength+1+wordlength])
        encrypted = encrypted[numberlength + 1 + wordlength:]

    return ans


encr = encode(strs)
print(encr)
dec = decode(encr)
print(dec)

# def encode(strs):
#     encrypted = ""
#     for i in range(0, len(strs)):
#         encrypted += strs[i] + ';:'
#     return encrypted
#
#
# def decode(encrypted):
#     holder = ""
#     ans = []
#     words = 0
#
#     for i in range(0, len(encrypted)):
#         if encrypted[i] == ';':
#             if encrypted[i+1] == ':':
#                 ans.append(holder)
#                 holder = ""
#         elif encrypted[i] == ':':
#             words += 1
#         else:
#             holder += encrypted[i]
#     return ans
#
#

