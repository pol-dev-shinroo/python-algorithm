class Solution:
    def twoSum(self, nums, target):
        # res = 0

        for a in range(0, len(nums) - 1):
            for b in range(a + 1, len(nums)):
                if nums[a] + nums[b] == target:
                    return a, b
                # res = nums[a] + nums[b]
                # if res == target:
                #     return a, b
                # else:
                #     res = 0


# Instantiate the Solution class
solution = Solution()

# Define the input values
nums = [11, 15, 2, 4, 2, 7]
target = 9

# Call the twoSum method
print(solution.twoSum(nums, target))
