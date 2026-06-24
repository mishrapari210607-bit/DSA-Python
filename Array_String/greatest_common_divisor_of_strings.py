"""
LeetCode 1071

Problem:
Greatest Common Divisor of Strings

Difficulty:
Easy

Approach:
If str1 + str2 is not equal to str2 + str1,
then no common divisor string exists.

Otherwise find the GCD of both lengths
and return the prefix of that length.

Time Complexity:
O(n + m)

Space Complexity:
O(1)
"""
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        length = gcd(len(str1), len(str2))

        return str1[:length]