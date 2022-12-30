# two pointers + binary


def solution(nums):
    res = nums[0]  # this can be set to any number in the array
    l, r = 0, len(nums) - 1

    while l <= r:
        # if the subarray is already sorted
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        m = (l + r) // 2
        res = min(res, nums[m])

        # determine if we are going to search to the left or to the right
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1

    return res


print(solution([2, 1]))
