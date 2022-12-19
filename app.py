def hash(nums, target):
    prevMap = {}  # value: index
    for i, v in enumerate(nums):
        diff = target - v
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[v] = i
    return


print(hash([2, 7, 11, 3], 9))
