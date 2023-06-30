class Solution:
    def maxSubArray(self, nums):
        max_sum = float('-inf')  # Initialize maximum sum to the smallest possible value
        for i in range(len(nums)):  # Starting index of subarray
            for j in range(i, len(nums)):  # Ending index of subarray
                curr_sum = sum(nums[i:j+1])  # Compute sum of current subarray
                max_sum = max(max_sum, curr_sum)  # Update maximum sum if current sum is greater
        return max_sum

# brute force 