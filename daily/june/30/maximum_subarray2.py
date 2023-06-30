class Solution:
    def maxSubArray(self, nums):
        l, r = 0, 0
        curr_value = nums[0]
        max_value = nums[0]  # Store the maximum value found so far

        while r < len(nums):
            # Only add nums[r] if r > l (it isn't already included in curr_value)
            if r > l:
                curr_value += nums[r]

            if curr_value > max_value:
                max_value = curr_value

            # If curr_value becomes negative, move the window
            if curr_value < 0:
                l = r + 1
                if l < len(nums):  # Check if l is still within bounds
                    curr_value = nums[l]
                    r = l

            r += 1

        return max_value


solution = Solution()
print(solution.maxSubArray([-1,-2]))

# does not work for if all elements are negative...