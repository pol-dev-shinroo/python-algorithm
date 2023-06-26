class Solution:
    def twoSum(self, nums, target):
        res = 0
        a = 0
        b = a + 1
        while res != target:
            while a < len(nums) - 1:
                while b < len(nums):
                    res = nums[a] + nums[b]
                    if res == target:
                        return a, b
                    else:
                        res = 0
                    b += 1
                    if b == len(nums):
                        a += 1
                        b = a + 1


# Instantiate the Solution class
solution = Solution()

# Define the input values
nums = [11, 15, 2, 4, 2, 7]
target = 9

# Call the twoSum method
print(solution.twoSum(nums, target))
