# Running sum of 1d array

- https://leetcode.com/problems/running-sum-of-1d-array/

## Expected Behavior

- Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
- Return the running sum of nums.

## Approaches

- [normal loop](#normal-loop)
- [array pre-allocation/ initialization](#array-pre-allocation-initialization)
- [use input array for output](#use-input-array-for-output)

### normal loop

**Using curr_sum**

```python
class Solution:
    def runningSum(self, nums):
        res_arr = []
        curr_sum = 0
        for i in range(len(nums)):
            res_arr.append(curr_sum + nums[i])
            curr_sum += nums[i]

        return res_arr
```

### array pre-allocation/ initialization

**first attempt:**

```python
class Solution:
    def runningSum(self, nums):
        res_arr = [0] * len(nums)
        for i in range(len(nums)):
            if i > 0:
                res_arr[i] = res_arr[i-1] + nums[i]
            else:
                res_arr[i] = nums[i]
        return res_arr
```

**refactored code:**

```python
class Solution:
    def runningSum(self, nums):
        res_arr = [0] * len(nums)
        res_arr[0] = nums[0]

        for i in range(len(nums)):
            res_arr[i] = nums[i] + res_arr[i-1]

        return nums
```

**Watch out for the first index!!!**
**
for i = 0,
then the nums[0-1] => nums[len(nums) -1] == last index
**

### use input array for output

```python
class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            print(nums[i-1])
            # nums[i] = nums[i] + nums[i-1]
            nums[i] += nums[i-1]

        return nums
```
