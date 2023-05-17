numbers = [2,7,11,15]
numbers = [1, -2, -2, 4]
set = [1, -2, 4]
target = 9
def twoSum(numbers, target):
    hashtable = set(numbers)

    for i in range(0, len(numbers)):

        if target - numbers[i] in hashtable:
            for j in range(0, len(numbers)):
                if numbers[j] == target - numbers[i] and i!=j:
                    return [i+1,j+1]

print(twoSum(numbers,target))