"""Lesson 5 - Pattern: frequency counting with a dict / Counter.

Turns many O(n^2) "compare everything with everything" solutions into O(n).
Run: python lessons/05_frequency_counting.py
"""
from collections import Counter


def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


def first_unique_char(s):
    """Index of the first character that appears once, or -1."""
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1


def is_anagram(a, b):
    return Counter(a) == Counter(b)


if __name__ == "__main__":
    print(char_frequency("banana"))
    print(Counter([1, 2, 2, 3, 3, 3]).most_common(1))
    print(first_unique_char("leetcode"), first_unique_char("aabb"))
    print(is_anagram("listen", "silent"), is_anagram("abc", "abd"))
