# brute force way (n to the power of 3 method...)
def brute_force(nums):
    maxNumber = 0
    for i in range(len(nums)):
        subarr = []
        for j in range(i + 1, len(nums)):
            subarr.append(nums[j])
            currentNumber = 0
            print(subarr)
            for k in range(len(subarr)):
                if currentNumber > maxNumber:
                    maxNumber = currentNumber
                currentNumber += subarr[k]
    return maxNumber


print(brute_force([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
