# brute force


def two_sum_fn(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == target:
                return [i, j]
    return []


print(two_sum_fn([2, 7, 2, 11], 9))

# hash map


def hash_map_fn(num, target):
    prevMap = {}  # val : index

    for i, n in enumerate(num):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return


print(hash_map_fn([2, 7, 2, 11], 9))
