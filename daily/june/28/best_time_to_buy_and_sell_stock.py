# running minimum 

class Solution: 
    def bestTime(self, prices):
        min_price = float("inf")
        max_price = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_price:
                max_price = prices[i] - min_price

        return max_price