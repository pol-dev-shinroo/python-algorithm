# brute force way (n to the power of 3 method...) => cubic solution
def brute_force(nums):
    maxNumber = 0
    for i in range(len(nums)):
        subarr = []
        for j in range(i + 1, len(nums)):
            subarr.append(nums[j])
            currentNumber = 0
            for k in range(len(subarr)):
                if currentNumber > maxNumber:
                    maxNumber = currentNumber
                currentNumber += subarr[k]
    return maxNumber


# linear solution (sliding window)
def solution(nums):
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub


# print(brute_force([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
