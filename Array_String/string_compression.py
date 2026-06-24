"""
LeetCode 443

Problem:
String Compression

Difficulty:
Medium

Approach:
Use two pointers.
Count consecutive occurrences.
Write character and count back into array.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""
class Solution:
    def compress(self, chars):

        write = 0
        read = 0

        while read < len(chars):

            char = chars[read]
            count = 0

            while (
                read < len(chars)
                and chars[read] == char
            ):
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write