"""
LeetCode 238

Problem:
Product of Array Except Self

Difficulty:
Medium

Approach:
Compute prefix products.
Compute suffix products.
Multiply corresponding prefix and suffix
values for each index.

Time Complexity:
O(n)

Space Complexity:
O(1) excluding output array
"""
class Solution:
    def productExceptSelf(self, nums):

        n = len(nums)

        result = [1] * n

        prefix = 1

        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result