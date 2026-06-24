"""
LeetCode 1768

Problem:
Merge Strings Alternately

Difficulty:
Easy

Approach:
Use two pointers to traverse both strings simultaneously.
Append remaining characters after one string ends.

Time Complexity:
O(n + m)

Space Complexity:
O(n + m)
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        i = j = 0

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])

            i += 1
            j += 1

        result.extend(word1[i:])
        result.extend(word2[j:])

        return "".join(result)