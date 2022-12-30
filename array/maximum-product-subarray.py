def solution(nums):
    res = max(nums)
    print(res)

    curMin, curMax = 1, 1

    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue

        temp = curMax * n  # need to compare before currMax gets updated
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(temp, n * curMin, n)
        res = max(res, curMax)
    return res


print(solution([-4, -3, -2]))
