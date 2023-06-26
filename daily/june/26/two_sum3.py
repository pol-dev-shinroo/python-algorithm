class Solution:
    def twoSum(self, nums, target):
        hashMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hashMap:
                return [hashMap[diff], i]

            hashMap[nums[i]] = i
            
solution = Solution()

print(solution.twoSum([-3,4,3,90], 0))