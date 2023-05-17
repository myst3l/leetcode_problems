height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
# height = [1,2,1]
# height = [2,3,4,5,18,17,6]

lcorner = 0
rcorner = len(height)-1
l = 0
r = len(height)-1


def area(x1,x2):
    smallest = min(height[x1],height[x2])
    return smallest*(x2-x1)

largest = area(lcorner, rcorner)

while l < r:
    current = area(l, r)
    if current > largest:
        rcorner = r
        lcorner = l
        largest = current

    # elif area(l, r) > area(lcorner, r):
    #     lcorner = l

    if height[l] > height[r]:
        r -= 1
    else:
        l += 1
        # print('l is: ' + str(l) + ' r is: ' + str(r))


print(lcorner)
print(rcorner)
print(area(lcorner,rcorner))

# print(smallest*smallest)