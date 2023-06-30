class Solution:
    def maxSubArray(self, nums):
        l, r = 0, 1
        curr_value = nums[l] 
        while r < len(nums):
            curr_value += nums[r]
            if curr_value < 0:
                l += 1
                r = 1 + 1
                curr_value = nums[l]
            else: 
                r += 1

        return curr_value


solution = Solution()
print(solution.maxSubArray([-1,-2]))

# does not work for if all elements are negative...