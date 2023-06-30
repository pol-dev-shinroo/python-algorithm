class Solution:
    def occurences(self, nums):
        hashMap = {}

        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1
        return len(hashMap.values()) == len(set(hashMap.values()))
            


solution = Solution()
print(solution.occurences([1, 2,2, 3, 3,3, 5,5,5]))
