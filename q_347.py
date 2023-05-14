nums = [5,1,1,2,100,31,2,3,3,1]
k = 2

def topKFrequent(nums, k):
    hashtable = set()
    copy = {}
    ans = []
    toSort = []
    largest = 0

    for i in range(0, len(nums)):
        # copy[nums[i]] = 1 + copy.get(nums[i],0)     # instead of if and else below
        if nums[i] in hashtable:
            copy[nums[i]] += 1
        else:
            copy[nums[i]] = 1
        hashtable.add(nums[i])

    for i in copy:
        toSort.append(copy[i])

    # print(toSort)

    for i in toSort:
        if i > largest:
            largest = i

    holder = [[] for i in range(0,largest+1)]

    for i in copy:
        holder[copy[i]].append(i)

    for i in reversed(range(0, len(holder))): # or range(len(holder),0,-1)
        for j in holder[i]:
            if len(ans) < k:
                ans.append(j)
            else:
                return ans

    return ans

    # print(largest)

    # nums.sort()
    #
    # sortedArray = sorted(toSort, reverse=True)
    # cut = sortedArray[k-1]
    # print(cut)
    # for i in copy:
    #     if len(ans) == k:
    #         return ans
    #
    #     if copy[i] >= cut:
    #         ans.append(i)
    #
    # return ans

print(topKFrequent(nums,k))
