def maxProfit(prices):
    l, r = 0, 1
    maxProfit = 0
    while r < len(prices):
        profit = prices[r] - prices[l]
        # profitable
        if profit > 0:
            maxProfit = max(profit, maxProfit)
        else:
            l = r
        r += 1
    return maxProfit


print(maxProfit([7, 1, 5, 3, 6, 4]))
