# Best Time to Buy and Sell Stock

- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

## Expected Behavior

- You are given an array prices where prices[i] is the price of a given stock on the ith day.
- You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
- Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Approaches

- [Two pointers](#two-pointers)
- [One pass/ running minumum with comparison](#one-pass-running-minumum-with-comparison)

### Two pointers

<span style="display: inline-block; background-color: blue; border-radius: 800px; padding:2px; color: white;">
    13.4%
</span>

![image](https://github.com/pol-dev-shinroo/python-algorithm/assets/102004753/474cc4af-81d9-4f44-b714-806ef1691d68)

<br>
<br>

**1. Problematic Code:**

```python
class Solution:
    def twoPoint(self, prices):
        l = 0
        r = l + 1
        max_number = 0
        while l < len(prices) -1 and r < len(prices):
            diff = prices[r] - prices[l]
            if diff > 0:
                max_number = max(max_number, diff)
                r += 1
                continue
            l += 1
            r = l + 1
        return max_number
```

**Reason for being problematic**

- This code implements two points like brute force
- The worst-case time complexity of this algorithm is O(n^2), where n is the number of elements in the prices list. This is because in the worst-case scenario (a list sorted in decreasing order), we would end up comparing each element with every other element that comes after it, resulting in approximately n\*(n-1)/2 comparisons, which simplifies to O(n^2) complexity.

**2. Refactored code: a proper implementation of two-pointer approach**

```python
class Solution:
    def twoPoint(self, prices):
        max_number = 0
        l, r = 0, 1

        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff < 0:
                l = r
            else:
                max_number = max(diff, max_number)
            r += 1
        return max_number
```

**Point to remember: Upate l to r!!**

- The algorithm continues this way, checking each price exactly once (not twice like before), until it has checked all prices.
- basically l is the running minimum (hence almost the same logic as the [running mimimum method](#one-pass-running-minumum-with-comparison)).
- However, two pointer method is slower than the running mimimum because it has to calculate diff for every loop + the for loop is faster than while (comparison logic)

### One pass/ running minumum with comparison

**1. Problematic Code:**

```python
class Solution:
    def onePass(self, prices):
        max_number = 0
        min_number = float("inf")

        for i in range(len(prices)):
            if prices[i] < min_number:
                min_number = prices[i]
            else:
                max_number = max(max_number, prices[i])

        return max_number - min_number
```

**Reason for being problematic**

- cannot account for [2,4,1] => since we are recording max and min, it does not account for time factor. My code outputs 3 instead of 2
- Hence, instead of recording max_number, calculate max_profit (updating max_profit when there is profit to be considered => if the current number is greater than min_number)

**2. Refactored code: 1**

```python
class Solution:
    def onePass(self, prices):
        min_number = float("inf")
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_number:
                min_number = prices[i]
            else:
                profit = prices[i] - min_number
                max_profit = max(profit, max_profit)

        return max_profit
```

**2. Refactored code: 2**

```python
class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit
```

Points to learn:

- while the second refactored code might be slightly more efficient than the first (elif is more specific), it is more important t ochoose an algorithm with good time complexity, like O(n) rather than O(n²), rather than focusing on these small differences between algorithms with the same time complexity.
