"""
LeetCode 1431

Problem:
Kids With the Greatest Number of Candies

Difficulty:
Easy

Approach:
Find the maximum candies any child has.
For each child check whether adding
extraCandies makes them reach or exceed
the maximum.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""
class Solution:
    def kidsWithCandies(self, candies, extraCandies):

        maximum = max(candies)

        result = []

        for candy in candies:
            result.append(candy + extraCandies >= maximum)

        return result