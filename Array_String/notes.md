# Array & String Notes

## Problems Solved

1. Merge Strings Alternately
2. Greatest Common Divisor of Strings
3. Kids With the Greatest Number of Candies
4. Can Place Flowers
5. Reverse Vowels of a String
6. Reverse Words in a String
7. Product of Array Except Self
8. Increasing Triplet Subsequence
9. String Compression

---

## Patterns Learned

### Two Pointers

Used when we need to process elements from both ends or from two sequences simultaneously.

Examples:

* Merge Strings Alternately
* Reverse Vowels of a String

Common Complexity:

* Time: O(n)
* Space: O(1) or O(n)

---

### Prefix & Suffix Arrays

Used when each position depends on elements before and after it.

Example:

* Product of Array Except Self

Key Idea:

* Prefix[i] = product of elements before i
* Suffix[i] = product of elements after i

---

### Greedy

Make the best local decision at each step.

Examples:

* Can Place Flowers
* Increasing Triplet Subsequence

Key Idea:

* Maintain conditions while traversing once.

---

### String Manipulation

Common Operations:

* split()
* join()
* slicing
* concatenation

Examples:

* Reverse Words in a String
* GCD of Strings

---

### Simulation

Follow the process exactly as described.

Example:

* String Compression

---

## Important Takeaways

* Two pointers often reduce nested loops.
* Prefix/Suffix arrays can replace division.
* Greedy solutions often achieve O(n).
* Strings are immutable in Python.
* Use lists when repeatedly building strings.

---

## Revision Checklist

* [ ] Can explain Two Pointer approach
* [ ] Can explain Prefix/Suffix approach
* [ ] Can explain Greedy approach
* [ ] Can derive time complexity
* [ ] Can solve similar problems without hints
