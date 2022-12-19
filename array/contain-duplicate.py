def duplicate(nums):
    # v: i
    hashMap = {}

    for i, v in enumerate(nums):
        if v in hashMap:
            return "true"
        hashMap[v] = i
    return "false"


print(duplicate([1, 2, 3, 1]))


# modal solution
def solution(nums):
    hashSet = set()

    for n in nums:
        if n in hashSet:
            return True
        hashSet.add(n)
    return False
