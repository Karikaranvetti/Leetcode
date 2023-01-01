[problem link here ](https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan&id=level-1)
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
function calculates the total sum of the elements in the nums list and then iterates over the list once, keeping track of the sum of the elements to the left of the current pivot index. If the sum of the elements to the left is equal to the sum of the elements to the right (which is the total sum minus the sum of the elements to the left and the current pivot element), then the current index is returned as the pivot index.

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:O(n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:O(1)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num
        return -1
```
