class Solution: 
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            print(nums[i-1])
            # nums[i] = nums[i] + nums[i-1]
            nums[i] += nums[i-1]
        
        return nums

solution = Solution()
print(solution.runningSum([1,2,3,4,5]))


nums = [1,2,3,4,5]
print(nums[0])
print(nums[-1])
