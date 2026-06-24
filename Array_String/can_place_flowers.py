"""
LeetCode 605

Problem:
Can Place Flowers

Difficulty:
Easy

Approach:
Traverse the flowerbed.
Plant a flower whenever current,
left and right positions are empty.

Count planted flowers and check
whether count >= n.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution:
    def canPlaceFlowers(self, flowerbed, n):

        count = 0

        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:

                left = (i == 0 or flowerbed[i - 1] == 0)
                right = (
                    i == len(flowerbed) - 1
                    or flowerbed[i + 1] == 0
                )

                if left and right:
                    flowerbed[i] = 1
                    count += 1

        return count >= n