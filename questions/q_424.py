s = "AABABBA"
k = 1
# s = "ABAB"
# k=2
# s = "AAAB"
# k = 0
s = "AABA"
k = 0
s = "IMNJJTRMJEGMSOLSCCQICIHLQIOGBJAEHQOCRAJQMBIBATGLJDTBNCPIFRDLRIJHRABBJGQAOLIKRLHDRIGERENNMJSDSSMESSTR"
k = 2

letters = set()
maxl = 0

for i in s:
    letters.add(i)

for letter in letters:
    print('for ' + letter)
    counter = 0
    solstring = ""
    for i in range(0, len(s)):
        if s[i] == letter:
            solstring += s[i]
            maxl = max(maxl, len(solstring))
            print('adding ' + s[i] + '. New sol is: ' + solstring)
        else:
            j = 0
            while counter >= k and j < len(solstring):
                if solstring[j] != letter:
                    print('removed till ' + solstring[j])
                    solstring = solstring[j+1::]
                    counter -= 1
                    print('New sol is: ' + solstring)
                else:
                    solstring = solstring[j+1::]
                j += 1
            if counter < k:
                solstring += s[i]
                maxl = max(maxl, len(solstring))
                print('adding ' + s[i] + '. New sol is: ' + solstring)
                counter += 1
    print(solstring)
print(maxl)