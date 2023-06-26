class Solution:
    def twoPoint(self, prices):
        max_number = 0
        l, r = 0, 1

        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff < 0:
                l = r
            else:
                max_number = max(diff, max_number)
            r += 1        
        return max_number
            

solution = Solution()

print(solution.twoPoint([1,0,2,3]))