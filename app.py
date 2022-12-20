def solution(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        if nums[l] == target:
            return l

    m = (l + r) // 2

    if nums[l] > target:
        if nums[m] <= nums[l]:
            l = 1 + m
        else:
            r = 1 - m
    else:
        l += 1

    return -1


print(solution([4, 5, 6, 7, 0, 1, 2], 0))

print("ol")
