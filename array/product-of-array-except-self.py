#  two pointer method => time limit exceeded


def product(nums):
    l, r = 0, 0
    answer = []
    product = 1

    while l < len(nums):
        if l == r:
            r += 1
        else:
            if r == len(nums):
                answer.append(product)
                r = 0
                l += 1
                product = 1
            product *= nums[r]
            r += 1
    return answer


# print(product([-1, 1, 0, -3, 3]))

# solution (backward iteration + prefix + postfix)
def solution(nums):
    res = [1] * (len(nums))
    print(res)
    # prefix
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    print(res)
    # postfix
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    print(res)
    return res


print(solution([1, 2, 3, 4]))
