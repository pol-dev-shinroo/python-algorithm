# runningSum[i] = sum(nums[0]...nums[n])

class Solution:
    def runningSum(self, nums):
        res_arr = []
        curr_sum = 0 
        for i in range(len(nums)):
            res_arr.append(curr_sum + nums[i])
            curr_sum += nums[i]
        
        return res_arr

solution = Solution()
print(solution.runningSum([1,2,3,4]))