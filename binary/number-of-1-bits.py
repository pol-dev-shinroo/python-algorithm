def solution1(n):
    res = 0
    while n:
        res += n % 2
        n = n >> 1
    return res


# Binary prefix: 0b
print(solution1(0b0000000000000000000000000001011))


def solution2(n):
    res = 0
    while n:
        n = n & (n - 1)
        res += 1

    return res


print(solution2(0b0000000000000000000000000001011))
