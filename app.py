def solution(nums):
    maxNum = 0
    currMax = 0
    for n in nums:
        if currMax < 0:
            currMax = 0
        currMax += n
        maxNum = max(maxNum, currMax)
    return maxNum


print(solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
