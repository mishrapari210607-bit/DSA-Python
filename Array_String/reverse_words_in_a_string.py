"""
LeetCode 151

Problem:
Reverse Words in a String

Difficulty:
Medium

Approach:
Split string into words.
Reverse the order.
Join them with a single space.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""
class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()

        words.reverse()

        return " ".join(words)