class Solution: 
    def runningSum(self, nums):
        res_arr = [0] * len(nums)
        for i in range(len(nums)):
            if i > 0: 
                res_arr[i] = res_arr[i-1] + nums[i]
            else: 
                res_arr[i] = nums[i]
        return res_arr


solution = Solution()
print(solution.runningSum([1,2,3,4,5]))

