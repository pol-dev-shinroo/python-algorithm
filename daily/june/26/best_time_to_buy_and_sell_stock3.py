class Solution:
    def onePass(self, prices):
        max_number = 0
        min_number = float("inf")

        for i in range(len(prices)):
            if prices[i] < min_number:
                min_number = prices[i]
            else:
                max_number = max(max_number, prices[i])
        
        return max_number - min_number
            
solution = Solution()

print(solution.twoPoint([1,0,2,3]))