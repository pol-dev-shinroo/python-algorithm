class Solution: 
    def runningSum(self, nums):
        res_arr = [0] * len(nums)
        res_arr[0] = nums[0]
    
        for i in range(len(nums)):
            res_arr[i] = nums[i] + res_arr[i-1]
        
        return nums

solution = Solution()
print(solution.runningSum([1,2,3,4,5]))

