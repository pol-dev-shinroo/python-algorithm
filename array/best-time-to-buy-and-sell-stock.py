# brute force
def profit(num):
    maxProfit = 0
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            profit = num[j] - num[i]
            if profit > maxProfit:
                maxProfit = profit

    return maxProfit


print(profit([7, 1, 5, 3, 6, 4]))

# two pointers

# 조건: 존버는 금지?
def twoPointers(prices):
    l, r = 0, 1  # left = buy, right = sell
    maxProfit = 0

    while r < len(prices):
        # profitable?
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            l = r
        r += 1
    return maxProfit
