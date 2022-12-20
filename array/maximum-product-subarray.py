def solution(nums):
    res = max(nums)
    print(res)

    curMin, curMax = 1, 1

    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(n * curMax, n * curMin, n)
        res = max(res, curMax)
    return res


print(solution([2, 3, -2, 4]))
