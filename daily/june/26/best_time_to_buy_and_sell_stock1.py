class Solution:
    def stock(self, prices):
        l = 0 
        r = l + 1
        max_number = 0 
        while l < len(prices) -1 and r < len(prices):
            diff = prices[r] - prices[l]
            if diff > 0:
                max_number = max(max_number, diff)
                r += 1
                continue
            l += 1
            r = l + 1
        return max_number
                

solution = Solution()

print(solution.stock([7,6,4,3,1]))