def bruteForce(height):
    # print(height)
    res = 0

    for l in range(len(height)):
        for r in range(l + 1, len(height)):
            # print(l, r)
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

    return res


# two pointer technique:
def solution(height):
    res = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = (r - 1) * min(height[l], height[r])
        res = max(res, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return res


print(solution([1, 8, 6, 2, 5, 4, 8, 3, 7]))
