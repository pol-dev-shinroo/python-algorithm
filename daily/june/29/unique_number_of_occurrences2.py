class Solution:
    def occurences(self, nums):
        hashMap = dict.fromkeys(nums, 0)
        print(hashMap)
        for i in range(len(nums)):
             hashMap[nums[i]] += 1
        print(hashMap)
        return len(hashMap.values()) == len(set(hashMap.values()))
            


solution = Solution()
print(solution.occurences([1, 2,2, 3, 3,3, 5,5,5,5]))
