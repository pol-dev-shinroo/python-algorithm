def solution(nums, target):

    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if target == nums[m]:
            return m

        # left sorted portion?
        if nums[m] >= nums[l]:
            if target > nums[m]:
                l = m + 1
            else:
                if target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

        # right sorted portion?
        else:
            if target < nums[m]:
                r = m - 1
            else:
                if target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

    return -1


# refactoring
# left sorted portion?
# if nums[m] >= nums[l]:
#     if target > nums[m] or target < nums[l]:
#         l = m + 1
#     else:
#         r = m - 1

# # right sorted portion?
# else:
#     if target < nums[m] or target > nums[r]:
#         r = m - 1
#     else:
#         l = m + 1


print(solution([1], 0))
