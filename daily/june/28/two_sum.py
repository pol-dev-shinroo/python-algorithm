# hashtable
# record items through the loop 
# then check if the item from the hashTable, when added to the current index => becomes the target=> the return

class Solution: 
    def twoSum(self,nums, target):
        hashMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                return hashMap[diff], i
            hashMap[nums[i]] = i 


solution = Solution()
print(solution.twoSum([0,0,0], 0))

