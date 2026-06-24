"""
LeetCode 334

Problem:
Increasing Triplet Subsequence

Difficulty:
Medium

Approach:
Track smallest and second smallest values.
If a number larger than both is found,
an increasing triplet exists.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""
class Solution:
    def increasingTriplet(self, nums):

        first = float('inf')
        second = float('inf')

        for num in nums:

            if num <= first:
                first = num

            elif num <= second:
                second = num

            else:
                return True

        return False