def solution(nums, target):

    l, r = -0, len(nums) - 1

    while l < r:
        curSum = nums[l] + nums[r]

        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l + 1, r + 1]

    return []


print(solution([2, 7, 11, 15], 9))
